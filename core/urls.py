from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', core_views.home, name='home'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('community/', core_views.community, name='community'),
    path('pillars/', core_views.pillars_overview, name='pillars_overview'),
    path('pillars/<slug:slug>/', core_views.pillar_detail, name='pillar_detail'),
    path('courses/', include('courses.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)