# Generated by Django 2.1.7 on 2019-04-29 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_name_hindi', models.CharField(default='', max_length=50)),
                ('subject_image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
                ('topic_name_hindi', models.CharField(default='', max_length=50)),
                ('topic_image', models.ImageField(default='default.jpg', upload_to='')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('video_title', models.CharField(default='', max_length=100)),
                ('video_title_hindi', models.CharField(default='', max_length=100)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Topic')),
            ],
        ),
    ]