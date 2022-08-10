import numpy as np

def diff_mean(val1, val2):
    percent = round(100*(val2 - val1)/val1,2)
    return percent

def calculate_consecutive_percentage(df, col):
    arr1=[]
    for i in range(1, df.shape[0]-1):
        val1=df.loc[i-1, col]
        val2=df.loc[i, col]
        result=diff_mean(val1, val2)
        arr1.append(result)

    return np.mean(arr1)