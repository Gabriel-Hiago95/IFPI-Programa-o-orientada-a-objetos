'''Utilizando o processo de abstração, implementar uma classe que represente uma consulta médica.
Execução:
- Criar um menu principal para manipulação das consultas médicas criadas.
opções:
1 - Nova consulta (agendamento)
2- Pagar Consulta
3- Cancelar consulta
4- Agendar retorno
5- Relatório de consultas realizadas no mes por médico
6- Relatório de faturamento da Clinica por mes
OBS:
1- Cada médico recebe R$ 200 por consulta realizada
2- Valor da consulta: R$ 300
3- utilizar todos os recursos vistos até o momento.'''

from datetime import date
from random import sample, uniform, seed
seed()

LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
MEDICOS = {'A':1, 'B': 2, 'C':3}
CONSULTAS = {}
PACIENTE = {}
INFOA = {}
INFOB = {}
INFOC = {}

class consulta_medica:
    global LETRAS, NUMEROS, MEDICOS, CONSULTAS, PACIENTE, INFOA, INFOB, INFOC

    def __init__(self, medico, paciente):
        self.cod_consulta = ''.join(sample(LETRAS, 2) + sample(NUMEROS, 2))
        self.medico = medico
        self.data_atual = date.today().strftime('%d/%m/%Y')
        self.paciente = paciente
        self.valor = float(f'{uniform(1, 1000):.2f}')
        self.pago = False

    def nova_consulta(self, dia, mes, ano):
        data_agendamento = f'{dia}/{mes}/{ano}'
        while True:
            if self.medico not in MEDICOS:
                print('Nome do médico não cadastrado, informe outro nome...')
            else:
                if self.medico == 'A':
                    INFOA[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                elif self.medico == 'B':
                    INFOB[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                elif self.medico == 'C':
                    INFOC[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                else:
                    print('Valores inválidos, digite novamente...')


    def pagar_consulta(self, valor_a_pagar):
        while True:
            if self.cod_consulta not in CONSULTAS:
                print('Consulta não existente no sistema')
            else:
                if valor_a_pagar != self.valor:
                    print('Pague o valor integral para ter direito a consulta')
                else:
                    self.pago = True
                    print('Sua consulta foi paga...')
                    break

    def cancelar_consulta(self, codigo):
        while True:
            if codigo not in CONSULTAS:
                print('Consulta não encontrada, digite outro código...')
            else:
                del CONSULTAS[codigo]
                del PACIENTE[codigo]
                del INFOA[codigo]
                del INFOB[codigo]
                del INFOC[codigo]
                print('Consulta cancelada com sucesso...')
                break

    def agendar_retorno(self, dia, mes, ano):
        data_agendamento = f'{dia}/{mes}/{ano}'
        while True:
            if self.medico not in MEDICOS:
                print('Nome do médico não cadastrado, informe outro nome...')
            else:
                if self.medico == 'A':
                    INFOA[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                elif self.medico == 'B':
                    INFOB[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                elif self.medico == 'C':
                    INFOC[self.cod_consulta] = (self.paciente, self.valor, data_agendamento)
                    PACIENTE[self.cod_consulta] = (self.medico, self.valor)
                    CONSULTAS[self.cod_consulta] = (self.medico, self.valor, data_agendamento)
                    print(f'Consulta marcada com sucesso! seu código é {self.cod_consulta}')
                    print(f'Valor da consulta: {self.valor}')
                    break
                else:
                    print('Valores inválidos, digite novamente...')

    def relatorio_medico(self):
        pass

    def relatorio_faturamento(self):
        pass

consulta = None
def main():
    global LETRAS, NUMEROS, MEDICOS, CONSULTAS, PACIENTE, INFOA, INFOB, INFOC, consulta
    opcao = ''
    while opcao != 'N':
        print('''========== MENU PRINCIPAL ==========
        1 - Nova consulta (agendamento)
        2- Pagar Consulta
        3- Cancelar consulta
        4- Agendar retorno
        5- Relatório de consultas realizadas no mes por médico
        6- Relatório de faturamento da Clinica por mes''')

        opc = int(input('Informe a opção desejada: ').strip())
        if opc == 1:
            med = input('Informe o nome do médico que deseja se consultar: ').strip()
            if med not in MEDICOS:
                print('Nome do médico não existe, digite novamente...')
            else:
                pac = input('Informe seu nome: ').strip()
                dia = int(input('Informe o dia da consulta').strip())
                mes = int(input('Informe o mes da consulta').strip())
                ano = int(input('Informe o ano da consulta').strip())
                consulta = consulta_medica(med, pac)
                consulta.nova_consulta(dia, mes, ano)
        elif opc == 2:
            pass
        opcao = int(input('Deseja realizar mais alguma operação? (S/N): ').strip())

if __name__ == '__main__':
    main()
