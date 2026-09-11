from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Reset all to andragogy first (adult - default Aba)
        Course.objects.all().update(learning_approach='andragogy')
        
        # PEDAGOGY - Children, Teaching, Nursery
        p = Course.objects.filter(title__icontains='children').update(learning_approach='pedagogy')
        p += Course.objects.filter(title__icontains='Child').update(learning_approach='pedagogy')
        p += Course.objects.filter(title__icontains='Teaching').update(learning_approach='pedagogy')
        p += Course.objects.filter(title__icontains='Nursery').update(learning_approach='pedagogy')
        
        # CYBERGOGY - IT, Renewable, Solar, AI, Digital
        c = Course.objects.filter(category__pillar__icontains='IT').update(learning_approach='cybergogy')
        c += Course.objects.filter(category__pillar__icontains='Renewable').update(learning_approach='cybergogy')
        c += Course.objects.filter(category__pillar__icontains='Technology').update(learning_approach='cybergogy')
        c += Course.objects.filter(title__icontains='Solar').update(learning_approach='cybergogy')
        c += Course.objects.filter(title__icontains='Inverter').update(learning_approach='cybergogy')
        
        # HEUTAGOGY - Business, Entrepreneurship, CEO, Leadership
        h = Course.objects.filter(category__pillar__icontains='Business').update(learning_approach='heutagogy')
        h += Course.objects.filter(title__icontains='Entrepreneur').update(learning_approach='heutagogy')
        h += Course.objects.filter(title__icontains='Leadership').update(learning_approach='heutagogy')
        h += Course.objects.filter(title__icontains='CEO').update(learning_approach='heutagogy')
        
        total = Course.objects.count()
        ped = Course.objects.filter(learning_approach='pedagogy').count()
        andr = Course.objects.filter(learning_approach='andragogy').count()
        heu = Course.objects.filter(learning_approach='heutagogy').count()
        cyb = Course.objects.filter(learning_approach='cybergogy').count()
        
        self.stdout.write(self.style.SUCCESS(f"TOTAL {total}: Pedagogy={ped} Andragogy={andr} Heutagogy={heu} Cybergogy={cyb}"))