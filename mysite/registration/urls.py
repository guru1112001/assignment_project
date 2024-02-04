from django.urls import path
from . import views
app_name='registration'

urlpatterns = [
    
    path('',views.registration_list.as_view(), name='registration_list'),
    path('detail/<int:pk>/', views.RegistrationDetailView.as_view(), name='registration_detail'),
    path('create/',views.RegistrationCreate,name='registration_create'),
    path('<int:pk>/edit/',views.registration_edit,name='registration_edit'),
    path('<int:pk>/delete/', views.RegistrationDeleteView.as_view(), name='registration_delete'),


    ]