from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Home"),
    path('login/', views.login, name="Login"),
    path('signup/', views.signup, name="SignUp"),
    path('userHome/', views.userHome, name="UserHome"),
    path('userHome/updateUser/<str:id>', views.updateUser, name="UpdateUser"),
    path('userHome/deleteUser/<str:id>', views.deleteUser, name="DeleteUser"),
    path('logout/', views.logout, name="Logout")
]