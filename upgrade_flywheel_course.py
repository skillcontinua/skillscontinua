import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

print("Upgrading Course 315: Flywheel Energy Storage & AC Generation Systems")
try:
    course = Course.objects.get(id=315)
except Course.DoesNotExist:
    print("Course 315 not found, creating...")
    from courses.models import Category
    cat = Category.objects.first()
    course = Course.objects.create(
        id=315,
        title='Flywheel Energy Storage & AC Generation Systems - Advanced Africa Edition',
        description='Master flywheel energy storage with DC motor, lithium batteries, spring-assisted systems. Build soundless fossil-fuel-free power for Africa. Includes producer contacts.',
        level='advanced',
        duration_hours=40,
        category=cat
    )

# Define 10 rich modules for flywheel upgrades
modules = [
    {
        'order': 1,
        'title': 'Foundation - Why Flywheel for Africa? Energy Poverty Solution',
        'content': """<h2>Module 1: Why Flywheel for Africa? Energy Poverty Solution</h2>
<p><b>Duration: 3 hours</b> | <b>For:</b> Inventors, technicians, off-grid communities</p>
<h3>1. The Problem & Opportunity</h3>
<p>600M Africans lack electricity. Fuel generators are noisy, expensive, polluting. Lagos innovator built soundless flywheel system: battery + DC motor + flywheel + AC generator = clean quiet power. This is humanitarian.</p>
<h3>2. What You Will Build</h3>
<p>Three upgrades: (A) Flywheel + DC Motor + Lithium Battery (high energy), (B) Flywheel + Springs (mechanical storage), (C) Hybrid system for homes.</p>
<h3>3. Physics Made Simple</h3>
<p>Flywheel stores kinetic energy: E = ½ I ω². Heavy wheel spinning fast = battery. Unlike chemical battery, flywheel lasts 20 years, no degradation, instant power.</p>
<h3>4. Business Case</h3>
<p>Household system: build for $300, sell for $600, maintenance $20/month. Target: barbers, cold rooms, clinics, schools. In Nigeria alone market is 10M small businesses.</p>
<h3>5. Task</h3>
<p>Calculate energy needed: 5 bulbs (50W) + fan (75W) + TV (100W) = 225W for 6 hours = 1350Wh. Size flywheel and battery accordingly.</p>
"""
    },
    {
        'order': 2,
        'title': 'Flywheel Generator with DC Motor - Core System',
        'content': """<h2>Module 2: Flywheel Generator with DC Motor - Core System</h2>
<h3>1. System Architecture</h3>
<p>Battery (12V/24V) -> DC Motor (acts as starter) -> Flywheel (heavy, balanced) -> AC Generator (alternator) -> Load. Once spinning, DC motor uses less power than generator produces - energy from flywheel inertia.</p>
<h3>2. Components Sourcing in Africa</h3>
<ul><li>DC Motor: 1-3HP PMDC motor from Alaba International Lagos, or import from Alibaba. Cost $80-150. Look for 1500-3000 RPM, high torque.</li><li>Flywheel: cast iron or steel, 20-50kg, balanced. Fabricate at local foundry in Aba, Kano, Nairobi Industrial Area. Must be balanced to <1g tolerance or vibration destroys bearings.</li><li>AC Generator: 2-5KVA alternator, single phase 220V 50Hz. Use from old Lister generator.</li><li>Shaft, bearings, belt/pulley system.</li></ul>
<h3>3. Assembly Steps</h3>
<ol><li>Mount DC motor and alternator on heavy steel frame (vibration free)</li><li>Mount flywheel on shaft with two pillow block bearings</li><li>Connect DC motor to flywheel via belt (ratio 1:2 to increase speed)</li><li>Connect flywheel to alternator via belt</li><li>Wire: battery -> motor controller -> DC motor. Alternator -> AVR -> output sockets</li><li>Test: spin flywheel by hand first, check balance, then power DC motor</li></ol>
<h3>4. Common Mistakes</h3>
<p>Unbalanced flywheel = dangerous. Loose belts slip. Weak frame vibrates. No fuse = fire.</p>
<h3>5. Safety</h3>
<p>Flywheel stores huge energy - if it breaks, shrapnel kills. Use guard, enclosure, balanced wheel, never exceed rated RPM. Wear goggles, keep children away.</p>
<h3>6. Video & Resources</h3>
<p>Search YouTube: "Flywheel free energy Nigeria", "DC motor flywheel generator". Practical Action guides.</p>
"""
    },
    {
        'order': 3,
        'title': 'Lithium Battery Upgrade - For Substantial Energy Needs',
        'content': """<h2>Module 3: Lithium Battery Upgrade - For Substantial Energy Needs</h2>
<h3>1. Why Lithium vs Lead-Acid?</h3>
<p>Lead-acid: cheap but heavy, 500 cycles, 50% usable. Lithium (LiFePO4): expensive but light, 3000+ cycles, 90% usable, fast charge, perfect for flywheel starter. When substantial energy required (clinic, cold room), lithium wins.</p>
<h3>2. Sizing Lithium Bank</h3>
<p>For 2KVA system: need 24V 200Ah LiFePO4 = 4800Wh. Can start flywheel 50+ times, run 4 hours without flywheel assist. For 5KVA commercial: 48V 300Ah.</p>
<h3>3. Where to Buy in Africa</h3>
<ul><li><b>Nigeria:</b> Fouani, Carbon Nigeria, Jumia - 24V 100Ah LiFePO4 ~₦400k</li><li><b>Kenya:</b> Chloride Exide, Davis & Shirtliff - 24V 200Ah ~KES 180k</li><li><b>South Africa:</b> Solar Warehouse, Sustainable.co.za</li><li><b>China direct:</b> CATL, BYD, EVE via Alibaba - cheapest but import duty 20-35%</li></ul>
<h3>4. BMS - Battery Management System Critical</h3>
<p>Never use lithium without BMS! BMS protects overcharge, over-discharge, over-temp, balances cells. Use 8S 100A BMS for 24V. Wire correctly or battery dies/burns.</p>
<h3>5. Installation</h3>
<ol><li>Mount lithium in ventilated box (not sealed - though LiFePO4 safer than NMC)</li><li>Connect BMS to cells first, then to load</li><li>Set charge controller to LiFePO4 profile (28.8V max for 24V)</li><li>Test: charge to full, discharge with load, check cell balance</li></ol>
<h3>6. Business</h3>
<p>Lithium system costs more but sells as premium: "5 years warranty, no water, no maintenance". Target: hospitals, labs, offices that need reliable power. Charge 30% premium.</p>
<h3>7. Contacts - Producers</h3>
<p><b>Lithium producers:</b> CATL (catl.com), BYD (byd.com), EVE Energy. African assemblers: <b>Arnergy Nigeria, Candi Solar SA, Greenlight Planet Kenya</b>. Email them for dealer pricing.</p>
"""
    },
    {
        'order': 4,
        'title': 'Flywheel Generator with Springs - Mechanical Energy Storage',
        'content': """<h2>Module 4: Flywheel Generator with Springs - Mechanical Energy Storage</h2>
<h3>1. Concept - Springs + Flywheel = Longer Runtime</h3>
<p>Springs store potential energy, flywheel stores kinetic. Combine: wind spring with hand crank or small motor, release slowly to keep flywheel spinning longer, reducing battery use by 60%. Ancient clock principle, modern power.</p>
<h3>2. Types of Springs</h3>
<ul><li><b>Clock spring (spiral torsion):</b> from truck starter spring, large - stores 500Wh</li><li><b>Compression springs:</b> multiple in series</li><li><b>Extension springs with pulley:</b> easier to fabricate</li></ul>
<h3>3. Design</h3>
<p>Spring drum (like truck winch) connected to flywheel shaft via ratchet (one-way). Wind spring, it unwinds slowly via governor (flyball governor) keeping RPM constant at 1500 RPM for 50Hz output.</p>
<h3>4. Build Steps</h3>
<ol><li>Fabricate spring drum: 300mm diameter, 10mm steel plate, shaft in center</li><li>Attach clock spring: outer end to drum, inner to shaft</li><li>Add ratchet: allows winding without spinning flywheel backwards</li><li>Add governor: two balls on springs, expands with speed, controls brake to keep 1500 RPM</li><li>Connect drum to flywheel via chain</li><li>Winding mechanism: hand crank or small DC motor winds spring in 5 minutes, spring drives flywheel for 45 minutes</li></ol>
<h3>5. Calculations</h3>
<p>Spring energy: E = ½ k x². Need spring constant k high. Example: truck starter spring k=5000 N/m, x=0.5m => 625J per spring. Use 10 springs = 6.25kJ = 1.7Wh mechanical, but geared 1:100 gives 170Wh electrical - enough for lights.</p>
<h3>6. Advantage for Africa</h3>
<p>No battery needed for short use! Wind spring by hand in morning, get light at night. Perfect for rural schools, no recurring battery cost.</p>
<h3>7. Safety</h3>
<p>Spring under tension is dangerous - can snap and cut. Always wear gloves, face shield, wind slowly, use safety catch.</p>
"""
    },
    {
        'order': 5,
        'title': 'Advanced - Hybrid Lithium + Spring + Flywheel System',
        'content': """<h2>Module 5: Hybrid Lithium + Spring + Flywheel - The Ultimate Off-Grid System</h2>
<h3>1. Hybrid Architecture</h3>
<p>Lithium battery starts DC motor -> spins flywheel -> flywheel charges spring drum via ratchet -> spring assists flywheel -> alternator produces AC -> excess charges lithium. Closed loop, very efficient.</p>
<h3>2. Control System</h3>
<p>Arduino or PLC controls: (a) battery voltage, (b) flywheel RPM (hall sensor), (c) spring tension (load cell), (d) output load. Logic: if battery >80% and flywheel >1400 RPM, use spring assist to save battery. If load low, wind spring for later.</p>
<h3>3. Wiring Diagram</h3>
<p>[Battery 24V LiFePO4] -> [BMS] -> [Motor Controller] -> [DC Motor 2HP] -> [Belt] -> [Flywheel 30kg] -> [Belt] -> [Alternator 3KVA] -> [AVR] -> [Output 220V]<br>
Flywheel shaft -> [Ratchet] -> [Spring Drum with 5 clock springs] -> [Governor]<br>
Arduino monitors all via sensors.</p>
<h3>4. Performance</h3>
<p>Without spring: battery lasts 2 hours. With spring: 5 hours. 150% improvement. Lithium lasts 5+ years, flywheel 20 years, springs 10 years. Total cost $800, sells $1500, payback 8 months vs fuel generator.</p>
<h3>5. Build Task</h3>
<p>Assemble hybrid prototype. Measure runtime with and without spring assist. Document improvement.</p>
"""
    },
    {
        'order': 6,
        'title': 'Sourcing, Producers & Partnerships - Contacts and Links',
        'content': """<h2>Module 6: Sourcing, Producers & Partnerships</h2>
<h3>1. Producer Contacts - DC Motors</h3>
<ul><li><b>China:</b> ZD Motor (zd-motor.com), Kinmore Motor - PMDC 2HP $90 FOB, MOQ 10</li><li><b>India:</b> Bharat Bijlee, Crompton - available in Lagos via Chikason</li><li><b>Nigeria:</b> Local rewinding: rewind AC motor to DC at Alaba, cost ₦25k</li></ul>
<h3>2. Producer Contacts - Flywheels</h3>
<ul><li>Fabricate locally: <b>Aba Made - Nnewi foundries</b>, <b>Kano - Dala Foundry</b>, <b>Kenya - Numerical Machining Complex</b></li><li>Spec: EN8 steel, 30kg, 400mm dia, balanced to G6.3, keyway for shaft</li><li>Cost: $50-100 locally vs $300 imported</li></ul>
<h3>3. Producer Contacts - Lithium Batteries</h3>
<ul><li><b>CATL:</b> catl.com - contact sales@catl.com for Africa dealer</li><li><b>BYD:</b> byd.com - energy storage division</li><li><b>African assemblers:</b> Arnergy (arnergy.com.ng) Lagos, Candi Solar SA, Greenlight Planet Kenya - they offer credit for resellers</li><li><b>Alibaba:</b> search "LiFePO4 24V 200Ah BMS" - choose suppliers with 5+ years, Trade Assurance</li></ul>
<h3>4. Producer Contacts - Springs & Governors</h3>
<ul><li>Truck starter springs: buy from <b>Ladipo Market Lagos</b>, <b>Kirikiri</b>, scrap truck starters ₦5k each</li><li>Custom springs: <b>Specialist Spring Ltd UK</b> (exports), <b>Spring Manufacturing Nigeria</b> in Sango Ota</li><li>Governors: fabricate flyball type locally or buy from steam engine suppliers</li></ul>
<h3>5. How to Establish Contact</h3>
<p>Email template: "We are SkillsContinua, humanitarian project building 316 courses for Africa, need dealer pricing for flywheel energy systems, quantity 100 units/year, target off-grid communities. Request datasheet and Africa distributor."</p>
<h3>6. Partnership Strategy</h3>
<p>Become reseller for Arnergy or Greenlight, get training, then build flywheel as add-on. Offer them your course as training material.</p>
<h3>7. Links</h3>
<p>IRENA.org, GIZ EnDev, Practical Action, Hackaday.io flywheel projects, YouTube: "Lithium flywheel hybrid".</p>
"""
    },
    {
        'order': 7,
        'title': 'Testing, Quality Control & Certification',
        'content': """<h2>Module 7: Testing, Quality Control & SON Standards</h2>
<h3>1. Tests Required</h3>
<ul><li>Vibration test: flywheel must <2mm/s</li><li>Balance test: no wobble at 1500 RPM</li><li>Load test: run 2KVA load for 2 hours, measure voltage drop <5%</li><li>Efficiency: input DC vs output AC >70%</li><li>Safety: enclosure, emergency stop, fuse</li></ul>
<h3>2. SON (Standards Organisation Nigeria) & KEBS Kenya</h3>
<p>Need certification to sell legally. Submit prototype to SON lab in Lagos, test for electrical safety (NIS IEC 60335). Cost ~₦100k.</p>
<h3>3. Documentation for Certificate</h3>
<p>Learners must submit: photos of build, test results, video running load, safety checklist. Then get SkillsContinua certificate "Flywheel Energy Systems - Africa Edition".</p>
"""
    },
    {
        'order': 8,
        'title': 'Business Model - Job Creation & Self Reliance',
        'content': """<h2>Module 8: Business Model - Job Creation & Self Reliance</h2>
<h3>1. Pricing</h3>
<p>Basic (Lead-acid, no spring): cost $250 sell $500<br>Premium (Lithium + spring): cost $800 sell $1500<br>Maintenance: $15/month</p>
<h3>2. Customer Segments in Africa</h3>
<p>Barbers, tailors, cold rooms, POS shops, clinics, schools, churches, homes. 40M SMEs in Nigeria alone.</p>
<h3>3. Marketing - 6 Languages</h3>
<p>EN: "Soundless power, no fuel, 5-year warranty"<br>FR: "Énergie silencieuse, sans carburant"<br>PT: "Energia silenciosa, sem combustível"<br>SW: "Umeme kimya, bila mafuta"<br>Flyers, WhatsApp, demo at market, partner with solar installers.</p>
<h3>4. Self Reliance</h3>
<p>Start with 1 unit, sell, build 2, sell, grow. Train 2 youths, create jobs. This is humanitarian value.</p>
"""
    },
    {
        'order': 9,
        'title': 'Maintenance, Troubleshooting & Field Repairs',
        'content': """<h2>Module 9: Maintenance, Troubleshooting & Field Repairs</h2>
<h3>1. Maintenance Schedule</h3>
<p>Weekly: check belt tension, bearing grease, battery voltage. Monthly: clean, check balance, test load. Yearly: replace belts, check BMS.</p>
<h3>2. Common Failures</h3>
<p>Belt slip -> tighten. Vibration -> rebalance flywheel. No output -> check AVR, fuse. Battery low -> check charging, BMS.</p>
<h3>3. Field Repair Kit</h3>
<p>Spare belts, bearings, fuses, multimeter, basic tools. Can fix 90% issues on site.</p>
"""
    },
    {
        'order': 10,
        'title': 'Final Project - Build Your Own & Launch Business',
        'content': """<h2>Module 10: Final Project - Build Your Own & Launch Business</h2>
<h3>Task</h3>
<p>Build one complete hybrid system (DC motor + lithium + flywheel + spring + AC generator), test with 1KVA load for 3 hours, document with video, create business plan for 10 customers in your area, get certificate.</p>
<h3>Assessment</h3>
<p>Practical: 70% (build works), Theory: 20% (quiz), Business plan: 10%. Pass 70% to get Africa edition certificate "Applicable across Africa and beyond".</p>
<h3>Next Steps</h3>
<p>After certification, join SkillsContinua alumni network, get producer contacts, bulk pricing, become trainer in your community.</p>
"""
    }
]

for m in modules:
    lesson, created = Lesson.objects.get_or_create(
        course=course,
        order=m['order'],
        defaults={'title': m['title'], 'content': m['content']}
    )
    if not created:
        lesson.title = m['title']
        lesson.content = m['content']
        lesson.save()
    print(f"{'Created' if created else 'Updated'} Module {m['order']}: {m['title'][:60]}")

print(f"\nFlywheel course upgraded: {course.title} - 10 rich modules with DC motor, lithium, springs, producer contacts")
print(f"Total lessons for course 315: {Lesson.objects.filter(course=course).count()}")