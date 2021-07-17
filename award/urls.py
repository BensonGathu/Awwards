from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search_results"),
    path('uploadproject/',views.uploadproject,name='uploadproject')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
