from django.urls import path,include
from . import views



urlpatterns = [
    
    path('', views.index, name="index"),
    path('base/',views.base, name="signup"),
    path('success/<path:upload>',views.sent_succesfully, name="success"),
    path('signup/',views.signup, name="signup"),
    path('send/',views.upload, name="send"),
    path('uploaded_files/',views.FilesListView.as_view(),name="uploaded_files_list"),
    
    path('<int:pk>/', views.delete_file, name='delete_file'),
    path('accounts/', include('django.contrib.auth.urls')),
 
]

