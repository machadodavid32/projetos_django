from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)  # Quantidade max de caracteres que este nome vai suportar
    preco = models.DecimalField('preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self): # Esta função que criamos vai dar nome ao objetivo produto que criamos no site
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


# Após a criação de um model, sempre executar o comando no terminal: python manage.py makemigrations

# Após executar python manage.py makemigrations, execute python manage.py migrate

