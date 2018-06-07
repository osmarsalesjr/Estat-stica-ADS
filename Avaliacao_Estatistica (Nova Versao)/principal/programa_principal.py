import calcular_propriedades as cp

def main():
    list_data = load_data()

    menu = "\n>>>>>>>>... MENU ...<<<<<<<<"
    menu += "\n1 - Listar Base de Dados"
    menu += "\n2 - Calcular propriedades (1ª Questao)"
    menu += "\n3 - Ver Tabela de Frequencia (2ª Questão)"
    menu += "\n4 - Ver Tabela de Frequencia Auxiliar (2ª Questão)"
    menu += "\n5 - Calcular Propriedades (2ª Questão)"
    menu += "\n6 - Ver Histograma (2ª Questão)"
    menu += "\n0 - Encerrar programa\n>> "

    tabela_de_frequencia = cp.criar_tabela_de_frequecia(list_data)
    tabela_de_frequencia_auxiliar = cp.criar_tabela_de_frequencia_auxiliar(list_data)
    propriedades_gerais = cp.propriedades_gerais(list_data)
    propriedades_gerais_amostral = cp.calcular_propriedades_por_amostra(tabela_de_frequencia_auxiliar)

    while(True):
        opcao = int(input(menu))
        if (opcao == 0):
            print("PROGRAMA ENCERRADO PELO USUÁRIO.")
            break
        elif (opcao == 1):
            print_lista_dados(list_data)
        elif (opcao == 2):
            print_propriedades_gerais(propriedades_gerais)
        elif (opcao == 3):
            print_tabela_de_frequencia(tabela_de_frequencia)
        elif (opcao == 4):
            print_tabela_de_frequencia_auxiliar(tabela_de_frequencia_auxiliar)
        elif(opcao == 5):
            print_propriedades_gerais_amostral(propriedades_gerais_amostral)
        elif (opcao == 6):
            print("O HISTOGRAMA AINDA NAO ESTA DISPONIVEL :[, POR FAVOR TENTE MAIS TARDE.")
            cp.criar_histograma(list_data)
        else:
            print("OPCAO INVALIDA.")
        input("Pressione enter para continuar...\n")



def load_data():
    file = open("dados.txt", "r")
    file_lines = file.readlines()
    list_data = list()

    if len(file_lines) <= 0:
        original_file = open("dados_originais.txt", "r")
        original_file_lines = original_file.readlines()
        temp = [i.upper() for i in original_file_lines[0].split()]

        for i in range(1, len(original_file_lines)):
            words = [i for i in original_file_lines[i].split()]
            list_data.append({temp[0]: words[0], temp[1]: eval(words[1]), temp[2]: float(words[2])})
        original_file.close()
    else:
        for line in file_lines:
            list_data.append(eval(line))
    file.close()
    save_data(list_data)
    return list_data


def print_list(list):
    for item in list:
        print(item)



def print_lista_dados(lista):
    print(">>>>>>>>>>>>>> BASE DE DADOS <<<<<<<<<<<<<<")
    print("|\t\t\tCURSO\t\t\t||\t\t\tANO\t\t\t||\t\t\tMATRICULADOS\t\t\t|")

    for item in lista:
        print("|\t\t%s\t\t||\t\t%d\t\t||\t\t%.2f\t\t|" % (item["CURSO"], item["ANO"], item["MATRICULADOS"]))


def print_propriedades_gerais(lista):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>> PROPRIEDADES <<<<<<<<<<<<<<")
    print("|\tVALOR MINIMO\t||\t\tVALOR MAXIMO\t||\t\tAMPLITUDE\t\t||"
          "\t\t\tMEDIA\t\t||\t\tMEDIANA\t\t\t||\t\tVARIANCIA\t\t||"
          "\t\tDESVIO PADRAO\t||\tCOEFICIENTE DE VARIACAO\t||\t\t\tMODA\t\t|")
    for item in lista:
        print("|\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||"
              "\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t\t%.4f\t\t\t|" % (item["VALOR_MINIMO"], item["VALOR_MAXIMO"], item["AMPLITUDE"],
                                                                        item["MEDIA"], item["MEDIANA"], item["VARIANCIA"],
                                                                        item["DESVIO_PADRAO"], item["COEFICIENTE_DE_VARIACAO"]),
              end="")
        if (item["MODA"] is None):
            print("|\t\tNao Ha Moda\t\t|")
        else:
            print("|\t\t%.4f\t\t|" % item["MODA"])



def print_propriedades_gerais_amostral(lista):
    print("\t\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>> PROPRIEDADES GERAIS AMOSTRAIS <<<<<<<<<<<<<<")
    print("|\t\t\tMEDIA\t\t||\t\tMEDIANA\t\t\t||\t\tVARIANCIA\t\t||"
          "\tDESVIO PADRAO\t||\tCOEFICIENTE DE VARIACAO\t||\t\tMODA\t\t|")
    for item in lista:
        print("|\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t||\t\t\t%.4f\t\t\t|" % (item["MEDIA"], item["MEDIANA"],
                                                                                        item["VARIANCIA"], item["DESVIO_PADRAO"],
                                                                                        item["COEFICIENTE_DE_VARIACAO"]),
              end="")
        if (item["MODA"] is None):
            print("|\tNao Ha Moda\t|")
        else:
            print("|\t\t%.4f\t|" % item["MODA"])




def print_tabela_de_frequencia(lista):
    print("\t\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>> TABELA DE FREQUENCIA <<<<<<<<<<<<<<")
    print("|\t\tCLASSES\t\t\t||\t\t\tfi\t\t\t||\t\t\txi\t\t\t||\t\tfri\t\t\t||"
          "\t\t\tFi\t\t\t||\t\t\tFri\t\t|")
    for item in lista:
        print("|\t\t%s\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t|" % (item["FAIXA"], item["fi"],
                                                                                               item["xi"], item["fri"],
                                                                                               item["Fi"], item["Fri"]))



def print_tabela_de_frequencia_auxiliar(lista):
    print("\t\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>> TABELA DE FREQUENCIA AUXILIAR <<<<<<<<<<<<<<")
    print("|\t\tCLASSES\t\t\t||\t\t\tfi\t\t\t||\t\t\txi\t\t\t||"
          "\t\t\tFi\t\t\t||\t\t\tfi*xi\t\t\t||\t\t\tfi*xi²\t\t\t\t|")
    for item in lista:
        print("|\t\t%s\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t||\t\t%.4f\t\t|" % (item["FAIXA"], item["fi"],
                                                                                  item["xi"], item["Fi"],
                                                                                  item["fixi"], item["fixi2"]))



def save_data(list):
    file = open("dados.txt", "w")

    for item in list:
        file.write(str(item) + "\n")
    file.close()



if __name__ == '__main__':
    main()