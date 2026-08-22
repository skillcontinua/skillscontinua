import os, django, time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()

# try install translator
try:
    from deep_translator import GoogleTranslator
except:
    os.system("pip install deep-translator")
    from deep_translator import GoogleTranslator

from courses.models import Course

def tr(text, target):
    if not text: return text
    try:
        return GoogleTranslator(source='en', target=target).translate(text[:4500])
    except Exception as e:
        print(f"  retry {target}: {e}")
        time.sleep(2)
        try:
            return GoogleTranslator(source='en', target=target).translate(text[:4500])
        except:
            return text

langs = [('fr','title_fr','description_fr'),('es','title_es','description_es'),('pt','title_pt','description_pt')]

qs = Course.objects.all().order_by('id')
total = qs.count()
print(f"TOTAL {total}")

for idx, c in enumerate(qs,1):
    # skip if already translated (different from EN)
    need = False
    for _, tf, df in langs:
        if getattr(c, tf) == c.title or not getattr(c, tf):
            need = True
    if not need:
        continue

    print(f"[{idx}/{total}] {c.id}: {c.title[:40]}")
    for code, tf, df in langs:
        if getattr(c, tf) == c.title or not getattr(c, tf):
            setattr(c, tf, tr(c.title, code))
            setattr(c, df, tr(c.description, code))
            c.save(update_fields=[tf, df])
            print(f"  -> {code} saved")
            time.sleep(0.8)  # avoid google block

print("DONE ALL TRANSLATED")