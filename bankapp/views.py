from django.shortcuts import render,redirect
from backendapp.models import sectiondb,categorydb
from bankapp.models import enquirydb,loandb,accountdb


# Create your views here.

def homepage(request):
    data=categorydb.objects.all()
    return render(request,"home.html",{'data':data})

def sectionloanpage(request):
    products=sectiondb.objects.all()
    return render(request,"sectionbank.html",{'products':products})

def formpage(request):
    return render(request,"accform.html")

def enuirydetails(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        em=request.POST.get('Email')
        nm=request.POST.get('Number')
        sr=request.POST.get('Service')
        obj=enquirydb(Name=na,Mail=em,Num=nm,Service=sr)
        obj.save()
        return redirect(homepage)


def aboutpage(request):
    return render(request,"about.html")

def servicepage(request,category):
    data=categorydb.objects.all()
    products = sectiondb.objects.filter(category=category)
    return render(request,"service.html",{'data':data,'products':products})

def contactpage(request):
    return render(request,"contact.html")

def loanapp(request):
    return render(request,"loanform.html")

def loanappdetails(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        em=request.POST.get('Email')
        nm=request.POST.get('Number')
        tp=request.POST.get('Type')
        am=request.POST.get('Amount')
        pd=request.POST.get('Period')
        obj=loandb(Name=na,Email=em,Number=nm,Type=tp,Amount=am,Period=pd)
        obj.save()
        return redirect(homepage)

def accountpage(request):
    return render(request,"accounts.html")



def accountpagedetails(request):
    if request.method=="POST":
        pr=request.POST.get('Prefix')
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        dob=request.POST.get('dob')
        gen=request.POST.get('gender')
        add=request.POST.get('address')
        addr=request.POST.get('address1')
        city=request.POST.get('city')
        sta=request.POST.get('state')
        pin=request.POST.get('pincode')
        con=request.POST.get('country')
        num=request.POST.get('no')
        mail=request.POST.get('email')
        nom=request.POST.get('nominee')
        rel=request.POST.get('relation')
        occ=request.POST.get('flexRadioDefault')
        idn=request.POST.get('identification')
        idc=request.FILES['idcard']
        acc=request.POST.get('account')
        cat=request.POST.get('category')
        img=request.FILES['image']
        sig=request.FILES['signature']
        obj=accountdb(Prefix=pr,Firstname=fn,Lastname=ln,Dob=dob,Gender=gen,Address=add,Address1=addr,City=city,
                      State=sta,Pincode=pin,Country=con,No=num,Email=mail,Nominee=nom,Relation=rel,Occupation=occ,
                      Ide=idn,Idcard=idc,Account=acc,Category=cat,Image=img,Sign=sig)
        obj.save()
        return redirect(homepage)


