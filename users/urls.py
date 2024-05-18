from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    #path('admin/', views.admin, name='admin'),
    path('index/', views.index, name='index'),
    
    path('profs/', views.prof_list, name='profs'),
    path('create_prof/', views.create_prof, name='create_prof'),
    path('update_prof/<int:pk>/', views.update_prof, name='update_prof'),
    path('delete_prof/<int:pk>/', views.delete_prof, name='delete_prof'),
    path('view_prof/<int:pk>/', views.view_prof, name='view_prof'),

    path('students/', views.student_list, name='students'),
    path('create_student/', views.create_student, name='create_student'),
    #path('update_student/<int:pk>/', views.update_student, name='update_student'),
    #path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('view_student/<int:pk>/', views.view_student, name='view_student'),




    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

