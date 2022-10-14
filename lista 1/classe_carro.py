class carro:
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = None
    estado = None

# metodo ligar, que muda o estado para ligado e exibe essa informação na tela
    def ligar(self):
        self.estado = 'ligado'
        print(f'{self.nome} {self.estado}')

# metodo parar, que muda a veloc p/ 0 e imprime que o carro está parado
    def parar(self):
        self.veloc_atual = 0
        print(f'{self.nome} parado')

# metodo desligar, que muda o estado para desligado e exibe essa informação na tela
    def desligar(self):
        self.estado = 'desligado'
        print(f'{self.nome} {self.estado} / ', end = '')
        self.parar()

# metodo acelerar, que muda a veloc de acordo com estado do carro
    def acelerar(self, valor):
        if self.estado == 'ligado': # se tiver ligado a veloc muda pro valor passado
            self.veloc_atual = valor
            if self.veloc_atual > self.veloc_max: # se esse valor for maior que a veloc maxima, ele n deixa passar
                self.veloc_atual = self.veloc_max
                print(f'{self.nome} atingiu sua velocidade máxima')
            else:
                print(f'{self.nome} acelerou para {self.veloc_atual}')
        else:
            print(f'{self.nome} está desligado, não pode acelerar')
            
fusc = carro() # objeto fusc, que recebe os atributos da classe carro
fusc.nome = 'Fusca'
fusc.ano = 1965
fusc.cor = 'Preto'
fusc.veloc_max = 80
fusc.veloc_atual = 20
fusc.estado = 'ligado'
