import pandas as pd
import random
import matplotlib.pyplot as plt
fig = plt.figure()
df = pd.read_excel(r'C:\Users\HP\Desktop\CropsDataFile.xlsx')
df.to_dict()
print("n=1 -> To view the graph of given crop's production ")
print("n=2 -> To view the file of crops in a given year ")
n = int(input("Enter either n=1 or n=2"))
if(n==1):
    prosum0 = 0
    prosum1 = 0
    prosum2 = 0
    prosum3 = 0
    prosum4 = 0
    prosum5 = 0
    prosum6 = 0
    prosum7 = 0
    crop_name = input("Enter the crop name")
    year = df['Unnamed: 2'].tolist()
    crop = df['Unnamed: 4'].tolist()
    production1 = df['Unnamed: 6'].tolist()
    for i in range(0,300):
        if(crop_name==crop[i]):
            if(year[i]==2000):
                prosum0 +=production1[i]
            elif(year[i]==2001):
                prosum1 +=production1[i]
            elif(year[i]==2002):
                prosum2 +=production1[i]
            elif(year[i]==2003):
                prosum3 +=production1[i]
            elif(year[i]==2004):
                prosum4 +=production1[i]
            elif(year[i]==2005):
                prosum5 +=production1[i]
            elif(year[i]==2006):
                prosum6 +=production1[i]
            elif(year[i]==2010):
                prosum7 +=production1[i]
    graph = fig.add_axes([0,0,1,1])
    year =[2000,2001,2002,2003,2004,2005,2006,2010]
    production = [prosum0,prosum1,prosum2,prosum3,prosum4,prosum5,prosum6,prosum7]
    graph.bar(year,production)
    plt.show()
if(n==2):
    prosumA = 0
    prosumOK = 0
    prosumR = 0
    prosumB = 0
    prosumC = 0
    prosumCo = 0
    prosumD = 0
    prosumS = 0
    prosumSp = 0
    prosumT = 0
    year1 = int(input("Enter the year"))
    year = df['Unnamed: 2'].tolist()
    crop = df['Unnamed: 4'].tolist()
    production1 = df['Unnamed: 6'].tolist()
    for i in range(0,300):
        if(year1==year[i]):
            if(crop[i]=='Arecanut'):
                prosumA +=production1[i]
            elif(crop[i]=='Other Kharif'):
                prosumOK +=production1[i]
            elif(crop[i]=='Rice'):
                prosumR +=production1[i]
            elif(crop[i]=='Banana'):
                prosumB +=production1[i]
            elif(crop[i]=='Cashewnut'):
                prosumC +=production1[i]
            elif(crop[i]=='Coconut'):
                prosumCo +=production1[i]
            elif(crop[i]=='Dry ginger'):
                prosumD +=production1[i]
            elif(crop[i]=='Sugarcane'):
                prosumS +=production1[i]
            elif(crop[i]=='Sweet potato'):
                prosumSp +=production1[i]
            elif(crop[i]=='Tapioca'):
                prosumT +=production1[i]
    file = open('yearwisedata.txt','w')
    file.write("\t\t\t\t\t\t\t")
    file.write(str(year1))
    file.write(" year Data")
    file.write("\nArecanut -> ")
    file.write(str(prosumA))
    file.write("\nOther Kharif -> ")
    file.write(str(prosumOK))
    file.write("\nRice -> ")
    file.write(str(prosumR))
    file.write("\nBanana -> ")
    file.write(str(prosumB))
    file.write("\nCashewnut -> ")
    file.write(str(prosumC))
    file.write("\nCoconut -> ")
    file.write(str(prosumCo))
    file.write("\nDry ginger -> ")
    file.write(str(prosumD))
    file.write("\nSugarcane -> ")
    file.write(str(prosumS))
    file.write("\nSweet potato -> ")
    file.write(str(prosumSp))
    file.write("\nTapioca -> ")
    file.write(str(prosumT))
    file.close()
count=209
access=int(input('enter 1 for USER purpose and any number for admin purpose\t'))
if (access!=1):
    a=int(input('Hi ADMIN! Enter number of crops u want to add in the data\t'))
    for i in range(1,a+1):
        s=input('enter the state name of crop '+"%d"%(i)+' data\t')
        df['crop_production'][count+i].append(s)
        dname=input('enter the district name of crop '+"%d"%(i)+' data '+'in '+"%s"%(s)+' state\t')
        df['Unnamed: 1'][count+i].append(dname)
        cropyear=int(input('enter crop year of crop '+"%d"%(i)+' data\t'))
        df['Unnamed: 2'][count+i].append(cropyear)
        season=input('enter the season of crop '+"%d"%(i)+' data in which the crop grows\t')
        df['Unnamed: 3'][count+i].append(season)
        cropname=input('enter the name of crop '+"%d"%(i)+' data\t')
        df['Unnamed: 4'][count+i].append(cropname)
        area=int(input('enter the Area of crop '+"%d"%(i)+' data\t'))
        df['Unnamed: 5'][count+i].append(area)
        production=int(input('enter the Production of crop '+"%d"%(i)+' data\t'))
        df['Unnamed: 6'][count+i].append(production) 
    