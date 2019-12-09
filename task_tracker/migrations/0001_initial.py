# Generated by Django 3.0 on 2019-12-09 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField()),
                ('status', models.CharField(choices=[('TODO', 'To Do'), ('IP', 'In Progress'), ('DONE', 'Done')], max_length=4)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
