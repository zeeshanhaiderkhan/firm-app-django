# Generated by Django 3.0.3 on 2020-07-02 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveIntegerField()),
                ('cnic', models.TextField(max_length=13)),
                ('phone', models.TextField(max_length=11)),
                ('address', models.TextField(max_length=150)),
                ('city', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]