from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http  import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Books,Profile
from .forms import CreateUserForm,UpdateUserForm,UpdateUserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        'books': Books.objects.all()
    }
    return render(request, 'index.html' , context)
@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account was successfully created')
                return redirect('login')
        context = {'form': form}
    return render(request,'registration/register.html',  context)

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            if user is not None:   
                login(request, user)
        context={}
        return render(request,'registration/login.html',  context) 
def logoutUser(request):
    logout(request)
    return redirect('login')
class BooksCreateView(LoginRequiredMixin,CreateView):
    model = Books
    fields = ['images', 'title', 'description', 'category']
    template_name = 'add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BooksCreateView(LoginRequiredMixin,CreateView):
    model = Books
    fields = ['title', 'author', ' description', 'category' 'images']
    template_name = 'add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# <app>/<model>_<viewtype>.html
class BooksListView(ListView):
    model = Books  
    template_name = 'index.html'   
    context_object_name = 'books'
    ordering = ['-pub_date']

class BooksCreateView(CreateView):
    model = Books
    template_name = 'add.html'   
    fields= ['images', 'title', 'author', 'description','category']    

class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'add.html'   
    fields= ['title', 'description','category']    

class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'delete.html', context )    

@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)


def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_books = Books.search_category(category)
        message = f"{category}"
        print("Books.......",searched_books)
        return render(request, 'books.html', {"message": message, "books": searched_books})
    else:
        message = "You haven't searched for any books"
        return render(request, 'search.html', {"message": message})
