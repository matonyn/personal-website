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
        image = request.POST['image']
        email = request.POST['email_url']
        linkedin = request.POST['linkedin_url']
        con = request.POST['connection']
        text = request.POST['text']
        num1 = len(fname.split())
        num2 = len(sname.split())
        num3 = len(text.split())
        if num1 > 200 or num2 > 200 or num3 > 1000:
            messages.info(request, "Your name and surname must be less than 200 characters and your text can only be 1000 characters long")
            return redirect('giveref')
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

