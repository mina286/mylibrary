from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),  
    path('books',views.books,name="books"),  
    path('update/<int:book_id>',views.update,name="update"),  
    path('delete/<int:book_id>',views.delete,name="delete"),  
    path('signup',views.signup,name="signup"),  
    path('signin',views.signin,name="signin"),  
    path('logout',views.logout,name="logout"),  

]