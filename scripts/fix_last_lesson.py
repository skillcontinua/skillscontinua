import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Lesson

print("="*70)
print("📚 FIXING THE LAST LESSON")
print("="*70)

# Find the lesson
try:
    lesson = Lesson.objects.get(title="Cattle Housing and Handling")
    print(f"📖 Found lesson: {lesson.title}")
    print(f"   Course: {lesson.course.title}")
    
    # Add real content
    lesson.content = """
## Cattle Housing and Handling

Proper housing and handling of cattle is essential for animal welfare, productivity, and farm efficiency. This lesson covers the key principles and practices for cattle housing and handling.

## Importance of Proper Housing

### Why Housing Matters
- **Animal Welfare:** Comfortable animals are healthier and more productive
- **Disease Prevention:** Good housing reduces disease risk
- **Productivity:** Well-housed cattle produce more milk and meat
- **Worker Safety:** Safe facilities protect workers

## Types of Cattle Housing

### 1. Open-Shed Housing
- Common in tropical climates
- Provides shelter from sun and rain
- Allows natural ventilation
- Cost-effective to construct

### 2. Confinement Housing
- Used in intensive farming
- Complete control of environment
- Higher initial cost
- Better disease control

### 3. Pasture-Based Housing
- Animals raised on pasture
- Natural living conditions
- Lower costs
- Seasonal limitations

## Key Housing Requirements

### Space Requirements
- **Adult Cattle:** 15-20 square meters per animal
- **Young Stock:** 8-10 square meters per animal
- **Calves:** 2-3 square meters per calf
- **Feeding Area:** Adequate space for all animals

### Ventilation
- **Natural Ventilation:** Open sides and roof vents
- **Mechanical Ventilation:** Fans and air circulation
- **Important:** Avoid drafts while ensuring fresh air

### Flooring
- **Concrete Floors:** Durable, easy to clean
- **Rubber Mats:** Provide comfort, reduce injury
- **Deep Litter:** Natural, requires management

### Water and Feed Access
- **Clean Water:** Always available
- **Feed Troughs:** Easy to clean, durable
- **Mineral Blocks:** Provide essential nutrients

## Cattle Handling Principles

### Understanding Cattle Behavior
- **Flight Zone:** Personal space of the animal
- **Point of Balance:** At the shoulder
- **Herding Instinct:** Move as a group
- **Vision:** Wide-angle vision, poor depth perception

### Safe Handling Techniques
1. **Approach Calmly:** Avoid sudden movements
2. **Use the Flight Zone:** Move animals gently
3. **Avoid Stress:** Stress reduces productivity
4. **Use Appropriate Facilities:** Cattle crushes, races

### Facilities for Handling
- **Cattle Race:** Narrow passage for handling
- **Head Gate:** Restrains head for procedures
- **Cattle Crush:** Restrains animal for treatment
- **Loading Ramp:** For transportation

## Health and Safety

### Worker Safety
- Use proper handling techniques
- Wear appropriate safety gear
- Be aware of animal behavior
- Never work alone when possible

### Animal Health
- Regular inspections
- Clean housing regularly
- Provide proper nutrition
- Monitor for signs of illness

## Best Practices

### Housing Management
1. **Clean regularly** - Remove manure and waste
2. **Maintain ventilation** - Check air flow
3. **Repair facilities** - Fix broken equipment
4. **Provide bedding** - Comfortable resting areas

### Handling Practices
1. **Move calmly** - Slow and steady
2. **Use pressure and release** - Respect flight zone
3. **Train animals** - Familiarity with handling
4. **Regular handling** - Reduce stress

## Common Challenges

### Challenge 1: Aggressive Animals
**Solution:** Identify and handle separately, use proper facilities

### Challenge 2: Calf Separation
**Solution:** Gradual weaning, familiar handling

### Challenge 3: Wet Conditions
**Solution:** Good drainage, proper bedding

### Challenge 4: Disease Spread
**Solution:** Quarantine new animals, maintain hygiene

## Summary

Proper housing and handling are fundamental to successful cattle farming. By understanding cattle behavior and providing appropriate facilities, you can ensure animal welfare, increase productivity, and maintain a safe working environment.

## Key Takeaways
- Good housing improves animal welfare and productivity
- Understand cattle behavior for safe handling
- Regular maintenance of facilities
- Monitor animal health regularly

## Next Steps
1. Assess your current housing facilities
2. Identify areas for improvement
3. Develop a handling plan
4. Train staff on proper handling techniques
"""
    lesson.save()
    print("✅ Added real content to: Cattle Housing and Handling")
    
except Lesson.DoesNotExist:
    print("⚠️ Lesson not found - it may have already been fixed!")

print("\n" + "="*70)
print("🎉 All lessons now have real content!")