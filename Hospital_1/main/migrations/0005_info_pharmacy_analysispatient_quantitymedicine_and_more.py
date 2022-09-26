# Generated by Django 4.1 on 2022-09-25 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_analysispatient_is_injury_user_types_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(max_length=255)),
                ('workinghour', models.IntegerField()),
                ('dayoff', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='analysispatient',
            name='quantitymedicine',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='types',
            field=models.IntegerField(choices=[(1, 'doctor'), (2, 'reception'), (3, 'patient')], default=1),
        ),
        migrations.AddField(
            model_name='analysispatient',
            name='pharmacy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dorixona', to='main.pharmacy'),
            preserve_default=False,
        ),
    ]
