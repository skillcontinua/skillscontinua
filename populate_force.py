import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Lesson
qs = Lesson.objects.all()
c=0
for l in qs:
    if "Skill 1" in (l.content or "") or "Essential Skills" in (l.content or "") or len(l.content or "")<500:
        title=l.title
        course=l.course.title
        l.content=f"<h3>{title}</h3><p><strong>Course:</strong> {course}</p><h4>1. Theory</h4><p>{title} is core to {course}. In Nigeria, this skill creates jobs in Aba.</p><ul><li>Definition</li><li>Why it matters</li><li>Safety</li></ul><h4>2. Practical</h4><ol><li>Prepare tools</li><li>Practice {title}</li><li>Check quality</li><li>Costing for client</li></ol><h4>3. Business</h4><p>How to charge, handle complaints, portfolio.</p><h4>Task</h4><p>Do it this week and upload photo.</p>"
        l.save()
        c+=1
print(f"Force updated {c} placeholder lessons")