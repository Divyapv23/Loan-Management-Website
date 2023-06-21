from django.urls import path
from backendapp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('categorydetails/',views.categorydetails,name="categorydetails"),
    path('displaycatdetails/',views.displaycatdetails,name="displaycatdetails"),
    path('editcatdetails/<int:dataid>',views.editcatdetails,name="editcatdetails"),
    path('updatcatdetails/<int:dataid>',views.updatcatdetails,name="updatcatdetails"),
    path('deletecat/<int:dataid>',views.deletecat,name="deletecat"),
    path('sectionpage/',views.sectionpage,name="sectionpage"),
    path('sectiondetails/',views.sectiondetails,name="sectiondetails"),
    path('sectiondisplaypage/',views.sectiondisplaypage,name="sectiondisplaypage"),
    path('editsecdetails/<int:dataid>',views.editsecdetails,name="editsecdetails"),
    path('deletesec/<int:dataid>',views.deletesec,name="deletesec"),
    path('uptsecdetails/<int:dataid>',views.uptsecdetails,name="uptsecdetails"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),
    path('enquirypage/',views.enquirypage,name="enquirypage"),
    path('denydetails/<int:dataid>',views.denydetails,name="denydetails"),
    path('loanrequest/',views.loanrequest,name="loanrequest"),
    path('loanaccept/<int:dataid>',views.loanaccept,name="loanaccept"),
    path('loanreject/<int:dataid>',views.loanreject,name="loanreject"),
    path('accformpage/',views.accformpage,name="accformpage")



]