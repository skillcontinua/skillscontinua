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
        'search_placeholder': 'Search vocational, IT, solar & business skills...',
        'search_btn': 'Search',
        'clear': 'Clear',
        'subscribe': 'Subscribe ₦2000',
        'leaderboard': 'Leaderboard',
        'live_badge': 'LIVE',
        'skills_badge': 'SKILLS',
        'featured': 'Featured',
        'view_course': 'View Course →',
        'no_courses': 'No courses found for',
        'try_keywords': 'Try: solar, tailoring, agriculture, Aba, market, Igbo, business',
        'show_all': 'Show All',
        'courses_word': 'Courses',
        'found_results': 'Found',
        'results_for': 'results for',
    },
    'fr': {
        'available_courses': 'Cours Disponibles',
        'live_db': 'COMPTE BD EN DIRECT',
        'pillars': 'Piliers',
        'pilot': 'Plateforme de Compétences',
        'youth': 'Autonomisation des Jeunes',
        'current_lang': 'Langue Actuelle',
        'all': 'Tous',
        'pedagogy': 'Pédagogie - Enfant',
        'andragogy': 'Andragogie - Adulte (Entreprise)',
        'heutagogy': 'Heutagogie - PDG',
        'cybergogy': 'Cybergogie - Tech (IA, Solaire)',
        'search_placeholder': 'Rechercher des compétences en informatique, solaire...',
        'search_btn': 'Rechercher',
        'clear': 'Effacer',
        'subscribe': 'S’abonner ₦2000',
        'leaderboard': 'Classement',
        'live_badge': 'EN DIRECT',
        'skills_badge': 'COMPÉTENCES',
        'featured': 'En Vedette',
        'view_course': 'Voir le Cours →',
        'no_courses': 'Aucun cours trouvé pour',
        'try_keywords': 'Essayez : solaire, couture, agriculture, commerce',
        'show_all': 'Afficher Tous les',
        'courses_word': 'Cours',
        'found_results': 'Trouvé',
        'results_for': 'résultats pour',
    },
    'ig': {
        'available_courses': 'Usoro Nkuzi Dị',
        'live_db': 'NGỤKỌTA NDỤ',
        'pillars': 'Ogidi Iri na Anọ',
        'pilot': 'Ikpo Okwu Nka',
        'youth': 'Ike Ntorobịa',
        'current_lang': 'Asụsụ Ugbu a',
        'all': 'Niile',
        'pedagogy': 'Nkuzi Ụmụaka',
        'andragogy': 'Nkuzi Ndị Okenye (Ahịa)',
        'heutagogy': 'Nkuzi CEO - Onwe',
        'cybergogy': 'Nkuzi Tech (AI, Anyanwụ)',
        'search_placeholder': 'Chọọ nkuzi nka, solar, na azụmahịa...',
        'search_btn': 'Chọọ',
        'clear': 'Hichapụ',
        'subscribe': 'Debanye Aha ₦2000',
        'leaderboard': 'Ndị Kachasị Elu',
        'live_badge': 'NDỤ',
        'skills_badge': 'NKA',
        'featured': 'Pụrụ Iche',
        'view_course': 'Lee Nkuzi →',
        'no_courses': 'Enweghị nkuzi achọtara maka',
        'try_keywords': 'Nwaa: solar, akwa, ọrụ ugbo, Aba, ahịa, Igbo, azụmahịa',
        'show_all': 'Gosi Niile',
        'courses_word': 'Nkuzi',
        'found_results': 'Achọtara',
        'results_for': 'nchoputa maka',
    },
    'sw': {
        'available_courses': 'Kozi Zinazopatikana',
        'live_db': 'HESABU YA DB',
        'pillars': 'Nguzo',
        'pilot': 'Jukwaa la Ujuzi',
        'youth': 'Uwezeshaji Vijana',
        'current_lang': 'Lugha ya Sasa',
        'all': 'Zote',
        'pedagogy': 'Pedagogy - Mtoto',
        'andragogy': 'Andragogy - Watu Wazima',
        'heutagogy': 'Heutagogy - CEO',
        'cybergogy': 'Cybergogy - Tekno',
        'search_placeholder': 'Tafuta ufundi, IT, nishati ya jua na biashara...',
        'search_btn': 'Tafuta',
        'clear': 'Futa',
        'subscribe': 'Jiandikishe ₦2000',
        'leaderboard': 'Ubao wa Vinara',
        'live_badge': 'MOJA KWA MOJA',
        'skills_badge': 'UJUZI',
        'featured': 'Maalum',
        'view_course': 'Tazama Kozi →',
        'no_courses': 'Hakuna kozi zilizopatikana kwa',
        'try_keywords': 'Jaribu: jua, ushonaji, kilimo, biashara',
        'show_all': 'Onyesha Zote',
        'courses_word': 'Kozi',
        'found_results': 'Zimepatikana',
        'results_for': 'matokeo ya',
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
        'search_placeholder': 'ابحث عن المهارات المهنية، تكنولوجيا المعلومات، والطاقة الشمسية...',
        'search_btn': 'بحث',
        'clear': 'مسح',
        'subscribe': 'اشترك ₦2000',
        'leaderboard': 'لوحة المتصدرين',
        'live_badge': 'مباشر',
        'skills_badge': 'مهارات',
        'featured': 'مميز',
        'view_course': 'عرض الدورة ←',
        'no_courses': 'لم يتم العثور على دورات لـ',
        'try_keywords': 'جرب: طاقة شمسية، خياطة، زراعة، تجارة',
        'show_all': 'عرض الكل',
        'courses_word': 'دورات',
        'found_results': 'تم العثور على',
        'results_for': 'نتائج لـ',
    },
    'es': {
        'available_courses': 'Cursos Disponibles',
        'live_db': 'CONTEO BD',
        'pillars': 'Pilares',
        'pilot': 'Plataforma de Habilidades',
        'youth': 'Empoderamiento Juvenil',
        'current_lang': 'Idioma Actual',
        'all': 'Todos',
        'pedagogy': 'Pedagogía - Niño',
        'andragogy': 'Andragogía - Adulto',
        'heutagogy': 'Heutagogía - CEO',
        'cybergogy': 'Cybergogía - Tech',
        'search_placeholder': 'Buscar habilidades vocacionales, TI, solar y de negocios...',
        'search_btn': 'Buscar',
        'clear': 'Borrar',
        'subscribe': 'Suscribirse ₦2000',
        'leaderboard': 'Clasificación',
        'live_badge': 'EN VIVO',
        'skills_badge': 'HABILIDADES',
        'featured': 'Destacado',
        'view_course': 'Ver Curso →',
        'no_courses': 'No se encontraron cursos para',
        'try_keywords': 'Prueba: solar, costura, agricultura, negocios',
        'show_all': 'Mostrar Todos los',
        'courses_word': 'Cursos',
        'found_results': 'Encontrados',
        'results_for': 'resultados para',
    },
    'pt': {
        'available_courses': 'Cursos Disponíveis',
        'live_db': 'CONTAGEM BD',
        'pillars': 'Pilares',
        'pilot': 'Plataforma de Competências',
        'youth': 'Empoderamento Jovem',
        'current_lang': 'Idioma Atual',
        'all': 'Todos',
        'pedagogy': 'Pedagogia - Criança',
        'andragogy': 'Andragogia - Adulto',
        'heutagogy': 'Heutagogia - CEO',
        'cybergogy': 'Cybergogia - Tech',
        'search_placeholder': 'Pesquisar competências profissionais, TI, solar e negócios...',
        'search_btn': 'Pesquisar',
        'clear': 'Limpar',
        'subscribe': 'Subscrever ₦2000',
        'leaderboard': 'Classificação',
        'live_badge': 'AO VIVO',
        'skills_badge': 'COMPETÊNCIAS',
        'featured': 'Destaque',
        'view_course': 'Ver Curso →',
        'no_courses': 'Nenhum curso encontrado para',
        'try_keywords': 'Tente: solar, costura, agricultura, negócios',
        'show_all': 'Mostrar Todos os',
        'courses_word': 'Cursos',
        'found_results': 'Encontrados',
        'results_for': 'resultados para',
    },
}

# === PILLAR TRANSLATIONS ===
PILLAR_NAMES = {
    'renewable_energy_solar': {
        'en': 'Renewable Energy & Solar', 'fr': 'Énergie Renouvelable & Solaire', 'ig': 'Ike Anyanwụ & Mmelite',
        'sw': 'Nishati Mbadala na Jua', 'ar': 'الطاقة المتجددة والشمسية', 'es': 'Energía Renovable y Solar', 'pt': 'Energia Renovável e Solar'
    },
    'it_technology_software': {
        'en': 'IT Technology & Software', 'fr': 'Technologie IT & Logiciels', 'ig': 'Nkà na Ụzụ Kọmputa & Software',
        'sw': 'Teknolojia ya Habari na Programu', 'ar': 'تكنولوجيا المعلومات والبرمجيات', 'es': 'Tecnología TI y Software', 'pt': 'Tecnologia de TI e Software'
    },
    'automotive_repairs_maintenance': {
        'en': 'Automotive Repairs & Maintenance', 'fr': 'Réparation & Entretien Automobile', 'ig': 'Nrụzi Ụgbọala & Mmekọrịta',
        'sw': 'Ukarabati na Matengenezo ya Magari', 'ar': 'إصلاح وصيانة السيارات', 'es': 'Reparación y Mantenimiento Automotriz', 'pt': 'Reparação e Manutenção Automóvel'
    },
    'trades_craftsmanship': {
        'en': 'Trades & Craftsmanship', 'fr': 'Métiers & Artisanat', 'ig': 'Ọrụ Aka & Nka',
        'sw': 'Ufundi na Sanaa za Mikono', 'ar': 'الحرف والمهن اليدوية', 'es': 'Oficios y Artesanía', 'pt': 'Ofícios e Artesanato'
    },
    'agriculture_agro_business': {
        'en': 'Agriculture & Agro-Business', 'fr': 'Agriculture & Agro-Business', 'ig': 'Ọrụ Ugbo & Azụmahịa Ugbo',
        'sw': 'Kilimo na Biashara ya Kilimo', 'ar': 'الزراعة والأعمال الزراعية', 'es': 'Agricultura y Agronegocios', 'pt': 'Agricultura e Agronegócios'
    },
    'business_entrepreneurship': {
        'en': 'Business & Entrepreneurship', 'fr': 'Affaires & Entrepreneuriat', 'ig': 'Azụmahịa & Ịmalite Ọrụ',
        'sw': 'Biashara na Ujasiriamali', 'ar': 'الأعمال وريادة الأعمال', 'es': 'Negocios y Emprendimiento', 'pt': 'Negócios e Empreendedorismo'
    },
    'finance_professional_services': {
        'en': 'Finance & Professional Services', 'fr': 'Finance & Services Professionnels', 'ig': 'Ego & Ọrụ Ọkachamara',
        'sw': 'Fedha na Huduma za Kitaalamu', 'ar': 'المالية والخدمات المهنية', 'es': 'Finanzas y Servicios Profesionales', 'pt': 'Finanças e Serviços Profissionais'
    },
    'health_wellness': {
        'en': 'Health & Wellness', 'fr': 'Santé & Bien-être', 'ig': 'Ahụike & Ọdịmma',
        'sw': 'Afya na Ustawi', 'ar': 'الصحة والعافية', 'es': 'Salud y Bienestar', 'pt': 'Saúde e Bem-Estar'
    },
    'education_teaching': {
        'en': 'Education & Teaching', 'fr': 'Éducation & Enseignement', 'ig': 'Agụmakwụkwọ & Nkuzi',
        'sw': 'Elimu na Ufundishaji', 'ar': 'التعليم والتدريس', 'es': 'Educación y Enseñanza', 'pt': 'Educação e Ensino'
    },
    'media_creative_arts': {
        'en': 'Media & Creative Arts', 'fr': 'Médias & Arts Créatifs', 'ig': 'Mgbasa Ozi & Nka Okike',
        'sw': 'Vyombo vya Habari na Sanaa', 'ar': 'الإعلام والفنون الإبداعية', 'es': 'Medios y Artes Creativas', 'pt': 'Mídia e Artes Criativas'
    },
    'beauty_personal_care': {
        'en': 'Beauty & Personal Care', 'fr': 'Beauté & Soins Personnels', 'ig': 'Ịma Mma & Nlekọta Onwe',
        'sw': 'Urembo na Utunzaji Binafsi', 'ar': 'الجمال والعناية الشخصية', 'es': 'Belleza y Cuidado Personal', 'pt': 'Beleza e Cuidados Pessoais'
    },
    'transport_logistics': {
        'en': 'Transport & Logistics', 'fr': 'Transport & Logistique', 'ig': 'Njem & Mbupu Ngwongwo',
        'sw': 'Usafiri na Usafirishaji', 'ar': 'النقل والخدمات اللوجستية', 'es': 'Transporte y Logística', 'pt': 'Transporte e Logística'
    },
    'government_social_impact': {
        'en': 'Government & Social Impact', 'fr': 'Gouvernement & Impact Social', 'ig': 'Gọọmentị & Mmetụta Obodo',
        'sw': 'Serikali na Athari za Kijamii', 'ar': 'الحكومة والأثر الاجتماعي', 'es': 'Gobierno e Impacto Social', 'pt': 'Governo e Impacto Social'
    },
    'vocational_technical_skills': {
        'en': 'Vocational & Technical Skills', 'fr': 'Compétences Professionnelles & Techniques', 'ig': 'Nka Ọrụ Aka & Teknụzụ',
        'sw': 'Ujuzi wa Ufundi na Kiufundi', 'ar': 'المهارات المهنية والتقنية', 'es': 'Habilidades Vocacionales y Técnicas', 'pt': 'Competências Profissionais e Técnicas'
    },
}

def translate_pillar(pillar_obj, lang):
    mapping = PILLAR_NAMES.get(pillar_obj.pillar, {})
    pillar_obj.translated_name = mapping.get(lang, pillar_obj.name)
    return pillar_obj

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
    
    courses = list(Course.objects.select_related('category').all().order_by('category__name', 'title'))
    
    if search:
        s_lower = search.lower()
        courses = [
            c for c in courses 
            if s_lower in c.title.lower() or s_lower in c.description.lower() or s_lower in c.category.name.lower()
        ]
    
    if theory != 'all':
        courses = [c for c in courses if c.learning_approach == theory]

    for c in courses:
        translate_pillar(c.category, current_lang)
        
    pillars = [translate_pillar(p, current_lang) for p in Category.objects.all()]

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
        'pillars': pillars,
        'current_lang': current_lang,
        'active_theory': theory,
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en']),
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    current_lang = get_lang_from_path(request)
    translate_pillar(course.category, current_lang)
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
    pillar = translate_pillar(get_object_or_404(Category, pillar=pillar_name), current_lang)
    base_qs = Course.objects.filter(category=pillar)
    theory = request.GET.get('theory', 'all')
    
    courses = list(base_qs.filter(learning_approach=theory) if theory != 'all' else base_qs)
    for c in courses:
        translate_pillar(c.category, current_lang)

    pillars = [translate_pillar(p, current_lang) for p in Category.objects.all()]
    
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
        'pillars': pillars,
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
    pillars = [translate_pillar(p, current_lang) for p in Category.objects.annotate(num_courses=Count('courses')).order_by('order', 'name')]
    return render(request, 'courses/pillars.html', {
        'pillars': pillars,
        'current_lang': current_lang,
        't': TRANSLATIONS.get(current_lang, TRANSLATIONS['en']),
    })