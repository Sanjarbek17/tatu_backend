# Generated by Django 5.2 on 2025-04-22 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IlmiyMaqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='articles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professorprofile')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.schoolyear')),
            ],
        ),
        migrations.CreateModel(
            name='GrantLoyiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant_name', models.CharField(max_length=255)),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='Dissertatsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_type', models.CharField(choices=[('PhD', 'PhD'), ('DSc', 'DSc')], max_length=50)),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='AmaliyMashgulotlarMetodikQollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='IlmiyTarjima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_language', models.CharField(max_length=50)),
                ('translated_language', models.CharField(max_length=50)),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='KonferensiyaMateriali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_full_text', models.BooleanField(default=False)),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='Monografiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='NazariyTadqiqot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='OquvQollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='OquvUslubiyQollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='PatentIxtiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_number', models.CharField(max_length=100)),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
        migrations.CreateModel(
            name='TexnikHisobot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilmiy_maqola', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ilmiymaqola')),
            ],
        ),
    ]
