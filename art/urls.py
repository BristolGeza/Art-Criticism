from . import views
from django.urls import path
#geza
from .views import my_view

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #Geza--- add a npage to write posts to art 
    path('new-post/', views.post_new, name="new-post"),
    path('admin/art/post/', views.post_list_view, name='post_list_view'),
    #---
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
         #geza
    path('art/', my_view, name='art'),
]