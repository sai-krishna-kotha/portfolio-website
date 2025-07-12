from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
def about(request):
    return render(request, 'myapp/about.html')
def skills(request):
    skills_data = {
        "Backend": [
            {"name": "Python", "level": "Advanced"},
            {"name": "Django", "level": "Advanced"},
            {"name": "Django REST Framework", "level": "Intermediate"},
        ],
        "Frontend": [
            {"name": "JavaScript", "level": "Intermediate"},
            {"name": "React", "level": "Intermediate"},
            {"name": "Tailwind CSS", "level": "Intermediate"},
        ],
        "Tools & DevOps": [
            {"name": "Git & GitHub", "level": "Proficient"},
            {"name": "PostgreSQL", "level": "Intermediate"},
            {"name": "Render", "level": "Intermediate"},
        ]
    }
    return render(request, 'myapp/skills.html', {'skills_data': skills_data})

def projects(request):
    return render(request, 'myapp/projects.html')
def achievements(request):
    return render(request, 'myapp/achievements.html')
def contact(request):
    return render(request, 'myapp/contact.html')