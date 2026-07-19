from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

class ForceLanguageMiddleware(MiddlewareMixin):
    """Force language based on URL prefix and session"""
    
    def process_request(self, request):
        # Check if language is set in session or cookie
        language = request.session.get('django_language')
        if not language:
            language = request.COOKIES.get('django_language')
        
        if language:
            translation.activate(language)
            request.LANGUAGE_CODE = language
        else:
            # Default to English
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'