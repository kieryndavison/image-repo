# Generated by Django 3.2 on 2021-04-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='offer',
        ),
        migrations.AddField(
            model_name='image',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
