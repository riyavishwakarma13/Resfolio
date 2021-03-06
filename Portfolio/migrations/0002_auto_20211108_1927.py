# Generated by Django 3.2.7 on 2021-11-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('Password', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='createportfolio',
            name='templates',
            field=models.CharField(choices=[('Template-1', 'pt-1.html'), ('Template-2', 'pt-2.html'), ('Template-3', 'pt-3.html')], default=1, max_length=122),
        ),
    ]
