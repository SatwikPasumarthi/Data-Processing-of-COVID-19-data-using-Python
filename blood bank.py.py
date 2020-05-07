import array as arr



donor0={'name':"Varun",'age':"18",'bloodgroup':"A+",'branch':"Vidyanagar"}
donor1={'name':"Satwik",'age':"18",'bloodgroup':"A-",'branch':"HDMC"}
donor2={'name':"Karthik",'age':"18",'bloodgroup':"O+",'branch':"Navnagar"}
donor3={'name':"Dhatri",'age':"18",'bloodgroup':"O-",'branch':"KIMS"}
l1=[donor0,donor1,donor2,donor3]

bloodg={'A+':['Rajajinagar','M G Road','Yelhanka'],'A-':['Rajajinagar','Sahkarnagar'],'O+':['Gandhinagar','Nagarbhavi'],'AB+':['Navnagar','HDMC','Vidyanagar'],'AB-':['Navnagar','HDMC','Vidyanagar'],'B+':['Navnagar','HDMC','Vidyanagar']}



n=input("type a for admin and u for user(not working)")
if(n=='a'):
    x=int(input("Enter 1 to see donors and 2 to add donors and any other number searching blood group"))
    if(x==1):
        for i in range(0,len(l1)):
            print(l1[i])
    elif(x==2):
        name=input("Enter the name")
        age=int(input("Enter age"))
        bg=input("Enter bloodgroup")
        branch1=input("Enter Branch")
        donor4={'name':name,'age':age,'bloodgroup':bg,'branch':branch1}
        l1.append(donor4)
        print("The new list of donors is")
        for i in range(0,5):
            print(l1[i], end=" ")
    else:
        bg=input("Enter the blood group you want")
        print(bloodg[bg])
else:
    bg = input("Enter the blood group you want")
    print(bloodg[bg])


