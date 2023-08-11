from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.forms import studentregis
# Create your views here.

def show_form_data(request):
    if request.method == 'POST':
        fm = studentregis(request.POST)
        if fm.is_valid():
            print('form data')
            print('Name:', fm.cleaned_data['name'])
            print('email:', fm.cleaned_data['email'])
            print('password:', fm.cleaned_data['password'])
            return render(request, 'form.html', {'form':fm,'status':True,'name':fm.cleaned_data['name']})
    else:
        fm = studentregis()
    return render(request, 'form.html', {'form':fm})