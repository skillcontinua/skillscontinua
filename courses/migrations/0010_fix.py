from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('courses', '0009_fix_quiz')]
    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_images/'),
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS courses_quiz;",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]