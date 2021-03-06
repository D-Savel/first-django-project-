# Generated by Django 4.0.4 on 2022-05-31 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_alter_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('JavaScript', 'Javascript'), ('C++', 'Cplus'), ('C#', 'Csharp'), ('Python', 'Python'), ('PHP', 'Php'), ('None', 'None')], default='----', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='project',
            field=models.ForeignKey(default='----', null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.project'),
        ),
    ]
