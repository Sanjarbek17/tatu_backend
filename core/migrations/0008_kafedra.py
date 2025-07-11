# Generated by Django 5.2 on 2025-04-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_ilmiymaqola_grantloyiha_dissertatsiya_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('amaliy_mashgulotlar_metodik_qollanmalar', models.ManyToManyField(related_name='kafedras', to='core.amaliymashgulotlarmetodikqollanma')),
                ('dissertatsiyalar', models.ManyToManyField(related_name='kafedras', to='core.dissertatsiya')),
                ('grant_loyihalar', models.ManyToManyField(related_name='kafedras', to='core.grantloyiha')),
                ('ilmiy_maqolalar', models.ManyToManyField(related_name='kafedras', to='core.ilmiymaqola')),
                ('ilmiy_tarjimalar', models.ManyToManyField(related_name='kafedras', to='core.ilmiytarjima')),
                ('konferensiya_materiallari', models.ManyToManyField(related_name='kafedras', to='core.konferensiyamateriali')),
                ('monografiyalar', models.ManyToManyField(related_name='kafedras', to='core.monografiya')),
                ('nazariy_tadqiqotlar', models.ManyToManyField(related_name='kafedras', to='core.nazariytadqiqot')),
                ('oquv_qollanmalar', models.ManyToManyField(related_name='kafedras', to='core.oquvqollanma')),
                ('oquv_uslubiy_qollanmalar', models.ManyToManyField(related_name='kafedras', to='core.oquvuslubiyqollanma')),
                ('patentlar_va_ixtirolar', models.ManyToManyField(related_name='kafedras', to='core.patentixtiro')),
                ('professors', models.ManyToManyField(related_name='kafedras', to='core.professorprofile')),
                ('texnik_hisobotlar', models.ManyToManyField(related_name='kafedras', to='core.texnikhisobot')),
            ],
        ),
    ]
