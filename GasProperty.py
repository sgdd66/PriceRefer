#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""空气物性算法"""
import math as mt

class GasProperty(object):

    def __init__(self,P,T,phi):

        self.Ra= 287.06 
        self.Rv= 461.52 
        self.Mrda= 28.96 
        self.Mrv= 18.016 
        self.P=P
        self.T=T
        self.phi=phi


    #计算温度T下的水蒸气饱和压力
    def getPs(self,T):

        return 2000*mt.exp(18.5916-3991.11/((T-273.15)+233.84))/15.0 


    #获取密度
    def getdensity(self):
        P=self.P
        T=self.T
        Ra=self.Ra
        phi=self.phi

        return P/(Ra*T)*(1-0.378*(phi*self.getPs(T)/P)) 



    def getd(self):
        phi=self.phi
        P=self.P
        T=self.T
    
        return 0.622*(phi*self.getPs(T)/(P-phi*self.getPs(T)))
    


    def getHeatCapacityOfDryAir(self):
        T=self.T
        return 1006.87-0.08722*T+1.236/10000*T*T 
    


    def getHeatCapacityOfVapour(self):
        T=self.T
        return 1853.14+0.6133*T+1.014/1000*T*T 



    def getHeatCapacityOfMixedAir(self):
    
        Cpda=self.getHeatCapacityOfDryAir()
        d=self.getd()
        Cpv=self.getHeatCapacityOfVapour()
        return Cpda/(1+d)*(1+d*Cpv/Cpda) 
    


    # 获取干空气的动力粘度
    def getKineticViscosityOfDryAir(self):
    
        t= self.T-273.15
        return (17.4945+4.799/100*t-3.5256/100000*t*t)/1000000 
    


    # 获取水蒸气的动力粘度
    def getKineticViscosityOfVapour(self):
    
        T=self.T
        return (8.1084+4.011/100*T-1.7858/100000*T*T)/1000000 
    


    def getKineticViscosityOfMixedAir(self):

        mu_da= self.getKineticViscosityOfDryAir()
        mu_v= self.getKineticViscosityOfVapour()
        d= self.getd()
        return mu_da*(1+1.268*mu_v/mu_da*d)/(1+1.28*d) 



    # 获取干空气的导热系数
    def getThermalConductivityOfDryAir(self):

        t= self.T-273.15
        return (2.4587+7.5855/1000*t-1.69/1000000*t*t)/100 



    # 获取水蒸气的导热系数
    def getThermalConductivityOfVapour(self):
        T=self.T
        return (1.6+6.179/1000*T+2.7535/100000*T*T)/100 



    # 获取混合空气的导热系数
    def getThermalConductivityOfMixedAir(self):

        mu_da= self.getKineticViscosityOfDryAir() 
        mu_v= self.getKineticViscosityOfVapour() 
        d= self.getd() 
        lambda_da= self.getThermalConductivityOfDryAir() 
        lambda_v= self.getThermalConductivityOfVapour() 
        return 4.56724*lambda_da/pow(1+0.8881*mt.sqrt(mu_da/mu_v),2)*(1/(1+1.60746*d)+lambda_v/lambda_da/(1+mu_v/mu_da/d))

