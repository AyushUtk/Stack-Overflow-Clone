# Generated by Django 4.2.3 on 2023-07-21 18:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stackbase", "0005_question_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
