import math

#计算样本之间的距离
def distance(list1,list2):
    distance_data=[]      #返回欧式距离
    cur=0
    for i in range(len(list1)-1):
        cur+=math.pow((list1[i]-list2[i]),2)
    distance_data=[math.sqrt(cur),int(list1[6])]
    return distance_data
##################################################################

def gaussian(dist, a=1, b=0, c=0.3):
    return a * math.e ** (-(dist - b) ** 2 / (2 * c ** 2))

#计算每个训练子集下的训练样本与测试样本之间的关系
#################################################################
def C_train(test_list,train_list):
    """
    :param test_list: 测试样本  1*7  1个样本、6个特征+1个标签
    :param train_list: 训练子集 566*7
    :return: 多数表决分类预测的标签、距离加权分类得到的标签
    """
    tt_data = []  # 存储每个测试样本与所有训练样本间的欧氏距离
    label_count = [0] * 7  # 多数表决标记数
    w_label_count = [0] * 7  # 距离加权标记数
    for x in train_list:
        tt_data.append(distance(x,test_list))
    tt_data = sorted(tt_data, key=(lambda x: x[0]))  # 按欧式距离升序
    for k in range(5):     #选取距离最近的10个样本，找到数量最多的标签数
        if tt_data[k][1] == 0:
            label_count[0] += 1
            w_label_count[0] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[0] +=gaussian(tt_data[k][0])
        elif tt_data[k][1] == 1:
            label_count[1] += 1
            w_label_count[1] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[1] += gaussian(tt_data[k][0])
        elif tt_data[k][1] == 2:
            label_count[2] += 1
            w_label_count[2] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[2] += gaussian(tt_data[k][0])
        elif tt_data[k][1] == 3:
            label_count[3] += 1
            w_label_count[3] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[3] += gaussian(tt_data[k][0])
        elif tt_data[k][1] == 4:
            label_count[4] += 1
            w_label_count[4] += 1 / math.pow(tt_data[k][0], 2)
        elif tt_data[k][1] == 5:
            label_count[5] += 1
            w_label_count[5] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[4] += gaussian(tt_data[k][0])
        elif tt_data[k][1] == 6:
            label_count[6] += 1
            w_label_count[6] += 1 / math.pow(tt_data[k][0], 2)
            #w_label_count[6] += gaussian(tt_data[k][0])
    max_num=max(label_count[0], label_count[1], label_count[2], label_count[3], label_count[4], label_count[5],
                  label_count[6])
    w_max_num=max(w_label_count[0], w_label_count[1], w_label_count[2], w_label_count[3], w_label_count[4], w_label_count[5],
                  w_label_count[6])
    return label_count.index(max_num),w_label_count.index(w_max_num)   #返回的是预测的类别