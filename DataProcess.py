#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""风机软件报价算法"""


import numpy as np
from .GasProperty import GasProperty as GP

PartArea={  1:'进风筒',
            2:'法兰',
            3:'叶轮前盘',
            4:'叶片',
            5:'叶轮后盘或中盘',
            6:'蜗壳后侧板',
            7:'蜗壳外圈',
            8:'蜗壳与进气箱公用侧板',
            9:'进气箱侧板',
            10:'进气箱外圈'}



class DataSource(object):
    """数据源，输入比转速和压力系数之后返回相关几何参数
    初始化有两种模式：
    1.输入数据文件，采用拉格朗日插值法获取数据
    2.输入与另一个数据源的关系函数，通过这个数据源获取相应的数据"""
    def __init__(self,P_in,T_in,P,Qn,n,isSingle,boardThickness,D):
        """压力：Pa
        温度：K
        流量：立方米/秒
        转速：转/分钟"""
        self.isSingle=isSingle
        self.boardThickness=boardThickness
        realGas=GP(P_in,T_in,0)
        realRho=realGas.getdensity()
        idealGas=GP(101325,293,0)
        idealRho=idealGas.getdensity()
        self.P=P*(idealRho/realRho)
        self.n=n
        self.P_in=101325
        self.T_in=293
        if self.isSingle:
            self.Qn=Qn
        else:
            self.Qn=Qn/2
        self.rho=idealRho
        self.ns=5.54*n*np.sqrt(self.Qn)/self.P**0.75
        self.psi=0.9*(1.505009664438608 * np.exp(-0.018463158347320 * self.ns) + 0.415434029011928)
        u2=np.sqrt(self.P/(idealRho/2*self.psi))
        if D==0:
            self.D2=u2*60/(np.pi*self.n)*1000

        else:
            self.D2=D
            self.psi = self.P / (0.5 * self.rho * u2 ** 2)
        self.phi=self.ns**2*self.psi**1.5*idealRho**1.5/24869
        self.data = np.loadtxt('data.txt')
        self.area=[]
        self.getData()
        self.getArea()

    def getData(self):

        #集流器进口半径
        k=self.D2/1000
        self.R_jlq=self.getParam(3,[2,1,0])*k
        self.L_jlq=self.getParam(4,[2,1,0])*k
        self.R2_jlq=self.getParam(5,[2,1,0])*k
        self.e=self.getParam(6,[2,1,0])*k
        self.b1_shroud=self.getParam(7,[2,1,0])*k
        self.b2_shroud=self.getParam(8,[2,1,0])*k
        self.beta_b2=self.getParam(9,[0,1,2])/180*np.pi

        self.L_wk=700*k

        self.D0=self.R2_jlq*2
        self.D1=self.D0+2*15*k
        self.D3=1040*k

        #叶片进口角度
        b=self.b1_shroud-self.b2_shroud
        L=(self.D3-self.D0)/2
        a=(L**2-b**2)/(2*b)
        x0=self.D0/2+L
        y0=self.b2_shroud+a+b
        def func1(x):
            return -np.sqrt((a+b)**2-(x-x0)**2)+y0
        self.b1=func1(self.D1/2)
        self.b2=func1(self.D2/2)

        c1=self.Qn*1000**3/(np.pi*self.D1*self.b1)
        u1=self.n/60*np.pi*self.D1
        self.beta_b1=np.arctan(c1/u1)
        if(self.psi<1.5):
            self.Z=12
        else:
            self.Z=16
        self.dh=self.D0*0.25
        if self.isSingle:
            self.B=self.L_jlq+self.b1_shroud+40
        else:
            self.B=(self.L_jlq+self.b1_shroud)*2+self.boardThickness[5]

        self.t_jqx=np.sqrt(np.pi*(self.D0)**2/8)*0.7
        self.W_jqx=4*self.t_jqx
        self.H1=(self.D3/2+2*self.e+50*k)
        self.H2=(self.R_jlq+2*self.e)
        self.alpha_jqx=5/180*np.pi


    def getArea(self):
        """计算各部分面积"""
        #集流器面积
        R_jlq=self.R_jlq
        R2_jlq=self.R2_jlq
        L_jlq=self.L_jlq
        S1=np.pi*(R2_jlq+R_jlq)*L_jlq
        S2= np.pi*(R_jlq**2-R2_jlq**2)+2*np.pi*R2_jlq*L_jlq
        S=(S1+S2)/2
        if self.isSingle:
            S=S
        else:
            S=2*S
        self.area.append(S)

        #集流器法兰盘面积
        if self.D3>1600:
            S=np.pi*(200*self.R_jlq+10000)
        else:
            S=np.pi*(120*self.R_jlq+3600)
        if self.isSingle:
            S=S
        else:
            S=2*S
        self.area.append(S)

        #叶轮前盘
        R=self.D3/2
        L=self.D3/2-self.D0/2
        b=self.b1_shroud-self.b2_shroud
        a=(L**2-b**2)/(2*b)
        def func1(x):
            return R-np.sqrt((a+b)**2-(x+a)**2)
        num=100
        delta=b/num
        area=np.zeros(num)
        for i in range(num):
            r1=func1(delta*i)
            r2=func1(delta*(i+1))
            l=np.sqrt((r1-r2)**2+delta**2)
            area[i]=2*np.pi*r1*l
        S=np.sum(area)
        if self.isSingle:
            S=S
        else:
            S=2*S
        self.area.append(S)

        #叶片面积
        cx1,cy1,cr1,c1_1,c2_1=self.getBlade()

        b = self.b1_shroud - self.b2_shroud
        L = (self.D3 - self.D0) / 2
        a = (L ** 2 - b ** 2) / (2 * b)
        x0 = self.D0 / 2 + L
        y0 = self.b2_shroud + a + b
        def func2(x):
            return -np.sqrt((a + b) ** 2 - (x - x0) ** 2) + y0

        num = 100
        delta = (c2_1 - c1_1) / num
        area=np.zeros(num)
        for i in range(num):
            eta = delta * i + c1_1
            x=cx1+cr1*np.cos(eta)
            y=cy1+cr1*np.sin(eta)
            r=np.sqrt(x**2+y**2)
            h=func2(r)
            area[i]=delta*cr1*h
        S=np.sum(area)*self.Z
        if self.isSingle:
            S=S
        else:
            S=2*S
        self.area.append(S)

        #叶轮后盘或者中盘
        S=np.pi*(self.D3/2)**2-np.pi*(self.dh/2)**2
        self.area.append(S)

        #蜗壳侧板
        R=self.D3/2
        L=self.e
        D=self.L_wk
        S1=np.pi/4*(R+L/2*1)**2
        S2 = np.pi / 4 * (R + L / 2 * 3) ** 2
        S3 = np.pi / 4 * (R + L / 2 * 5) ** 2
        S4 = np.pi / 4 * (R + L / 2 * 7) ** 2
        S5=0.5*(4*L+R+4.5*L-(R+0.5*L)*np.cos(np.pi/4))*((R+L/2)*np.cos(np.pi/4))
        S6=(R+4.5*L-(R+0.5*L)*np.cos(np.pi/4))*(D-(R+0.5*L)*np.cos(np.pi/4))
        S=S1+S2+S3+S4+S5+S6
        if self.isSingle:
            S=S-(self.dh/2)**2*np.pi
        else:
            S=0
        self.area.append(S)


        #蜗壳外圈面积
        perimeter=0.25*np.pi*(R+L/2)+0.5*np.pi*(3*R+7.5*L)+2*D-(R+L/2)*np.cos(np.pi/4)
        S=self.B*perimeter
        self.area.append(S)

        #蜗壳与进气箱公用侧板
        R = self.D3 / 2
        L = self.e
        D = self.L_wk
        S1 = np.pi / 4 * (R + L / 2 * 1) ** 2
        S2 = np.pi / 4 * (R + L / 2 * 3) ** 2
        S3 = np.pi / 4 * (R + L / 2 * 5) ** 2
        S4 = np.pi / 4 * (R + L / 2 * 7) ** 2
        S5 = 0.5 * (4 * L + R + 4.5 * L - (R + 0.5 * L) * np.cos(np.pi / 4)) * ((R + L / 2) * np.cos(np.pi / 4))
        S6 = (R + 4.5 * L - (R + 0.5 * L) * np.cos(np.pi / 4)) * (D - (R + 0.5 * L) * np.cos(np.pi / 4))
        S = S1 + S2 + S3 + S4 + S5 + S6

        H=self.H1
        H2=self.H2
        W=self.W_jqx
        if(W/2<=R+L):
            S7=0.25*W*(H-(R+L*2)+H+L/2-np.sqrt((R+0.25*L)**2-(W/2-L/2)**2))+\
                0.25*W*(H-(R+2*L)+H-L/2-np.sqrt((R+1.5*L)**2-(W/2+L/2)**2))
        elif(W/2>R+L and W/2<=R+3*L):
            S7=0.25*W*(H-(R+2*L)+H+L/2-np.sqrt((R+2.5*L)**2-(W/2-L/2)**2))+\
                0.5*W*(H+(R+L/2)*np.cos(np.pi/4)-L/2)-0.25*np.pi*(R+1.5*L)**2-0.25*np.pi*(R+L/2)**2
        elif(W/2>R+3*L):
            S7=0.5*W*(H+(R+L/2)*np.cos(np.pi/4)-L/2)-0.25*np.pi*(R+1.5*L)**2-0.25*np.pi*(R+0.5*L)**2+\
                H*W/2-0.25*np.pi*(R+2.5*L)**2+H2/2*(W/2-(R+3*L)+W/2-np.sqrt((R+3.5*L)**2-(H2-L/2)**2))
        S+=S7
        S-=self.R_jlq**2*np.pi
        if self.isSingle:
            S=S
        else:
            S=2*S
        self.area.append(S)

        #进气箱侧板面积
        H1=self.H1
        H2=self.H2
        W=self.W_jqx
        alpha=self.alpha_jqx

        H=H1+H2
        S=H*W-H*H*np.tan(alpha)
        if(self.isSingle):
            S=S
        else:
            S=2*S
        self.area.append(S)

        #进气箱外圈面积
        perimeter=H/np.cos(alpha)*2+W-2*H*np.tan(alpha)
        S=perimeter*self.t_jqx
        if (self.isSingle):
            S = S
        else:
            S = 2 * S
        self.area.append(S)

    def getWeight(self,ratio,density,hasInputBox):

        weight=np.zeros(11)
        if hasInputBox:
            for i in range(1,11):
                weight[i]=self.area[i-1]*self.boardThickness[i]*ratio[i]*density/1000**3
            self.weight=weight
        else:
            for i in range(1, 8):
                weight[i] = self.area[i - 1] * self.boardThickness[i] * ratio[i] * density / 1000 ** 3
            weight[8]= self.area[6] * self.boardThickness[7] * ratio[7] * density / 1000 ** 3
            self.weight = weight
        return weight


    def getBlade(self):
        beta_b1 = self.beta_b1/np.pi*180
        beta_b2 = self.beta_b2/np.pi*180
        alpha = 90.0 - beta_b1
        R1 = self.D1 / 2
        R2 = self.D2 / 2

        alpha = alpha / 180.0 * np.pi
        beta_b2 = beta_b2 / 180.0 * np.pi
        beta = 2 * np.arctan((R2 * np.cos(beta_b2) - R1 * np.sin(alpha)) / (
        R1 * np.cos(alpha) + R2 * np.sin(beta_b2))) / np.pi * 180
        alpha = alpha / np.pi * 180
        beta_b2 = beta_b2 / np.pi * 180

        angle1 = 100

        x1 = R1 * np.cos(angle1 / 180 * np.pi)
        y1 = R1 * np.sin(angle1 / 180 * np.pi)
        k1 = np.tan((angle1 + alpha) / 180 * np.pi)

        a = 1.0
        b = -2.0 * R1 * np.cos(np.pi - alpha / 180 * np.pi - beta / 2 / 180 * np.pi)
        c = R1 * R1 - R2 * R2
        l = (-b + np.sqrt(b * b - 4.0 * a * c)) / (2.0 * a)

        angle2 = (R1 * R1 + R2 * R2 - l * l) / (2.0 * R1 * R2)
        angle2 = np.arccos(angle2) * 180 / np.pi
        angle3 = angle1 + angle2

        x2 = R2 * np.cos(angle3 / 180 * np.pi)
        y2 = R2 * np.sin(angle3 / 180 * np.pi)

        cx1, cy1, cr1 = self.CalcuCircle(x1, y1, k1, x2, y2)
        c1_1 = self.CalcuCeta(x1, y1, cx1, cy1, cr1)
        c2_1 = self.CalcuCeta(x2, y2, cx1, cy1, cr1)

        return cx1,cy1,cr1,c1_1,c2_1






    def CalcuCircle(self,dx1, dy1, dk1, dx2, dy2):
        x1 = dx1 
        y1 = dy1 
        k1 = -1.0 / dk1 
        b1 = y1 - k1 * x1 

        x2 = (dx1 + dx2) / 2 
        y2 = (dy1 + dy2) / 2 

        k2 = -(dx2 - dx1) / (dy2 - dy1)
        b2 = y2 - k2 * x2

        cx = -(b1 - b2) / (k1 - k2)
        cy = k1 * cx + b1
        cr = np.sqrt((cx - x1) * (cx - x1) + (cy - y1) * (cy - y1))

        return cx,cy,cr

    def CalcuCeta(self,x,y,cx,cy,cr):
        tx = x - cx 
        ty = y - cy 

        ceta = np.arccos(np.abs(tx) / cr)
        if (tx < 0 and ty >= 0):
            ceta =  np.pi - ceta 
        if (tx <= 0 and ty < 0):
            ceta =  np.pi + ceta 
        if (tx > 0 and ty < 0):
            ceta = 2 *  np.pi - ceta 

        return ceta 


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
                    return k * (self.ns - data[index - 1, sortIndex[0]]) + data[index - 1, paramIndex]
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
                    return k * (self.phi - data[index - 1, sortIndex[0]]) + data[index - 1, paramIndex]
        elif sortIndex[0]==0:
            psi=np.around(self.psi/0.2)*0.2

            if psi>1.3 and psi<1.5:
                return 70
            if psi<0.8:
                return data[0,9]
            if psi>2:
                return data[data.shape[0]-1,9]
            else:
                data=data[np.where(np.abs(data[:,0]-psi)<0.000000001)[0],:]
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
                    return k * (self.ns - data[index - 1, 2]) + data[index - 1, paramIndex]


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
    boardThick=np.zeros(11)+1
    test=DataSource(101325,293,2760,40921/3600,1450,True,boardThick)