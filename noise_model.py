#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:52:47 2021

@author: kanferg
"""

def sCEMOS_offset(image="",M="",h="",l="",CC="",QE="",Print_i = "True or False", Image_mode=""):
    data=pd.DataFrame()
    for i in range(M):
        df = pd.DataFrame(data=image[i].flatten())
        df = df.T
        data=data.append(df)
        if Print_i: 
            print(i)
    data.reset_index(drop=True,inplace=True)
    # float all the values
    data=data/Image_mode
    # getting electrons
    electron=(data/CC)/QE
    Offset_df=electron.sum(axis=0)
    Offset_df=Offset_df/M
    Offset_df=Offset_df.T
    Offset_mat_1d=Offset_df.values
    offset_mat_2d=np.reshape(Offset_mat_1d,(h,l))
    return electron, Offset_mat_1d, offset_mat_2d               
    
def sCEMOS_Variance(elec="electron",offset_1d="Offset_mat_1d",M="",h="",l=""):
    electro_sq=elec**2
    Offset_mat_1d_sq=offset_1d**2    
    Var_df = pd.DataFrame()
    for i in range(M):
        temp=electro_sq.loc[i]-Offset_mat_1d_sq   # can it be minus ? chack
        temp=temp.T
        Var_df=Var_df.append(temp)
        print(i)
    Var_df_sum=Var_df.sum(axis=0)
    Var_df_sum=Var_df_sum/M
    Var_df_sum_1d=Var_df_sum.values
    Var_df_sum_2d=np.reshape(Var_df_sum_1d,(h,l))
    return Var_df_sum, Var_df_sum_1d, Var_df_sum_2d
