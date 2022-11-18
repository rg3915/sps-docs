# Generated by Django 3.2.12 on 2022-11-18 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('thematic_areas', '0002_auto_20221016_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericThematicAreaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('is_valid', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is valid?')),
                ('line_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of lines')),
                ('attachment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Attachment')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='genericthematicareafile_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genericthematicareafile_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name_plural': 'Generic Thematic Areas Upload',
            },
        ),
        migrations.CreateModel(
            name='GenericThematicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Thematic Area')),
                ('lang', models.CharField(blank=True, choices=[('', ''), ('UNDEFINED', 'UNDEFINED'), ('de', 'Alemão'), ('ar', 'Árabe'), ('bn', 'Bengali'), ('zh', 'Chinês'), ('ko', 'Coreano'), ('da', 'Dinamarquês'), ('sk', 'Eslovaco'), ('sl', 'Esloveno'), ('es', 'Espanhol'), ('fi', 'Finlandês'), ('fr', 'Francês'), ('el', 'Grego'), ('nl', 'Holandês'), ('hu', 'Húngaro'), ('hi', 'Indiano'), ('id', 'Indonésio'), ('en', 'Inglês'), ('it', 'Italiano'), ('ja', 'Japonês'), ('no', 'Norueguês'), ('pl', 'Polonês'), ('pt', 'Português'), ('ro', 'Romeno'), ('ru', 'Russo'), ('sr', 'Sérvio'), ('sv', 'Sueco'), ('th', 'Tailandês'), ('cs', 'Tcheco'), ('tr', 'Turco')], max_length=10, null=True, verbose_name='Idioma')),
                ('origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Origin Data Base')),
                ('level', models.CharField(blank=True, choices=[('', ''), ('UNDEFINED', 'UNDEFINED'), ('0', 'Level 0'), ('1', 'Level 1'), ('2', 'Level 2'), ('3', 'Level 3')], max_length=20, null=True, verbose_name='Nível')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='genericthematicarea_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('level_up', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Generic_Thematic_Area_Level_Up', to='thematic_areas.genericthematicarea')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genericthematicarea_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Generic Thematic Area',
                'verbose_name_plural': 'Generic Thematic Areas',
            },
        ),
    ]
