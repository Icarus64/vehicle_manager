# Generated by Django 4.2.4 on 2023-08-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20, unique=True)),
                ('vehicle_type', models.CharField(choices=[('Two', 'Two Wheeler'), ('Three', 'Three Wheeler'), ('Four', 'Four Wheeler')], max_length=10)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_description', models.TextField()),
            ],
            options={
                'permissions': [('read_vehicle', 'Can view vehicle'), ('create_vehicle', 'Can create new vehicle'), ('update_vehicle', 'Can update existing vehicle'), ('del_vehicle', 'Can delete existing vehicle')],
            },
        ),
    ]
