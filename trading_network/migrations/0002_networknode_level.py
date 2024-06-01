# Generated by Django 5.0.4 on 2024-06-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='networknode',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Уровень'),
        ),
    ]
