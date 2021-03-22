# Generated by Django 3.0.8 on 2021-03-21 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0002_auto_20210321_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpVoteDownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(1, 'Upvote'), (0, 'Neutralvote'), (-1, 'Downvote')])),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotedownvotes', to='qa.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotedownvotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]