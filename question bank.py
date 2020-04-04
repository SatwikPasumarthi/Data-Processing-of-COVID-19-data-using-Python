import pandas as pd
import random
df = pd.read_excel(r'C:\Users\ruttu\Desktop\CurrencyData File.xlsx')
df.to_dict()
def qp(c):
    list2 = []
    listmain = []
    k=1
    file.write("Name :\n\n")
    file.write("Registration Number :\n\n")
    file.write("\t\t\t\t\tQuestion Paper\n")
    for j in range(c,c+18):
        string1 = 'k'
        file.write(str(k) )
        file.write(" What is the symbol of ")
        file.write(df['Unnamed: 1'][j])
        for g in range(0,3):
            l=random.choice(list(df['Unnamed: 2']))
            list2.append(l)
        listmain.append(df['Unnamed: 2'][j])
        listmain.append(list2[0])
        listmain.append(list2[1])
        listmain.append(list2[2])
        random.shuffle(listmain)
        p = listmain[0]
        q = listmain[1]
        r = listmain[2]
        s = listmain[3]
        file.write("\na. ")
        file.write(p)
        file.write("\nb. ")
        file.write(q)
        file.write("\nc. ")
        file.write(r)
        file.write("\nd. ")
        file.write(s)
        file.write("\n")
        k = k+1
    file.close()
def a(c):
    k=1
    answer.write("\t\t\t\t\tAnswer Sheet\n")
    for j in range(c,c+18):
        answer.write(str(k))
        answer.write(" ")
        answer.write(df['Unnamed: 2'][j])
        answer.write("\n")
        k= k+1
    answer.close()
c=1
file= open('questionPaper[1].txt','w')
answer = open('answerpaper[1].txt','w')
qp(c)
a(c)
c=18
file= open('questionPaper[2].txt','w')
answer = open('answerpaper[2].txt','w')
qp(c)
a(c)
c=36
file= open('questionPaper[3].txt','w')
answer = open('answerpaper[3].txt','w')
qp(c)
a(c)
c=54
file= open('questionPaper[4].txt','w')
answer = open('answerpaper[4].txt','w')
qp(c)
a(c)
c=72
file= open('questionPaper[5].txt','w')
answer = open('answerpaper[5].txt','w')
qp(c)
a(c)
c=90
file= open('questionPaper[6].txt','w')
answer = open('answerpaper[6].txt','w')
qp(c)
a(c)
c=108
file= open('questionPaper[7].txt','w')
answer = open('answerpaper[7].txt','w')
qp(c)
a(c)
c=126
file= open('questionPaper[8].txt','w')
answer = open('answerpaper[8].txt','w')
qp(c)
a(c)
c=144
file= open('questionPaper[9].txt','w')
answer = open('answerpaper[9].txt','w')
qp(c)
a(c)
c=162
file= open('questionPaper[10].txt','w')
answer = open('answerpaper[10].txt','w')
qp(c)
a(c)


    

   