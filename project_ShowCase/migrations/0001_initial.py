# Generated by Django 4.2.7 on 2024-04-30 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Title', models.CharField(max_length=50)),
                ('Despcription', models.TextField()),
                ('Project_Url', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_ShowCase.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.CharField(choices=[('★', 1), ('★★', 2), ('★★★', 3), ('★★★★', 4), ('★★★★★', 5), ('★★★★★★', 6), ('★★★★★★★', 7)], max_length=50)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_ShowCase.projectdetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project_ShowCase.projectdetailsmodel')),
            ],
        ),
        migrations.AddField(
            model_name='projectdetailsmodel',
            name='tech_stack',
            field=models.ManyToManyField(related_name='projects', to='project_ShowCase.techstack'),
        ),
    ]