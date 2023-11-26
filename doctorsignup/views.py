from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
pp=''
un=''
em=''
pwd=''
cpwd=''
ad=''
# Create your views here.
def signaction(request):
    global fn,ln,pp,un,em,pwd,cpwd,ad
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Tanmay172@@",database='registration')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstName":
                fn=value
            if key=="lastName":
                ln=value
            if key=="profilePicture":
                s=value
            if key=="username":
                em=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="confirmPassword":
                pwd=value
            if key=="address":
                em=value
                
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,pp,un,em,pwd,cpwd,ad)
        cursor.execute(c)
        m.commit()

    return render(request,'signupdoctor.html')
