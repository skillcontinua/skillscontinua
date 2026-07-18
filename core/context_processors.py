from django.utils import translation

def language_processor(request):
    """Make language settings available to all templates"""
    current_language = translation.get_language()
    
    LANGUAGES = [
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('pt', 'Portuguese'),
        ('sw', 'Swahili'),
        ('ar', 'Arabic'),
    ]
    
    return {
        'current_language': current_language,
        'LANGUAGES': LANGUAGES,
        'language_choices': LANGUAGES,
    }

def site_settings(request):
    """Site-wide settings for templates"""
    return {
        'SITE_NAME': 'SkillsContinua',
        'SITE_TAGLINE': 'From Literacy to Livelihood',
        'SITE_DESCRIPTION': 'Skills for life, career and self-employment',
        'CONTACT_EMAIL': 'info@skillscontinua.com',
    }