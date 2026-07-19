import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course, Lesson

print("="*60)
print("🌍 ADDING TRANSLATIONS TO DATABASE")
print("="*60)

# French Translations
french_translations = {
    'Foundational Literacy': {
        'name': 'Alphabétisation Fondamentale',
        'description': 'De l\'analphabétisme complet à la lecture, l\'écriture et la numératie confiantes dans votre propre langue.'
    },
    'Computer Literacy': {
        'name': 'Informatique',
        'description': 'Des bases aux avancées — matériel, logiciels, cybersécurité, drones, robotique et IA.'
    },
    'Vocational Trades': {
        'name': 'Métiers Professionnels',
        'description': 'Menuiserie, soudure, plomberie, maçonnerie, réparations automobiles, compétences maritimes et plus.'
    },
    'Certifications': {
        'name': 'Certifications',
        'description': 'CompTIA, Network+, Hacking Éthique, Drones, CCTV, Robotique et certifications IA.'
    },
    'Life Skills': {
        'name': 'Compétences de Vie',
        'description': 'Développement cognitif, intelligence émotionnelle, gestion financière et communication.'
    },
    'Primary Education': {
        'name': 'Enseignement Primaire',
        'description': 'Programmes scolaires complets en ligne — Arts, Sciences, Technologie, Commerce.'
    },
    'Secondary Education': {
        'name': 'Enseignement Secondaire',
        'description': 'Études avancées en Sciences, Commerce et Technologie.'
    },
}

# Spanish Translations
spanish_translations = {
    'Foundational Literacy': {
        'name': 'Alfabetización Fundamental',
        'description': 'Del analfabetismo total a la lectura, escritura y aritmética con confianza en tu propio idioma.'
    },
    'Computer Literacy': {
        'name': 'Alfabetización Informática',
        'description': 'Desde lo básico hasta lo avanzado — hardware, software, ciberseguridad, drones, robótica e IA.'
    },
    'Vocational Trades': {
        'name': 'Oficios Profesionales',
        'description': 'Carpintería, soldadura, fontanería, albañilería, reparación de automóviles, habilidades marítimas y más.'
    },
    'Certifications': {
        'name': 'Certificaciones',
        'description': 'CompTIA, Network+, Hacking Ético, Drones, CCTV, Robótica y credenciales de IA.'
    },
    'Life Skills': {
        'name': 'Habilidades para la Vida',
        'description': 'Desarrollo cognitivo, inteligencia emocional, gestión financiera y comunicación.'
    },
    'Primary Education': {
        'name': 'Educación Primaria',
        'description': 'Currículos escolares completos en línea — Artes, Ciencias, Tecnología, Comercio.'
    },
    'Secondary Education': {
        'name': 'Educación Secundaria',
        'description': 'Estudios avanzados en Ciencias, Comercio y Tecnología.'
    },
}

# Portuguese Translations
portuguese_translations = {
    'Foundational Literacy': {
        'name': 'Alfabetização Fundamental',
        'description': 'Do analfabetismo completo à leitura, escrita e numeracia com confiança em sua própria língua.'
    },
    'Computer Literacy': {
        'name': 'Alfabetização Informática',
        'description': 'Do básico ao avançado — hardware, software, cibersegurança, drones, robótica e IA.'
    },
    'Vocational Trades': {
        'name': 'Ofícios Profissionais',
        'description': 'Carpintaria, soldadura, canalização, alvenaria, reparação automóvel, habilidades marítimas e mais.'
    },
    'Certifications': {
        'name': 'Certificações',
        'description': 'CompTIA, Network+, Hacking Ético, Drones, CCTV, Robótica e credenciais de IA.'
    },
    'Life Skills': {
        'name': 'Habilidades para a Vida',
        'description': 'Desenvolvimento cognitivo, inteligência emocional, gestão financeira e comunicação.'
    },
    'Primary Education': {
        'name': 'Ensino Primário',
        'description': 'Currículos escolares completos online — Artes, Ciências, Tecnologia, Comércio.'
    },
    'Secondary Education': {
        'name': 'Ensino Secundário',
        'description': 'Estudos avançados em Ciências, Comércio e Tecnologia.'
    },
}

# Swahili Translations
swahili_translations = {
    'Foundational Literacy': {
        'name': 'Kusoma na Kuandika Msingi',
        'description': 'Kutoka kutojua kusoma hadi kusoma, kuandika, na kuhesabu kwa ujasiri katika lugha yako mwenyewe.'
    },
    'Computer Literacy': {
        'name': 'Ujuzi wa Kompyuta',
        'description': 'Kuanzia msingi hadi ngazi za juu — vifaa, programu, usalama wa mtandao, ndege zisizo na rubani, roboti na AI.'
    },
    'Vocational Trades': {
        'name': 'Ufundi',
        'description': 'Useremala, ufundi wa chuma, mabomba, uashi, matengenezo ya magari, ujuzi wa baharini na mengine.'
    },
    'Certifications': {
        'name': 'Vyeti',
        'description': 'CompTIA, Network+, Udukuzi wa Maadili, Ndege zisizo na rubani, CCTV, Roboti na vyeti vya AI.'
    },
    'Life Skills': {
        'name': 'Stadi za Maisha',
        'description': 'Ukuzaji wa akili, akili ya hisia, usimamizi wa fedha na mawasiliano.'
    },
    'Primary Education': {
        'name': 'Elimu ya Msingi',
        'description': 'Mitaala kamili ya shule mtandaoni — Sanaa, Sayansi, Teknolojia, Biashara.'
    },
    'Secondary Education': {
        'name': 'Elimu ya Sekondari',
        'description': 'Masomo ya juu katika Sayansi, Biashara na Teknolojia.'
    },
}

# Arabic Translations
arabic_translations = {
    'Foundational Literacy': {
        'name': 'محو الأمية الأساسي',
        'description': 'من الأمية الكاملة إلى القراءة والكتابة والحساب بثقة في لغتك الخاصة.'
    },
    'Computer Literacy': {
        'name': 'محو الأمية الحاسوبية',
        'description': 'من الأساسي إلى المتقدم — الأجهزة والبرامج والأمن السيبراني والطائرات بدون طيار والروبوتات والذكاء الاصطناعي.'
    },
    'Vocational Trades': {
        'name': 'المهن الحرفية',
        'description': 'النجارة واللحام والسباكة والبناء وإصلاح السيارات والمهارات البحرية والمزيد.'
    },
    'Certifications': {
        'name': 'الشهادات',
        'description': 'CompTIA، Network+، الاختراق الأخلاقي، الطائرات بدون طيار، CCTV، الروبوتات واعتمادات الذكاء الاصطناعي.'
    },
    'Life Skills': {
        'name': 'مهارات الحياة',
        'description': 'التطور المعرفي، الذكاء العاطفي، الإدارة المالية والتواصل.'
    },
    'Primary Education': {
        'name': 'التعليم الابتدائي',
        'description': 'مناهج مدرسية كاملة عبر الإنترنت — الفنون والعلوم والتكنولوجيا والتجارة.'
    },
    'Secondary Education': {
        'name': 'التعليم الثانوي',
        'description': 'دراسات متقدمة في العلوم والتجارة والتكنولوجيا.'
    },
}

# Update Categories with translations
lang_mappings = {
    'fr': french_translations,
    'es': spanish_translations,
    'pt': portuguese_translations,
    'sw': swahili_translations,
    'ar': arabic_translations,
}

total_updated = 0

for lang_code, translations in lang_mappings.items():
    print(f"\n📝 Adding {lang_code.upper()} translations...")
    for cat in Category.objects.all():
        if cat.name in translations:
            translation = translations[cat.name]
            
            # Set the translation fields
            name_field = f'name_{lang_code}'
            desc_field = f'description_{lang_code}'
            
            setattr(cat, name_field, translation['name'])
            setattr(cat, desc_field, translation['description'])
            cat.save()
            total_updated += 1
            print(f"  ✅ Updated: {cat.name} -> {translation['name']}")

print("\n" + "="*60)
print(f"✅ Total Categories Updated: {total_updated}")
print("🎉 Translations added successfully!")