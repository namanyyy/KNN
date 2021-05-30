import pandas as pd
def EvaluateTarget(list_label,test_data):
    pretict0_0,pretict0_1,pretict0_2,pretict0_3,pretict0_4,pretict0_5,pretict0_6=0,0,0,0,0,0,0    #x_y用于记录真实值为x但却预测为y的数量
    pretict1_0,pretict1_1,pretict1_2,pretict1_3,pretict1_4,pretict1_5,pretict1_6=0,0,0,0,0,0,0
    pretict2_0,pretict2_1,pretict2_2,pretict2_3,pretict2_4,pretict2_5,pretict2_6=0,0,0,0,0,0,0
    pretict3_0,pretict3_1,pretict3_2,pretict3_3,pretict3_4,pretict3_5,pretict3_6=0,0,0,0,0,0,0
    pretict4_0,pretict4_1,pretict4_2,pretict4_3,pretict4_4,pretict4_5,pretict4_6=0,0,0,0,0,0,0
    pretict5_0,pretict5_1,pretict5_2,pretict5_3,pretict5_4,pretict5_5,pretict5_6=0,0,0,0,0,0,0
    pretict6_0,pretict6_1,pretict6_2,pretict6_3,pretict6_4,pretict6_5,pretict6_6=0,0,0,0,0,0,0
    j=0
    for i in test_data:
        num=int(i[6])           #样本实际标签
        if num==0:
            if list_label[j]==0:
                pretict0_0+=1
            elif list_label[j]==1:
                pretict0_1+=1
            elif list_label[j]==2:
                pretict0_2+=1
            elif list_label[j]==3:
                pretict0_3+=1
            elif list_label[j]==4:
                pretict0_4+=1
            elif list_label[j]==5:
                pretict0_5+=1
            else:
                pretict0_6+=1
        elif num==1:
            if list_label[j]==0:
                pretict1_0+=1
            elif list_label[j]==1:
                pretict1_1+=1
            elif list_label[j]==2:
                pretict1_2+=1
            elif list_label[j]==3:
                pretict1_3+=1
            elif list_label[j]==4:
                pretict1_4+=1
            elif list_label[j]==5:
                pretict1_5+=1
            else:
                pretict1_6+=1
        elif num==2:
            if list_label[j]==0:
                pretict2_0+=1
            elif list_label[j]==1:
                pretict2_1+=1
            elif list_label[j]==2:
                pretict2_2+=1
            elif list_label[j] == 3:
                pretict2_3 += 1
            elif list_label[j] == 4:
                pretict2_4 += 1
            elif list_label[j] == 5:
                pretict2_5 += 1
            else:
                pretict2_6+=1
        elif num==3:
            if list_label[j]==0:
                pretict3_0+=1
            elif list_label[j]==1:
                pretict3_1+=1
            elif list_label[j]==2:
                pretict3_2+=1
            elif list_label[j]==3:
                pretict3_3+=1
            elif list_label[j]==4:
                pretict3_4+=1
            elif list_label[j]==5:
                pretict3_5+=1
            else:
                pretict3_6+=1
        elif num == 4:
            if list_label[j] == 0:
                pretict4_0 += 1
            elif list_label[j] == 1:
                pretict4_1 += 1
            elif list_label[j] == 2:
                pretict4_2 += 1
            elif list_label[j] == 3:
                pretict4_3 += 1
            elif list_label[j] == 4:
                pretict4_4 += 1
            elif list_label[j] == 5:
                pretict4_5 += 1
            else:
                pretict4_6+=1
        elif num == 5:
            if list_label[j] == 0:
                pretict5_0 += 1
            elif list_label[j] == 1:
                pretict5_1 += 1
            elif list_label[j] == 2:
                pretict5_2 += 1
            elif list_label[j] == 3:
                pretict5_3 += 1
            elif list_label[j] == 4:
                pretict5_4 += 1
            elif list_label[j] == 5:
                pretict5_5 += 1
            else:
                pretict5_6+=1
        elif num==6:
            if list_label[j]==0:
                pretict6_0+=1
            elif list_label[j]==1:
                pretict6_1+=1
            elif list_label[j]==2:
                pretict6_2+=1
            elif list_label[j]==3:
                pretict6_3+=1
            elif list_label[j]==4:
                pretict6_4+=1
            elif list_label[j]==5:
                pretict6_5+=1
            else:
                pretict6_6+=1

        j+=1
    graph={}
    graph["预测为0"]=[pretict0_0,pretict1_0,pretict2_0,pretict3_0,pretict4_0,pretict5_0,pretict6_0]
    graph["预测为1"]=[pretict0_1,pretict1_1,pretict2_1,pretict3_1,pretict4_1,pretict5_1,pretict6_1]
    graph["预测为2"]=[pretict0_2,pretict1_2,pretict2_2,pretict3_2,pretict4_2,pretict5_2,pretict6_2]
    graph["预测为3"]=[pretict0_3, pretict1_3, pretict2_3, pretict3_3, pretict4_3, pretict5_3,pretict6_3]
    graph["预测为4"]=[pretict0_4, pretict1_4, pretict2_4, pretict3_4, pretict4_4, pretict5_4,pretict6_4]
    graph["预测为5"]=[pretict0_5, pretict1_5, pretict2_5, pretict3_5, pretict4_5, pretict5_5,pretict6_5]
    graph["预测为6"] = [pretict0_6, pretict1_6, pretict2_6, pretict3_6, pretict4_6, pretict5_6, pretict6_6]
    hunxiao=pd.DataFrame(graph)    #绘制混洗矩阵
    print(hunxiao)
    #print("准确率为：",(pretict2_2+pretict1_1+pretict0_0+pretict4_4+pretict5_5+pretict6_6)/(2830*0.2))  #计算分类的准确率