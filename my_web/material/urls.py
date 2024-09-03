# urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('add/', views.MaterialCreateView.as_view(), name='material'),
    path('edit/<int:pk>/', views.MaterialEditView.as_view(), name='edit_material'),
    path('list/', views.MaterialListView.as_view(), name='list_material'),
    path('search/', views.search_material, name='search_material'),
    ]