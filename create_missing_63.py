import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

missing = {
254:"Printing Technology",255:"Offset Printing",256:"Digital Printing",257:"3D Printing",258:"Printing Materials",259:"Print Finishing",260:"Color Management",261:"Prepress Workflow",262:"Printing Business",263:"Fish Farming",264:"Aquaculture",265:"Catfish Farming",266:"Poultry Farming",267:"Broiler Production",268:"Layer Production",269:"Piggery Farming",270:"Breeding and Farrowing",271:"Beekeeping",272:"Advanced Beekeeping",273:"Cattle Rearing",274:"Dairy Production",275:"Cheese and Yogurt",276:"Leather Tanning",277:"Leather Craft",278:"Shoe and Bag Making",279:"Blockchain Technology",280:"Cryptocurrency",281:"Smart Contracts",282:"AI Fundamentals",283:"Machine Learning",284:"Generative AI",285:"Cloud Computing",286:"AWS Fundamentals",287:"Google Cloud",288:"Microsoft Azure",289:"Sculpture",290:"Wood Carving",291:"Stone Carving",292:"Painting",293:"Drawing and Sketching",294:"Advanced Drawing",295:"Pottery and Ceramics",296:"Basket Weaving",297:"Advanced Weaving",298:"Mixed Media Art",299:"Tai Chi",300:"Advanced Tai Chi",301:"Meditation",302:"Yoga",303:"Advanced Yoga",304:"Holistic Health",305:"Stress Management",306:"Mind-Body Connection",307:"Advanced AI",308:"Quantum Computing",309:"Biotechnology",310:"Renewable Energy",311:"Robotics Advanced",312:"Space Technology",313:"VR and AR",314:"Nano Technology",315:"Flywheel Energy Storage",316:"Sample Course"
}

for cid, title in missing.items():
    c, created = Course.objects.get_or_create(id=cid, defaults=dict(title=title, category="Vocational Trades", description=f"{title} complete guide for Nigeria self-employment.", level="Beginner", duration_hours=10, is_active=True))
    if created:
        print(f"CREATED {cid}")
        for i in range(1,11):
            Lesson.objects.create(course=c, title=f"Module {i}: {title}", order=i, content=f"<h3>Module {i}: {title}</h3><p>Learn {title}.</p>")

print(f"COUNT: {Course.objects.count()}")