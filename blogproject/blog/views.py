from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from blog.models import Signup,BlogPost,Comment
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    else:
        # print(f'User:',{request.user})
        posts = BlogPost.objects.all().order_by('-date_posted')
        context={
            'posts':posts
        }
        return render(request,'index.html',context)
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f"Username:",{username})
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Login credentials didn't match")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("/login")
def signup(request):
    return render(request,"signup.html") 
def submitsignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        DOB = request.POST.get('DOB')
        #Age calculation
        if DOB:
            try:
                DOB1 = datetime.strptime(DOB, '%Y-%m-%d')
                today = datetime.today()
                age = today.year - DOB1.year - ((today.month, today.day) < (DOB1.month, DOB1.day))
                if(age>=18):
                    if(password==confirmpassword):
                        my_user=User.objects.create_user(username,email,password)
                        my_user.save()
                        signup=Signup(name=name,email=email,username=username,password=password,DOB=DOB)
                        signup.save()
                        messages.success(request,"Your Signup Details have been saved.Remember the Username and password for the logins!!")
                        return redirect("signup")
                    else:
                        messages.error(request,"Password and confirm password did not match")
                        return redirect("signup")
                else:
                    messages.error(request,"Age is under 18 years not allowed to create blogs.")
                    return redirect("signup")
            except ValueError as e:
                    return HttpResponse(f"Error: {e}")
        else:
            return HttpResponse("Error: 'DOB' not found in signup data")
    

def create_post(request):
    return render(request,'create_post.html')

@login_required
def post_created(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        Catagories=request.POST.get('Catagories')
        author=request.user
        post_created=BlogPost(title=title,content=content,Catagories=Catagories,author=author,date_posted=datetime.today())
        post_created.save()
        messages.success(request,"Your blog has been posted!!")
        return redirect("create_post")
    
def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    if query:
        results = BlogPost.objects.filter(title__icontains=query) 
    else:
        results = []
    context = { 'posts': results}
    return render(request, 'index.html', context)

def catagories(request):
    query = request.GET.get('Catagories','')
    print(query)
    results=BlogPost.objects.filter(Catagories__icontains=query)
    print(results)
    context={'posts':results}
    return render(request,'index.html',context)

def about(request):
    return render(request,"about.html")

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        name = request.user
        content = request.POST.get('content')

        if name and content:
            Comment.objects.create(post=post, name=name, comment_content=content,created_at=datetime.today())
            # return redirect('post_detail', pk=pk)
            return redirect('index')
    
    return render(request, 'index.html', {'post': post, 'comments': comments})
def account_details(request):
    user=Signup.objects.get(username= request.user)
    name=user.name
    email = user.email
    username = user.username
    password = user.password
    date_of_birth = user.DOB

    context={
        'name':name,
        'email':email,
        'username':username,
        'password':password,
        'dob':date_of_birth
    }
    return render(request,'account.html',context)