#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""风机软件报价算法"""


import numpy as np
import matplotlib.pyplot as plt
import mayavi.mlab as mlab
from PriceRefer.GasProperty import GasProperty as GP
import os
os.environ['QT_API']='pyside'

ParamName={'集流器进口半径':0,
           '集流器出口半径':1,
           '集流器长度':2,
           '叶轮出口直径':3,
           '蜗舌间隙':4,
           '正方形边长':5,
           '蜗壳出口段长度':6,
           '叶道进口宽度':7,
           '叶轮入口直径':8,
           '叶道出口宽度':9,
           'test':10,
           '叶片入口直径':11,
           '叶片出口直径':12,
           '叶片入口宽度':13,
           '进气箱厚度':14,
           '进气箱宽度':15,
           '进气箱上侧高度':16,
           '进气箱下侧高度':17,
           'test2':18}



class DataSource(object):
    """数据源，输入比转速和压力系数之后返回相关几何参数
    初始化有两种模式：
    1.输入数据文件，采用拉格朗日插值法获取数据
    2.输入与另一个数据源的关系函数，通过这个数据源获取相应的数据"""
    def __init__(self,P_in,T_in,P,Qn,n):
        """压力：Pa
        温度：K
        流量：立方米/秒
        转速：转/分钟"""

        realGas=GP(P_in,T_in,0)
        realRho=realGas.getdensity()
        idealGas=GP(101325,293,0)
        idealRho=idealGas.getdensity()
        self.P=P*(idealRho/realRho)
        self.n=n
        self.P_in=101325
        self.T_in=293
        self.Qn=Qn
        self.rho=idealRho
        self.ns=5.54*n*np.sqrt(Qn)/self.P**0.75
        self.psi=0.9*(1.505009664438608 * np.exp(-0.018463158347320 * self.ns) + 0.415434029011928)
        u2=np.sqrt(self.P/(idealRho/2*self.psi))
        self.D2=u2*60/(np.pi*self.n)
        self.phi=self.ns**2*self.psi**1.5*idealRho**1.5/24869
        self.data = np.loadtxt('data.txt')
        self.getData()

    def getData(self):

        #集流器进口半径
        self.R_jlq=self.getParam(3,[2,1,0])



    def getParam(self,paramIndex,sortIndex):
        """sortIndex是指对data数组排序时的关键字段的序号
        一般是1和2为第一关键字，此时依照第一关键字插值
        如果data[0]等于0，即以压力系数为第一关键字，此时专指对叶片出口角度插值
        其插值方法也比较特殊"""

        data=self.data
        self.sort(data,sortIndex)
        if(sortIndex[0]==2):
            if self.ns<data[0,2]:
                return data[0,paramIndex]
            elif self.ns>data[data.shape[0]-1,2]:
                return data[data.shape[0]-1,paramIndex]
            else:
                for i in range(data.shape[0]):
                    if (self.ns == data[i, 2] or self.ns < data[i, 2]):
                        index = i
                        break
                if self.ns == data[index, 2]:
                    return data[index, paramIndex]
                else:
                    k = (data[index, paramIndex] - data[index - 1, paramIndex]) / (data[index, 2] - data[index - 1, 2])
                    return k * (self.ns - data[index - 1, paramIndex]) + data[index - 1, paramIndex]
        elif(sortIndex[0]==1):
            if self.phi < data[0, 1]:
                return data[0, paramIndex]
            elif self.phi > data[data.shape[0] - 1, 1]:
                return data[data.shape[0] - 1, paramIndex]
            else:
                for i in range(data.shape[0]):
                    if (self.phi == data[i, 1] or self.phi < data[i, 1]):
                        index = i
                        break
                if self.phi == data[index, 1]:
                    return data[index, paramIndex]
                else:
                    k = (data[index, paramIndex] - data[index - 1, paramIndex]) / (data[index, 2] - data[index - 1, 2])
                    return k * (self.phi - data[index - 1, paramIndex]) + data[index - 1, paramIndex]
        elif sortIndex[0]==0:
            psi=np.around(self.psi/0.2)*0.2

            if psi>1.3 and psi<1.5:
                return 70
            else:
                data=data[np.where(data[:,0]==psi)[0],:]
                if self.ns<=data[0,2]:
                    return data[0,9]
                elif self.ns>=data[data.shape[0]-1,2]:
                    return data[data.shape[0]-1,9]
                else:
                    for i in range(data.shape[0]):
                        if self.ns<data[i,2]:
                            index=i
                            break
                    k=(data[index, paramIndex] - data[index - 1, paramIndex]) / (data[index, 2] - data[index - 1, 2])
                    return k * (self.ns - data[index - 1, paramIndex]) + data[index - 1, paramIndex]


    def sort(self,data,sortIndex):
        firstIndex=sortIndex[0]
        secondIndex=sortIndex[1]
        thirdIndex=sortIndex[2]
        def lt(A,B):
            if A[firstIndex]<B[firstIndex]:
                return True
            elif A[firstIndex]==B[firstIndex] and A[secondIndex]<B[secondIndex]:
                return True
            elif A[firstIndex]==B[firstIndex] and A[secondIndex]==B[secondIndex] \
                    and A[thirdIndex]<B[thirdIndex]:
                return True
            else:
                return False
        dim=data.shape[1]
        temp=np.zeros(dim)
        for i in range(data.shape[0]-1):
            for i in range(0,data.shape[0]-i-1):
                if lt(data[i+1,:],data[i,:]):
                    temp[:]=data[i,:]
                    data[i,:]=data[i+1,:]
                    data[i+1,:]=temp[:]


if __name__=='__main__':
    test=DataSource(63740,393,4500,340000/3600,960)