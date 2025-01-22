from . import views
from django.urls import path
from art import views  # Ensure correct app name


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    
    # Page to write new posts
    path('post_list/', views.post_list_view, name='post_list_view'),

    # Search functionality (uses same PostList view, query handled via GET parameter)
    path('search/', views.PostList.as_view(), name='search'),

    # Post detail page
    path('<slug:slug>/', views.post_detail, name="post_detail"),

    # Comment edit and delete
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
