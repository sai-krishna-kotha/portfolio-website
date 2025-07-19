from django.urls import path
from myblog import views

app_name="myblog"

urlpatterns = [
    path('topics/',views.topics,name="blog"),
    # topics/<topic_name>/
    # topics/<topic_name>/<post_id>/
]