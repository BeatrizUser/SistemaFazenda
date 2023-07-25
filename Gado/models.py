from django.db import models

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=4, choices=[('CPF', 'Pessoa Física'), ('CNPJ', 'Pessoa Jurídica')])
    documento = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Clientes'

class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=4, choices=[('CPF', 'Pessoa Física'), ('CNPJ', 'Pessoa Jurídica')])
    documento = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"

class Animal(models.Model):
    brinco = models.CharField(max_length=20, primary_key=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('F', 'Fêmea')])
    origem = models.ForeignKey('Origem', on_delete=models.SET_NULL, null=True, blank=True)
    data_compra = models.DateField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    raca = models.ForeignKey('Raca', on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey('StatusAnimal', on_delete=models.SET_NULL, null=True, blank=True)
    pasto = models.ForeignKey('Pasto', on_delete=models.SET_NULL, null=True, blank=True)
    caracteristica = models.ForeignKey('Caracteristica', on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    nome_pai = models.CharField(max_length=100, null=True, blank=True)
    nome_mae = models.CharField(max_length=100, null=True, blank=True)
    data_entrada = models.DateField(null=True, blank=True)
    data_desmama = models.DateField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    campo = models.ForeignKey('Fornecedor', on_delete=models.SET_NULL, null=True, blank=True)
    data_morte = models.DateField(null=True, blank=True)
    motivo_morte = models.ForeignKey('CausaMorte', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.brinco

    class Meta:
        verbose_name_plural = 'Animais'

class Medicamento(models.Model):
    brinco = models.ForeignKey('Animal', on_delete=models.CASCADE)
    data = models.DateField()
    medicamento = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    unidade = models.CharField(max_length=10)
    obs = models.TextField()
    classificacao = models.ForeignKey('ClassificacaoSanidade', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[('ATIVO', 'Ativo'), ('MORTO', 'Morto')])

    def __str__(self):
        return f"{self.medicamento} - {self.quantidade} {self.unidade}"

class Origem(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Origens'

class Raca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Raças'

class StatusAnimal(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class CausaMorte(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Pasto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class ClassificacaoSanidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Lote(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Despesa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Caracteristica(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome
