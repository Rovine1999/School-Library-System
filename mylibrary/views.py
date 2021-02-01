from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Books
from .forms import CreateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
    fields = ['images', 'title', 'description', 'category']
    template_name = 'post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# <app>/<model>_<viewtype>.html
class BooksListView(ListView):
    model = Books  
    template_name = 'index.html'   
    context_object_name = 'flashcards'
    ordering = ['-pub_date']

class BooksCreateView(CreateView):
    model = Books
    template_name = 'post.html'   
    fields= ['title', 'description','category']    

class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'post.html'   
    fields= ['title', 'description','category']    

class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'delete.html', context )    

