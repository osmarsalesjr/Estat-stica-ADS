import statistics as st
from math import sqrt as raiz

def main():
    pass


def variancia(lista):
    return st.variance(lista)


def mediana(lista):
    return st.median(lista)


def media(lista):
    return st.mean(lista)


def amplitude(lista):
    return max(lista) - min(lista)


def moda(lista):
    try:
        return st.mode(lista)
    except:
        return None


def coeficiente_de_variacao(lista):
    return desvio_padrao(lista) / media(lista)


def desvio_padrao(lista):
    return st.stdev(lista)


def ponto_medio(lista):
    return max(lista) + min(lista) / 2.0


def media_amostral(lista):
    somatorio = 0
    soma_fi = 0

    for item in lista:
        somatorio += item["xi"] * item["fi"]
        soma_fi += item["fi"]
    media = somatorio/soma_fi

    return media

def modal_classes(lista, lista_t):
    maior_frequencia = lista[0]["fi"]
    for i in range(len(lista)):
        if lista[i]["fi"] >= maior_frequencia:
            maior_frequencia = lista[i]["fi"]
            classe = lista[i]["FAIXA"]

    for item in lista_t:
        if item["FAIXA"] == classe:
            sequencia = item["SEQUENCIA"]
            break

    limite_inferior = min(sequencia)
    limite_superior = max(sequencia)

    moda = (limite_inferior + limite_superior) / 2.0

    return moda


def mediana_amostral(lista, sequencias):
    soma_fi = 0
    for item in lista:
        soma_fi += item["fi"]
    posicao = int(soma_fi/2)

    soma_fi = 0
    index_anterior = None
    index_atual = None
    for i in range(len(lista)):
        soma_fi += lista[i]["fi"]
        if soma_fi >= posicao:
            index_anterior = i - 1
            index_atual = i
            break
    limite_inferior = min(sequencias[index_atual]["SEQUENCIA"])
    amplitude_t = amplitude(sequencias[index_atual]["SEQUENCIA"])
    fi = lista[index_atual]["fi"]
    Fi = lista[index_anterior]["Fi"]
    mediana_am = limite_inferior + (((posicao - Fi) / fi) * amplitude_t)
    return mediana_am



def variancia_amostral(lista):
    soma_fi = 0
    soma_fixi = 0
    soma_fixi2 = 0

    for item in lista:
        soma_fi += item["fi"]
        soma_fixi += item["fixi"]
        soma_fixi2 += item["fixi2"]

    variance = (soma_fixi2 - ((soma_fixi * soma_fixi) / soma_fi)) / soma_fi - 1
    return variance


def desvio_padrao_amostral(lista):
    return raiz(variancia_amostral(lista))




if __name__ == '__main__':
    main()