# Generated by Django 3.2.7 on 2021-10-24 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Createportfolio',
            fields=[
                ('template_url', models.SlugField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('prof', models.CharField(max_length=100)),
                ('about_info', models.CharField(max_length=1000)),
                ('p1_title', models.CharField(max_length=50)),
                ('p1_content', models.CharField(max_length=500)),
                ('p1_url', models.URLField()),
                ('p2_title', models.CharField(max_length=50)),
                ('p2_content', models.CharField(max_length=500)),
                ('p2_url', models.URLField()),
                ('p3_title', models.CharField(max_length=50)),
                ('p3_content', models.CharField(max_length=500)),
                ('p3_url', models.URLField()),
                ('instagram', models.URLField(blank=True)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('gmail', models.URLField()),
                ('templates', models.CharField(choices=[('Template-1', 'Template-1.html'), ('Template-2', 'Template-2.html'), ('Template-3', 'Template-3.html')], default=1, max_length=122)),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
