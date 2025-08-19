from django.shortcuts import render
from .forms import user_form

def get_data(request):
    if request.method == 'POST':
        form = user_form(request.POST)

        if form.is_valid():
            num = form.cleaned_data['num']
            if num % 2 ==0 :
                num="Even"
            else :
                num="Odd"
            return render(request,'display_data.html',{'num':num})

    
    else : 
        form = user_form()
        return render(request,'input_form.html',{'form':form})