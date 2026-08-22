import os, django, time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
try:
    from deep_translator import GoogleTranslator
except:
    os.system("pip install deep-translator")
    from deep_translator import GoogleTranslator
from courses.models import Lesson

def tr(text, target):
    if not text or len(text)<5: return text
    try:
        # split big HTML content into chunks
        chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
        out = ""
        for ch in chunks:
            out += GoogleTranslator(source='en', target=target).translate(ch)
            time.sleep(0.3)
        return out
    except Exception as e:
        print(f" retry {target}: {e}")
        time.sleep(2)
        return text

langs = [('fr','title_fr','content_fr'),('es','title_es','content_es'),('pt','title_pt','content_pt'),('sw','title_sw','content_sw'),('ar','title_ar','content_ar')]

qs = Lesson.objects.all().order_by('id')
print(f"LESSONS {qs.count()} x5 = {qs.count()*5}")

for idx, les in enumerate(qs,1):
    for code, tf, cf in langs:
        if getattr(les, tf, None) and getattr(les, cf, None) and len(getattr(les, cf))>20:
            continue
        print(f"[{idx}/{qs.count()}] Lesson {les.id} {les.title[:40]} -> {code}")
        if not getattr(les, tf):
            setattr(les, tf, tr(les.title, code))
        setattr(les, cf, tr(les.content, code))
        les.save(update_fields=[tf, cf])
        time.sleep(0.8)
print("LESSON TRANSLATION DONE")