import os, django, time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()

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
        time.sleep(3)
        return text

langs = [
  ('fr','title_fr','description_fr'),
  ('es','title_es','description_es'),
  ('pt','title_pt','description_pt'),
  ('sw','title_sw','description_sw'),
  ('ar','title_ar','description_ar'),
]

qs = Course.objects.all().order_by('id')
print(f"TOTAL {qs.count()} - TARGET 5 LANGS = {qs.count()*5} translations")

for idx, c in enumerate(qs,1):
    for code, tf, df in langs:
        cur_t = getattr(c, tf, None)
        if cur_t and cur_t != c.title and len(cur_t) > 3:
            continue
        print(f"[{idx}] {c.id} {c.title[:30]} -> {code}")
        setattr(c, tf, tr(c.title, code))
        setattr(c, df, tr(c.description, code))
        c.save(update_fields=[tf, df])
        time.sleep(1)

print("DONE 1.5B COVERAGE")