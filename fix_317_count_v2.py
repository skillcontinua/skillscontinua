import os, django, json, pathlib
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

print(f"Current courses in DB: {Course.objects.count()}")
for c in Course.objects.filter(id__in=[315,316,317]).order_by('id'):
    lessons = Lesson.objects.filter(course=c).count()
    print(f"  ID {c.id}: {c.title[:70]} - {lessons} lessons")

exam_file = pathlib.Path("final_exams_316.json")
if exam_file.exists():
    data = json.loads(exam_file.read_text(encoding='utf-8'))
    print(f"\nfinal_exams_316.json type: {type(data).__name__}")
    if isinstance(data, list):
        print(f"  List length: {len(data)}")
        if len(data) > 0:
            print(f"  First element type: {type(data[0]).__name__}")
            print(f"  First element sample: {str(data[0])[:500]}")
        # Try to get IDs
        ids = []
        for d in data:
            if isinstance(d, dict):
                ids.append(d.get('course_id') or d.get('course') or d.get('id'))
            elif isinstance(d, (int, str)):
                ids.append(d)
        print(f"  Found {len(ids)} IDs, sample: {ids[:10]}")
        if 317 not in ids and '317' not in ids:
            print("  Adding course 317...")
            # Find template exam from 315
            template = None
            for d in data:
                if isinstance(d, dict) and (d.get('course_id')==315 or d.get('course')==315 or d.get('id')==315):
                    template = d
                    break
            if not template and len(data)>0 and isinstance(data[0], dict):
                template = data[0]
            if template:
                new_exam = json.loads(json.dumps(template))
                if 'course_id' in new_exam:
                    new_exam['course_id'] = 317
                if 'course' in new_exam:
                    new_exam['course'] = 317
                if 'id' in new_exam:
                    new_exam['id'] = 317
                if 'title' in new_exam:
                    new_exam['title'] = "Final Exam - Flywheel Generator with Springs"
                data.append(new_exam)
                print(f"  Added, new length: {len(data)}")
                pathlib.Path("final_exams_317.json").write_text(json.dumps(data, indent=2), encoding='utf-8')
                exam_file.write_text(json.dumps(data, indent=2), encoding='utf-8')
                print(f"  Created final_exams_317.json with {len(data)} exams")
            else:
                print("  No template found - creating minimal exam for 317")
                # Create minimal
                minimal = {"course_id": 317, "course": 317, "title": "Final Exam - Flywheel with Springs", "questions": []}
                data.append(minimal)
                pathlib.Path("final_exams_317.json").write_text(json.dumps(data, indent=2), encoding='utf-8')
                exam_file.write_text(json.dumps(data, indent=2), encoding='utf-8')
    elif isinstance(data, dict):
        print(f"  Dict keys: {list(data.keys())[:10]} length {len(data)}")
        if '317' not in data and 317 not in data:
            print("  Adding course 317 to dict...")
            # Find template
            template_key = '315' if '315' in data else (315 if 315 in data else list(data.keys())[0])
            data['317'] = json.loads(json.dumps(data[str(template_key)] if str(template_key) in data else data[template_key]))
            pathlib.Path("final_exams_317.json").write_text(json.dumps(data, indent=2), encoding='utf-8')
            exam_file.write_text(json.dumps(data, indent=2), encoding='utf-8')
            print(f"  Added, new dict size: {len(data)}")
        else:
            print("  317 already in dict")
            pathlib.Path("final_exams_317.json").write_text(json.dumps(data, indent=2), encoding='utf-8')

print(f"\nFinal: Courses={Course.objects.count()}, Lessons={Lesson.objects.count()}")