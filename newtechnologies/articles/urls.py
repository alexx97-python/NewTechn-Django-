from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='home_page'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]