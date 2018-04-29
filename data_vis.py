#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 02:02:26 2018

@author: deepthisen
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data_Visual:
    
    
    def __init__(self,df,vartype):
        self.df=df
        self.vartype=vartype
        self.mode_=df.mode()
        self.nuniq=len(df.unique())
        self.length=len(df)
    
    def __str__(self):
        pass
    
class nomi_visual(Data_Visual):
    def __init__(self,df,vartype,display_bar):
        super().__init__(df,vartype)
        if display_bar==1:
            self.plt=df.value_counts().plot(kind='bar')
    def piechart(self):
        #print(self.length)
        df=self.df
        labels = list(pd.unique(df))
        sizes = list(df.value_counts())
        patches, texts = plt.pie(sizes)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

class inter_visual(Data_Visual):   
    fact=2
    def __init__(self,df,vartype):
        super().__init__(df,vartype)
        self.mean=df.mean()
        self.stdev=df.std()
        self.max=df.max()
        self.min=df.min()
    def histogram(self,range_type):
        df=self.df
        df_array=np.array(df)
        if range_type=='minmax':
            plthist=plt.hist(df_array,range=(df_array.min(),df_array.max()))
        else:
            left_range=self.mean-(inter_visual.fact*self.stdev)
            right_range=self.mean+(inter_visual.fact*self.stdev)
            plthist=plt.hist(df_array,range=(left_range,right_range))
        plt.title("Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

