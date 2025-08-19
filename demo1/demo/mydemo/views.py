from django.shortcuts import render
from .forms import user_form

def get_data(request):
    if request.method == 'POST':
        form = user_form(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            res = a+b
            return render(request,'display_data.html',{'a':a ,'b':b,'res':res})
    
    else : 
        form = user_form()
        return render(request,'input_form.html',{'form':form})