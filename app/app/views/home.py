from django.shortcuts import render
def index(request):
    return render(request, 'index.html', {'mensaje':'app con django'})