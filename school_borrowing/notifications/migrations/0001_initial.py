# Generated by Django 5.1.4 on 2024-12-31 05:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifikasi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pesan', models.TextField()),
                ('tanggal_waktu', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('terkirim', 'Terkirim'), ('dibaca', 'Dibaca')], default='terkirim', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]