# Generated by Django 4.2 on 2023-04-08 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vouchers', '0002_category_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vouchers.voucher')),
            ],
        ),
    ]
