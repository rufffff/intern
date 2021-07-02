# Generated by Django 3.2.4 on 2021-06-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0012_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='jobname',
            new_name='skills',
        ),
        migrations.AddField(
            model_name='job',
            name='ask_application_for',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_requirement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='meta_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='section_visibility',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='total_positions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]