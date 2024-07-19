from django.urls import path
from . import views

app_name='groceries'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:grocery_id>/delete', views.delete, name='delete'),
    path('<int:grocery_id>/update', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('test/', views.test_message, name='test')
]