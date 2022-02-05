# Generated by Django 4.0.2 on 2022-02-05 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalorieCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(help_text='Enter age.')),
                ('weight', models.IntegerField(help_text='Enter weight.')),
                ('height', models.IntegerField(help_text='Enter height.')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', help_text='Enter gender.', max_length=1)),
                ('activity', models.CharField(blank=True, choices=[('s', 'sedentary'), ('l', 'light'), ('m', 'moderate'), ('v', 'very'), ('e', 'extremely')], default='s', help_text='Select your level of daily activity.', max_length=1)),
            ],
            options={
                'ordering': ['-age'],
            },
        ),
        migrations.CreateModel(
            name='FitnessPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1, help_text='Choose how many days you will work out in a week.')),
            ],
            options={
                'ordering': ['-days'],
            },
        ),
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Enter field documentation', max_length=20)),
            ],
            options={
                'ordering': ['-my_field_name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name.', max_length=20)),
                ('last_name', models.CharField(help_text='Enter last name.', max_length=20)),
                ('email', models.CharField(help_text='Enter email.', max_length=40)),
                ('calorie_count', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='healthhacks.caloriecalc')),
                ('fitness_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='healthhacks.fitnessplan')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
