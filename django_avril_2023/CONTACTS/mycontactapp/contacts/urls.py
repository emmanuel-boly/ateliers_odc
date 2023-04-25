from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.contacts_list, name='contacts_list'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/update/<int:pk>/', views.update_contact, name='update_contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('contacts/import/', views.import_contacts, name='import_contacts'),
    path('contacts/export/', views.export_contacts, name='export_contacts'),
]
