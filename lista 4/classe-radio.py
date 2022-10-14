Estacoes = {89.5:'Cocais', 91.5:'Mix', 94.1:'Boa', 99.1:'Clube'}

class radiofm:
    global Estacoes

    def __init__(self, vol_max, estacoes = Estacoes, freq_atual = 80, est_atual = 'Sem Estação'):
        self.__vol_min = 0
        self.__vol_max = vol_max
        self.__freq_min = 80
        self.__freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = est_atual
        self.frequencia_atual = freq_atual
        self.antena_habilitada = False

    @property
    def vol_min(self):
        return self.__vol_min

    @property
    def vol_max(self):
        return self.__vol_max

    @property
    def freq_min(self):
        return self.__freq_min

    @property
    def freq_max(self):
        return self.__freq_max

    @vol_min.setter
    def vol_min(self, vol_min):
        vm1 = self.__vol_min
        vm2 = vol_min
        if vm1 == vm2:
            self.__vol_min = vol_min
        else:
            print('Volume mínimo não pode ser alterado')

    @vol_max.setter
    def vol_max(self, vol_max):
        vm1 = self.__vol_max
        vm2 = vol_max
        if vm1 == vm2:
            self.__vol_max = vol_max
        else:
            print('Volume máximo não pode ser alterado')

    @freq_min.setter
    def freq_min(self, freq_min):
        fm1 = self.__freq_min
        fm2 = freq_min
        if fm1 == fm2:
            self.__freq_min = freq_min
        else:
            print('Frequência mínima não pode ser alterada')

    @freq_max.setter
    def freq_max(self, freq_max):
        fm1 = self.__freq_max
        fm2 = freq_max
        if fm1 == fm2:
            self.__freq_max = freq_max
        else:
            print('Frequência máxima não pode ser alterada')

    def habilitar_antena(self):
        self.antena_habilitada = True
        print('antena habilitada...')

    def ligar(self):
        est = list(Estacoes.keys())
        self.ligado = True
        self.volume = self.vol_min
        if self.antena_habilitada == True:
            self.frequencia_atual = est[0]
            self.estacao_atual = Estacoes[self.frequencia_atual]
            print(f'Estação Atual: {self.frequencia_atual} -> {Estacoes[self.frequencia_atual]}')
        else:
            print(f'Estação Atual: {self.frequencia_atual} -> {self.estacao_atual}')
            print('antena desabilitada, habilite a antena para sintonizar as estações...')

    def desligar(self, freq_atual = 80, est_atual = 'Sem Estação'):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = freq_atual
        self.estacao_atual = est_atual
        self.antena_habilitada = False
        print('Rádio desligado...')

    def aumentar_volume(self, valor_vol = 1):
        if self.ligado == True:
            if self.volume + valor_vol > self.vol_max:
                self.volume = self.vol_max
                print(f'Volume máximo atingido...\n Volume atual: {self.volume}')
            elif self.volume < 0:
                self.volume = self.vol_min
                print(f'Volume mínimo atingido...\nVolume atual: {self.volume}')
            else:
                self.volume += valor_vol
                print(f'Volume atual do rádio: {self.volume}')
        else:
            print('Ligue o rádio para poder ajustar o volume')

    def diminuir_volume(self, valor_vol = 1):
        if self.ligado == True:
            if valor_vol > self.vol_max:
                self.volume = self.vol_max
                print(f'Volume máximo atingido...\n Volume atual: {self.volume}')
            elif valor_vol < 0:
                self.volume = self.vol_min
                print(f'Volume mínimo atingido...\nVolume atual: {self.volume}')
            else:
                self.volume -= valor_vol
                print(f'Volume atual do rádio: {self.volume}')
        else:
            print('Ligue o rádio para poder ajustar o volume')

    def mudar_frequencia(self, valor_freq = 0):
        if self.antena_habilitada == True:
            self.frequencia_atual = valor_freq
            if self.frequencia_atual in Estacoes.keys():
                self.estacao_atual = Estacoes[self.frequencia_atual]
                print(f'Estação Atual: {self.frequencia_atual} -> {self.estacao_atual}')
            elif valor_freq == 0:
                for chave in list(Estacoes.keys()):
                    if self.frequencia_atual != chave:
                        self.frequencia_atual = chave
                        break
                print(f'Estação Atual: {self.frequencia_atual} -> {Estacoes[self.frequencia_atual]}')
            else:
                print(f'Estação Atual: inexistente')
        else:
            print('antena desabilitada, habilite a antena para sintonizar as estações...')

meu_radio = radiofm(100)

print('caso 1 ===== ', end = '')
meu_radio.ligar()

print('caso 1.1 ===== ', end = '')
meu_radio.habilitar_antena()

print('caso 1.2 ===== ', end = '')
meu_radio.ligar()

print('caso 2 ===== ', end = '')
meu_radio.desligar()

print('caso 3 ===== ', end = '')
meu_radio.aumentar_volume(50)

print('caso 4 ===== ', end = '')
meu_radio.diminuir_volume(20)

print('caso 5 ===== ', end = '')
meu_radio.ligar()

print('caso 6 ===== ', end = '')
meu_radio.aumentar_volume(200)

print('caso 6.1 ===== ', end = '')
meu_radio.aumentar_volume(85)

print('caso 7 ===== ', end = '')
meu_radio.diminuir_volume(20)

print('caso 7.1 ===== ', end = '')
meu_radio.diminuir_volume(-58)

print('caso 8 ===== ', end = '')
meu_radio.mudar_frequencia(25.5)

print('caso 9 ===== ', end = '')
meu_radio.habilitar_antena()

print('caso 10 ===== ', end = '')
meu_radio.mudar_frequencia(91.5)

print('caso 11 ===== ', end = '')
meu_radio.mudar_frequencia(55.5)

print('caso 12 ===== ', end = '')
meu_radio.mudar_frequencia()

print('caso 13 ===== ', end = '')
meu_radio.mudar_frequencia(94.1)
