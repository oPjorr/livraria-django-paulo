# Generated by Django 4.1.2 on 2022-10-11 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="media.image",
            ),
        ),
    ]
