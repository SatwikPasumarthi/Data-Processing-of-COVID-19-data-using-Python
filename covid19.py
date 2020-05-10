import xlrd as xl 
import datetime 
import pandas as pd
import webbrowser
import matplotlib as mat
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import random
path='C:\\time_series_covid_19_deaths.xlsx'
path1='C:\\time_series_covid_19_recovered.xlsx'
path2='C:\\time_series_covid_19_confirmed.xlsx'
path3='C:\\AgeGroupDetails.xlsx'
wb=xl.open_workbook(path)
wb1=xl.open_workbook(path1)
wb2=xl.open_workbook(path2)
wb3=xl.open_workbook(path3)
sheet=wb.sheet_by_index(0)
sheet1=wb1.sheet_by_index(0)
sheet2=wb2.sheet_by_index(0)
sheet3=wb3.sheet_by_index(0)
wb_date=wb1.datemode
country=[]
cordila=[]
cordilo=[]
ndeaths=[]
nrecover=[]
ncases=[]
totald=[]
totalr=[]
for i in range(1,sheet.nrows):
    country.append(sheet.cell_value(i,1).lower())
    cordila.append(sheet.cell_value(i,2))
    cordilo.append(sheet.cell_value(i,3))
dicc={country[j]:[cordila[j],cordilo[j]] for j in range(len(country))}
for i1 in range(1,sheet.nrows):
    tempc=[]
    for j1 in range(4,sheet.ncols):
        if sheet.cell_value(i1,j1)=='':
            pass
        else:
            if type(sheet.cell_value)==float:
                tempc.append(int(sheet.cell_value(i1,j1)))
            else:
                tempc.append(int(sheet.cell_value(i1,j1)))
        ndeaths.append(tempc)
    totald.append(sum(tempc))
dicco={country[j2]:totald[j2] for j2 in range(len(country))}
for i2 in range(1,sheet1.nrows):
    tempr=[]
    for j2 in range(4,sheet1.ncols):
        tempr.append(int(sheet1.cell_value(i2,j2)))
        nrecover.append(tempr)
    totalr.append(sum(tempr))
diccor={country[j2]:totalr[j2] for j2 in range(len(country))}
dicdata={}
dates=[]
for l in range(4,sheet1.ncols):
    value=sheet1.cell_value(0,l)
    value1=datetime.datetime.strptime(value,'%m/%d/%y').strftime('%d-%m-%y')
    dates.append(value1)
f=open('total.txt','w+')
rgt=[]
totalc=[]
for i3 in range(1,sheet2.nrows):
    tempc=[]
    for j3 in range(4,sheet2.ncols):
        if type(sheet2.cell_value)==float:
            tempc.append(int(sheet2.cell_value(i3,j3)))
        else:
            tempc.append(int(sheet2.cell_value(i3,j3)))
    totalc.append(sum(tempc))
    ncases.append(tempc)
dicdata=pd.DataFrame({country[k]:[totald[k],totalr[k],totalc[k]] for k in range(len(country))}).transpose()  #add here 
dicdata.columns=['DEATHS','RECOVERED','CONFIRMED']                                                             #change here              
dicdata.to_csv('total.txt',header=True,index=True,sep='\t',mode='a')
for j4 in range(len(totalc)):
    if totalc[j4]==0 or totalc[j4]==1:
        rgt.append(random.choice([44,62,26]))
    else:
        rgt.append((totald[j4]/totalc[j4])*100)
red=[]
rgtr=[]
for j5 in range(len(country)):
    if rgt[j5]>=2:
        red.append(country[j5]) 
        rgtr.append(rgt[j5])
    else:
        pass
print('THE TWO FOLLOWING BAR-GRAPHS ARE DEATH RATE IN HIGH RISK COUNTRIES AND DEATH RATE IN ALL COUNTRIES\n')
x=rgtr
y=red
plt.tick_params(axis="x", labelsize=5)
plt.tick_params(axis="y", labelsize=10)
plt.xticks(rotation=90)
mat.pyplot.title('DEATH RATE IN HIGH RISK COUNTRIES',loc='center')
mat.pyplot.xlabel('COUNTRIES')
mat.pyplot.ylabel('NUMBERS')
plt.bar(y,x,color=['red','blue','green'])
plt.show()
x1=rgt
y1=country
plt.tick_params(axis='x',labelsize=3)
plt.tick_params(axis='y',labelsize=10)
plt.xticks(rotation=90)
mat.pyplot.title('DEATH RATE IN SOME COUNTRIES',loc='center')
mat.pyplot.xlabel('COUNTRIES')
mat.pyplot.ylabel('NUMBERS')
plt.bar(y1,x1,color=['red','blue','green'])
plt.show()
dicrgt={country[k1]:ncases[k1] for k1 in range(len(country))}
dicrgtd={country[k1]:ndeaths[k1] for k1 in range(len(country))}
dicrgtr={country[k1]:nrecover[k1] for k1 in range(len(country))}
print('THE FOLLOWING GRAPHS SHOW NUMBER OF CASES & DEATHS & RECOVERIES\n')
name=input('ENTER THE NAME OF COUNTRY FOR DATE WISE GRAPH\n').lower()
x2=dates[::2]
while (1):
    if name in dicrgt.keys():
        break
    elif name=='south korea' or name=='southkorea':
        name='south korea'
    elif name=='america':
        name='us'
    else:
        name=input('ENTER A VALID COUNTRY')
print(name)
h2=dicrgt[name]
h9=dicrgtd[name]
h8=dicrgtr[name]
y2=h2[::2]
y9=h9[::2]
y8=h8[::2]
plt.tick_params(axis='x',labelsize=3)
plt.tick_params(axis='y',labelsize=10)
plt.xticks(rotation=90)
mat.pyplot.title(name,loc='center')
mat.pyplot.xlabel('DATES')
mat.pyplot.ylabel('NUMBER OF CASES')
plt.plot(x2,y2,label='CASES')
plt.legend()
plt.show()
plt.tick_params(axis='x',labelsize=3)
mat.pyplot.title(name,loc='center')
plt.plot(x2,y9,label='DEATHS')
mat.pyplot.ylabel('NUMBER OF DEATHS')
plt.xticks(rotation=90)
plt.legend()
plt.show()
plt.tick_params(axis='x',labelsize=3)
mat.pyplot.title(name,loc='center')
plt.plot(x2,y8,label='RECOVERIES')
mat.pyplot.ylabel('NUMBER OF RECOVERIES')
plt.xticks(rotation=90)
plt.legend()
plt.show()
f1=open('redzo.txt','w+')
for b2 in range(len(red)):
    f1.write(red[b2]+'\n')
f1.close()
p6=int(input('FOR A TEXT FILE CONTAINING LIST OF DANGEROUS COUNTRIES FOR NEXT TWO YEARS TO VISIT ENTER 1 FOR A NORMAL LIST IN TERMINAL ENTER 2\n'))
while(1):
    if p6==1:
        webbrowser.open('redzo.txt')
        break
    elif p6==2:
        print(red)
        break
    else:
        p6=int(input('ENTER A VALID INPUT\n'))
namec=input('ENTER THE COUNTRY NAME TO VIEW THE GRAPHICAL REPRESNTATION OF AVERAGE WEEKLY STATISTICS\n').lower()
while(1):
    if namec in country:
        break
    elif namec=='south korea' or namec=='southkorea':
        namec='south korea'
        break
    elif namec=='america':
        namec='us'
    else:
        namec=input('THE ENTERED NAME IS NOT CORRECT TRY ANOTHER COUNTRY OR TRY ANOTHER NAME OF SAME COUNTRY\n')
tem=dicrgt[namec]
temd=dicrgtd[namec]
temr=dicrgtr[namec]
avcases=[]
avdeaths=[]
avrecover=[]
jsum=0
jsum1=0
jsum2=0
b=0
while(b<7):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(7<=b<14):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(14<=b<21):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(21<=b<35):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(35<=b<42):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(42<=b<49):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(49<=b<56):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(56<=b<63):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(63<=b<70):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
while(70<=b<75):
    jsum=jsum+tem[b]
    jsum1=jsum1+temd[b]
    jsum2=jsum2+temr[b]
    b+=1
avcases.append(jsum/7)
avdeaths.append(jsum1/7)
avrecover.append(jsum2/7)
x3=['WEEK-1','WEEK-2','WEEK-3','WEEK-4','WEEK-5','WEEK-6','WEEK-7','WEEK-8','WEEK-9','WEEK-10']
y3=avcases
y4=avdeaths
y5=avrecover
mat.pyplot.title(namec,loc='center')
mat.pyplot.xlabel('DATES')
mat.pyplot.ylabel('AVERAGE VALUES OF CASES')
plt.xticks(rotation=90)
plt.plot(x3,y3)
plt.show()
mat.pyplot.title(namec,loc='center')
plt.xticks(rotation=90)
plt.plot(x3,y4)
mat.pyplot.ylabel('AVERAGE VALUE OF DEATHS')
plt.show()
plt.xticks(rotation=90)
mat.pyplot.title(namec,loc='center')
plt.plot(x3,y5)
mat.pyplot.ylabel('AVERAGE VALUE OF RECOVER')
plt.show()
p7=int(input('FOR CHECKING A COUNTRY IS IN DANGER LIST OR NOT ENTER 1 ELSE ENTER 2'))
while(1):
    if p7==1:
        nam=input('ENTER THE NAME OF COUNTRY TO SEARCH\n').lower()
        if nam=='india':
            print('THE ENTERED COUNTRY IS NOT A DANGER COUNTRY\n')
        elif nam=='america' or 'us':
            print('THE ENTERED COUNTRY IS A DANGER COUNTRY\n')
        elif nam=='south korea' or 'southkorea':
            print('THE ENTERED COUNTRY IS NOT A DANGER COUNTRY\n')
        elif nam in red:
            print('THE ENTERED COUNTRY IS DANGER COUNTRY\n')
        else:
            print('THE ENTERED COUNTRY IS NOT A DANGER COUNTRY\n')
        break
    elif p7==2:
        break
    else:
        p7=int(input('ENTER A VALID ENTRY\n'))
        break
ages=[]
per=[]
for g in range(2,sheet3.nrows):
    if sheet3.cell_value(g,1)=='':
        pass
    else:
        ages.append(sheet3.cell_value(g,1))
per=[3.18,3.90,24.86,21.10,16.18,11.13,12.86,4.05,1.45,1.30]
expl=[0,0,0.1,0,0,0,0,0,0,0]
plt.title('AGES AND PERCENTAGE OF DEATHS IN THAT AGE')
plt.pie(per,explode=expl,labels=ages,autopct='%1.1f%%',shadow=True,startangle=180)
plt.axis('equal')
plt.show()
didt={red[l4]:rgtr[l4] for l4 in range(len(red))}
didts=dict(sorted(dicco.items(),key=lambda kv:(kv[1],kv[0])))
print('THE TOP 15 COUNTRIES THAT ARE DANGEROUS TO VIST ARE \n')
lis=list(didts.keys())
print(lis[-1:-16:-1])
