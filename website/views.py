from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
def faqs(request):
    return render(request, 'faqs.html', {})
def about_us(request):
    return render(request, 'about_us.html', {})
def about_us(request):
    return render(request, 'about_us.html', {})