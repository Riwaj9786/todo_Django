from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo),
    path('todo/', views.todo, name = 'todo'),
    path('delete/<id>', views.delete, name = 'delete'),
    path('complete/<id>', views.complete, name='update'),
    path('not_complete/<id>', views.not_complete, name='not_complete')
]