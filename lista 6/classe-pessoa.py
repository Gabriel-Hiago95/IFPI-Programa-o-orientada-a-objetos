class pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado = 'vivo(a)', estado_civil = 'solteiro(a)', conjuje = None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuje = conjuje
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def sexo(self):
        return self.__sexo
        
    @property
    def idade(self):
        return self.__idade
        
    @property
    def peso(self):
        return self.__peso
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def estado_civil(self):
        return self.__estado_civil
    
    @property
    def conjuje(self):
        return self.__conjuje
    
    @idade.setter
    def idade(self, idade):
        print('Sem permissão')
        
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
        
    @conjuje.setter
    def conjuje(self, conjuje):
        self.__conjuje = conjuje

    def divorciar(self):
        pass
    
    def mostrar_idade(self):
        if self.__estado == 'vivo(a)':
            print(f'{self.__nome} tem atualmente {self.__idade} anos')
        else:
            print(f'{self.__nome} está morto(a)')
    
    def envelhecer(self):
        if self.__estado.lower() == 'vivo(a)':
            self.__idade += 1
            if self.__idade < 21:
                self.__altura += 5
                print(f'{self.__nome} está com {self.__idade} anos e {self.__altura}cm de altura')
            print(f'{self.__nome} envelheceu mais 1 ano, sua idade agora é {self.__idade} anos')
        else:
            print(f'Operação não realizada. {self.__nome} está morto(a)')
    
    def engordar(self, valor):
        if self.__estado.lower() == 'vivo(a)':
            self.__peso += valor
            print(f'{self.__nome} engordou mais {valor}Kg, seu peso agora é {self.__peso}Kg')
        else:
            print(f'Operação não realizada. {self.__nome} está morto(a)')
    
    def emagrecer(self, valor):
        if self.__estado.lower() == 'vivo(a)':
            self.__peso -= valor
            print(f'{self.__nome} emagreceu {valor}Kg, seu peso agora é {self.__peso}Kg')
        else:
            print(f'Operação não realizada. {self.__nome} está morto(a)')
        
    def crescer(self, valor):
        if self.__idade <= 21:
            self.__altura += valor
            if self.__altura > 200:
                self.__altura = 200
                print(f'{self.__nome} cresceu ao máximo, agora ele tem {self.__altura}cm')
            print(f'{self.__nome} cresceu mais {valor} cm, agora ele tem {self.__altura}cm')
        elif self.__estado.lower() == 'morto(a)':
            print(f'Operação não realizada. {self.__nome} está morto(a)')
        else:
            print(f'{self.__nome} não pode mais crescer pois está com 21 anos ou mais')
    
    def casar(self, obj_pessoa):
        if type(obj_pessoa) == pessoa:
            if self.__estado == 'morto(a)':
                print(f'operação não permitida. {self.__nome} está morto(a).')
            elif obj_pessoa.__estado == 'morto(a)':
                print(f'operação não permitida. {obj_pessoa.__nome} está morto(a).')
            elif self.__estado_civil.lower() == 'casado(a)':
                print(f'casamento não realizado, {self.__nome} é casado(a).')
            elif obj_pessoa.__estado_civil.lower() == 'casado(a)':
                print(f'casamento não realizado, {obj_pessoa.__nome} é casado(a).')
            elif self.__idade < 18:
                print(f'casamento não permitido. {self.__nome} é de menor.')
            elif obj_pessoa.__idade < 18:
                print(f'casamento não permitido. {obj_pessoa.__nome} é de menor.')
            else:
                self.__conjuje = obj_pessoa
                self.__estado_civil = 'casado(a)'
                obj_pessoa.__estado_civil = 'casado(a)'
                print(f'{self.__nome} está casado(a) com {obj_pessoa.__nome}')
        else:
            print('Operação não realizada!')
    
    def conjuje(self):
        return self.__conjuje
    
    def morrer(self):
        self.__estado = 'morto(a)'
        if self.__estado_civil == 'casado(a)':
            conjuje = self.__conjuje
            if conjuje.__estado == 'vivo(a)':
                conjuje.__estado_civil = 'viúvo(a)'
        print(f'{self.__nome} morreu')

def main():
    maria = pessoa('Maria', 5, 20, 100, 'F')
    joao = pessoa('João', 12, 40, 140, 'M')
    pedro = pessoa('Pedro', 22, 65, 170, 'M')
    bia = pessoa('Bia', 18, 55, 160, 'F')
    julia = pessoa('Julia', 30, 65, 170, 'F')
    carlos = pessoa('Carlos', 2, 11, 80, 'M')
    jonas = pessoa('Jonas', 34, 70, 180, 'M')
    
    print('caso a =====> ', end = '')
    maria.idade = 10
    
    print('caso b =====> ', end = '')
    maria.envelhecer()
    
    print('caso c =====> ', end = '')
    pedro.crescer(2)
    
    print('caso d =====> ', end = '')
    bia.casar(carlos)
    
    print('caso e =====> ', end = '')
    pedro.casar(maria)
    
    print('caso f =====> ', end = '')
    pedro.casar(julia)
    
    print('caso g =====> ', end = '')
    pedro.casar(bia)
    
    print('caso h =====> ', end = '')
    maria.morrer()
    
    print('caso i =====> ', end = '')
    maria.engordar(3)
    
    print('caso j =====> ', end = '')
    bia.casar(jonas)
    
    print('caso k =====> ', end = '')
    bia.morrer()
    
    print('caso l =====> ', end = '')
    pedro.morrer()
    
    print('caso m =====> ', end = '')
    jonas.casar(julia)
    
    print('caso n =====> ', end = '')
    pedro.casar(bia)
    
    print('caso o =====> ', end = '')
    pedro.mostrar_idade()
    
    print('caso p =====> ', end = '')
    joao.idade = 50

if __name__ == '__main__':
    main()
