# Generated by Django 5.1.1 on 2024-10-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0009_employeesprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeesprofile",
            name="employeeID",
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
