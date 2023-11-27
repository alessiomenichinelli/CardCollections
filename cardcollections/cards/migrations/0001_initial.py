# Generated by Django 4.2.1 on 2023-11-16 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codice', models.CharField(max_length=255)),
                ('relase_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.company')),
                ('league', models.ManyToManyField(to='cards.league')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.nation')),
            ],
        ),
        migrations.CreateModel(
            name='Subset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.set')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.player')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.set')),
                ('subset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.subset')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.team')),
            ],
        ),
    ]
