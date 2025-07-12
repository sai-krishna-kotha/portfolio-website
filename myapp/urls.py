from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('skills/',views.skills, name="skills"),
    path('projects/',views.projects, name="projects"),
    path('achievements/',views.achievements, name="achievements"),
    path('contact/',views.contact, name="contact"),
]