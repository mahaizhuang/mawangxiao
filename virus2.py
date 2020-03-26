import matplotlib.pyplot as plt
import xlrd 
import pprint
import numpy as np

from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.family']='sans-serif'
#
book = xlrd.open_workbook(r'C:\\Users\csjmj\Desktop\武汉肺炎趋势预测.xlsx')
sheet = book.sheet_by_name('Sheet1')
#
a3 = '河南省重症病例人数'
a4 = '河南省危重病例人数'
a5 = '河南省累计死亡病例人数'
a6 = '河南省累计治愈病例'
#
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
list2 = []
list3 = []
list4 = [] 
list6 = []
list7 = []
list8 = []
list9 = []
list5 = ['2020/1/23','2020/1/24','2020/1/25','2020/1/26','2020/1/27','2020/1/28','2020/1/29','2020/1/30','2020/1/31',
'2020/2/1','2020/2/2','2020/2/3','2020/2/4','2020/2/5','2020/2/6','2020/2/7','2020/2/8','2020/2/9','2020/2/10',
'2020/2/11','2020/2/12','2020/2/13','2020/2/14','2020/2/15','2020/2/16','2020/2/17','2020/2/18','2020/2/19',
'2020/2/20','2020/2/21','2020/2/22','2020/2/23','2020/2/24','2020/2/25','2020/2/26','2020/2/27','2020/2/28','2020/2/29',
'2020/3/1','2020/3/2','2020/3/3','2020/3/4','2020/3/5','2020/3/6','2020/3/7','2020/3/8','2020/3/9','2020/3/10','2020/3/11',
'2020/3/12','2020/3/13','2020/3/14']
r1 = 2
r2 = 2 
r3 = 2
r6 = 2
r7 = 2 
r8 = 2 
r9 = 2
r4 = len(list1)-1
r5 = len(list1)+1
r10 = len(list1)+1
print(r4)
for i in range(8):
    if i == 1:
        while r1 <=r5:
            row1 = sheet.cell(i,r1).value
            list2.append(row1)
            r1 = r1 + 1 
    elif i == 2:
        while r2 <=r5:
            row1 = sheet.cell(i,r2).value
            list3.append(row1)
            r2 = r2 + 1
    elif i == 3:
        while r3 <=r5:
            row1 = sheet.cell(i,r3).value
            list4.append(row1)
            r3 = r3 + 1 
    elif i == 4: 
        while r6 <=r5:
            row1 = sheet.cell(i,r6).value
            list6.append(row1)
            r6 = r6 + 1 
    elif i == 5: 
        while r7 <=r5:
            row1 = sheet.cell(i,r7).value
            list7.append(row1)
            r7 = r7 + 1 
    elif i == 6: 
        while r8 <=r5:
            row1 = sheet.cell(i,r8).value
            list8.append(row1)
            r8 = r8 + 1 
    elif i == 7: 
        while r9 <=r5:
            row1 = sheet.cell(i,r9).value
            list9.append(row1)
            r9 = r9 + 1 
#             
print(list1)
print(list2)
x = list1
y = list3
y1 = list4
y2 = list6
y3 = list7 
y4 = list8
#
fig = plt.figure(num=1,facecolor='linen',frameon=True)
ax25 = fig.add_axes([0.06,0.1,0.89,0.85])
ax25 = plt.plot(x,y4,marker='o',color='green',label=a6,linestyle='--',mfc='red',mec='red',ms=4)
ax25 = plt.legend(fontsize=8)
fig = plt.xlim(0,20)
fig = plt.ylim(0,1500)
fig = plt.xlabel('日期',fontdict=None,labelpad=None,color='k',fontsize=12)
fig = plt.ylabel('相关人数',fontdict=None,labelpad=None,color='k',fontsize=12)
fig = plt.axhspan(0,1500,facecolor='silver')
#
i1 = 0
while i1 <=r4:
    ax25 = plt.text(list1[i1],list8[i1],list8[i1],fontsize=9,color='k',horizontalalignment='center',verticalalignment='bottom',rotation=30)
    i1 = i1 + 1
#
x_ticks=np.linspace(1,20,20)
y_ticks=np.linspace(0,1500,11)
y_major_locator=MultipleLocator(20)
axx1=plt.gca()
axx1.yaxis.set_major_locator(y_major_locator)   
axx1.spines['right'].set_color('k')
axx1.spines['right'].set_visible(False)
#
axx1.spines['top'].set_color('k')
axx1.spines['top'].set_visible(False)
#
axx1.spines['left'].set_color('k')
axx1.spines['left'].set_visible(False)
#
axx1.spines['bottom'].set_color('k')
#
axx1.xaxis.set_ticks_position('bottom')
axx1.spines['bottom'].set_position(('data',0))
axx1.yaxis.set_ticks_position('left')
axx1.spines['left'].set_position(('data',0))
#
fig = plt.xticks(x_ticks,list5,rotation=60)
fig = plt.yticks(y_ticks)
fig = plt.show()

#
fig1 = plt.figure(num=2,facecolor='linen',frameon=True)
axx2 = fig1.add_axes([0.06,0.1,0.89,0.85])
ax22 = plt.plot(x,y1,marker='o',color='yellow',label=a3,linestyle='--',mfc='red',mec='red',ms=4)
ax22 = plt.legend(fontsize=8)
ax23 = plt.plot(x,y2,marker='o',color='sienna',label=a4,linestyle='--',mfc='red',mec='red',ms=4)
ax23 = plt.legend(fontsize=8)
ax24 = plt.plot(x,y3,marker='o',color='steelblue',label=a5,linestyle='--',mfc='red',mec='red',ms=4)
ax24 = plt.legend(fontsize=8)

fig1 = plt.xlim(0,r10)
fig1 = plt.ylim(0,100)
fig1 = plt.xlabel('日期',fontdict=None,labelpad=None,color='k',fontsize=12)
fig1 = plt.ylabel('相关人数',fontdict=None,labelpad=None,color='k',fontsize=12)
fig1 = plt.axhspan(0,100,facecolor='silver')
#
i1 = 0
while i1 <=r4:
    ax22 = plt.text(list1[i1],list4[i1],list4[i1],fontsize=9,color='k',horizontalalignment='center',verticalalignment='bottom')
    i1 = i1 + 1
i1 = 0
#
while i1 <=r4:
    ax23 = plt.text(list1[i1],list6[i1],list6[i1],fontsize=9,color='k',horizontalalignment='center',verticalalignment='bottom')
    i1 = i1 + 1
i1 = 0
#
while i1 <=r4:
    ax24 = plt.text(list1[i1],list7[i1],list7[i1],fontsize=9,color='k',horizontalalignment='center',verticalalignment='bottom')
    i1 = i1 + 1
#
x_ticks=np.linspace(1,r10,r10)
y_ticks=np.linspace(0,100,11)
y_major_locator=MultipleLocator(20)
#
axx2=plt.gca()
axx2.yaxis.set_major_locator(y_major_locator)
axx2.spines['right'].set_color('k')
axx2.spines['right'].set_visible(False)
#
axx2.spines['top'].set_color('k')
axx2.spines['top'].set_visible(False)
#
axx2.spines['left'].set_color('k')
axx2.spines['left'].set_visible(False)
#
axx2.spines['bottom'].set_color('k')
#
axx2.xaxis.set_ticks_position('bottom')
axx2.spines['bottom'].set_position(('data',0))
axx2.yaxis.set_ticks_position('left')
axx2.spines['left'].set_position(('data',0))
#
fig1 = plt.xticks(x_ticks,list5,rotation=60)
fig1 = plt.yticks(y_ticks)
fig1 = plt.show()