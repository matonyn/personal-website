from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ref
from django.contrib import messages

# Create your views here.

def hello(request):
    features = Ref.objects.all()
    return render(request, 'hi.html', {'features': features})

def giveref(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        image = request.FILES['image']
        email = request.POST['email_url']
        linkedin = request.POST['linkedin_url']
        con = request.POST['connection']
        text = request.POST['text']
        num1 = len(fname)
        num2 = len(sname)
        num3 = len(text)
        num4 = len(linkedin)
        if num1 > 200:
            messages.error(request, "Your name must be less than 200 characters")
        elif num2 > 200:
            messages.error(request, "Your surname must be less than 200 characters")
        elif num3 > 1000:
            messages.error(request, "Your text can only be 1000 characters long")
        elif num4 > 400:
            messages.error(request, "Your LinkedIn URL must be maximum 400 characters")
        else:
            feature = Ref()
            feature.name = fname
            feature.surname = sname
            feature.connection = con
            feature.image = image
            feature.email_adress = email
            feature.linkedin_url = linkedin
            feature.details = text
            feature.review = False
            feature.save()
            return render(request, 'counter.html')
    
    return redirect('giveref')

