# Generated by Django 2.0.6 on 2018-06-17 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placar1', models.IntegerField()),
                ('placar2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('pontos', models.IntegerField(default=0)),
                ('usuario', models.CharField(max_length=10)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Selecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('grupo', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='jogo',
            name='time1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='main.Selecao'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='time2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='main.Selecao'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Jogador'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Jogo'),
        ),
    ]
