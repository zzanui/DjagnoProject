from django.urls import path
from django.contrib.auth import views as auth_views
from common import views



app_name = 'common'

urlpatterns = [
    
    #로그인
    path('login/',auth_views.LoginView.as_view(template_name = 'common/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('signup/',views.singup,name="signup"),
    
    #프로필
    path('profile_detail/<int:user_id>/',views.profile_detail,name='profile_detail'),
    path('profile_modify/<int:user_id>/',views.profile_modify,name='profile_modify'),
    
    #팔로우
    path('follow_list/<int:user_id>/',views.follow_list,name='follow_list'),
    path('following/<int:to_user_id>/',views.following,name="following"),
    path('unFollowing/<int:to_user_id>/',views.unFollowing,name="unFollowing"),
    
]