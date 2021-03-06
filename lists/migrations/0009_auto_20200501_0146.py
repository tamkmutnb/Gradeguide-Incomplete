# Generated by Django 3.0 on 2020-04-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20200324_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('Grade', models.CharField(max_length=255)),
                ('GPA', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term1',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term2',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term3',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term4',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term5',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term6',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term7',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='term8',
        ),
        migrations.DeleteModel(
            name='Term1',
        ),
        migrations.DeleteModel(
            name='Term2',
        ),
        migrations.DeleteModel(
            name='Term3',
        ),
        migrations.DeleteModel(
            name='Term4',
        ),
        migrations.DeleteModel(
            name='Term5',
        ),
        migrations.DeleteModel(
            name='Term6',
        ),
        migrations.DeleteModel(
            name='Term7',
        ),
        migrations.DeleteModel(
            name='Term8',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term_all',
            field=models.ManyToManyField(to='lists.Term'),
        ),
    ]
