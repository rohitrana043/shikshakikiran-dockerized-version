# Generated by Django 2.1.7 on 2019-03-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=100)),
                ('card_content', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='card_pics')),
            ],
        ),
    ]
