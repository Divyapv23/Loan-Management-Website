from django.urls import path
from bankapp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('sectionloanpage/',views.sectionloanpage,name="sectionloanpage"),
    path('formpage/',views.formpage,name="formpage"),
    path('enuirydetails/',views.enuirydetails,name="enuirydetails"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('servicepage/<category>/',views.servicepage,name="servicepage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('loanapp/',views.loanapp,name="loanapp"),
    path('loanappdetails/',views.loanappdetails,name="loanappdetails"),
    path('accountpage/',views.accountpage,name="accountpage"),
    path('accountpagedetails/',views.accountpagedetails,name="accountpagedetails")


]