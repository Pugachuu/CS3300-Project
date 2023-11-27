from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),

#URLS to access the pages holding the list and details of the teams and posts
path('team/', views.TeamsListView.as_view(), name= 'team'),
path('team/<int:pk>', views.TeamsDetailView.as_view(), name='team-detail'),
path('post/', views.PostsListView.as_view(), name= 'post'),
path('post/<int:pk>', views.PostsDetailView.as_view(), name='post-detail'),

#URL to create a post in team page
path('team/<int:team_id>/create_post/', views.createPost, name='create_post'),
#URL to update a post in team page
path('team/<int:team_id>/update_post/<int:id>', views.updatePost, name='update_post'),
#URL to delete a post from a team page
path('team/<int:team_id>/delete_post/<int:id>', views.deletePost, name='delete_post'),
#URL to register an account with The web app
path('accounts/register/', views.registerPage, name='register_page'),
#URL to login an account with the web app
path('accounts/login/', views.userLogin, name='login'),
#URL to logout when logged in with an account on the web app
path('accounts/logout/', views.userLogout, name='logout'),
]
