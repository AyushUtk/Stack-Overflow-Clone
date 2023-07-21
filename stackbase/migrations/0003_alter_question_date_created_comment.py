# Generated by Django 4.2.3 on 2023-07-20 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stackbase", "0002_question_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=1000)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
