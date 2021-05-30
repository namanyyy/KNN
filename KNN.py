"""
     funtion:KNN分类
     Author:ZhangNan
"""

import numpy as np     #numpy 存储和处理大型矩阵
from sklearn.model_selection import train_test_split #划分训练集和测试集
from scipy import signal
import pandas as pd    #处理数据
import math      #引入数学函数
import C_train   #训练
import Evaluate  #计算评价指标
from DataVisiable import DV #数据可视化

class Feature:
    def __init__(self,list1):
        self.mean_=np.mean(list1)    #均值
        self.var_data=np.var(list1)  #方差
        self.skew = pd.Series(list1).skew()  # 计算偏度
        self.change_mark=((list1[:-1] * list1[1:]) < 0).sum()                         #过零点次数
        self.petrosian=math.log10(len(list1))/(math.log10(len(list1)/(len(list1)+0.4*self.change_mark)))  #petrosian分形维数
        self.max_=np.max(list1)   #最大值
    def Data_L(self):
        data_l=[]
        data_l.append(self.mean_)
        data_l.append(self.var_data)
        data_l.append(self.skew)
        data_l.append(self.change_mark)
        data_l.append(self.petrosian)
        data_l.append(self.max_)
        return data_l
##############################################################################

#读取文件、划分数据集，采用交叉验证方式、分为4个训练集、1个测试集。
##############################################################################
f_data=np.loadtxt("sc4002e0_data.txt",dtype=float)
f_label=np.loadtxt("sc4002e0_label.txt",dtype=float)
sf_label=np.delete(f_label,2830)         #删除标签数据集中的最后一个没有对应数据的标签
#滤波
fs = 3000                                           #设立频率变量fs
lowcut = 1
highcut = 30
order = 2                                           #设立滤波器阶次变量
nyq = 0.5*fs                                        #设立采样频率变量nyq，采样频率=fs/2。
low = lowcut/nyq
high = highcut/nyq
b,a = signal.butter(order,[low,high],btype='band')   #设计巴特沃斯带通滤波器 “band”
data_filter = signal.lfilter(b,a,f_data)             #将s1带入滤波器，滤波结果保存在s1_filter1中

#DV(f_data,f_label)#原始数据分类,数据可视化

#计算每个时间窗的数据特性
datas=[]
for i in range(0,len(data_filter),3000):    #每3000个采样点作为一个时间窗
    cur=Feature(data_filter[i:i+2999])
    datas.append(cur.Data_L())    #data是二维数组 2830*6

#特征可视化
graph={}
features=["均值","方差","偏度","过零点次数","petrosian分形维数","最大值"]     #特征
for i in range(len(features)):
    cur=[]
    for j in datas:
        cur.append(j[i])
    graph[features[i]]=cur
#print(pd.DataFrame(graph))
#全部的特征提取表
features_data=pd.DataFrame(graph)
features_data.to_csv("features_data.csv")

data=[]     #所用样本
for index,value in enumerate(datas):
    data.append(list(value))

f_label=[]   #标签
for line in sf_label:
    line=float(line)
    f_label.append(line)
#划分训练集和测试集
train_data,test_data,train_label,test_label=train_test_split(data,f_label,test_size=0.2)

#将得到的训练集划分为多个训练子集
train_dataset1=[]   #训练子集
train_dataset2=[]
train_dataset3=[]
train_dataset4=[]
train_dataset=[]   #总的训练集是一个三维数组，4*566*7：有四个训练集，每个有566个样本，每个样本6个特征+标签
test_dataset=[]
for index,value in enumerate(train_data):
    value.append(train_label[index])
    if index<0.2*2830:
        train_dataset1.append(value)
    elif 0.2*2830<=index<0.4*2830:
        train_dataset2.append(value)
    elif 0.4*2830<=index<0.6*2830:
        train_dataset3.append(value)
    else:
        train_dataset4.append(value)
train_dataset.append(train_dataset1)
train_dataset.append(train_dataset2)
train_dataset.append(train_dataset3)
train_dataset.append(train_dataset4)
for index, value in enumerate(test_data):
    value.append(test_label[index])
    test_dataset.append(value)
################################################################

#依次读取每个样本，计算相似度   K=10
#############################################################
pretict_label=[]   #多数表决分类得到的预测标签
w_pretict_label=[] #距离加权分类得到的预测标签
for i in test_dataset:
    C_max = []     #多数表决得到的每个训练子集下的预测标签
    C_W_max = []   #距离加权得到的每个训练子集下的预测标签
    for j in train_dataset:
        max_num,w_max_num=C_train.C_train(i,j)  #计算每个训练子集下的预测标签
        C_max.append(max_num)
        C_W_max.append(w_max_num)
    pretict_label.append(max(C_max, key=C_max.count))   #只保留预测标签最多的那个标签
    w_pretict_label.append(max(C_W_max,key=C_max.count))
#########################################################################

#计算分类器评价指标、计算混淆矩阵、正确率等评价指标
#########################################################################
print("     多数表决分类K=10")
Evaluate.EvaluateTarget(pretict_label,test_dataset)
print("     距离加权分类K=10")
Evaluate.EvaluateTarget(w_pretict_label,test_dataset)
#########################################################################
