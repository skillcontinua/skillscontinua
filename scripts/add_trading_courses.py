import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Category, Course, Lesson
from accounts.models import User

admin = User.objects.filter(is_superuser=True).first()

# Add to entrepreneurship/financial pillar
ent_cat = Category.objects.filter(pillar='entrepreneurship').first()
fin_cat = Category.objects.filter(pillar='financial').first()
voc_cat = Category.objects.filter(pillar='vocational').first()

if not ent_cat:
    ent_cat = Category.objects.create(name='Entrepreneurship', pillar='entrepreneurship', language='English')
if not fin_cat:
    fin_cat = Category.objects.create(name='Financial Skills', pillar='financial', language='English')

new_courses = [
    {
        'title': 'Trading and Petty Business Management',
        'description': 'Essential business skills for market traders, street vendors and petty traders. Learn to calculate the TRUE cost of goods, understand profit and loss, manage cash flow, keep simple records and grow from surviving to thriving. Designed for traders at all levels of education.',
        'category': ent_cat,
        'level': 'beginner',
        'duration_hours': 25,
        'is_compulsory': True,
    },
    {
        'title': 'Simple Bookkeeping for Small Businesses',
        'description': 'Every business needs records. Learn to record income and expenses daily, calculate real profit, understand the difference between cash and profit, and produce simple financial statements. No accounting background needed — designed for traders, artisans and small business owners.',
        'category': fin_cat,
        'level': 'beginner',
        'duration_hours': 20,
        'is_compulsory': True,
    },
    {
        'title': 'Value-Added Business — Transforming Raw Materials into Profit',
        'description': 'For businesses that buy raw materials and transform them before selling. Learn to price correctly when you add value through cooking, sewing, crafting or processing. Covers costing, pricing, quality control and scaling a value-added business.',
        'category': ent_cat,
        'level': 'beginner',
        'duration_hours': 20,
        'is_compulsory': False,
    },
    {
        'title': 'Market Trading — Buying and Reselling for Profit',
        'description': 'For pure traders who buy goods and resell them. Master the calculation of true cost including transport, fees, losses and time. Learn to identify profitable products, negotiate with suppliers, manage stock and maximise margins.',
        'category': ent_cat,
        'level': 'beginner',
        'duration_hours': 20,
        'is_compulsory': False,
    },
]

for data in new_courses:
    course, created = Course.objects.get_or_create(
        title=data['title'],
        defaults={
            'category': data['category'],
            'description': data['description'],
            'level': data['level'],
            'age_group': 'adult',
            'language': 'English',
            'duration_hours': data['duration_hours'],
            'is_compulsory': data['is_compulsory'],
            'is_active': True,
            'created_by': admin,
        }
    )
    status = 'CREATED' if created else 'EXISTS'
    print(f'{status}: {data["title"]}')

print(f'\nTotal courses: {Course.objects.count()}')
