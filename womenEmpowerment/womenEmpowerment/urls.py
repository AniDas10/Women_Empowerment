from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='main_home'),
    path('organizations/', views.organizations_all, name='main_organizations_all'),
    path('organization/', include('organization.urls')),
    path('women/', include('woman.urls')),
] + static(settings.MEDIA_URL, directory_root=settings.MEDIA_ROOT)
