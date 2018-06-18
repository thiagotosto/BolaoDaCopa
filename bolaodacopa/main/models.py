from django.db import models
import datetime


class Jogador(models.Model):
    nome = models.CharField(max_length=200)
    pontos = models.IntegerField(default=0)
    usuario = models.CharField(max_length=10)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.nome

class Selecao(models.Model):

    nome = models.CharField(max_length=20)
    grupo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    time1 = models.ForeignKey(Selecao, on_delete=models.CASCADE, related_name='time1')
    placar1 = models.IntegerField(default=0)
    placar2 = models.IntegerField(default=0)
    time2 = models.ForeignKey(Selecao, on_delete=models.CASCADE, related_name='time2')
    data = models.DateField()

    def __str__(self):
        if datetime.date.today() > self.data :
            return "{} {} x {} {}: {}".format(self.time1, self.placar1, self.placar2, self.time2, self.data)
        else:
            return "{} x {}: {}".format(self.time1, self.time2, self.data)

class Aposta(models.Model):
    dono = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    placar1 = models.IntegerField()
    placar2 = models.IntegerField()
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} x {} {}: {}".format(self.jogo.time1, self.placar1, self.placar2, self.jogo.time2, self.jogo.data)
