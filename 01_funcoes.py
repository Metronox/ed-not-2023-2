#Função que calcula o IMC de uma pessoa
def cal_imc(peso, altura):
    return peso / altura ** 2

    # p = 85
    # a = 1.72
    # imc = cal_imc(p, a)

    # print(imc)

    print(cal_imc(85, 1.72))