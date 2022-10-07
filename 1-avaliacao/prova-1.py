'''INSTITUTO FEDERAL DO PIAUÍ
DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETOS
PROFESSOR: ROGÉRIO BATISTA
ALUNOS: GABRIEL HIAGO MACIEL DE OLIVEIRA e ÁLVARO JOSÉ PASSOS DE FREITAS NETO'''

class cartao_de_credito:
    def __init__(self, numero, titular, validade, codigo, limite = 100):
        self.__numero = numero
        self.__titular = titular
        self.__validade = float(validade)
        self.__limite_de_compra = limite
        self.__cod_seguranca = codigo
        self.__senha = None
        self.__fatura_a_pagar = 0
        self.__status = 'bloqueado'
        self.__valor_min_a_pagar = 0

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def validade(self):
        return self.__validade

    @property
    def limite_de_compra(self):
        return self.__limite_de_compra

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def senha(self):
        return self.__senha

    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar

    @property
    def status(self):
        return self.__status

    @property
    def valor_min_a_pagar(self):
        return self.__valor_min_a_pagar

    def desbloquear(self):
        if self.__status == "liberado":
            print("O cartão ja esta liberado.")
        else:
            if self.__senha == None:
                self.mudar_senha()
                if self.__senha != None:
                    self.__status = "liberado"
                    print("O cartão foi liberado.")
                else:
                    print("OPS ocorreu um erro ao definir a senha.")
            elif self.__senha != None:
                self.__status = "liberado"
                print("O cartão foi liberado.")

    def bloquear(self):
        if self.__status == "bloqueado":
            print("O cartão ja esta bloqueado.")
        else:
            self.__status = "bloqueado"
            print("O cartão foi bloqueado.")

    def mudar_senha(self):
        cod = input("Digite o codigo de segurança do cartão: ")
        if cod == self.__cod_seguranca:
            self.__senha = input("Digite a nova senha: ")
        else:
            print("O codigo do cartão esta incorreto.")

    def comprar(self):
        valor = float(input("Digite o valor da compra: ").strip())
        senha = input("Digite a senha do cartão: ").strip()
        while True:
            try:
                data = float(input("Digite a data (ANO.MES): ").strip())
                break
            except:
                print("Digite a data no formato exigido e use o sistema numerico")
        if valor <= self.__limite_de_compra and self.__status == "liberado" and data <= self.__validade and senha == self.__senha:
            self.__limite_de_compra -= valor
            self.__fatura_a_pagar += valor
            self.__valor_min_a_pagar = 0.3 * self.__fatura_a_pagar
            print('Compra efetuada com sucesso!')
            print(f"Limite atual: {self.__limite_de_compra}")
        else:
            print("Compra não efetuada!")

    def pagar_fatura(self):
        valor = float(input("Digite o valor a ser pago: ").strip())
        if valor >= self.__valor_min_a_pagar and valor <= self.__fatura_a_pagar:
            self.__fatura_a_pagar -= valor
            self.__limite_de_compra += valor
            print(f"Pagamento de fatura efetuado, limite atual: {self.__limite_de_compra}")
        else:
            print('Valor inválido')

    def __str__(self):
        return f'Número do cartão: {self.__numero}\nTitular: {self.__titular}\nValor da Fatura: {self.__fatura_a_pagar}\nValor mínimo a pagar: {self.__valor_min_a_pagar}'

def main():
    print('''INSTITUTO FEDERAL DO PIAUÍ
DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETOS
PROFESSOR: ROGÉRIO BATISTA
ALUNOS: GABRIEL HIAGO MACIEL DE OLIVEIRA e ÁLVARO JOSÉ PASSOS DE FREITAS NETO
=====================================================================================''')
    cartao1 = cartao_de_credito('0258', 'Josias', 2024.03, '2203')
    cartao2 = cartao_de_credito('0568', 'Pedro', 2025.10, '2478', 1000)
    cartao3 = cartao_de_credito('5478', 'Maria', 2030.02, '4578', 2500)
    cartao4 = cartao_de_credito('4587', 'Xeleleu', 2022.11, '1010')

    print('teste 1, cartao 1 ==> ', end = '')
    print(cartao1.__str__())

    print('teste 2, cartao 1 ==> ', end='')
    cartao1.comprar()

    print('teste 3, cartao 1 ==> ', end='')
    cartao1.desbloquear()

    print('teste 4, cartao 1 ==> ', end='')
    cartao1.comprar()

    print('teste 5, cartao 1 ==> ', end='')
    cartao1.pagar_fatura()

    print('teste 6, cartao 1 ==> ', end='')
    print(cartao1.__str__())

    print('teste 7, cartao 1 ==> ', end='')
    cartao1.bloquear()

    print('teste 8, cartao 1 ==> ', end='')
    cartao1.comprar()

    print('teste 1, cartao 2 ==> ', end = '')
    print(cartao2.__str__())

    print('teste 2, cartao 2 ==> ', end='')
    cartao2.pagar_fatura()

    print('teste 3, cartao 2 ==> ', end='')
    cartao2.bloquear()

    print('teste 4, cartao 2 ==> ', end='')
    cartao2.mudar_senha()

    print('teste 5, cartao 2 ==> ', end='')
    cartao2.comprar()

    print('teste 6, cartao 2 ==> ', end='')
    print(cartao2.__str__())

    print('teste 7, cartao 2 ==> ', end='')
    cartao2.desbloquear()

    print('teste 8, cartao 2 ==> ', end='')
    cartao2.comprar()

    print('teste 9, cartao 2 ==> ', end='')
    print(cartao2.__str__())

    print('teste 1, cartao 3 ==> ', end='')
    print(cartao3.__str__())

    print('teste 2, cartao 3 ==> ', end='')
    cartao3.mudar_senha()

    print('teste 3, cartao 3 ==> ', end='')
    cartao3.desbloquear()

    print('teste 4, cartao 3 ==> ', end='')
    cartao3.comprar()

    print('teste 5, cartao 3 ==> ', end='')
    cartao3.pagar_fatura()

    print('teste 6, cartao 3 ==> ', end='')
    print(cartao3.__str__())

    print('teste 7, cartao 3 ==> ', end='')
    cartao3.desbloquear()

    print('teste 1, cartao 4 ==> ', end='')
    cartao4.desbloquear()

    print('teste 2, cartao 4 ==> ', end='')
    cartao4.comprar()

    print('teste 3, cartao 4 ==> ', end='')
    cartao4.pagar_fatura()

    print('teste 4, cartao 4 ==> ', end='')
    print(cartao4.__str__())

if __name__ == '__main__':
    main()
