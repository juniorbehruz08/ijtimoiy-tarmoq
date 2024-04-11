from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('HomePage/', HomePage, name='HomePage'),
    path('logout/', exit, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('add_article', add_article, name='add_article'),
    path('categories/', category, name='categories'),
    path('category/<slug:slug>/', category_page, name='category_page'),
    path('article_detail/<slug:slug>', article_detail, name='article_detail'),
    path('save_comment/<slug:article_pk>', save_comment, name='save_comment'),
    path('search/', search, name='search'),
    path('chat/', chat, name='chat'),
    path('message/<slug:chat_slug>/', message, name='message'),
    path('save_message/<str:slug>/', save_message, name='save_message'),
    path('add_chat/', add_chat, name='add_chat'),
    path('save_photo/', save_photo, name='save_photo'),
    path('view_account/<str:username>/', view_account, name='view_account'),
    path('save_chat/<str:username>/', save_chat, name='save_chat'),
    path('yes_or_no/<slug:chat_slug>/', delete_chat, name='delete_chat'),
    path('delete_article/<str:article_slug>/', delete_article, name='delete_article'),
    path('ranking/', ranking, name='ranking'),
    path('save_like/<str:article_slug>/', save_like, name='save_like'),
    path('liked/<str:slug>/', liked, name='liked'),
    path('photo_delete/', photo_delete, name='photo_delete'),
    path('favourite/', favourite, name='favourite'),
    path('saved_message/', saved_message, name='saved_message'),
    path('share/<slug:article_slug>', share_post, name='share')
]
