# Generated by Django 4.0.1 on 2022-02-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PROSSED', 'process'), ('SHIPING', 'shiping'), ('ONTHEWAY', 'ontheway'), ('RECIVED', 'receved')], default='PROSSED', max_length=9),
        ),
    ]
