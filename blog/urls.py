from . import views
from django.urls import path
app_name="blog"
urlpatterns=[
    path('',views.post_list,name="post_list"),
    path('<slug:slug>/',views.post_detail,name="post_detail"),
    path('category/<category>/',views.category,name="category"),
    path('search',views.search,name="search"),
    path('contact',views.contact,name="contact"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),

]
