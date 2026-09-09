from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# URLs that DON'T need language prefix
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # language switch
    path('admin/', admin.site.urls),
]

# URLs that NEED language prefix /en/ /fr/ /es/ /pt/ /sw/ /ar/
urlpatterns += i18n_patterns(
    path('', include('core.urls_main')),  # home
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('community/', include('community.urls')),  # <-- FIXED! Inside i18n!
    path('certifications/', include('certifications.urls')),
    path('vocational/', include('vocational.urls')),
    path('blog/', include('blog.urls')),
    path('diagnostics/', include('site_diagnostics.urls')),
    path('health/', include('skills_health.urls')),
    prefix_default_language=False,
)

# Media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)