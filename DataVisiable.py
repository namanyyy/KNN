import matplotlib.pyplot as plt

def DV(list1,list2):
    """
    :param list1: data
    :param list2: label
    """
    #分期绘图
    W_figure=[]   #W期所对应的所有数据
    N1_figure=[]
    N2_figure=[]
    N3_figure=[]
    N4_figure=[]
    R_figure=[]
    M_figure=[]
    for i in range(len(list2)):
        if int(list2[i])==0:
            W_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i])==1:
            N1_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i])==2:
            N2_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i])==3:
            N3_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i])==4:
            N4_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i])==5:
            R_figure.extend(list1[i*3000:i*3000+2999])
        elif int(list2[i]) == 6:
            M_figure.extend(list1[i*3000:i*3000+2999])

    x=list(range(8000))
    plt.figure(1)
    plt.plot(x,W_figure[0:8000],'b-')
    plt.title("W")

    plt.figure(2)
    plt.plot(x,N1_figure[0:8000],'b-')
    plt.title("N1")

    plt.figure(3)
    plt.plot(x,N2_figure[0:8000],'b-')
    plt.title("N2")

    plt.figure(4)
    plt.plot(x,N3_figure[0:8000],'b-')
    plt.title("N3")

    plt.figure(5)
    plt.plot(x,N4_figure[0:8000],'b-')
    plt.title("N4")

    plt.figure(6)
    plt.plot(x,R_figure[0:8000],'b-')
    plt.title("R")
    plt.show()



