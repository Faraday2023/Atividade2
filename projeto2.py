# Segundo Programa em Python

class Pessoa:
    def __init__(self, nome, idade, altura, peso):

      self.nome = nome
      self.idade = idade
      self.altura = altura
      self.peso = peso

    def eh_maior(self):
       if self.idade >= 18:
          print('{}'.format(True))
    
       else:
          print('{}'.format(False))
    
    def imc(self):
       
       self.imc = self.peso/(self.altura*self.altura)
       print(self.imc)
    
    def imc_longo(self):
       if self.imc < 17:
          print('Muito Abaixo do peso')
       elif self.imc >=17 and self.imc <=18.49:
          print('Abaixo do Peso')

       elif self.imc >=18.5 and self.imc <=24.99:
          print('Peso Normal')

       elif self.imc >=25 and self.imc <=29.99:
          print('Acima do Peso')

    def apresentar(self):
       
       print('Eu sou {} e tenho {} anos'.format(self.nome,self.idade))

    def compara (self):
       
       self.id = 20

       if self.idade >= self.id:
          print('A pessoa é mais mais velha do que a idade estabelecida')

       else:
          print('A pessoa não é mais mais velha do que a idade estabelecida')
        
pessoa1 = Pessoa("Zezinho", 15, 1.53, 68.2)
pessoa1.eh_maior()
pessoa1.imc()
pessoa1.imc_longo()
pessoa1.apresentar()
pessoa1.compara()