from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [('courses', '0008_lesson_audio_file_lesson_content_type_and_more')]
    operations = [
        migrations.RunSQL(sql="DROP TABLE IF EXISTS courses_quiz;", reverse_sql=migrations.RunSQL.noop),
    ]