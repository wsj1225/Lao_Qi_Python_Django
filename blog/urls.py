from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    #path('', views.blog_title, name='blog_title'),
    path('',views.blog_title_c.as_view(),name='blog_title'),
    #path('<int:article_id>/',views.blog_article,name='blog_article')
    path('<int:pk>/',views.blog_article_c.as_view(),name='blog_article'),
    path('information/',views.hello_app)
]
