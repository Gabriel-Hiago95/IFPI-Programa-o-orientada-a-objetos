class gato:
  raça = None
  nome = None
  peso = None
  idade = None
  sexo = None
  fertil = None
  cio = None
  prenhe = None
  puerperio = None

  def mudar_nome(self, nome):
    self.nome = nome
    print(f'Nome do gato mudado para {self.nome}')

  def engordar(self, peso):
    self.peso += peso
    print(f'{self.nome} engordou {peso}kg, seu peso agora é de {self.peso}kg')
  
  def envelhecer(self):
    self.idade += 1
    print(f'{self.nome} envelheceu mais 1 ano, sua idade agora é de {self.idade} anos')
  
  def entrar_no_cio(self):
    if self.sexo == 'F' and self.idade >= 1:
      self.cio = True
    print(f'{self.nome} entrou no cio')
  
  def parir(self):
    if self.sexo == 'F' and self.prenhe == True:
      self.puerperio = True
      gato()
    print(f'{self.nome} pariu seus filhotes e não pode cruzar por enquanto...')
  
  def cruzar(self, gato_m):
    if self.puerperio == True:
      print('Femea em puerperio não pode cruzar')
    elif self.sexo == 'F' and gato_m.sexo == 'M' and self.cio == True:
      self.prenhe = True
      print(f'{self.nome} e {gato_m.nome} cruzaram e fizeram filhotinhos...')
    else:
      print('Dois gatos do mesmo sexo não podem cruzar')

gato_macho = gato()
gato_macho.nome = 'Tom'
gato_macho.raça = 'vira lata'
gato_macho.peso = 10
gato_macho.idade = 1
gato_macho.sexo = 'M'
gato_femea = gato()
gato_femea.nome = 'Mimi'
gato_femea.raça = 'vira lata'
gato_femea.peso = 10
gato_femea.idade = 1
gato_femea.sexo = 'F'
gato_femea.fertil = True
gato_femea.cio = False
gato_femea.prenhe = False
gato_femea.puerperio = False

print(f'caso 1: ==== ',end = '')
gato_femea.entrar_no_cio()

print(f'caso 2: ==== ',end = '')
gato_femea.cruzar(gato_macho)

print(f'caso 3: ==== ',end = '')
gato_femea.parir()

print(f'caso 4: ==== ',end = '')
gato_femea.cruzar(gato_macho)

print(f'caso 5: ==== ',end = '')
gato_femea.envelhecer()

print(f'caso 6: ==== ',end = '')
gato_macho.envelhecer()

print(f'caso 7: ==== ',end = '')
gato_femea.mudar_nome('Lolita')

print(f'caso 7: ==== ',end = '')
gato_femea.puerperio = False
gato_femea.entrar_no_cio()

print(f'caso 8: ==== ',end = '')
gato_femea.cruzar(gato_macho)
