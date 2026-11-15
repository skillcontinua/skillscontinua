# C:\skillscontinua\courses\views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import Course, Category, Lesson

# === TRANSLATIONS FOR 7 LANGUAGES ===
TRANSLATIONS = {
    'en': {
        'available_courses': 'Available Courses',
        'live_db': 'LIVE DB COUNT',
        'pillars': 'Pillars',
        'pilot': 'Skills Platform',
        'youth': 'Youth Empowerment',
        'current_lang': 'Current Language',
        'all': 'All',
        'pedagogy': 'Pedagogy - Child Led',
        'andragogy': 'Andragogy - Adult Led (Market Enterprise)',
        'heutagogy': 'Heutagogy - CEO Self-Determined',
        'cybergogy': 'Cybergogy - Tech (AI, Solar)',
    },
    'fr': {
        'available_courses': 'Cours Disponibles',
        'live_db': 'COMPTE BD EN DIRECT',
        'pillars': 'Piliers',
        'pilot': 'Plateforme',
        'youth': 'Autonomisation des Jeunes',
        'current_lang': 'Langue Actuelle',
        'all': 'Tous',
        'pedagogy': 'Pédagogie - Enfant',
        'andragogy': 'Andragogie - Adulte (Entreprise)',
        'heutagogy': 'Heutagogie - PDG',
        'cybergogy': 'Cybergogie - Tech (IA, Solaire)',
    },
    'ig': {
        'available_courses': 'Usoro Nkuzi Di',
        'live_db': 'NGỤKỌTA NDỤ',
        'pillars': 'Ogidi Iri na Anọ',
        'pilot': 'Ikpo Okwu',
        'youth': 'Ike Umuaka',
        'current_lang': 'Asụsụ Ugbu a',
        'all': 'Niile',
        'pedagogy': 'Nkuzi Umuaka',
        'andragogy': 'Nkuzi Ndi Okenye',
        'heutagogy': 'Nkuzi CEO - Onwe',
        'cybergogy': 'Nkuzi Tech (AI, Anyanwu)',
    },
    'sw': {
        'available_courses': 'Kozi Zinazopatikana',
        'live_db': 'HESABU YA DB',
        'pillars': 'Nguzo',
        'pilot': 'Jukwaa',
        'youth': 'Uwezeshaji Vijana',
        'current_lang': 'Lugha ya Sasa',
        'all': 'Zote',
        'pedagogy': 'Pedagogy - Mtoto',
        'andragogy': 'Andragogy - Watu Wazima',
        'heutagogy': 'Heutagogy - CEO',
        'cybergogy': 'Cybergogy - Tekno',
    },
    'ar': {
        'available_courses': 'الدورات المتاحة',
        'live_db': 'عدد قاعدة البيانات الحية',
        'pillars': 'الأعمدة',
        'pilot': 'منصة المهارات',
        'youth': 'تمكين الشباب',
        'current_lang': 'اللغة الحالية',
        'all': 'الكل',
        'pedagogy': 'علم التربية - الطفل',
        'andragogy': 'تعليم الكبار',
        'heutagogy': 'التعلم الذاتي',
        'cybergogy': 'التعلم السيبراني',
    },
    'es': {
        'available_courses': 'Cursos Disponibles',
        'live_db': 'CONTEO BD',
        'pillars': 'Pilares',
        'pilot': 'Plataforma',
        'youth': 'Empoderamiento Juvenil',
        'current_lang': 'Idioma Actual',
        'all': 'Todos',
        'pedagogy': 'Pedagogía - Niño',
        'andragogy': 'Andragogía - Adulto',
        'heutagogy': 'Heutagogía - CEO',
        'cybergogy': 'Cybergogía - Tech'
    },
    'pt': {
        'available_courses': 'Cursos Disponíveis',
        'live_db': 'CONTAGEM BD',
        'pillars': 'Pilares',
        'pilot': 'Plataforma',
        'youth': 'Empoderamento Jovem',
        'current_lang': 'Idioma Atual',
        'all': 'Todos',
        'pedagogy': 'Pedagogia - Criança',
        'andragogy': 'Andragogia - Adulto',
        'heutagogy': 'Heutagogia - CEO',
        'cybergogy': 'Cybergogia - Tech'
    },
}

def get_lang_from_path(request):
    path = request.path
    for lang in ['en', 'fr', 'es', 'pt', 'sw', 'ar', 'ig']:
        if path.startswith(f'/{lang}/'):
            return lang
    return 'en'

def course_list(request):
    current_lang = get_lang_from_path(request)
    theory = request.GET.get('theory', 'all')
    search = request.GET.get('q', '')
    
    courses = Course.objects.select_related('category').all().order_by('category__name', 'title')
    
    if search:
        courses = courses.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search) |
            Q(category__name__icontains=search)
        )
    
    if theory != 'all':
        courses = courses.filter(learning_approach=theory)
        
    counts = {
        'all': Course.objects.count(),
        'pedagogy': Course.objects.filter(learning_approach='pedagogy').count(),
        'andragogy': Course.objects.filter(learning_approach='andragogy').count(),
        'heutagogy': Course.objects.filter(learning_approach='heutagogy').count(),
        'cybergogy': Course.objects.filter(learning_approach='cybergogy').count(),
    }
    context = {
        'courses': courses,
        'counts': counts,
        'pillars': Category.objects.all(),
        'current_lang': current_lang,
        'active_theory': theory,
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en']),
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    current_lang = get_lang_from_path(request)
    return render(request, 'courses/course_detail.html', {
        'course': course, 
        'current_lang': current_lang, 
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en'])
    })

def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/enroll.html', {'course': course})

def pillar_courses(request, pillar_name):
    current_lang = get_lang_from_path(request)
    pillar = get_object_or_404(Category, pillar=pillar_name)
    base_qs = Course.objects.filter(category=pillar)
    theory = request.GET.get('theory', 'all')
    
    courses = base_qs.filter(learning_approach=theory) if theory != 'all' else base_qs
    
    counts = {
        'all': base_qs.count(),
        'pedagogy': base_qs.filter(learning_approach='pedagogy').count(),
        'andragogy': base_qs.filter(learning_approach='andragogy').count(),
        'heutagogy': base_qs.filter(learning_approach='heutagogy').count(),
        'cybergogy': base_qs.filter(learning_approach='cybergogy').count(),
    }
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'selected_pillar': pillar,
        'counts': counts,
        'pillars': Category.objects.all(),
        'current_lang': current_lang,
        'active_theory': theory,
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en']),
    })

def lesson_view(request, course_pk, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/lesson.html', {'lesson': lesson})

def complete_lesson(request, course_pk, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/complete.html', {'lesson': lesson})

def pillars_list(request):
    current_lang = get_lang_from_path(request)
    pillars = Category.objects.annotate(num_courses=Count('courses')).order_by('order', 'name')
    return render(request, 'courses/pillars.html', {
        'pillars': pillars,
        'current_lang': current_lang,
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en']),
    })