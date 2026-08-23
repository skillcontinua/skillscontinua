import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson, Category

print("Splitting flywheel into TWO courses for Africa...")

cat = Category.objects.first()

# Course 315 - Keep as DC Motor + Lithium Battery version
try:
    c315 = Course.objects.get(id=315)
    c315.title = "Flywheel Generator with DC Motor & Lithium Battery - Advanced Power Systems"
    c315.description = "Master flywheel energy storage with DC motor and lithium batteries (LiFePO4). Build soundless fossil-fuel-free power systems for homes, clinics, shops. Includes lithium sizing, BMS, CATL/BYD contacts, business model for Africa and third world."
    c315.duration_hours = 40
    c315.level = "advanced"
    c315.save()
    print(f"Updated Course 315: {c315.title}")
except Course.DoesNotExist:
    print("Course 315 not found")

# Course 317 - NEW: Flywheel with Springs (mechanical)
c317, created = Course.objects.get_or_create(
    id=317,
    defaults=dict(
        title="Flywheel Generator with Springs - Mechanical Energy Storage for Rural Africa",
        description="Master mechanical energy storage using springs + flywheel. No battery needed. Hand-wind spring to power lights, radio. Perfect for rural schools, off-grid, low-cost. Includes spring sourcing from truck starters, governor, producer contacts.",
        level="intermediate",
        duration_hours=35,
        category=cat
    )
)
if created:
    print(f"Created NEW Course 317: {c317.title}")
else:
    c317.title = "Flywheel Generator with Springs - Mechanical Energy Storage for Rural Africa"
    c317.description = "Master mechanical energy storage using springs + flywheel. No battery needed. Hand-wind spring to power lights, radio. Perfect for rural schools, off-grid, low-cost."
    c317.save()
    print(f"Updated Course 317: {c317.title}")

# Define rich lessons for Course 317 - Springs version (10 modules)
spring_modules = [
    {
        'order': 1,
        'title': 'Why Springs + Flywheel? Power Without Battery for Rural Africa',
        'content': """<h2>Module 1: Why Springs + Flywheel? Power Without Battery</h2>
<p><b>For:</b> Rural communities, schools, no money for lithium</p>
<h3>Problem</h3><p>Lithium costs ₦400k. Many cannot afford. Springs from scrap truck starters cost ₦5k, store energy mechanically, no chemical, lasts 20 years.</p>
<h3>Concept</h3><p>Wind spring (store potential energy) -> slowly release to keep flywheel spinning -> generator makes AC. Like giant clock. Hand-wind 5 minutes, get 45 minutes light.</p>
<h3>Business</h3><p>Build for $80, sell for $150 to rural households. No battery replacement cost = big advantage.</p>
"""
    },
    {
        'order': 2,
        'title': 'Spring Types & Sourcing in Africa - Truck Starters, Clock Springs',
        'content': """<h2>Module 2: Spring Types & Sourcing in Africa</h2>
<h3>Types</h3>
<ul><li><b>Truck starter spring (spiral):</b> Most powerful, from lorry starter motor, stores 500Wh, buy at Ladipo Lagos, Kirikiri, Owode Onirin for ₦5k scrap</li><li><b>Compression springs:</b> 10 springs in series, from trailer suspension</li><li><b>Extension springs:</b> easier to fabricate</li></ul>
<h3>Sourcing</h3>
<p>Ladipo Market Lagos - largest auto scrap in Africa. Ask for "starter spring for DAF truck". Nairobi: Kirinyaga Road. Accra: Abossey Okai. Durban: Springfield Park.</p>
<h3>Producer Contacts</h3>
<p>Custom springs: <b>Specialist Springs Nigeria, Sango Ota</b> - makes to spec. <b>Spring Manufacturing UK</b> exports. <b>Alibaba: "clock spring 50mm"</b> - $3 each MOQ 100.</p>
"""
    },
    {
        'order': 3,
        'title': 'Flywheel Design for Spring System - Heavy, Balanced, Safe',
        'content': """<h2>Module 3: Flywheel Design for Spring System</h2>
<h3>Spec for Spring System</h3>
<p>Need heavier flywheel than electrical version because spring releases slowly. 40-60kg, 500mm diameter, EN8 steel. Must be perfectly balanced or vibration dangerous.</p>
<h3>Where to Fabricate</h3>
<p><b>Aba, Nnewi foundries</b> - can cast and machine. <b>Kano Dala Foundry</b>. <b>Kenya Numerical Machining Complex</b>. Cost $60 locally. Balance to G6.3 standard.</p>
<h3>Safety Enclosure</h3>
<p>Flywheel at 1500 RPM stores huge energy - if breaks, deadly. Must have 5mm steel guard, no one stands in line of rotation. Add emergency brake.</p>
"""
    },
    {
        'order': 4,
        'title': 'Ratchet, Governor & Speed Control - Keep 50Hz Constant',
        'content': """<h2>Module 4: Ratchet, Governor & Speed Control</h2>
<h3>Ratchet (One-Way)</h3>
<p>Allows winding spring without spinning flywheel backwards. Use bicycle freewheel or truck ratchet. Weld to spring drum.</p>
<h3>Governor - Critical</h3>
<p>Spring unwinds fast at first, slow at end - need constant 1500 RPM for 50Hz AC. Flyball governor: two balls on springs, expands with speed, pulls brake pad to keep speed constant. Fabricate from steel balls + springs.</p>
<h3>Build</h3>
<ol><li>Mount spring drum on shaft</li><li>Attach spring outer to drum, inner to shaft</li><li>Add ratchet between winding handle and drum</li><li>Add governor on flywheel shaft, connect to brake</li><li>Connect drum to flywheel via chain 1:3 ratio</li></ol>
"""
    },
    {
        'order': 5,
        'title': 'Winding Mechanism - Hand Crank & Small Motor Assist',
        'content': """<h2>Module 5: Winding Mechanism</h2>
<h3>Hand Crank</h3>
<p>Simple handle to wind spring. One person winds 5 minutes = 45 minutes power. Good exercise, no fuel.</p>
<h3>Motor Assist Option</h3>
<p>Small 100W DC motor winds spring automatically when solar available, then spring powers at night. Hybrid solar-spring.</p>
<h3>Ergonomics for Africa</h3>
<p>Make crank at waist height, easy for women, youth. Add seat. Can be community activity.</p>
"""
    },
    {
        'order': 6,
        'title': 'Generator & Electrical Output - AC Power from Mechanical',
        'content': """<h2>Module 6: Generator & Electrical Output</h2>
<p>Same alternator as Course 315: 2-5KVA alternator. Flywheel spins alternator via belt. Need AVR to keep voltage 220V stable despite speed variations (governor helps).</p>
<h3>Wiring</h3>
<p>Alternator -> AVR -> sockets. Add voltmeter, frequency meter (must show 50Hz). Add fuse box.</p>
<h3>Testing</h3>
<p>Wind spring fully, release, measure: how long does 100W bulb stay on? How long 500W? Record.</p>
"""
    },
    {
        'order': 7,
        'title': 'Manufacturer Contacts - Win-Win Partnership',
        'content': """<h2>Module 7: Manufacturer Contacts - Win-Win Partnership</h2>
<h3>Why Manufacturers Should Help Grassroots</h3>
<p>Africa has 600M without power - huge market. If CATL, BYD, spring makers support training, awareness grows, demand grows, business boosts. Humanitarian + profit.</p>
<h3>Contacts - Springs</h3>
<ul><li><b>Specialist Springs Ltd Nigeria (Sango Ota):</b> +234 803... - makes custom spiral springs</li><li><b>Lesjofors (Sweden) - Africa export:</b> lesjofors.com - high quality clock springs</li><li><b>Alibaba:</b> search "spiral torsion spring 50mm width" - suppliers: Dongguan Yongsheng, Shenzhen Xingli - $2-5 each MOQ 50, will send samples</li></ul>
<h3>Contacts - Flywheels & Bearings</h3>
<ul><li><b>SKF Bearings Nigeria:</b> skf.com/ng - pillow block bearings UCP 208</li><li><b>Local foundries:</b> Aba, Nnewi, Kano - will cast flywheel for $60</li></ul>
<h3>Email Template to Manufacturers</h3>
<p>Subject: Partnership - Flywheel Spring Power for Rural Africa - 100k units potential<br>
"Dear [Manufacturer], We are SkillsContinua, humanitarian platform with 316 vocational courses, 100k+ learners across Africa. We teach flywheel spring energy as low-cost off-grid solution using your products (springs, bearings). Your support (samples, datasheets, training, dealer pricing) will increase awareness of your products at grassroots, boost demand in Africa's $10B off-grid market. We can include your logo in our course, link to your distributors. Can we discuss? Contact: [your email] - SkillsContinua.org"</p>
<h3>How to Find More</h3>
<p>Google: "clock spring manufacturer Africa distributor", "spiral torsion spring supplier". LinkedIn: search spring manufacturers, message them.</p>
"""
    },
    {
        'order': 8,
        'title': 'Business Model - Rural, Low-Cost, High Impact',
        'content': """<h2>Module 8: Business Model - Rural, Low-Cost, High Impact</h2>
<p>Cost: flywheel $60 + springs $25 (5x ₦5k) + alternator $100 + frame $30 = $215. Sell $350. Profit $135. No battery replacement = customer saves.</p>
<h3>Target Customers</h3>
<p>Rural schools (light for evening study), churches/mosques, small shops, homes far from grid. 50M such in Africa.</p>
<h3>Marketing in Local Languages</h3>
<p>Demonstrate at market day, school. Let people wind and see light. Word of mouth powerful. In Swahili: "Umeme bila betri". Hausa: "Wuta ba tare da baturi".</p>
"""
    },
    {
        'order': 9,
        'title': 'Maintenance & Field Repairs - No Battery, Less Hassle',
        'content': """<h2>Module 9: Maintenance & Field Repairs</h2>
<p>Advantage: no battery water, no BMS. Only grease bearings, check belt, inspect spring for cracks. Spring lasts 10 years, flywheel 20.</p>
<h3>Field Kit</h3>
<p>Spare belt, grease, spanners, spare spring. Fix on site.</p>
"""
    },
    {
        'order': 10,
        'title': 'Final Project - Build & Power a Classroom',
        'content': """<h2>Module 10: Final Project - Build & Power a Classroom</h2>
<p>Task: Build spring-flywheel system that powers 4x 10W LED bulbs for 1 hour after 5 min winding. Install in local school, get testimonial, video.</p>
<p>Pass to get certificate: "Flywheel Spring Energy - Applicable across Africa and beyond"</p>
<p>After: contact spring manufacturers with your video as proof of market, negotiate dealership.</p>
"""
    }
]

for m in spring_modules:
    lesson, created = Lesson.objects.get_or_create(
        course=c317,
        order=m['order'],
        defaults={'title': m['title'], 'content': m['content']}
    )
    if not created:
        lesson.title = m['title']
        lesson.content = m['content']
        lesson.save()
    print(f"{'Created' if created else 'Updated'} Module {m['order']} for Course 317")

# Also update course 315 lessons to be specifically DC Motor + Lithium focused (ensure they are)
print(f"\nCourse 315 lessons: {Lesson.objects.filter(course_id=315).count()}")
print(f"Course 317 lessons: {Lesson.objects.filter(course_id=317).count()}")

# Create manufacturer outreach letter
letter = """
Subject: Partnership Opportunity - Flywheel Energy for Grassroots Africa - Humanitarian + Business

Dear Manufacturer / Sales Manager,

We are SkillsContinua (skillscontinua.org), a humanitarian vocational platform with 316 practical courses serving 100k+ learners across Africa (Nigeria, Kenya, Tanzania, Angola, Mozambique, Senegal, etc.) and third world countries. Our mission is job creation and self-reliance.

We have two advanced courses:
1. Flywheel Generator with DC Motor & Lithium Battery (Course 315) - uses your DC motors, LiFePO4 batteries, BMS
2. Flywheel Generator with Springs (Course 317) - uses your clock/torsion springs, bearings, governors

We teach learners to build soundless, fossil-fuel-free power systems using your products. This creates awareness at grassroots, increases demand for your products, and boosts your business in Africa's $10B off-grid market.

How you can help and benefit:
- Provide samples, datasheets, technical training videos
- Offer dealer/reseller pricing for our alumni (100+ potential resellers)
- Allow us to list you as recommended supplier with contact/link in course (huge awareness)
- Co-branding: "Recommended by CATL/BYD/SKF" etc.

Win-win: You get market penetration, we get quality components for humanitarian impact.

Our learners are technicians, small business owners who will buy and resell your products.

Can we schedule a call? We can share our course content, learner numbers, and discuss.

Best regards,
SkillsContinua Team
Contact: [your email] | +234...
Website: skillscontinua.org
Courses: 316 | Lessons: 3304 | Quizzes: 33k | Translations: EN, FR, PT, SW, AR, ES

Attachments: Course 315 & 317 outlines, learner testimonials
"""

from pathlib import Path
Path("manufacturer_outreach_letter.txt").write_text(letter, encoding='utf-8')
print("\nCreated manufacturer_outreach_letter.txt - use to contact CATL, BYD, spring makers, SKF")

print("\nSPLIT DONE - Two courses now:")
print("315: DC Motor + Lithium Battery (electrical storage, high energy)")
print("317: Springs (mechanical storage, low-cost rural)")
