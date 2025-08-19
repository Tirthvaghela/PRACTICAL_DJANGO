from django.shortcuts import render
from .forms import user_form

def get_data(request):
    if request.method == 'POST':
        form = user_form(request.POST)

        if form.is_valid():
            p = form.cleaned_data['p']
            r = form.cleaned_data['r']
            t = form.cleaned_data['t']

            i = (p * r * t)/100

          
            return render(request,'display_data.html',{'p':p,'r':r,'t':t,'i':i})

    
    else : 
        form = user_form()
        return render(request,'input_form.html',{'form':form})