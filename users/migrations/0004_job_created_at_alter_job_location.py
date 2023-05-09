# Generated by Django 4.2.1 on 2023-05-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_jobapplication_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(choices=[('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Hyderabad', 'Hyderabad'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata')], max_length=50),
        ),
    ]
