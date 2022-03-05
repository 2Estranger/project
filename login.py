import json

print(" *  WELCOM TO THE LOGIN / SIGN-UP   *")
user=input('1.signup/2.login  -->')

if user=='1':
    name=input("enter your name")
    pass1=input("enter your password")

    l,u,s,d = 0,0,0,0
    if len(pass1) >= 6:
        for i in pass1:
            if (i.isupper()):
                u=1
            if (i.islower()):
                l=1
            if (i.isdigit()):
                d=1
            if "@" in pass1 or '#' in pass1 or "$" in pass1:
                s=1
        sum=u+l+s+d
        if sum!=4:        
            print("atleast one should be special character and digit")
        else:
            pass2=input("enter the second password")
            if pass1!=pass2:
                print("both password is not correct")
            elif pass1==pass2:
                hobby=input("enter your hobby")  
                description=input("enter your discription") 
                DOB=(input("enter yor DOB"))
                gender=input("gender")
                d= {}
                l=[]
                d["name"]=name
                d["password"]=pass2
                d['DOB'] = DOB
                d["gender"] = gender
                d['hobby'] = hobby
                d["description"]=description
                l.append(d)
            
                with open("estranger.json","w") as a:
                    json.dump(l,a,indent=4)
                print("your are signed up succesfully")
    else:
        print("password is too short")
# login   
# 
         
elif user=='2':
    name=input("enter your name")
    password=(input("enter your password"))
    with open("loginsignup.json","r")as a:
        f=a.read()
        if name in f:
            if password in f:
                print(name ,"your name is exixt")
        else:
            hobby=input("enter your hobby")  
            description=input("enter your discription") 
            DOB=(input("enter yor DOB"))
            gender=input("gender")
            d= {}
            l=[]
            d["name"]=name
            d["password"]=password
            d['DOB'] = DOB
            d["gender"] = gender
            d['hobby'] = hobby
            d["description"]=description 
            l.append(d) 

            with open("estranger.json","w") as a:
                f=json.dump(l,a,indent=4)
                print("congratulation",name ,"you are logen is sucsessfull")
