import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("="*70)
print("📚 ADDING LESSONS TO WIND ENERGY & PRINTING TECHNOLOGY COURSES")
print("="*70)

# Lesson content for Wind Energy courses
wind_lessons = {
    'Wind Energy Technology - Complete Guide': [
        {'title': 'Introduction to Wind Energy', 'content': 'What is wind energy? History, evolution from ancient windmills to modern turbines, and the importance of wind as a renewable energy source.', 'order': 1, 'duration': 30},
        {'title': 'Wind Energy Fundamentals', 'content': 'Wind energy principles - how wind is generated, wind patterns, and the science behind converting wind to electricity.', 'order': 2, 'duration': 35},
        {'title': 'Wind Turbine Components', 'content': 'Complete breakdown of wind turbine components - blades, rotor, nacelle, gearbox, generator, tower, and foundation.', 'order': 3, 'duration': 35},
        {'title': 'Wind Turbine Types and Configurations', 'content': 'Horizontal axis vs vertical axis turbines. Onshore vs offshore installations. Advantages and disadvantages of each type.', 'order': 4, 'duration': 30},
        {'title': 'Wind Resource Assessment', 'content': 'Assessing wind resources - wind speed measurement, site selection, and wind mapping for optimal turbine placement.', 'order': 5, 'duration': 25},
        {'title': 'Wind Turbine Installation', 'content': 'Step-by-step wind turbine installation - site preparation, foundation construction, tower erection, and turbine assembly.', 'order': 6, 'duration': 35},
        {'title': 'Wind Turbine Maintenance', 'content': 'Regular maintenance - lubrication, bolt torque, blade inspection, gearbox maintenance, and troubleshooting common issues.', 'order': 7, 'duration': 30},
        {'title': 'Wind Energy Economics', 'content': 'Wind energy economics - cost analysis, ROI, financing, government incentives, and wind farm profitability.', 'order': 8, 'duration': 25},
        {'title': 'Wind-Solar Hybrid Systems', 'content': 'Integrating wind and solar for reliable power - system design, complementary generation, and hybrid system management.', 'order': 9, 'duration': 30},
        {'title': 'Future of Wind Energy', 'content': 'Emerging technologies - floating turbines, smart wind farms, energy storage integration, and the future of wind energy.', 'order': 10, 'duration': 25},
    ],
    'Wind Turbine Types and Selection': [
        {'title': 'Horizontal Axis Wind Turbines (HAWT)', 'content': 'Complete guide to HAWT - design, operation, advantages, disadvantages, and applications.', 'order': 1, 'duration': 30},
        {'title': 'Vertical Axis Wind Turbines (VAWT)', 'content': 'Complete guide to VAWT - Darrieus, Savonius, and other designs. Advantages, disadvantages, and applications.', 'order': 2, 'duration': 30},
        {'title': 'Onshore vs Offshore Wind Turbines', 'content': 'Comparing onshore and offshore installations - site selection, cost, maintenance, and performance differences.', 'order': 3, 'duration': 25},
        {'title': 'Small-Scale Wind Turbines', 'content': 'Small wind turbines for residential, farm, and community use. Sizing, installation, and grid connection.', 'order': 4, 'duration': 25},
        {'title': 'Utility-Scale Wind Turbines', 'content': 'Large-scale wind turbines for commercial wind farms. Design, capacity, and operational considerations.', 'order': 5, 'duration': 30},
        {'title': 'Wind Turbine Selection Criteria', 'content': 'How to select the right wind turbine - capacity, wind speed, site conditions, budget, and application requirements.', 'order': 6, 'duration': 25},
        {'title': 'Wind Turbine Performance Metrics', 'content': 'Understanding performance metrics - capacity factor, availability, efficiency, and power curve analysis.', 'order': 7, 'duration': 25},
        {'title': 'Wind Turbine Safety', 'content': 'Safety protocols - during installation, operation, and maintenance. Electrical safety, working at heights, and emergency procedures.', 'order': 8, 'duration': 30},
        {'title': 'Wind Turbine Environmental Impact', 'content': 'Environmental considerations - bird and bat protection, noise, visual impact, and sustainable decommissioning.', 'order': 9, 'duration': 25},
        {'title': 'Case Studies - Wind Turbine Projects', 'content': 'Real-world case studies - successful wind turbine projects around the world. Lessons learned and best practices.', 'order': 10, 'duration': 30},
    ],
    'Wind Turbine Installation and Maintenance': [
        {'title': 'Wind Turbine Installation Planning', 'content': 'Planning wind turbine installation - site assessment, logistics, permitting, and project management.', 'order': 1, 'duration': 30},
        {'title': 'Foundation Construction', 'content': 'Wind turbine foundation types - gravity, pile, and floating. Construction methods and quality control.', 'order': 2, 'duration': 35},
        {'title': 'Tower Erection', 'content': 'Erecting wind turbine towers - crane selection, tower sections, bolting, and safety during erection.', 'order': 3, 'duration': 30},
        {'title': 'Turbine Assembly', 'content': 'Assembling wind turbine components - rotor, nacelle, generator, and complete system integration.', 'order': 4, 'duration': 35},
        {'title': 'Electrical Connection', 'content': 'Wind turbine electrical connections - generator wiring, transformer, grid connection, and protection systems.', 'order': 5, 'duration': 30},
        {'title': 'Commissioning and Testing', 'content': 'Testing wind turbines after installation - functional tests, performance tests, and safety checks.', 'order': 6, 'duration': 25},
        {'title': 'Maintenance Planning', 'content': 'Developing maintenance plans - regular inspections, lubrications, and replacement schedules.', 'order': 7, 'duration': 25},
        {'title': 'Preventive Maintenance', 'content': 'Preventive maintenance tasks - bolt torque, oil analysis, bearing inspection, and system diagnostics.', 'order': 8, 'duration': 30},
        {'title': 'Troubleshooting and Repairs', 'content': 'Troubleshooting common wind turbine problems - electrical, mechanical, and control system issues.', 'order': 9, 'duration': 30},
        {'title': 'Maintenance Safety', 'content': 'Safety during maintenance - confined spaces, working at heights, lockout/tagout, and rescue procedures.', 'order': 10, 'duration': 25},
    ],
}

# Lesson content for Printing Technology courses
printing_lessons = {
    'Printing Technology - Complete Guide': [
        {'title': 'Introduction to Printing Technology', 'content': 'What is printing? History of printing - from ancient woodblock to modern digital printing. Evolution of the printing industry.', 'order': 1, 'duration': 30},
        {'title': 'Types of Printing Processes', 'content': 'Overview of printing processes - offset, digital, screen, flexography, gravure, and 3D printing.', 'order': 2, 'duration': 35},
        {'title': 'Printing Materials and Substrates', 'content': 'Printing materials - papers, boards, plastics, fabrics, and special substrates for different printing methods.', 'order': 3, 'duration': 30},
        {'title': 'Inks and Toners', 'content': 'Printing inks and toners - types, composition, properties, and selection for different printing processes.', 'order': 4, 'duration': 30},
        {'title': 'Color Theory and Management', 'content': 'Color theory for printing - RGB vs CMYK, color matching, calibration, and achieving accurate color reproduction.', 'order': 5, 'duration': 35},
        {'title': 'Prepress Operations', 'content': 'Prepress - file preparation, proofing, plate making, and quality control before printing.', 'order': 6, 'duration': 30},
        {'title': 'Print Production Workflow', 'content': 'Managing print production - planning, scheduling, quality control, and post-press finishing.', 'order': 7, 'duration': 25},
        {'title': 'Quality Control in Printing', 'content': 'Print quality control - densitometry, color measurement, registration, and print evaluation.', 'order': 8, 'duration': 30},
        {'title': 'Sustainable Printing Practices', 'content': 'Sustainable printing - eco-friendly materials, waste reduction, recycling, and green printing initiatives.', 'order': 9, 'duration': 25},
        {'title': 'Future Trends in Printing', 'content': 'Emerging trends - digital transformation, 3D printing, smart packaging, and the future of the printing industry.', 'order': 10, 'duration': 25},
    ],
    'Offset Printing - Traditional and Modern': [
        {'title': 'Offset Printing Basics', 'content': 'Principles of offset printing - lithography, plate making, and the offset printing process.', 'order': 1, 'duration': 30},
        {'title': 'Offset Printing Press Types', 'content': 'Types of offset presses - sheet-fed, web, and hybrid presses. Advantages and applications.', 'order': 2, 'duration': 30},
        {'title': 'Offset Plates', 'content': 'Offset plate technology - aluminum plates, plate coating, exposure, and processing.', 'order': 3, 'duration': 25},
        {'title': 'Offset Ink and Dampening Systems', 'content': 'Ink and dampening systems - ink rollers, dampening systems, and achieving print quality.', 'order': 4, 'duration': 25},
        {'title': 'Offset Press Setup and Operation', 'content': 'Setting up and operating an offset press - preparation, registration, and running production.', 'order': 5, 'duration': 30},
        {'title': 'Troubleshooting Offset Printing', 'content': 'Troubleshooting offset printing problems - hickies, ghosting, color variations, and registration issues.', 'order': 6, 'duration': 30},
        {'title': 'Digital Offset Technology', 'content': 'Digital offset - computer-to-plate, digital workflow, and modern offset technology.', 'order': 7, 'duration': 25},
        {'title': 'Offset Printing Applications', 'content': 'Offset printing applications - magazines, newspapers, books, packaging, and commercial printing.', 'order': 8, 'duration': 25},
        {'title': 'Maintenance and Care', 'content': 'Offset press maintenance - daily, weekly, and monthly maintenance procedures.', 'order': 9, 'duration': 25},
        {'title': 'Offset Printing Business', 'content': 'Running an offset printing business - pricing, customers, quality, and profitability.', 'order': 10, 'duration': 30},
    ],
    '3D Printing Technology - Complete Guide': [
        {'title': 'Introduction to 3D Printing', 'content': 'What is 3D printing? History, evolution, and the impact of additive manufacturing.', 'order': 1, 'duration': 30},
        {'title': '3D Printing Technologies', 'content': '3D printing technologies - FDM, SLA, SLS, DLP, and emerging methods.', 'order': 2, 'duration': 35},
        {'title': '3D Printer Types and Selection', 'content': 'Types of 3D printers - consumer, prosumer, industrial. Selection criteria for different applications.', 'order': 3, 'duration': 30},
        {'title': 'Materials for 3D Printing', 'content': '3D printing materials - plastics, resins, metals, composites, and emerging materials.', 'order': 4, 'duration': 30},
        {'title': '3D Modeling and Design', 'content': 'Designing for 3D printing - CAD software, file formats, and design guidelines.', 'order': 5, 'duration': 35},
        {'title': '3D Printing Software', 'content': '3D printing software - slicers, printing software, and workflow optimization.', 'order': 6, 'duration': 25},
        {'title': '3D Printer Setup and Calibration', 'content': 'Setting up and calibrating 3D printers - bed leveling, temperature, and print settings.', 'order': 7, 'duration': 30},
        {'title': 'Post-Processing and Finishing', 'content': 'Post-processing 3D prints - support removal, sanding, painting, and surface finishing.', 'order': 8, 'duration': 25},
        {'title': '3D Printing Applications', 'content': '3D printing applications - prototyping, manufacturing, medical, construction, and education.', 'order': 9, 'duration': 30},
        {'title': '3D Printing Business', 'content': 'Starting a 3D printing business - equipment, materials, pricing, customers, and marketing.', 'order': 10, 'duration': 30},
    ],
}

# Combine all lessons
all_lessons = {}
all_lessons.update(wind_lessons)
all_lessons.update(printing_lessons)

# Add lessons
total_added = 0
total_courses = 0

for course_title, lessons in all_lessons.items():
    try:
        course = Course.objects.get(title=course_title)
        print(f"\n📖 Adding lessons to: {course_title}")
        course_count = 0
        
        for lesson_info in lessons:
            exists = Lesson.objects.filter(course=course, title=lesson_info['title']).exists()
            if not exists:
                lesson = Lesson.objects.create(
                    course=course,
                    title=lesson_info['title'],
                    content=lesson_info['content'],
                    order=lesson_info['order'],
                    duration_minutes=lesson_info['duration'],
                    is_free_preview=True if lesson_info['order'] == 1 else False,
                )
                course_count += 1
                total_added += 1
                print(f"  ✅ Added: {lesson.title}")
        
        if course_count > 0:
            total_courses += 1
            print(f"  📊 Added {course_count} lessons to {course_title}")
            
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found - skipping")

print("\n" + "="*70)
print(f"📊 Courses Updated: {total_courses}")
print(f"📚 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Lesson addition complete!")