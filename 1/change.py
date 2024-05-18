file=open('人物.txt','r',encoding='utf-8')
file2=open('人物2.txt','w',encoding='utf-8')
str=file.read()
print(str)
list=str.split('、')
for i in list:
    file2.write(i)
    file2.write('\n')