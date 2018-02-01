from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.urls import include, path


from . import views
from .forms import CustomAuthenticationForm

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
        url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
        url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
