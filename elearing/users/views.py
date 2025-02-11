from django.shortcuts import render ,redirect
from .forms import StudentRegisterForm

# Create your views here.

def home(request):
    return render(request, 'users/HomePage.html')

def login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('teachers_home')
            else:
                messages.info(request, 'Username or Password is incorrect')
    return render(request, 'users/login.html')




def register(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            user = form.save()
            # login(request, user)
            return redirect('login_student')
            
    else:
        form = StudentRegisterForm()
    return render(request, 'users/register.html', {'form': form})


