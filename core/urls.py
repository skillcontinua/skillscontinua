from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from courses.models import Course

# Get the total number of active courses
total_courses = Course.objects.filter(is_active=True).count()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', TemplateView.as_view(
        template_name='home.html',
        extra_context={'total_courses': total_courses}
    ), name='home'),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('certifications/', include('certifications.urls')),
    path('blog/', include('blog.urls')),
    path('skills-health/', include('skills_health.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)