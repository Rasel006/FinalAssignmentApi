# Generated by Django 4.2.7 on 2024-04-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_pdf', models.FileField(upload_to='Skills/resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_skill', models.ImageField(upload_to='Skills/media/images')),
                ('description', models.TextField(blank=True, null=True)),
                ('project_link', models.CharField(blank=True, max_length=150, null=True)),
                ('Prficiency_levels', models.CharField(choices=[('★', 1), ('★★', 2), ('★★★', 3), ('★★★★', 4), ('★★★★★', 5), ('★★★★★★', 6), ('★★★★★★★', 7)], max_length=50)),
            ],
        ),
    ]
