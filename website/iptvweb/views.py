from django.shortcuts import render


def home(request):
    return render(request,'home.html', {} ) 

def contact(request):
    return render(request,'contact.html', {} ) 

def about(request):
    return render(request,'about.html', {} ) 

def subscribe(request):
    return render(request,'subscribe.html', {} ) 