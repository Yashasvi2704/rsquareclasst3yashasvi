# Generated by Django 3.0.2 on 2020-01-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_coursetaken_extrafee_studentcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='student',
        ),
        migrations.CreateModel(
            name='GuardianGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Guardian')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.StudentProfile')),
            ],
        ),
    ]
