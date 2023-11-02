from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login_page/',views.login_page, name = 'login_page'),
    path('login/',views.login_user, name = 'login_user'),
    path('logout/',views.logout_user, name = 'logout'),
    path('register/', views.register_user, name='register'),
    path('contactInfo/', views.contactInfo, name='contactInfo'),
    path('survey/',views.survey, name = 'survey'),
    path('predictions/',views.predict, name = 'predict'),
    path('scrape/',views.scrape, name = 'scrape')
]