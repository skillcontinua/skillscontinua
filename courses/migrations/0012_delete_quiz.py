# C:\skillscontinua\courses\migrations\0012_delete_quiz.py
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_category_name_alter_category_pillar_and_more'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql="DROP TABLE IF EXISTS courses_quiz;",
                    reverse_sql=migrations.RunSQL.noop,
                ),
            ],
            state_operations=[
                migrations.DeleteModel(
                    name='Quiz',
                ),
            ],
        ),
    ]