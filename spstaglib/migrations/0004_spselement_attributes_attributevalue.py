# Generated by Django 4.1.7 on 2023-04-06 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("spstaglib", "0003_spsattribute"),
    ]

    operations = [
        migrations.AddField(
            model_name="spselement",
            name="attributes",
            field=models.ManyToManyField(to="spstaglib.spsattribute"),
        ),
        migrations.CreateModel(
            name="AttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("value", models.CharField(max_length=256, verbose_name="Valor")),
                (
                    "description",
                    wagtail.fields.RichTextField(
                        blank=True, null=True, verbose_name="Description"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "parent",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attribute_value",
                        to="spstaglib.spsattribute",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "verbose_name": "Attribute value",
                "verbose_name_plural": "Attribute values",
            },
        ),
    ]
