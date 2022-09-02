def pega_periodo():
    '''
    Função que obtém o período de monitoramento das temperaturas 
    retorno: periodo -> lista contendo o número de dias(colunas) e de semanas(linhas) obtidos pelo usuário
    '''
    dias = int(input('Dias por semana: '))
    semanas = int(input('Semanas: '))
    periodo = [dias, semanas]
    return periodo


def cria_matriz(periodo):
    '''
    (int, int) -> temperaturas : matriz 
    Recebe o número de linhas e colunas e cria uma matriz com essas dimensões, 
    preenhce com as temperaturas médias no período e retorna a matriz
    '''
    temperaturas = []
    for i in range(periodo[1]):
        semanas = []
        for j in range(periodo[0]):
            print(f'{i + 1}ª semana, {j + 1}º dia')
            semanas.append(float(input(f'Temperatura: ')))
        temperaturas.append(semanas)
    return temperaturas


def pega_menor_maior(temperaturas):
    '''
    Função que pega a menor e a maior temperatura em uma matriz de temperaturas
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: menor_maior -> Lista contendo a menor e a maior temperatura respectivamente
    '''
    menor = temperaturas[0][0]
    maior = temperaturas[0][0]
    for semana in temperaturas:
        for temp in semana:
            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp
    menor_maior = [menor, maior]
    return menor_maior

def separa_negativas(temperaturas):
    '''
    Função que cria um array com os valores negativos de uma matriz
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: negativas -> Array contendo os valores negativos da matriz
    '''
    negativas = []
    for semana in temperaturas:
        for temp in semana:
            if temp < 0:
                negativas.append(temp)
    return negativas

def soma(temperaturas):
    '''
    Função que calcula a soma das temperaturas em uma matriz
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: soma -> soma das temperaturas da matriz
    '''
    soma = 0
    for semana in temperaturas:
        for temp in semana:
            soma += temp
    return soma

def media_temp(temperaturas):
    '''
    Função que calcula a média das temperaturas em uma matriz
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: media -> média das temperaturas da matriz
    '''
                            # quantidade de semanas * quantidade de dias na semana(temperaturas)
    media = soma(temperaturas) / (len(temperaturas) * len(temperaturas[0]))
    return media

def imprimir_dados(temperaturas, menor_maior, negativas, media):
    '''
    Função que imprime os dados obtidos
    parâmetro: temperaturas -> Matriz contendo temperaturas
    parâmetro: menor_maior -> Lista contendo a menor e a maior temperatura respectivamente
    parâmetro: negativas -> Array contendo os valores negativos da matriz
    parâmetro: media -> média das temperaturas da matriz
    '''
    print(f'Temperaturas: {temperaturas}\n')
    print(f'Menor temperatura: {menor_maior[0]}°C | Maior temperatura: {menor_maior[1]}°C\n')
    print(f'Temperaturas negativas: {negativas}\n')
    print(f'Média das temperaturas: {media}°C')

def main():
    periodo = pega_periodo()
    temperaturas = cria_matriz(periodo)
    menor_maior = pega_menor_maior(temperaturas)
    negativas = separa_negativas(temperaturas)
    media = media_temp(temperaturas)
    imprimir_dados(temperaturas, menor_maior, negativas, media)

# Chamada da função principal
main()