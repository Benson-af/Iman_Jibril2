from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


# --- TEMPORARY SUPERUSER CREATION VIEW ---
def create_temp_superuser(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin2').exists():
        User.objects.create_superuser('admin2', 'admin2@example.com', 'TempAdminPass456')
        return HttpResponse("Superuser 'admin2' created. Password: TempAdminPass456")
    return HttpResponse("Superuser 'admin2' already exists.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-temp-superuser/', create_temp_superuser),  # TEMPORARY
    path('', include('accounts.urls')),  # Homepage is now your accounts app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)