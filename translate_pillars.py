from courses.models import Category
from deep_translator import GoogleTranslator

langs = ['fr','sw']
for cat in Category.objects.all():
    print(f"Translating {cat.name}...")
    try:
        if not cat.name_fr:
            cat.name_fr = GoogleTranslator(source='en', target='fr').translate(cat.name)
        if not cat.description_fr:
            desc = cat.description[:400] if cat.description else cat.name
            cat.description_fr = GoogleTranslator(source='en', target='fr').translate(desc)
        if not cat.name_sw:
            cat.name_sw = GoogleTranslator(source='en', target='sw').translate(cat.name)
        if not cat.description_sw:
            desc = cat.description[:400] if cat.description else cat.name
            cat.description_sw = GoogleTranslator(source='en', target='sw').translate(desc)
        cat.save()
        print(f"  -> FR: {cat.name_fr} | SW: {cat.name_sw}")
    except Exception as e:
        print(f"  Error: {e}")

print("Done - 9 pillars translated to FR + SW")