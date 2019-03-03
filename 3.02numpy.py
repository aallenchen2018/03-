import numpy as np
a=np.arange(1,10,2)
b=np.linspace(1,10,22)
c=np.random.randn(1,10)
d=np.random.randint(1,11)
f=np.random.randint(1,10,3)
e=np.random.randint(10)
g=np.array([1,2,3,4,5,6])
g[2]=88
ob=np.array([21001,22033,23088,24086,26989])
obn=ob[1:]-ob[:-1]
aa=np.array([[0,1,2,3],[4,5,6,7]])
aa[1,2]=66
aa1=aa[:,1]
bb=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
bb1=bb[0,1:4]
bb2=bb[2:,2:]
bb3=bb[1,2],bb[1,3]
bb4=bb[2,1:].copy()
bb4[0]=100
cc=np.arange(0,100,10)
index=[1,2,-3]
y=cc[index]
mask=np.array([0,2,2,0,0,1,0,0,1,0],dtype=bool)
cc[mask]
bb=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
bb[(0,1,2),(1,2,3)]
bb[-3:,(1,3)]
bb[(1,3)]
mask2=np.array([0,0,1,1],dtype=bool)
bb>10
bb_con=np.where(bb>10)
bb[bb>10]

#数组类型
z=np.array([1.5,-3],dtype=float)
y=np.array([1,2,3])  #没有改变原数据类型
np.asarray(y,dtype=float)
y.astype(float)  #没有改变原数据类型

#数组操作
mv_name=('肖申克的救赎','控方证人','美丽人生','阿甘正传','霸王别姬')
mv_num=np.array([60098,42890,32897,58763,47896])
mv_score=np.array([9.6,9.5,9.5,9.4,9.4])
mv_length=np.array([142,116,142,171,194])
np.sort(mv_num)
order=np.argsort(mv_num)
mv_name[order[0]]
np.sum(mv_num)
np.max(mv_length)
np.min(mv_score) 
np.std(mv_length)
#多维数组的操作
x=np.arange(6)
x.shape=2,3
xx=x.reshape(3,2)
x.transpose()
w=np.arange(6)
w.shape=2,3
t=np.concatenate((x,w),axis=0)
s=np.concatenate((w,x),axis=1)
q=np.array((w,x))
p=np.vstack((x,w))



print(bb)








