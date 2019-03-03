import pandas as pd
import numpy as np
import xlrd

a=pd.Series([1,3,5,np.nan,6,8])
a.index
a.values
a[2:5]
a[::2]
a.index=list('abcdef')
a.index.name='索引'
a['a':'c']#不再是左开右闭
date=pd.date_range('19900120',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=date,columns=list('abcd'))
df2=pd.DataFrame({'A':1,'B':pd.Timestamp('20181001'),'C':pd.Series(1,index=list(range(4)),dtype=float),'D':np.array([3]*4,dtype=int),'E':pd.Categorical(['test','train','test','train']),'F':'abc'})
df.head(3)
df2.dtypes
df2.columns
df2.index
df2.values
#pandas读取数据及数据操作
df3=pd.read_excel(r'C:\GitHub\2019.03.02数据分析\moviedata.xlsx')
dit={'名字':'复仇者联盟3','投票人数':23,'类型':'科幻','产地':'美国','上映时间':'2018-10-6','时长':144,'年代':2018,'评分':'9.1','首映时间':'深圳万象天地','投票':np.nan}
b=pd.Series(dit)
b.name=6
df4=df3.append(b)
df4['名字']
df4['新增序号']=range(1,len(df4)+1)
# df4=df4.drop('评分',axis=1)
#通过标签选择数据
df4.loc[1,'名字']
df4.loc[[1,3],['名字','上映时间']]
df4[df4['产地']=='美国']
# df4[((df4.产地=='美国')|(df4.产地=='中国'))&(df4.评分>9.1)]
df4.isnull()
df4[df4['名字'].notnull()]
df4['投票'].fillna(np.mean(df4['投票']),inplace=True)

print(df4)
print(df4[df4['投票'].isnull()])
