import pandas as pd
import numpy as np
import jieba as jb

file = open('三国演义.txt','r',encoding='utf-8')
# 将内容转为列表
text = jb.lcut(file.read())
jb.load_userdict('人物2.txt')
file2 = open('人物.txt','r',encoding='utf-8')
#所有人物
set = set(file2.read().split('、'))
#排除重复
list=list(set)
value = np.zeros((len(list)))
arr=pd.Series(value,index=list)
for i in text:
    if i in arr:
        arr[i]+=1
result = arr[arr>0]
result = result.sort_values(ascending=False)

#生成云图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签2

plt.bar(result.head(10).index,result.head(10).values)
plt.xlabel('人物名字')
plt.ylabel('人物出现次数')
plt.show()


