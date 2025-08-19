from django.shortcuts import render
from .forms import user_form

def get_data(request):
    if request.method == 'POST':
        form = user_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return render(request,'display_data.html',{'name':name,'age':age})
    
    else : 
        form = user_form()
        return render(request,'input_form.html',{'form':form})