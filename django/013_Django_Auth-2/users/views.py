from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages

from .forms import UserForm, UserProfileForm

from django.contrib.auth.forms import AuthenticationForm

# !==================HOME==========================
def home(request):
    return render(request, 'users/home.html')



# !==================LOGOUT==========================
def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect("home")


# !==================REGİSTER==========================
def register(request):
    form_user =UserForm()
    form_profile =  UserProfileForm()
    if request.method=="POST":
         form_user = UserForm(request.POST)
         form_profile= UserProfileForm(request.POST, request.FILES)
         if form_user.is_valid() and form_profile.is_valid():
              user =  form_user.save()
              profile = form_profile.save(commit=False) #Kaydetme bekle
              profile.user=user
              profile.save()

              login(request,user) # logine yönlendir

    context={
        "form_profile":form_profile,
        "form_user":form_user
    }
    return render(request, 'users/register.html', context) 




# !==================LOGİN==========================
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
         # username = form.cleaned_data('username')
        # password = form.cleaned_data('password')

        # user = authenticate(username=username, password=password)
     
         #yukarıdaki uç satır için get_user tek başına yeterli

        user=form.get_user()
        if user :
            messages.success(request,'login successfully')
            login(request, user)
 
            return redirect('home')  # form doluysa buraya değilde aşağıyı render ediyor

    return render(request, 'users/user_login.html', {'form': form})