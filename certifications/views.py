"""
certifications/views.py - Africa edition with auto LANGUAGE_CODE detection
Supports: en, fr, pt, sw, ar, es + fallback
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import translation
from courses.models import Course
import datetime, uuid

# Translations for certificate text - Africa edition
CERT_TRANSLATIONS = {
    'en': {
        'certificate': 'CERTIFICATE',
        'of_achievement': 'OF ACHIEVEMENT',
        'presented_to': 'THIS CERTIFICATE IS PROUDLY PRESENTED TO',
        'verified': 'VERIFIED CERTIFICATE',
        'desc1': 'For successfully completing the final examination with a score of',
        'desc2': 'and demonstrating practical competence in',
        'desc3': 'This certifies hands-on skills applicable across Africa and beyond.',
        'date': 'Date of Completion',
        'director': 'Director of Learning',
        'cert_id': 'Certificate ID',
    },
    'fr': {
        'certificate': 'CERTIFICAT',
        'of_achievement': 'DE RÉUSSITE',
        'presented_to': 'CE CERTIFICAT EST FIÈREMENT DÉCERNÉ À',
        'verified': 'CERTIFICAT VÉRIFIÉ',
        'desc1': "Pour avoir réussi l'examen final avec un score de",
        'desc2': "et démontré une compétence pratique en",
        'desc3': "Ceci certifie des compétences pratiques applicables à travers l'Afrique et au-delà.",
        'date': "Date d'achèvement",
        'director': "Directeur de l'apprentissage",
        'cert_id': "ID du certificat",
    },
    'pt': {
        'certificate': 'CERTIFICADO',
        'of_achievement': 'DE CONCLUSÃO',
        'presented_to': 'ESTE CERTIFICADO É ORGULHOSAMENTE APRESENTADO A',
        'verified': 'CERTIFICADO VERIFICADO',
        'desc1': 'Por concluir com sucesso o exame final com pontuação de',
        'desc2': 'e demonstrar competência prática em',
        'desc3': 'Isto certifica habilidades práticas aplicáveis em toda a África e além.',
        'date': 'Data de Conclusão',
        'director': 'Diretor de Aprendizagem',
        'cert_id': 'ID do Certificado',
    },
    'sw': {
        'certificate': 'CHETI',
        'of_achievement': 'CHA MAFANIKIO',
        'presented_to': 'CHETI HIKI KINATOLEWA KWA FAHARI KWA',
        'verified': 'CHETI KILICHOTHIBITISHWA',
        'desc1': 'Kwa kukamilisha mtihani wa mwisho kwa alama ya',
        'desc2': 'na kuonyesha umahiri wa vitendo katika',
        'desc3': 'Hii inathibitisha ujuzi wa vitendo unaotumika kote Afrika na kwingineko.',
        'date': 'Tarehe ya Kukamilisha',
        'director': 'Mkurugenzi wa Mafunzo',
        'cert_id': 'Kitambulisho cha Cheti',
    },
    'ar': {
        'certificate': 'شهادة',
        'of_achievement': 'إنجاز',
        'presented_to': 'تم منح هذه الشهادة بفخر إلى',
        'verified': 'شهادة موثقة',
        'desc1': 'لإكمال الامتحان النهائي بنجاح بدرجة',
        'desc2': 'وإظهار الكفاءة العملية في',
        'desc3': 'هذا يثبت المهارات العملية القابلة للتطبيق في جميع أنحاء أفريقيا وخارجها.',
        'date': 'تاريخ الإكمال',
        'director': 'مدير التعلم',
        'cert_id': 'رقم الشهادة',
    },
    'es': {
        'certificate': 'CERTIFICADO',
        'of_achievement': 'DE LOGRO',
        'presented_to': 'ESTE CERTIFICADO SE OTORGA CON ORGULLO A',
        'verified': 'CERTIFICADO VERIFICADO',
        'desc1': 'Por completar con éxito el examen final con una puntuación de',
        'desc2': 'y demostrar competencia práctica en',
        'desc3': 'Esto certifica habilidades prácticas aplicables en toda África y más allá.',
        'date': 'Fecha de finalización',
        'director': 'Director de Aprendizaje',
        'cert_id': 'ID del certificado',
    },
}

def get_lang(request):
    # 1. URL param ?lang=pt
    lang = request.GET.get('lang')
    if lang in CERT_TRANSLATIONS:
        return lang
    # 2. Django LANGUAGE_CODE from user profile / session
    django_lang = translation.get_language()  # e.g. 'pt-br', 'sw-ke'
    if django_lang:
        short = django_lang.split('-')[0].lower()
        if short in CERT_TRANSLATIONS:
            return short
    # 3. Browser Accept-Language header - already handled by Django, fallback to en
    return 'en'

@login_required
def certificate_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # In real app, fetch from Certificate model
    # For now, build context
    lang = get_lang(request)
    trans = CERT_TRANSLATIONS.get(lang, CERT_TRANSLATIONS['en'])
    
    context = {
        'course': course,
        'user': request.user,
        'score': request.GET.get('score', '85'),
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'certificate_id': f'SC-{course_id}-{request.user.id}-{uuid.uuid4().hex[:6].upper()}',
        'lang': lang,
        't': trans,
        # For template that still uses {{ }} tags
        'certificate': trans['certificate'],
        'of_achievement': trans['of_achievement'],
    }
    # Choose template - hyphen version is new Africa edition
    return render(request, 'certifications/certificate-view.html', context)

def verify_certificate(request, cert_id):
    # Public verification - no login
    lang = get_lang(request)
    trans = CERT_TRANSLATIONS.get(lang, CERT_TRANSLATIONS['en'])
    return render(request, 'certifications/verify_certificate.html', {
        'certificate_id': cert_id,
        'lang': lang,
        't': trans,
    })
