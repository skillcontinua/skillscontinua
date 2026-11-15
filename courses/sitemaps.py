# C:\skillscontinua\courses\sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Course, Category

LANGS = ['en', 'fr', 'es', 'pt', 'sw', 'ar', 'ig']

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        urls = ['/']
        for lang in LANGS:
            urls.append(f'/{lang}/courses/')
        urls.extend(['/en/pillars/', '/fr/pillars/', '/ig/pillars/'])
        return urls

    def location(self, item):
        return item


class PillarSitemap(Sitemap):
    priority = 0.85
    changefreq = 'weekly'

    def items(self):
        return Category.objects.exclude(pillar__isnull=True).exclude(pillar='')

    def location(self, obj):
        return f'/en/courses/pillar/{obj.pillar}/'


class CourseSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Course.objects.filter(is_active=True).order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/en/courses/{obj.pk}/'