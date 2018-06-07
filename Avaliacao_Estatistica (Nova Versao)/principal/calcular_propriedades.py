import propriedades_estatisticas as pe
from matplotlib import pyplot as plt

classes = ["2010-2011", "2011-2012", "2012-2013", "2013-2014",
           "2014-2015", "2015-2016", "2016-2017", "2017-2018"]

def main():
    pass


def matriculados_por_curso(lista):
    matriculados = list()
    for item in lista:
        matriculados.append(item["MATRICULADOS"])
    return matriculados


def propriedades_gerais(lista_de_dados):
    arquivo = open("propriedades_gerais.txt", "r")
    linhas = arquivo.readlines()
    lista_de_propriedades = list()
    moda = None

    if len(linhas) <= 0:
        arquivo_t = open("propriedades_gerais.txt", "r")
        arquivo_t_linhas = arquivo_t.readlines()
        media_t = arquivo_t_linhas[0]["MEDIA"]

        matriculados_curso = matriculados_por_curso(lista_de_dados)
        valor_minimo = min(matriculados_curso)
        valor_maximo = max(matriculados_curso)
        amplitude = pe.amplitude(matriculados_curso)
        media = pe.media(matriculados_curso)
        mediana = pe.mediana(matriculados_curso)
        moda = pe.moda(matriculados_curso)
        variancia = pe.variancia(matriculados_curso)
        desvio_padrao = pe.desvio_padrao(matriculados_curso)
        coeficiente_de_variacao = pe.coeficiente_de_variacao(matriculados_curso)

        pg = {"VALOR_MINIMO": valor_minimo, "VALOR_MAXIMO": valor_maximo,
                               "AMPLITUDE": amplitude, "MEDIA": media, "MEDIANA": mediana,
                               "MODA": moda, "VARIANCIA": variancia, "DESVIO_PADRAO": desvio_padrao,
                               "COEFICIENTE_DE_VARIACAO": coeficiente_de_variacao}
        arquivo.close()
        arquivo = open("propriedades_gerais.txt", "w")
        arquivo.write(str(pg) + "\n")
        arquivo.close()
        lista_de_propriedades.append(pg)
    else:
        lista_de_propriedades = [eval(i) for i in linhas]

    return lista_de_propriedades


def criar_tabela_de_frequecia(lista):

    arquivo = open("tabela_de_frequencia.txt", "r")
    linhas_arquivos = arquivo.readlines()
    tabela_frequencia = list()
    total_matriculados = sum(matriculados_por_curso(lista))
    qtd_parcial_matriculados = 0

    if (len(linhas_arquivos) <= 0):
        temp_percent = 0.0
        index = 0
        for classe in classes:
            intervalo = [eval(i) for i in classe.split("-")]
            temp_lista = list()
            for i in range(index, len(lista)):
                if lista[i]["ANO"] >= intervalo[0] and lista[i]["ANO"] < intervalo[1]:
                    temp_lista.append(lista[i]["MATRICULADOS"])
                    index = i

            qtd_matriculados = sum(temp_lista)
            qtd_parcial_matriculados += qtd_matriculados
            percent = qtd_matriculados / total_matriculados
            temp_percent += percent

            tabela_frequencia.append({"FAIXA": classe, "fi": qtd_matriculados, "xi": pe.ponto_medio(temp_lista),
                                      "fri": percent, "Fi": qtd_parcial_matriculados, "Fri": temp_percent})
    else:
        for linha in linhas_arquivos:
            tabela_frequencia.append(eval(linha))
    arquivo.close()
    save_tabela_de_frequencia(tabela_frequencia)
    return tabela_frequencia


def criar_tabela_de_sequencias_por_classe(lista):
    arquivo = open("sequencia_de_valores_por_classe.txt", "r")
    arquivo_linhas = arquivo.readlines()
    sequencia_de_valores_por_classe = list()

    if len(arquivo_linhas) <= 0:
        index = 0
        for classe in classes:
            intervalo = [eval(i) for i in classe.split("-")]
            temp_lista = list()
            for i in range(index, len(lista)):
                if lista[i]["ANO"] >= intervalo[0] and lista[i]["ANO"] < intervalo[1]:
                    temp_lista.append(lista[i]["MATRICULADOS"])
                    index = i
            sequencia_de_valores_por_classe.append({"FAIXA": classe, "SEQUENCIA": temp_lista})
    else:
        for linha in arquivo_linhas:
            sequencia_de_valores_por_classe.append(eval(linha))
    arquivo.close()
    save_sequencia_de_valores_por_classe(sequencia_de_valores_por_classe)
    return sequencia_de_valores_por_classe



def criar_tabela_de_frequencia_auxiliar(lista):
    arquivo = open("tabela_de_frequencia_auxiliar.txt", "r")
    linhas_arquivo = arquivo.readlines()
    tabela_frequencia_auxiliar = list()

    if len(linhas_arquivo) <= 0:
        linhas_tabela = criar_tabela_de_frequecia(lista)

        for linha in linhas_tabela:
            dado_amostral = {"FAIXA": linha["FAIXA"], "fi": linha["fi"], "xi": linha["xi"], "Fi": linha["Fi"],
                             "fixi": linha["fi"] * linha["xi"], "fixi2": linha["xi"] * linha["xi"] * linha["fi"]}
            tabela_frequencia_auxiliar.append(dado_amostral)
        save_tabela_de_frequencia_auxiliar(tabela_frequencia_auxiliar)
    else:
        for linha in linhas_arquivo:
            tabela_frequencia_auxiliar.append(eval(linha))
    arquivo.close()
    return tabela_frequencia_auxiliar


def calcular_propriedades_por_amostra(tabela_de_frequencia):
    arquivo_t = open("propriedades_por_amostra.txt", "r")
    arquivo_t_linhas = arquivo_t.readlines()
    valores_amostrais = list()

    if len(arquivo_t_linhas) <= 0:
        dados = open("dados.txt", "r")
        lista_de_dados = list(eval(i) for i in dados.readlines())
        tabela_de_frequencia_auxiliar = criar_tabela_de_frequencia_auxiliar(tabela_de_frequencia)
        sequencia_de_valores_por_classe = criar_tabela_de_sequencias_por_classe(lista_de_dados)

        media = pe.media_amostral(tabela_de_frequencia_auxiliar)
        mediana = pe.mediana_amostral(tabela_de_frequencia_auxiliar, sequencia_de_valores_por_classe)
        moda = pe.modal_classes(tabela_de_frequencia_auxiliar, sequencia_de_valores_por_classe)
        variancia = pe.variancia_amostral(tabela_de_frequencia_auxiliar)
        desvio_padrao = pe.desvio_padrao_amostral(tabela_de_frequencia_auxiliar, media)
        coeficiente_de_variacao = desvio_padrao / media

        dados_amostrais = {"MEDIA": media, "MEDIANA": mediana, "MODA": moda,
                           "VARIANCIA": variancia, "DESVIO_PADRAO": desvio_padrao,
                           "COEFICIENTE_DE_VARIACAO": coeficiente_de_variacao}
        arquivo_t.close()
        arquivo = open("propriedades_por_amostra.txt", "w")
        arquivo.write(str(dados_amostrais) + "\n")
        arquivo.close()
        valores_amostrais.append(dados_amostrais)
    else:
        for linha in arquivo_t_linhas:
            valores_amostrais.append(eval(linha))
    arquivo_t.close()

    return valores_amostrais



def save_tabela_de_frequencia(valores):
    arquivo = open("tabela_de_frequencia.txt", "w")
    for item in valores:
        arquivo.write(str(item) + "\n")
    arquivo.close()


def save_sequencia_de_valores_por_classe(sequencia_de_valores_por_classe):
    arquivo = open("sequencia_de_valores_por_classe.txt", "w")
    for linha in sequencia_de_valores_por_classe:
        arquivo.write(str(linha) + "\n")
    arquivo.close()



def save_tabela_de_frequencia_auxiliar(lista):
    arquivo = open("tabela_de_frequencia_auxiliar.txt", "w")
    for linha in lista:
        arquivo.write(str(linha) + "\n")
    arquivo.close()




def criar_histograma(lista):
    tabela_de_sequencias_por_classe = criar_tabela_de_sequencias_por_classe(lista)
    x_axis = list()
    y_axis = list()
    for item in tabela_de_sequencias_por_classe:
        x_axis.append(item["SEQUENCIA"])
        y_axis.append(sum(item["SEQUENCIA"]))

    largura = 0.8
    cor = "blue"

    plt.bar(range(len(x_axis)), y_axis, width = largura, color = cor, align = "center", linewidth = 1)
    plt.xticks(range(len(x_axis)), classes)
    plt.savefig("histograma.png")
    plt.show()


if __name__ == '__main__':
    main()