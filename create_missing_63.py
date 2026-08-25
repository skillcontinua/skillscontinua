import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson
# ... rest of your file stays
from courses.models import Course, Lesson

c, created = Course.objects.get_or_create(id=254, defaults=dict(
    title='Offset Printing - Traditional and Modern',
    description='''Offset printing - history, principles, equipment, plate making, press operations, and modern digital offset technology.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=255, defaults=dict(
    title='Digital Printing Technology',
    description='''Digital printing - laser printing, inkjet printing, 3D printing, digital workflow, and applications in modern printing.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=256, defaults=dict(
    title='Screen Printing - Techniques and Applications',
    description='''Screen printing - history, methods, equipment, materials, and applications in textiles, signage, and commercial printing.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=257, defaults=dict(
    title='3D Printing Technology - Complete Guide',
    description='''3D printing - evolution, types (FDM, SLA, SLS, DLP), materials, applications, and emerging trends in additive manufacturing.''',
    level='advanced',
    duration_hours=30,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=258, defaults=dict(
    title='Printing Materials and Inks',
    description='''Printing materials - papers, boards, inks, toners, special coatings, and sustainable materials in modern printing.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=259, defaults=dict(
    title='Print Finishing and Binding',
    description='''Print finishing - cutting, folding, binding, lamination, and post-press processes for professional print production.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=260, defaults=dict(
    title='Color Management in Printing',
    description='''Color management - color theory, calibration, ICC profiles, and achieving accurate color reproduction in printing.''',
    level='advanced',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=261, defaults=dict(
    title='Prepress and Print Production Workflow',
    description='''Prepress and production workflow - file preparation, proofing, plate making, and quality control in print production.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=262, defaults=dict(
    title='Printing Business Management and Marketing',
    description='''Printing business management - operations, pricing, customer service, marketing, and building a successful printing enterprise.''',
    level='advanced',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=263, defaults=dict(
    title='Fish Farming - Complete Guide',
    description='''Complete fish farming - pond construction, fingerling production, feeding, water quality management, harvesting, and fish processing.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=264, defaults=dict(
    title='Aquaculture and Fish Processing',
    description='''Advanced aquaculture - fish hatchery, feed production, disease management, processing, and value addition for fish products.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=265, defaults=dict(
    title='Catfish Farming - Production and Marketing',
    description='''Catfish farming - breeding, feeding, pond management, harvesting, processing, and marketing catfish products.''',
    level='beginner',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=266, defaults=dict(
    title='Poultry Farming - Complete Guide',
    description='''Complete poultry farming - broiler and layer production, housing, feeding, health management, and egg processing.''',
    level='beginner',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=267, defaults=dict(
    title='Broiler Production and Management',
    description='''Broiler production - day-old chick management, feeding programs, vaccination, housing, disease prevention, and processing.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=268, defaults=dict(
    title='Layer Production and Egg Processing',
    description='''Layer production - pullet rearing, egg production, egg grading, processing, and marketing eggs for profit.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=269, defaults=dict(
    title='Piggery Farming - Complete Guide',
    description='''Complete piggery farming - pig breeds, housing, feeding, breeding, health management, and pork production.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=270, defaults=dict(
    title='Breeding and Farrowing Management',
    description='''Breeding and farrowing - sow management, breeding techniques, farrowing, piglet care, and lactation management.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=271, defaults=dict(
    title='Beekeeping and Honey Production',
    description='''Beekeeping - bee biology, hive construction, colony management, honey extraction, and marketing honey products.''',
    level='beginner',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=272, defaults=dict(
    title='Advanced Beekeeping and Apiary Management',
    description='''Advanced beekeeping - queen rearing, disease management, pollination services, and commercial apiary management.''',
    level='advanced',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=273, defaults=dict(
    title='Cattle Rearing and Herd Management',
    description='''Cattle rearing - breeds, housing, feeding, health management, herd recording, and sustainable cattle production.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=274, defaults=dict(
    title='Dairy Production and Milk Processing',
    description='''Dairy production - milk production, milking techniques, milk quality, processing, and value-added dairy products.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=275, defaults=dict(
    title='Cheese and Yogurt Making',
    description='''Cheese and yogurt making - milk preparation, fermentation, cheese types, ripening, and dairy product quality control.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=276, defaults=dict(
    title='Leather Tanning and Processing',
    description='''Leather tanning - hide collection, preservation, tanning methods, finishing, and quality control in leather production.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=277, defaults=dict(
    title='Leather Craft and Product Making',
    description='''Leather craft - leather products, cutting, stitching, finishing, and creating quality leather goods for the market.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=278, defaults=dict(
    title='Shoe and Bag Making',
    description='''Shoe and bag making - pattern making, cutting, assembly, finishing, and producing quality footwear and bags.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=279, defaults=dict(
    title='Blockchain Technology - Complete Guide',
    description='''Complete blockchain technology - history, evolution, types, uses, advantages, and emerging applications in various industries.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=280, defaults=dict(
    title='Cryptocurrency and Digital Finance',
    description='''Cryptocurrency - Bitcoin, Ethereum, and other digital currencies. Trading, investing, and digital finance management.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=281, defaults=dict(
    title='Smart Contracts and Decentralized Applications',
    description='''Smart contracts - creation, deployment, and management. DApps and decentralized finance (DeFi) applications.''',
    level='advanced',
    duration_hours=30,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=282, defaults=dict(
    title='Artificial Intelligence Fundamentals',
    description='''AI fundamentals - history, evolution, types, and applications. Understanding AI and its impact on society and business.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=283, defaults=dict(
    title='Machine Learning - Complete Guide',
    description='''Machine learning - supervised, unsupervised, and reinforcement learning. Algorithms, models, and practical applications.''',
    level='advanced',
    duration_hours=30,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=284, defaults=dict(
    title='ChatGPT and Generative AI',
    description='''ChatGPT and generative AI - prompt engineering, content creation, automation, and practical uses in business and education.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=285, defaults=dict(
    title='Cloud Computing - Complete Guide',
    description='''Cloud computing - history, evolution, types (IaaS, PaaS, SaaS), and major cloud providers. Understanding cloud architecture.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=286, defaults=dict(
    title='Amazon Web Services (AWS) Fundamentals',
    description='''AWS cloud services - EC2, S3, RDS, and other AWS services. Cloud deployment and management on AWS.''',
    level='advanced',
    duration_hours=30,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=287, defaults=dict(
    title='Google Cloud Platform (GCP) Fundamentals',
    description='''Google Cloud Platform - computing, storage, databases, and machine learning services on GCP.''',
    level='advanced',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=288, defaults=dict(
    title='Microsoft Azure Fundamentals',
    description='''Microsoft Azure - cloud services, virtual machines, storage, and Azure solutions for business.''',
    level='advanced',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=289, defaults=dict(
    title='Sculpture - Complete Guide',
    description='''Complete sculpture - materials, techniques, tools, and creating professional sculptures. From clay to bronze and modern materials.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=290, defaults=dict(
    title='Wood Carving - Techniques and Tools',
    description='''Wood carving - tools, techniques, wood selection, and creating beautiful carved pieces. From basic to advanced carving.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=291, defaults=dict(
    title='Stone Carving and Sculpture',
    description='''Stone carving - stone selection, tools, techniques, and creating durable stone sculptures and architectural elements.''',
    level='advanced',
    duration_hours=30,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=292, defaults=dict(
    title='Painting - Complete Guide',
    description='''Complete painting - oils, acrylics, watercolors, techniques, color theory, and creating professional paintings.''',
    level='beginner',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=293, defaults=dict(
    title='Drawing and Sketching Fundamentals',
    description='''Drawing and sketching - techniques, materials, perspective, anatomy, and creating professional drawings.''',
    level='beginner',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=294, defaults=dict(
    title='Advanced Drawing and Illustration',
    description='''Advanced drawing - figure drawing, portraiture, illustration techniques, and professional illustration work.''',
    level='advanced',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=295, defaults=dict(
    title='Pottery and Ceramics - Complete Guide',
    description='''Pottery and ceramics - clay preparation, wheel throwing, hand building, glazing, firing, and creating professional pottery.''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=296, defaults=dict(
    title='Basket Weaving and Fiber Arts',
    description='''Basket weaving and fiber arts - materials, weaving techniques, patterns, and creating functional and decorative baskets.''',
    level='beginner',
    duration_hours=15,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=297, defaults=dict(
    title='Advanced Weaving and Textile Arts',
    description='''Advanced weaving - loom techniques, pattern design, textile creation, and professional weaving practices.''',
    level='advanced',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=298, defaults=dict(
    title='Mixed Media and Contemporary Art',
    description='''Mixed media and contemporary art - combining materials, techniques, and creating innovative contemporary artwork.''',
    level='advanced',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=299, defaults=dict(
    title='Tai Chi - Complete Guide',
    description='''Complete Tai Chi - history, philosophy, forms, health benefits, and mastering Tai Chi for physical and mental wellness.''',
    level='beginner',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=300, defaults=dict(
    title='Advanced Tai Chi and Qigong',
    description='''Advanced Tai Chi and Qigong - complex forms, energy cultivation, and advanced health applications.''',
    level='advanced',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=301, defaults=dict(
    title='Meditation and Mindfulness',
    description='''Meditation and mindfulness - techniques, practices, health benefits, and incorporating mindfulness into daily life.''',
    level='beginner',
    duration_hours=15,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=302, defaults=dict(
    title='Yoga - Complete Guide',
    description='''Complete yoga - history, philosophy, postures, breathing techniques, and yoga for health and wellness.''',
    level='beginner',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=303, defaults=dict(
    title='Advanced Yoga and Pranayama',
    description='''Advanced yoga - complex postures, advanced breathing techniques, meditation, and holistic health practices.''',
    level='advanced',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=304, defaults=dict(
    title='Holistic Health and Wellness',
    description='''Holistic health - nutrition, exercise, stress management, sleep, and creating a balanced healthy lifestyle.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=305, defaults=dict(
    title='Stress Management and Relaxation',
    description='''Stress management - techniques, relaxation practices, and building resilience for a balanced life.''',
    level='beginner',
    duration_hours=15,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=306, defaults=dict(
    title='Mind-Body Connection and Health',
    description='''Mind-body connection - understanding the relationship between mental and physical health, and practices for optimal well-being.''',
    level='intermediate',
    duration_hours=20,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=307, defaults=dict(
    title='Advanced AI and Machine Learning Applications',
    description='''Master artificial intelligence and machine learning with practical applications in Python, neural networks, deep learning, and real-world AI deployment across industries like healthcare, finance, and autonomous systems.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=308, defaults=dict(
    title='Quantum Computing Fundamentals',
    description='''Explore the revolutionary field of quantum computing, covering qubits, quantum gates, superposition, entanglement, and practical algorithms that will transform computing power beyond classical limits.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=309, defaults=dict(
    title='Biotechnology and Genetic Engineering',
    description='''Dive into biotechnology and genetic engineering, covering DNA manipulation, CRISPR technology, bioinformatics, and practical applications in medicine, agriculture, and environmental science.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=310, defaults=dict(
    title='Renewable Energy Systems Engineering',
    description='''Master renewable energy systems including solar, wind, hydro, biomass, and geothermal energy. Learn system design, implementation, efficiency optimization, and sustainable energy management.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=311, defaults=dict(
    title='Robotics and Automation Advanced',
    description='''Explore advanced robotics and automation covering robotic kinematics, control systems, machine vision, industrial automation, and applications in manufacturing, logistics, and service industries.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=312, defaults=dict(
    title='Space Technology and Exploration',
    description='''Discover space technology and exploration covering rocket science, satellite technology, space systems, orbital mechanics, and the future of human space exploration and colonization.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=313, defaults=dict(
    title='Virtual and Augmented Reality Development',
    description='''Learn virtual and augmented reality development covering 3D modeling, interactive experiences, game engines, and practical applications in education, healthcare, entertainment, and enterprise.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=314, defaults=dict(
    title='Nano Technology and Materials Science',
    description='''Explore nanotechnology and materials science covering nanomaterials, molecular engineering, surface science, and practical applications in medicine, electronics, energy, and manufacturing.''',
    level='intermediate',
    duration_hours=40,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=315, defaults=dict(
    title='Flywheel Energy Storage & AC Generation Systems',
    description=''' ### Master Flywheel Energy Storage & AC Generation  This course teaches you how to build a soundless, fossil-fuel-free power system using a battery, DC motor, flywheel, and AC generator.  Based on real-world innovation from Lagos, Nigeria, this system provides clean, quiet, and sustainable electricity.  ### What You\'ll Learn - How flywheels store and release energy - How to use a DC motor as a generator - The physics of rotational energy - How to generate AC power from DC sources - System asse''',
    level='intermediate',
    duration_hours=25,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))

c, created = Course.objects.get_or_create(id=316, defaults=dict(
    title='Sample Course',
    description='''Demo''',
    level='',
    duration_hours=10,
    pillar_id=1
))
if created:
    print(f"Created {c.id} {c.title}")
    for i in range(1,11):
        Lesson.objects.get_or_create(course=c, order=i, defaults=dict(title=f"Module {i}: {c.title}", content=f"<h3>Module {i}: {c.title}</h3><p>Theory and practical for module {i}.</p>"))
