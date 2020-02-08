from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'blog'

urlpatterns = [

    path("",views.home,name='home'),
    path("my_posts/", views.post_list_view, name='post-list'),
    path("add/post/", views.post_form, name = "add-post"),
    # path('signup/', views.signup, name = "signup"),
    path('search/',views.post_search_view, name='search-user'),
    path('delete_post/<int:pk>/',views.delete_post_view, name="delete-post"),
    path('edit_post/<int:pk>/',views.edit_post_view,name='edit-post'),

]
