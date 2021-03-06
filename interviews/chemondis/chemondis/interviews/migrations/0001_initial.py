# Generated by Django 2.0.7 on 2018-08-02 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilitySlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('role', models.CharField(choices=[('interviewer', 'Interviewer'), ('candidate', 'Candidate')], max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='persons',
            field=models.ManyToManyField(to='interviews.Person'),
        ),
        migrations.AddField(
            model_name='availabilityslot',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviews.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='availabilityslot',
            unique_together={('person', 'time')},
        ),
    ]
