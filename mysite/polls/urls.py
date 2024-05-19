from django.urls import path

from . import views

# How does one make it so that Django knows which app 
# view to create for a url when using the {% url %} template tag?
# The answer is to add namespaces to your URLconf. 
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]