from django.urls import path
from django.contrib.auth import views as auth_views
from common import views

#media
from django.conf.urls.static import static
from django.conf import settings

app_name = 'common'

urlpatterns = [
    
    #로그인
    path('login/',auth_views.LoginView.as_view(template_name = 'common/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('signup/',views.singup,name="signup"),
    
    #프로필
    path('profile_detail/<int:user_id>>',views.profile_detail,name='profile_detail'),
    path('profile_modiry/<int:user_id>/',views.profile_modify,name='profile_modify'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   