# C:\skillscontinua\core\urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from courses.sitemaps import StaticViewSitemap, PillarSitemap, CourseSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'pillars': PillarSitemap,
    'courses': CourseSitemap,
}

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('en/pillars/', include(('courses.urls_pillars', 'pillars'), namespace='pillars_en')),
    path('fr/pillars/', include(('courses.urls_pillars', 'pillars'), namespace='pillars_fr')),
    path('ig/pillars/', include(('courses.urls_pillars', 'pillars'), namespace='pillars_ig')),
    # One include per language with unique namespace - NO WARNING
    path('en/courses/', include(('courses.urls', 'courses'), namespace='en')),
    path('fr/courses/', include(('courses.urls', 'courses'), namespace='fr')),
    path('es/courses/', include(('courses.urls', 'courses'), namespace='es')),
    path('pt/courses/', include(('courses.urls', 'courses'), namespace='pt')),
    path('sw/courses/', include(('courses.urls', 'courses'), namespace='sw')),
    path('ar/courses/', include(('courses.urls', 'courses'), namespace='ar')),
    path('ig/courses/', include(('courses.urls', 'courses'), namespace='ig')),
    path('courses/', include(('courses.urls', 'courses'), namespace='default')),
    path('', include(('courses.urls', 'courses'), namespace='home')),
    path('', include('village.urls')),
]