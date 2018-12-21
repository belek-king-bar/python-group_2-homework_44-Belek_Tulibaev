# Generated by Django 2.1 on 2018-12-20 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderFoods',
            new_name='OrderFood',
        ),
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='delivered', to=settings.AUTH_USER_MODEL, verbose_name='Курьер'),
        ),
        migrations.AddField(
            model_name='order',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Оператор'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('preparing', 'Готовится'), ('on way', 'В пути'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], default='new', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
    ]
