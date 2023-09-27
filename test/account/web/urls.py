from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='emp'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),

]
