
# import matplotlib.pyplot as plt
# x=[x for x in range(1,20,2)]
# # print(x)
# y=[15,34,23,20,14,20,35,27,19,28]
# # 设置 图片大小； 每英寸上 点的像素 为 80
# fig=plt.figure(figsize=(20,8),dpi=80)
# # 通过plot 绘制折线图
# plt.plot(x,y,'r')
#
# #设置 指定的x 轴刻度
# plt.xticks(x)
# plt.yticks(range(min(x),max(y)+1))
# # 保存
# # plt.savefig('')
# plt.show()

# # 例1：
# import matplotlib.pyplot as plt
# import random
# # 设置字体
# plt.rcParams['font.sans-serif']=['Simhei']
#
# t=[i for i in range(0,120)]
# T=[random.randint(20,35) for i in range(120)]
# # 设置图片大小
# fig=plt.figure(figsize=(40,20),dpi=50)
# plt.plot(t,T,'r')
# # 设置坐标轴格式
# _x=t[::3]
# # _xticks_labels=['hello,{}'.format(i) for i in _x]
# _xticks_labels=['10点{}分'.format(i) for i in range(60)]
# _xticks_labels+=['11点{}分'.format(i) for i in range(60)]
# # 取步长，数字和字符串一一对应， 数据长度一样
# # rotation=90 x 轴标签旋转90 度
# plt.xticks(_x,_xticks_labels[::3],rotation=45,fontsize=15)
#
# # 添加描述信息
# plt.xlabel('时间',fontsize=20)
# plt.ylabel('温度',fontsize=20)
# plt.title('10：00到12;00气温每分钟的变化情况',fontsize=20)
# plt.show()

# 例2
import matplotlib.pyplot as plt
x=[age for age in range(11,31)]
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
plt.rcParams['font.sans-serif']=['Simhei']
# 设置图片大小
fig=plt.figure(figsize=(35,20),dpi=50)
# 画图
plt.plot(x,y,'r')
# 设置x 轴 刻度
plt.xticks(x,fontsize=18)
plt.yticks(y,fontsize=18)
plt.xlabel('年龄',fontsize=16)
plt.ylabel('男/女朋友个数',fontsize=16)
plt.show()


