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
print("📚 ADDING LESSONS TO ANIMAL HUSBANDRY COURSES")
print("="*70)

# Lesson content for Animal Husbandry courses
animal_lessons = {
    # === FISHERY ===
    'Fish Farming - Complete Guide': [
        {'title': 'Introduction to Fish Farming', 'content': 'What is fish farming? History, importance, and the potential of aquaculture for food security and income generation.', 'order': 1, 'duration': 30},
        {'title': 'Fish Species and Selection', 'content': 'Common fish species for farming - tilapia, catfish, and others. Selecting the right species for your environment and market.', 'order': 2, 'duration': 30},
        {'title': 'Pond Construction and Preparation', 'content': 'Building and preparing fish ponds - site selection, pond design, lining, filling, and preparation for stocking.', 'order': 3, 'duration': 35},
        {'title': 'Fingerling Production', 'content': 'Producing fish fingerlings - broodstock management, breeding techniques, hatchery operations, and fingerling care.', 'order': 4, 'duration': 35},
        {'title': 'Feeding and Nutrition', 'content': 'Fish feeding and nutrition - feed types, feeding schedules, and nutritional requirements for different fish species.', 'order': 5, 'duration': 30},
        {'title': 'Water Quality Management', 'content': 'Managing water quality - oxygen levels, pH, temperature, waste management, and water exchange techniques.', 'order': 6, 'duration': 30},
        {'title': 'Disease Management', 'content': 'Fish diseases - identification, prevention, and treatment of common fish diseases in aquaculture.', 'order': 7, 'duration': 25},
        {'title': 'Harvesting and Processing', 'content': 'Harvesting fish - techniques, handling, processing, and preparation for market.', 'order': 8, 'duration': 25},
        {'title': 'Fish Farming Economics', 'content': 'Fish farming business - costs, returns, profitability, and marketing strategies for fish products.', 'order': 9, 'duration': 30},
        {'title': 'Sustainable Fish Farming', 'content': 'Sustainable aquaculture - environmental impact, best practices, and sustainable fish farming techniques.', 'order': 10, 'duration': 25},
    ],
    'Catfish Farming - Production and Marketing': [
        {'title': 'Introduction to Catfish Farming', 'content': 'Catfish farming - importance, potential, and the catfish value chain from production to market.', 'order': 1, 'duration': 30},
        {'title': 'Catfish Hatchery Management', 'content': 'Catfish hatchery - broodstock selection, breeding, egg incubation, and fingerling production.', 'order': 2, 'duration': 35},
        {'title': 'Catfish Grow-out Systems', 'content': 'Catfish grow-out - pond systems, cage systems, and intensive production techniques.', 'order': 3, 'duration': 30},
        {'title': 'Catfish Nutrition and Feeding', 'content': 'Catfish nutrition - feed types, feeding practices, and nutritional requirements for catfish.', 'order': 4, 'duration': 25},
        {'title': 'Catfish Health Management', 'content': 'Catfish health - disease identification, prevention, and treatment strategies.', 'order': 5, 'duration': 25},
        {'title': 'Harvesting Catfish', 'content': 'Harvesting techniques - partial harvesting, total harvesting, and post-harvest handling.', 'order': 6, 'duration': 25},
        {'title': 'Catfish Processing', 'content': 'Processing catfish - dressing, filleting, smoking, and value-added products.', 'order': 7, 'duration': 30},
        {'title': 'Catfish Marketing', 'content': 'Marketing catfish - market channels, pricing, packaging, and branding catfish products.', 'order': 8, 'duration': 25},
        {'title': 'Catfish Farming Economics', 'content': 'Catfish business - financial planning, cost analysis, profitability, and investment strategies.', 'order': 9, 'duration': 30},
        {'title': 'Scaling Up Catfish Production', 'content': 'Expanding catfish operations - diversification, value addition, and building a sustainable catfish business.', 'order': 10, 'duration': 30},
    ],
    
    # === POULTRY ===
    'Poultry Farming - Complete Guide': [
        {'title': 'Introduction to Poultry Farming', 'content': 'Poultry farming - importance, types of poultry, and the poultry value chain.', 'order': 1, 'duration': 30},
        {'title': 'Poultry Breeds and Selection', 'content': 'Poultry breeds - layers, broilers, and dual-purpose breeds. Selecting the right breed for your goals.', 'order': 2, 'duration': 30},
        {'title': 'Poultry Housing and Equipment', 'content': 'Poultry housing - types, design, construction, and essential equipment for poultry farming.', 'order': 3, 'duration': 35},
        {'title': 'Brooding and Rearing', 'content': 'Brooding and rearing - chick management, temperature control, vaccination, and feeding programs.', 'order': 4, 'duration': 35},
        {'title': 'Nutrition and Feeding', 'content': 'Poultry nutrition - feed types, formulation, and feeding management for different growth stages.', 'order': 5, 'duration': 30},
        {'title': 'Health Management', 'content': 'Poultry health - disease prevention, vaccination, and treatment strategies.', 'order': 6, 'duration': 30},
        {'title': 'Egg Production', 'content': 'Egg production - layer management, egg collection, grading, and quality control.', 'order': 7, 'duration': 25},
        {'title': 'Broiler Production', 'content': 'Broiler production - rearing meat birds, growth management, and processing.', 'order': 8, 'duration': 25},
        {'title': 'Poultry Processing and Marketing', 'content': 'Processing and marketing poultry products - slaughtering, processing, and selling poultry products.', 'order': 9, 'duration': 30},
        {'title': 'Poultry Business Management', 'content': 'Poultry business - financial planning, record keeping, and building a successful poultry enterprise.', 'order': 10, 'duration': 30},
    ],
    
    # === PIGGERY ===
    'Piggery Farming - Complete Guide': [
        {'title': 'Introduction to Pig Farming', 'content': 'Pig farming - importance, breeds, and the pork value chain.', 'order': 1, 'duration': 30},
        {'title': 'Pig Breeds and Selection', 'content': 'Pig breeds - selection for meat production, breeding purposes, and specific environments.', 'order': 2, 'duration': 30},
        {'title': 'Pig Housing and Environment', 'content': 'Pig housing - design, construction, and management of pig shelters and facilities.', 'order': 3, 'duration': 35},
        {'title': 'Pig Nutrition and Feeding', 'content': 'Pig nutrition - feed types, formulation, and feeding management for sows, growers, and finishers.', 'order': 4, 'duration': 30},
        {'title': 'Breeding and Reproduction', 'content': 'Pig breeding - breeding systems, mating, pregnancy diagnosis, and farrowing management.', 'order': 5, 'duration': 35},
        {'title': 'Piglet Care', 'content': 'Piglet care - management, colostrum, creep feeding, and weaning.', 'order': 6, 'duration': 25},
        {'title': 'Health Management', 'content': 'Pig health - disease prevention, vaccination, and biosecurity for pig farms.', 'order': 7, 'duration': 30},
        {'title': 'Pork Processing', 'content': 'Pork processing - slaughtering, butchering, and value-added pork products.', 'order': 8, 'duration': 25},
        {'title': 'Pig Farming Economics', 'content': 'Pig business - cost analysis, profitability, and marketing pigs and pork products.', 'order': 9, 'duration': 30},
        {'title': 'Sustainable Pig Farming', 'content': 'Sustainable pig farming - waste management, environmental impact, and sustainable practices.', 'order': 10, 'duration': 25},
    ],
    
    # === BEEKEEPING ===
    'Beekeeping and Honey Production': [
        {'title': 'Introduction to Beekeeping', 'content': 'Beekeeping - history, importance, and the honey value chain.', 'order': 1, 'duration': 30},
        {'title': 'Bee Biology and Behavior', 'content': 'Bee biology - honeybee species, colony structure, and bee behavior.', 'order': 2, 'duration': 35},
        {'title': 'Hive Construction and Types', 'content': 'Hive types - traditional, modern, and advanced bee hives. Construction and preparation.', 'order': 3, 'duration': 35},
        {'title': 'Bee Colony Management', 'content': 'Colony management - inspection, feeding, swarm control, and seasonal management.', 'order': 4, 'duration': 30},
        {'title': 'Honey Production', 'content': 'Honey production - harvesting, extraction, filtration, and quality control.', 'order': 5, 'duration': 30},
        {'title': 'Queen Rearing', 'content': 'Queen rearing - selecting, raising, and introducing queens to colonies.', 'order': 6, 'duration': 25},
        {'title': 'Bee Health Management', 'content': 'Bee health - pests, diseases, and prevention strategies for healthy colonies.', 'order': 7, 'duration': 25},
        {'title': 'Value-Added Bee Products', 'content': 'Bee products - propolis, royal jelly, beeswax, and pollen. Processing and marketing.', 'order': 8, 'duration': 30},
        {'title': 'Pollination Services', 'content': 'Pollination services - using bees for crop pollination and building a pollination business.', 'order': 9, 'duration': 25},
        {'title': 'Beekeeping Business', 'content': 'Beekeeping business - planning, costs, marketing, and building a successful apiary enterprise.', 'order': 10, 'duration': 30},
    ],
    
    # === CATTLE & DAIRY ===
    'Cattle Rearing and Herd Management': [
        {'title': 'Introduction to Cattle Rearing', 'content': 'Cattle rearing - importance, breeds, and the cattle value chain.', 'order': 1, 'duration': 30},
        {'title': 'Cattle Breeds and Selection', 'content': 'Cattle breeds - beef breeds, dairy breeds, and dual-purpose breeds. Selection for specific purposes.', 'order': 2, 'duration': 30},
        {'title': 'Cattle Housing and Handling', 'content': 'Cattle housing - designs, construction, and handling facilities for cattle management.', 'order': 3, 'duration': 35},
        {'title': 'Cattle Nutrition and Feeding', 'content': 'Cattle nutrition - pasture management, feed types, and nutritional requirements.', 'order': 4, 'duration': 30},
        {'title': 'Herd Health Management', 'content': 'Cattle health - disease prevention, vaccination, and parasite control for cattle herds.', 'order': 5, 'duration': 30},
        {'title': 'Breeding and Reproduction', 'content': 'Cattle breeding - natural breeding, artificial insemination, and pregnancy management.', 'order': 6, 'duration': 35},
        {'title': 'Calf Management', 'content': 'Calf management - birth to weaning, colostrum, feeding, and health management.', 'order': 7, 'duration': 25},
        {'title': 'Record Keeping and Herd Improvement', 'content': 'Record keeping - herd recording, performance tracking, and genetic improvement.', 'order': 8, 'duration': 25},
        {'title': 'Cattle Marketing', 'content': 'Cattle marketing - market channels, pricing, and selling cattle for breeding or meat.', 'order': 9, 'duration': 25},
        {'title': 'Sustainable Cattle Farming', 'content': 'Sustainable cattle farming - environmental management, waste management, and sustainable practices.', 'order': 10, 'duration': 30},
    ],
}

# Add lessons
total_added = 0
total_courses = 0

for course_title, lessons in animal_lessons.items():
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