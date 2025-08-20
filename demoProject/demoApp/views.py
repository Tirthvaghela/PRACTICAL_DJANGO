from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated
    
    return render(request, 'home.html', {'user': request.user})  # Render home page with user info


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


