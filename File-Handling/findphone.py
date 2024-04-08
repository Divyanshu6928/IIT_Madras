n=int(input("Search the number : "))

f=open('phone.txt','r')
flag=0
s='0'
while(s!=''):
    s=f.readline()
    if(s!=''):
        a=int(s)
        if(a==n):
            print("Number is already registered !!")
            flag=1
            break
if(flag==0):
    print("Please register your number first")