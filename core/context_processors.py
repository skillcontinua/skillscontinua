from django.utils import translation

def language_processor(request):
    """Make language settings available to all templates"""
    current_language = translation.get_language()
    
    # If no language is set, use English
    if not current_language:
        current_language = 'en'
    
    LANGUAGES = [
        ('en', 'English'),
        ('fr', 'Français'),
        ('es', 'Español'),
        ('pt', 'Português'),
        ('sw', 'Kiswahili'),
        ('ar', 'العربية'),
    ]
    
    return {
        'current_language': current_language,
        'LANGUAGES': LANGUAGES,
    }

def site_settings(request):
    """Site-wide settings for templates with translations"""
    current_lang = translation.get_language()
    
    # Helper function to get translation
    def get_translation(trans_dict):
        return trans_dict.get(current_lang, trans_dict.get('en', ''))
    
    # Translated site content
    site_name = {
        'en': 'SkillsContinua',
        'fr': 'SkillsContinua',
        'es': 'SkillsContinua',
        'pt': 'SkillsContinua',
        'sw': 'SkillsContinua',
        'ar': 'سكيلزكونتينوا',
    }
    
    site_tagline = {
        'en': 'From Literacy to Livelihood',
        'fr': "De l'alphabétisation à l'autonomie",
        'es': 'De la alfabetización al sustento',
        'pt': 'Da alfabetização ao sustento',
        'sw': 'Kutoka Kusoma hadi Maisha',
        'ar': 'من محو الأمية إلى سبل العيش',
    }
    
    site_description = {
        'en': 'Skills for life, career and self-employment',
        'fr': 'Compétences pour la vie, la carrière et l\'auto-emploi',
        'es': 'Habilidades para la vida, carrera y autoempleo',
        'pt': 'Habilidades para a vida, carreira e autoemprego',
        'sw': 'Stadi za maisha, kazi na kujiajiri',
        'ar': 'مهارات للحياة والعمل الحر',
    }
    
    contact_email = {
        'en': 'info@skillscontinua.com',
        'fr': 'info@skillscontinua.com',
        'es': 'info@skillscontinua.com',
        'pt': 'info@skillscontinua.com',
        'sw': 'info@skillscontinua.com',
        'ar': 'info@skillscontinua.com',
    }
    
    # Navigation translations
    nav_home = {
        'en': 'Home',
        'fr': 'Accueil',
        'es': 'Inicio',
        'pt': 'Início',
        'sw': 'Nyumbani',
        'ar': 'الرئيسية',
    }
    
    nav_courses = {
        'en': 'Courses',
        'fr': 'Cours',
        'es': 'Cursos',
        'pt': 'Cursos',
        'sw': 'Kozi',
        'ar': 'الدورات',
    }
    
    nav_dashboard = {
        'en': 'Dashboard',
        'fr': 'Tableau de bord',
        'es': 'Tablero',
        'pt': 'Painel',
        'sw': 'Dashibodi',
        'ar': 'لوحة القيادة',
    }
    
    nav_login = {
        'en': 'Login',
        'fr': 'Connexion',
        'es': 'Iniciar sesión',
        'pt': 'Entrar',
        'sw': 'Ingia',
        'ar': 'تسجيل الدخول',
    }
    
    nav_logout = {
        'en': 'Logout',
        'fr': 'Déconnexion',
        'es': 'Cerrar sesión',
        'pt': 'Sair',
        'sw': 'Toka',
        'ar': 'تسجيل الخروج',
    }
    
    nav_register = {
        'en': 'Register',
        'fr': "S'inscrire",
        'es': 'Registrarse',
        'pt': 'Registar',
        'sw': 'Jisajili',
        'ar': 'التسجيل',
    }
    
    nav_start_free = {
        'en': 'Start Free',
        'fr': 'Commencer Gratuit',
        'es': 'Comenzar Gratis',
        'pt': 'Começar Grátis',
        'sw': 'Anza Bure',
        'ar': 'ابدأ مجاناً',
    }
    
    # Footer translations
    footer_learning_pillars = {
        'en': 'Learning Pillars',
        'fr': "Piliers d'apprentissage",
        'es': 'Pilares de aprendizaje',
        'pt': 'Pilares de aprendizagem',
        'sw': 'Nguzo za Kujifunza',
        'ar': 'أركان التعلم',
    }
    
    footer_quick_links = {
        'en': 'Quick Links',
        'fr': 'Liens rapides',
        'es': 'Enlaces rápidos',
        'pt': 'Links rápidos',
        'sw': 'Viungo vya Haraka',
        'ar': 'روابط سريعة',
    }
    
    footer_contact = {
        'en': 'Contact',
        'fr': 'Contact',
        'es': 'Contacto',
        'pt': 'Contacto',
        'sw': 'Mawasiliano',
        'ar': 'اتصل بنا',
    }
    
    footer_all_courses = {
        'en': 'All Courses',
        'fr': 'Tous les cours',
        'es': 'Todos los cursos',
        'pt': 'Todos os cursos',
        'sw': 'Kozi Zote',
        'ar': 'جميع الدورات',
    }
    
    footer_about = {
        'en': 'About Us',
        'fr': 'À propos',
        'es': 'Sobre nosotros',
        'pt': 'Sobre nós',
        'sw': 'Kuhusu Sisi',
        'ar': 'من نحن',
    }
    
    footer_copyright = {
        'en': 'SkillsContinua. Building communities through skills.',
        'fr': 'SkillsContinua. Construire des communautés par les compétences.',
        'es': 'SkillsContinua. Construyendo comunidades a través de habilidades.',
        'pt': 'SkillsContinua. Construindo comunidades através de habilidades.',
        'sw': 'SkillsContinua. Kujenga jamii kupitia stadi.',
        'ar': 'سكيلزكونتينوا. بناء المجتمعات من خلال المهارات.',
    }
    
    # ===== HERO SECTION TRANSLATIONS =====
    hero_title = {
        'en': 'From Literacy to Livelihood',
        'fr': "De l'alphabétisation à l'autonomie",
        'es': 'De la alfabetización al sustento',
        'pt': 'Da alfabetização ao sustento',
        'sw': 'Kutoka Kusoma hadi Maisha',
        'ar': 'من محو الأمية إلى سبل العيش',
    }
    
    hero_subtitle = {
        'en': 'SkillsContinua takes every person — young or adult — from where they are to where they want to be. Literacy, skills, certifications, and self-employment tools, all in one place.',
        'fr': "SkillsContinua accompagne chaque personne — jeune ou adulte — de là où elle est à là où elle veut être. Alphabétisation, compétences, certifications et outils d'auto-emploi, tout en un seul endroit.",
        'es': 'SkillsContinua lleva a cada persona — joven o adulta — desde donde está hasta donde quiere estar. Alfabetización, habilidades, certificaciones y herramientas de autoempleo, todo en un solo lugar.',
        'pt': 'A SkillsContinua leva cada pessoa — jovem ou adulta — de onde está para onde quer estar. Alfabetização, habilidades, certificações e ferramentas de autoemprego, tudo num só lugar.',
        'sw': 'SkillsContinua inachukua kila mtu — kijana au mtu mzima — kutoka alipo hadi anapotaka kuwa. Kusoma, stadi, vyeti, na zana za kujiajiri, zote mahali pamoja.',
        'ar': 'سكيلزكونتينوا تأخذ كل شخص — شاباً أو بالغاً — من حيث هو إلى حيث يريد أن يكون. محو الأمية، المهارات، الشهادات، وأدوات العمل الحر، كلها في مكان واحد.',
    }
    
    hero_button_start = {
        'en': 'Start Learning Free',
        'fr': 'Commencer Gratuitement',
        'es': 'Comenzar a Aprender Gratis',
        'pt': 'Começar a Aprender Grátis',
        'sw': 'Anza Kujifunza Bure',
        'ar': 'ابدأ التعلم مجاناً',
    }
    
    hero_button_browse = {
        'en': 'Browse Courses',
        'fr': 'Parcourir les Cours',
        'es': 'Explorar Cursos',
        'pt': 'Explorar Cursos',
        'sw': 'Vinjari Kozi',
        'ar': 'تصفح الدورات',
    }
    
    # ===== STATS TRANSLATIONS =====
    stats_learning_pillars = {
        'en': 'Learning Pillars',
        'fr': "Piliers d'apprentissage",
        'es': 'Pilares de aprendizaje',
        'pt': 'Pilares de aprendizagem',
        'sw': 'Nguzo za Kujifunza',
        'ar': 'أركان التعلم',
    }
    
    stats_courses_available = {
        'en': 'Courses Available',
        'fr': 'Cours Disponibles',
        'es': 'Cursos Disponibles',
        'pt': 'Cursos Disponíveis',
        'sw': 'Kozi Zinazopatikana',
        'ar': 'الدورات المتاحة',
    }
    
    stats_learning_approaches = {
        'en': 'Learning Approaches',
        'fr': "Approches d'apprentissage",
        'es': 'Enfoques de aprendizaje',
        'pt': 'Abordagens de aprendizagem',
        'sw': 'Mbinu za Kujifunza',
        'ar': 'أساليب التعلم',
    }
    
    stats_skills_to_learn = {
        'en': 'Skills to Learn',
        'fr': 'Compétences à apprendre',
        'es': 'Habilidades para aprender',
        'pt': 'Habilidades para aprender',
        'sw': 'Stadi za Kujifunza',
        'ar': 'المهارات للتعلم',
    }
    
    # ===== SECTION TITLES =====
    section_pillars_title = {
        'en': 'Our Learning Pillars',
        'fr': 'Nos Piliers d\'apprentissage',
        'es': 'Nuestros Pilares de Aprendizaje',
        'pt': 'Nossos Pilares de Aprendizagem',
        'sw': 'Nguzo Zetu za Kujifunza',
        'ar': 'أركان التعلم لدينا',
    }
    
    section_pillars_subtitle = {
        'en': 'Every path begins here. Choose your starting point.',
        'fr': 'Chaque chemin commence ici. Choisissez votre point de départ.',
        'es': 'Cada camino comienza aquí. Elige tu punto de partida.',
        'pt': 'Cada caminho começa aqui. Escolha o seu ponto de partida.',
        'sw': 'Kila njia inaanza hapa. Chagua mahali pa kuanzia.',
        'ar': 'كل طريق يبدأ هنا. اختر نقطة البداية الخاصة بك.',
    }
    
    # ===== CTA SECTION =====
    cta_title = {
        'en': 'Ready to Build Your Future?',
        'fr': 'Prêt à construire votre avenir ?',
        'es': '¿Listo para construir tu futuro?',
        'pt': 'Pronto para construir o seu futuro?',
        'sw': 'Je, uko tayari kujenga maisha yako?',
        'ar': 'هل أنت مستعد لبناء مستقبلك؟',
    }
    
    cta_subtitle = {
        'en': 'SkillsContinua is not about finding a job. It is about creating one — for yourself and your community.',
        'fr': 'SkillsContinua ne consiste pas à trouver un emploi. Il s\'agit d\'en créer un — pour vous-même et pour votre communauté.',
        'es': 'SkillsContinua no se trata de encontrar un trabajo. Se trata de crear uno — para ti y para tu comunidad.',
        'pt': 'A SkillsContinua não se trata de encontrar um emprego. Trata-se de criar um — para si e para a sua comunidade.',
        'sw': 'SkillsContinua siyo kuhusu kupata kazi. Ni kuhusu kuunda kazi — kwa ajili yako na jamii yako.',
        'ar': 'سكيلزكونتينوا ليست عن إيجاد وظيفة. إنها عن خلق وظيفة — لنفسك ولمجتمعك.',
    }
    
    cta_button = {
        'en': 'Join SkillsContinua Today',
        'fr': 'Rejoignez SkillsContinua Aujourd\'hui',
        'es': 'Únete a SkillsContinua Hoy',
        'pt': 'Junte-se à SkillsContinua Hoje',
        'sw': 'Jiunge na SkillsContinua Leo',
        'ar': 'انضم إلى سكيلزكونتينوا اليوم',
    }
    
    return {
        # Site Info
        'SITE_NAME': get_translation(site_name),
        'SITE_TAGLINE': get_translation(site_tagline),
        'SITE_DESCRIPTION': get_translation(site_description),
        'CONTACT_EMAIL': get_translation(contact_email),
        
        # Navigation
        'NAV_HOME': get_translation(nav_home),
        'NAV_COURSES': get_translation(nav_courses),
        'NAV_DASHBOARD': get_translation(nav_dashboard),
        'NAV_LOGIN': get_translation(nav_login),
        'NAV_LOGOUT': get_translation(nav_logout),
        'NAV_REGISTER': get_translation(nav_register),
        'NAV_START_FREE': get_translation(nav_start_free),
        
        # Footer
        'FOOTER_LEARNING_PILLARS': get_translation(footer_learning_pillars),
        'FOOTER_QUICK_LINKS': get_translation(footer_quick_links),
        'FOOTER_CONTACT': get_translation(footer_contact),
        'FOOTER_ALL_COURSES': get_translation(footer_all_courses),
        'FOOTER_ABOUT': get_translation(footer_about),
        'FOOTER_COPYRIGHT': get_translation(footer_copyright),
        
        # Hero Section
        'HERO_TITLE': get_translation(hero_title),
        'HERO_SUBTITLE': get_translation(hero_subtitle),
        'HERO_BUTTON_START': get_translation(hero_button_start),
        'HERO_BUTTON_BROWSE': get_translation(hero_button_browse),
        
        # Stats
        'STATS_PILLARS': get_translation(stats_learning_pillars),
        'STATS_COURSES': get_translation(stats_courses_available),
        'STATS_APPROACHES': get_translation(stats_learning_approaches),
        'STATS_SKILLS': get_translation(stats_skills_to_learn),
        
        # Section Titles
        'SECTION_PILLARS_TITLE': get_translation(section_pillars_title),
        'SECTION_PILLARS_SUBTITLE': get_translation(section_pillars_subtitle),
        
        # CTA
        'CTA_TITLE': get_translation(cta_title),
        'CTA_SUBTITLE': get_translation(cta_subtitle),
        'CTA_BUTTON': get_translation(cta_button),
    }