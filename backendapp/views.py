from django.shortcuts import render,redirect
from backendapp.models import categorydb,sectiondb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from bankapp.models import enquirydb,loandb,accountdb
# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def categorypage(request):
    return render(request,"category.html")

def categorydetails(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        im=request.FILES['Image']
        ds=request.POST.get('description')
        obj=categorydb(Name=na,Image=im,Descript=ds)
        obj.save()
        return redirect(categorypage)

def displaycatdetails(request):
    data=categorydb.objects.all()
    return render(request,"categorydisplay.html",{'data':data})

def editcatdetails(request,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(request,"editcategory.html",{'data':data})

def updatcatdetails(request,dataid):
    if request.method=="POST":
        na=request.POST.get('Name')
        ds=request.POST.get('Descript')
        try:
            img=request.FILES['Image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=na,Descript=ds,Image=file)
        return redirect(displaycatdetails)

def deletecat(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycatdetails)

def sectionpage(request):
    data=categorydb.objects.all()
    return render(request,"section.html",{'data':data})

def sectiondetails(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        ds=request.POST.get('Descript')
        cg=request.POST.get('Category')
        im=request.FILES['Image']
        obj=sectiondb(Name=na,Image=im,Descript=ds,category=cg)
        obj.save()
        return redirect(sectionpage)

def sectiondisplaypage(request):
    data=sectiondb.objects.all()
    return render(request,"sectiondisplay.html",{'data':data})

def editsecdetails(request,dataid):
    data=sectiondb.objects.get(id=dataid)
    da=categorydb.objects.all()
    return render(request,'editsection.html',{'data':data,'da':da})

def deletesec(request,dataid):
    data=sectiondb.objects.filter(id=dataid)
    data.delete()
    return redirect(sectiondisplaypage)

def uptsecdetails(request,dataid):
    if request.method=="POST":
        na=request.POST.get('Name')
        cg=request.POST.get('Category')
        ds=request.POST.get('Descript')
        try:
            img=request.FILES['Image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=sectiondb.objects.get(id=dataid).Image
        sectiondb.objects.filter(id=dataid).update(Name=na,Descript=ds,category=cg,Image=file)
        return redirect(sectiondisplaypage)

def loginpage(request):
    return render(request,"login.html")

def adminpage(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def logoutpage(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def enquirypage(request):
    data=enquirydb.objects.all()
    return render(request,"displayenquiry.html",{'data':data})

def denydetails(request,dataid):
    data=enquirydb.objects.filter(id=dataid)
    data.delete()
    return redirect(enquirypage)

def loanrequest(request):
    data=loandb.objects.all()
    return render(request,"loanappdisplay.html",{'data':data})

def loanaccept(request,dataid):
    data=loandb.objects.filter(id=dataid)
    data.delete()
    return redirect(loanrequest)

def loanreject(request,dataid):
    data=loandb.objects.filter(id=dataid)
    data.delete()
    return redirect(loanrequest)


def accformpage(request):
    data=accountdb.objects.all()
    return render(request,"accappdisplay.html",{'data':data})






