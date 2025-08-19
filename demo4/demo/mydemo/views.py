from django.shortcuts import render
from .forms import user_form

def get_data(request):
    if request.method == 'POST':
        form = user_form(request.POST)

        if form.is_valid():
            sub1 = form.cleaned_data['sub1']
            sub2 = form.cleaned_data['sub2']
            sub3 = form.cleaned_data['sub3']

            total = sub1 + sub2 + sub3
            percentage = (total*100)/300

            final ='pass'

            if percentage < 33 :
                final='fail'
            return render(request,'display_data.html',{'sub1':sub1,'sub2':sub2,'sub3':sub3,'total':total,'percentage':percentage,'final':final})

    
    else : 
        form = user_form()
        return render(request,'input_form.html',{'form':form})