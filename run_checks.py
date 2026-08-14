import subprocess
import sys

print("=" * 60)
print("RUNNING CODE CHECKS")
print("=" * 60)

checks = [
    ("flake8 courses/", "Python Style Check"),
    ("black --check courses/", "Python Formatting Check"),
    ("python manage.py check", "Django System Check"),
]

for command, description in checks:
    print(f"\n🔍 {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print(f"✅ {description} passed!")
    else:
        print(f"❌ {description} failed!")

print("\n" + "=" * 60)
print("CHECKS COMPLETE!")
print("=" * 60)