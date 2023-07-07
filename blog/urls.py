from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 

# add at the last
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
