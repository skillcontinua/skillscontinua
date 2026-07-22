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
print("📚 ADDING LESSONS TO NEW COURSES")
print("="*70)

# Lesson content for new courses
lesson_data = {
    # === MARINE COURSES ===
    'Marine Engine Systems - Complete Guide': [
        {'title': 'Introduction to Marine Engines', 'content': 'Overview of marine engine systems - inboard, outboard, and stern drive engines. Understanding the basic components and their functions.', 'order': 1, 'duration': 30},
        {'title': 'Engine Types and Configurations', 'content': 'Different marine engine types - 2-stroke, 4-stroke, diesel, and gasoline. Configurations and applications for different vessels.', 'order': 2, 'duration': 35},
        {'title': 'Engine Cooling Systems', 'content': 'Marine engine cooling - raw water cooling, closed cooling systems, heat exchangers, and troubleshooting cooling issues.', 'order': 3, 'duration': 30},
        {'title': 'Fuel Systems and Carburetion', 'content': 'Marine fuel systems - carburetors, fuel injection, fuel pumps, filters, and troubleshooting fuel issues.', 'order': 4, 'duration': 35},
        {'title': 'Ignition and Electrical Systems', 'content': 'Marine ignition systems - spark plugs, coils, distributors, and electrical system troubleshooting.', 'order': 5, 'duration': 30},
        {'title': 'Lubrication and Oil Systems', 'content': 'Marine lubrication systems - oil pumps, filters, oil types, and proper lubrication practices.', 'order': 6, 'duration': 25},
        {'title': 'Exhaust Systems', 'content': 'Marine exhaust systems - manifolds, risers, mufflers, and troubleshooting exhaust issues.', 'order': 7, 'duration': 25},
        {'title': 'Engine Diagnostics and Troubleshooting', 'content': 'Systematic marine engine diagnostics - identifying problems, using diagnostic tools, and effective troubleshooting.', 'order': 8, 'duration': 35},
        {'title': 'Regular Maintenance and Service', 'content': 'Marine engine maintenance schedules - daily, weekly, monthly, and yearly maintenance tasks.', 'order': 9, 'duration': 25},
        {'title': 'Winterization and Storage', 'content': 'Proper winterization and storage procedures for marine engines to ensure longevity and reliability.', 'order': 10, 'duration': 30},
    ],
    'Outboard Motor Repair - Advanced': [
        {'title': 'Advanced Outboard Engine Theory', 'content': 'Advanced concepts in outboard engine operation - 2-stroke vs 4-stroke, powerhead, and lower unit.', 'order': 1, 'duration': 30},
        {'title': 'Fuel System Diagnostics', 'content': 'Advanced fuel system diagnostics - carburetor rebuild, fuel injection troubleshooting, and fuel pump repair.', 'order': 2, 'duration': 35},
        {'title': 'Ignition System Repair', 'content': 'Advanced ignition system repair - CDI, stator, trigger, and spark plug troubleshooting.', 'order': 3, 'duration': 30},
        {'title': 'Lower Unit and Gearcase Service', 'content': 'Lower unit service - gearcase disassembly, bearing replacement, seal installation, and drive shaft repair.', 'order': 4, 'duration': 35},
        {'title': 'Powerhead Rebuild', 'content': 'Complete powerhead rebuild - cylinder, piston, ring replacement, and engine reassembly.', 'order': 5, 'duration': 40},
        {'title': 'Electrical System Diagnostics', 'content': 'Advanced electrical diagnostics - charging system, starter system, and wiring troubleshooting.', 'order': 6, 'duration': 30},
        {'title': 'Computer Diagnostics', 'content': 'Using diagnostic computers for outboard engines - error codes, sensor testing, and system analysis.', 'order': 7, 'duration': 30},
        {'title': 'Performance Optimization', 'content': 'Optimizing outboard engine performance - prop selection, carburetor tuning, and timing adjustment.', 'order': 8, 'duration': 25},
        {'title': 'Routine Maintenance', 'content': 'Comprehensive maintenance schedules - impeller replacement, oil changes, and filter replacements.', 'order': 9, 'duration': 25},
        {'title': 'Professional Business Practices', 'content': 'Building a professional outboard repair business - pricing, customer service, and shop management.', 'order': 10, 'duration': 30},
    ],
    # === AGRICULTURE COURSES ===
    'Hydroponics - Modern Growing Systems': [
        {'title': 'Introduction to Hydroponics', 'content': 'What is hydroponics? History, benefits, and the science behind soilless growing.', 'order': 1, 'duration': 30},
        {'title': 'Hydroponic System Types', 'content': 'NFT, DWC, Aeroponics, Drip Systems, Ebb & Flow - comparing and selecting the right system.', 'order': 2, 'duration': 35},
        {'title': 'Nutrient Solutions', 'content': 'Understanding nutrient solutions - essential elements, mixing, pH management, and EC monitoring.', 'order': 3, 'duration': 30},
        {'title': 'Growing Mediums', 'content': 'Growing mediums - rockwool, coco coir, perlite, vermiculite, and clay pebbles.', 'order': 4, 'duration': 25},
        {'title': 'Water Quality Management', 'content': 'Water quality - pH, EC, temperature, oxygen levels, and water treatment for hydroponics.', 'order': 5, 'duration': 30},
        {'title': 'Crop Selection and Planning', 'content': 'Choosing crops for hydroponics - leafy greens, herbs, tomatoes, and commercial crop planning.', 'order': 6, 'duration': 25},
        {'title': 'Lighting Systems', 'content': 'Lighting for hydroponics - natural light, LED, HPS, fluorescent, and light management.', 'order': 7, 'duration': 25},
        {'title': 'Pest and Disease Management', 'content': 'Managing pests and diseases in hydroponic systems - prevention, organic solutions, and treatment.', 'order': 8, 'duration': 30},
        {'title': 'System Maintenance and Troubleshooting', 'content': 'Maintaining hydroponic systems - cleaning, equipment maintenance, and troubleshooting problems.', 'order': 9, 'duration': 25},
        {'title': 'Commercial Hydroponic Business', 'content': 'Starting a commercial hydroponic business - planning, costs, marketing, and profitability.', 'order': 10, 'duration': 30},
    ],
    'Vertical Farming Technology': [
        {'title': 'Introduction to Vertical Farming', 'content': 'Vertical farming - history, concept, benefits, and the future of urban agriculture.', 'order': 1, 'duration': 30},
        {'title': 'Vertical Farming Systems', 'content': 'Different vertical farming systems - vertical towers, tiered shelves, and rotating systems.', 'order': 2, 'duration': 35},
        {'title': 'LED Lighting Technology', 'content': 'LED lighting for vertical farms - spectrum, intensity, energy efficiency, and light management.', 'order': 3, 'duration': 30},
        {'title': 'Climate Control Systems', 'content': 'Climate control - temperature, humidity, CO2, and environmental management in vertical farms.', 'order': 4, 'duration': 30},
        {'title': 'Automated Irrigation and Nutrient Delivery', 'content': 'Automated systems - drip irrigation, ebb and flow, nutrient dosing, and automation technology.', 'order': 5, 'duration': 30},
        {'title': 'Crop Selection for Vertical Farming', 'content': 'Selecting crops for vertical farming - leafy greens, herbs, microgreens, and commercial crop planning.', 'order': 6, 'duration': 25},
        {'title': 'Smart Sensors and IoT', 'content': 'IoT in vertical farming - sensors, monitoring, data analytics, and smart farming technologies.', 'order': 7, 'duration': 30},
        {'title': 'Vertical Farming Economics', 'content': 'Economics of vertical farming - startup costs, operational costs, ROI, and profitability analysis.', 'order': 8, 'duration': 25},
        {'title': 'Sustainability and Environmental Impact', 'content': 'Environmental impact - water conservation, energy use, carbon footprint, and sustainable practices.', 'order': 9, 'duration': 25},
        {'title': 'Building a Vertical Farm Business', 'content': 'Starting a vertical farm - business planning, location, funding, and scaling.', 'order': 10, 'duration': 30},
    ],
    # === HEALTH COURSES ===
    'Nutrition and Healthy Living': [
        {'title': 'Introduction to Nutrition', 'content': 'Understanding nutrition - macronutrients, micronutrients, and the role of food in health.', 'order': 1, 'duration': 30},
        {'title': 'Macronutrients - Carbohydrates', 'content': 'Carbohydrates - types, functions, sources, and the role of carbs in a healthy diet.', 'order': 2, 'duration': 25},
        {'title': 'Macronutrients - Proteins', 'content': 'Proteins - functions, sources, amino acids, and protein requirements for health.', 'order': 3, 'duration': 25},
        {'title': 'Macronutrients - Fats', 'content': 'Fats - types, functions, sources, and the importance of healthy fats in the diet.', 'order': 4, 'duration': 25},
        {'title': 'Micronutrients - Vitamins', 'content': 'Vitamins - types, functions, sources, and understanding vitamin deficiencies.', 'order': 5, 'duration': 30},
        {'title': 'Micronutrients - Minerals', 'content': 'Minerals - types, functions, sources, and the importance of mineral balance.', 'order': 6, 'duration': 25},
        {'title': 'Meal Planning and Balanced Diet', 'content': 'Creating balanced meals - food groups, portion control, and meal planning for health.', 'order': 7, 'duration': 30},
        {'title': 'Food Safety and Hygiene', 'content': 'Food safety - handling, storage, preparation, and preventing foodborne illness.', 'order': 8, 'duration': 25},
        {'title': 'Diet and Disease Prevention', 'content': 'The role of nutrition in disease prevention - heart disease, diabetes, obesity, and cancer prevention.', 'order': 9, 'duration': 30},
        {'title': 'Sustainable and Healthy Eating', 'content': 'Sustainable eating - plant-based diets, local food, reducing food waste, and healthy eating habits.', 'order': 10, 'duration': 25},
    ],
    'Community Health and Hygiene': [
        {'title': 'Introduction to Community Health', 'content': 'Community health - concepts, importance, and the role of communities in health promotion.', 'order': 1, 'duration': 30},
        {'title': 'Water and Sanitation', 'content': 'Water and sanitation - safe water sources, sanitation facilities, and hygiene practices.', 'order': 2, 'duration': 30},
        {'title': 'Disease Prevention and Control', 'content': 'Preventing and controlling diseases - vaccination, screening, and public health measures.', 'order': 3, 'duration': 30},
        {'title': 'Environmental Health', 'content': 'Environmental health - air quality, waste management, and the impact of environment on health.', 'order': 4, 'duration': 25},
        {'title': 'Health Education and Awareness', 'content': 'Health education - strategies, community engagement, and promoting health awareness.', 'order': 5, 'duration': 25},
        {'title': 'Maternal and Child Health', 'content': 'Maternal and child health - prenatal care, child development, and community support.', 'order': 6, 'duration': 30},
        {'title': 'Community Health Workers', 'content': 'The role of community health workers - training, responsibilities, and impact.', 'order': 7, 'duration': 25},
        {'title': 'Emergency Preparedness', 'content': 'Emergency preparedness - natural disasters, outbreaks, and community response.', 'order': 8, 'duration': 25},
        {'title': 'Monitoring and Evaluation', 'content': 'Monitoring community health programs - indicators, data collection, and evaluation.', 'order': 9, 'duration': 30},
        {'title': 'Building Healthy Communities', 'content': 'Strategies for building healthy communities - partnerships, advocacy, and sustainable programs.', 'order': 10, 'duration': 30},
    ],
}

# Add lessons
total_added = 0
total_courses = 0

for course_title, lessons in lesson_data.items():
    try:
        course = Course.objects.get(title=course_title)
        print(f"\n📖 Adding lessons to: {course_title}")
        course_count = 0
        
        for lesson_info in lessons:
            # Check if lesson already exists
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