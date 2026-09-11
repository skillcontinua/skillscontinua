from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
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
]