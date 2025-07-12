from django.shortcuts import render

def health(request):
    return render(request, 'myapp/health.html')
def home(request):
    return render(request, 'myapp/home.html')
def about(request):
    return render(request, 'myapp/about.html')
def skills(request):
    return render(request, 'myapp/skills.html')
def projects(request):
    return render(request, 'myapp/projects.html')
def achievements(request):
    return render(request, 'myapp/achievements.html')
def contact(request):
    return render(request, 'myapp/contact.html')