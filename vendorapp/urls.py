from django.urls import path
from vendorapp import views

urlpatterns=[

    path("register/",views.signUpView.as_view(),name="signup"),
    path("login/",views.signin_view,name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
]
