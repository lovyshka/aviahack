from django.shortcuts import render

def home(request):
    return render(request, 'accounts/aouth_page.html')

def rabotyaga(request):
    return render(request, 'accounts/voditel_page.html')

def dispetch(request):
    return render(request, 'accounts/dispetcher_page.html')