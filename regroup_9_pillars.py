import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Category

PILLARS = {
 1: "DIGITAL & TECH SKILLS",
 2: "GREEN & CLIMATE SKILLS",
 3: "ENTREPRENEURSHIP & HANDIWORK",
 4: "CONSTRUCTION & TECHNICAL",
 5: "HEALTH & SOCIAL CARE",
 6: "AFRICAN HERITAGE & CULTURAL SKILLS",
 7: "SCHOOL-BASED & CAREER SKILLS",
 8: "RETURNEE & REINTEGRATION",
 9: "ENERGY, POWER & OFF-GRID"
}

for pid, name in PILLARS.items():
    cat, _ = Category.objects.get_or_create(name=name, defaults={'pillar': pid})
    cat.pillar = pid
    cat.save()

def assign(c):
    t = (c.title + " " + (c.description or "")).lower()
    if any(k in t for k in ['cryogenic','cryo']):
        return 9
    if any(k in t for k in ['cctv','surveillance','robot','mechatronics','automation','drone']):
        return 1
    if any(k in t for k in ['solar','hydro','wind','flywheel','generator','battery','inverter','biogas','diesel','turbine','grid','power','energy storage','fuel cell']):
        return 9
    if any(k in t for k in ['carburetor','carburator','injector','fuel pump','turbo','obd','diagnostic','engine tune','fuel management','automotive','mechanic','car repair','motor vehicle']):
        return 9 # All fuel management + diagnostics grouped with Power & Auto
    if any(k in t for k in ['coding','python','data','cloud','ui','ux','marketing','software','web','app',' ai ','machine learning','programming']):
        return 1
    if any(k in t for k in ['agric','farm','recycl','climate','compost','organic','crop','livestock','poultry','fish','irrigation']):
        return 2
    if any(k in t for k in ['plumb','electrical install','weld','mason','bricklay','carpentry','tiling','construction']):
        return 4
    if any(k in t for k in ['health','caregiv','first aid','nursing','hygiene','community health']):
        return 5
    if any(k in t for k in ['igbo','yoruba','hausa','swahili','kente','adire','pottery','palm oil','shea','bead','drum','language','culture','heritage','african']):
        return 6
    if any(k in t for k in ['teen','cv ','public speak','interview','career','school','student']):
        return 7
    if any(k in t for k in ['returnee','reintegration','migration','grant','resettlement','business plan']):
        return 8
    return 3

counts={}
for course in Course.objects.all():
    pid = assign(course)
    cat = Category.objects.get(name=PILLARS[pid])
    course.category = cat
    course.save()
    counts[pid]=counts.get(pid,0)+1

print("\nRegrouped 317 courses:")
for i in range(1,10):
    print(f"{i}. {PILLARS[i]}: {counts.get(i,0)}")

print("\nSample Energy Pillar (9) - should include flywheel both + fuel management:")
for c in Course.objects.filter(category__name=PILLARS[9])[:20]:
    print("-", c.title)


import json, os
# --- EXPORT FOR WEBSITE DYNAMIC SYNC ---
output_path = os.path.join(os.path.dirname(__file__), "core", "pillars_data.json")
# Assuming you have a dict like pillars = {"DIGITAL & TECH SKILLS": [list of courses], ...}
# If your variable is named differently, change below
try:
    # Try to export the regrouped dict you already built
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(pillars_dict, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Exported dynamic pillars_data.json to {output_path}")
except NameError:
    print("\n⚠️ Could not find pillars_dict variable. Please tell me your variable name inside regroup_9_pillars.py so I fix it.")
