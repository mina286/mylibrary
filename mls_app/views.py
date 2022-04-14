from django.shortcuts import render,redirect
from django.contrib import  messages
from mls_app.models import Book
from mls_app.models import  Category
import re
from .forms import BookForm,CategoryForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
# Create your views here.
# def index
def index(request):
    #add book from index
    if request.method == 'POST':
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
    #add category from slide bar
    if request.method == 'POST':
        add_category=CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    books=Book.objects.all()
    #first way start calculat number of status availbe and sold an rental
    #not empty
    list_status_for_allbooks=[]
    list_count_for_allstatus=[]
    #empty
    list_status_finalstatus=[]
    list_count_finalstatus=[]  
    for book in books:
        list_status_for_allbooks.append(book.status) 

    for book in books:
        for i in range(0,len(list_status_for_allbooks)): 
            if list_status_for_allbooks[i]==book.status:
                x=list_status_for_allbooks.count(list_status_for_allbooks[i])
                list_count_for_allstatus.append(x)
 
    for y in list_status_for_allbooks:
        if y not in list_status_finalstatus:
            list_status_finalstatus.append(y) 
    #new dic for status and thier counts
    alldic={}
    list_count3=[]
    for z in list_status_for_allbooks:
        for v in list_count_for_allstatus:
                if v not in list_count3 and z not in alldic: 
                    list_count3.append(v)               
                    alldic.update({z:v})
    # end calculat number of status availbe and sold an rental
    #second way start calculat number of status availbe and sold an rental
    allbooks=Book.objects.filter(is_active=True).count()
    countavailble=Book.objects.filter(status='availble').count()
    countrentale=Book.objects.filter(status='rental').count()
    countsold=Book.objects.filter(status='sold').count()

    #second way end calculat number of status availbe and sold an rental


    context={
        'books':Book.objects.all(),
        'category':Category.objects.all(),
        'book_form':BookForm(),
        'category_form':CategoryForm(),
        'alldic':alldic,
        'allbooks':allbooks
    }

    return render(request,'pages/index.html',context) 


#def show book######################################################################################
def books(request):
    context=None
    if request.method=='GET' and 'searchname' in request.GET:
        searchname=request.GET['searchname']
        if searchname:
            book=Book.objects.filter(title__icontains=searchname)
            

    else:
        book=Book.objects.all()

    context={
        'books':book,
        'category':Category.objects.all()
    }
    return render(request,'pages/books.html',context) 


#def update ######################################################################################
def update(request,book_id):
    this_book = Book.objects.get(id=book_id)
    if request.method=='POST':
        this_book = BookForm(request.POST,request.FILES,instance=this_book)
        if this_book.is_valid():
            this_book.save()
            return redirect('/')
    
    context = {
        'book_form':BookForm(instance=this_book), 
    }
    return render(request,'pages/update.html',context) 




#def delete ###########################################################################
def delete(request,book_id):
    this_book = Book.objects.get(id=book_id)
    if request.method=='POST':
        this_book.delete()
        return redirect('/')


    return render(request,'pages/delete.html') 

#def sigin ###########################################################################
def signup(request):
  
    context=None
    if request.method=='GET' and 'btnsigup' in request.GET:
        user_name =request.GET['username']
        email =request.GET['email']

        formuser = SignupForm(request.GET)       
        if  not User.objects.filter(email=email).exists(): 
            if  not User.objects.filter(username=user_name).exists(): 
                if formuser.is_valid():
                    formuser.save()
                    return redirect('/')
                else:
                    messages.error(request,'error valid')

            else:
                messages.error(request,'this username already exists')

        else:
            messages.error(request,'this email already exists')

    
    context ={
        'formfromuser':SignupForm(),
    }

    return render(request,'pages/sigup.html',context) 

#def login ###########################################################################
def signin(request):
    if request.method=='POST' and 'btnlogin' in request.POST: 
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'password error or username')
            



    return render(request,'pages/sigin.html') 


#def login ###########################################################################
def logout(request):    
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')






