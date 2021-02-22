from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,PostDetailView,UpdatePostView,DeletePostView,LikeView


urlpatterns=[
    url('^$',HomeView.as_view(),name = 'index'),
    url('add-post/',views.post, name='post'),
    url('settings/',views.settings, name='setting'),
    url('notifications/',views.email, name='notifications'),
    url('bookmarks/',views.bookmark,name='bookmark'),
    url('post/<int:pk>',PostDetailView.as_view(), name='post-detail'),
    url('post/edit/<int:pk>',UpdatePostView.as_view(), name='update-post'),
    url('post/delete/<int:pk>',DeletePostView.as_view(), name='delete-post'),
    url('like/<int:pk>',views.LikeView, name='like_post'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)