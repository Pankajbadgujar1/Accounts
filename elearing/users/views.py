from django.shortcuts import render ,redirect
from .forms import StudentRegisterForm

# Create your views here.
def login(request):
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


