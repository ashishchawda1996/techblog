# Generated by Django 4.2 on 2023-05-24 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_usercontactnumber_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userContact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserContactNumber',
        ),
    ]
