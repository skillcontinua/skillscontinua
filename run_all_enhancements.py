import os
import sys
import subprocess

print("🚀 Running all enhancement scripts...")
print("="*60)

scripts = [
    'add_video_content.py',
    'add_quizzes_to_courses.py',
    'add_practical_exercises.py',
]

for script in scripts:
    script_path = os.path.join('scripts', script)
    print(f"\n📝 Running: {script}")
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False,
        text=True
    )
    print(f"✅ Completed: {script}")

print("\n" + "="*60)
print("🎉 All enhancements complete!")