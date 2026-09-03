from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core import views as core_views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', core_views.home, name='home'),
    path('pillars/', core_views.pillars_overview, name='pillars_overview'),
    path('pillars/<slug:slug>/', core_views.pillar_detail, name='pillar_detail'),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('certifications/', include('certifications.urls')),
    path('community/', include('community.urls')),
    path('blog/', include('blog.urls')),
    path('skills-health/', include('skills_health.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)