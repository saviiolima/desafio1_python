# Missão 1: Restaurando as Regras Escolares / No final verifica se a nota do aluno é maior ou igual a 5

def verificar_aprovacao(nota):
    if nota >= 5:
        return "Aprovado"
    else:
        return "Reprovado"

# Missão 2: O Sistema Eleitoral Secreto / Verifica se a pessoa pode votar


def verificar_votacao(idade):
    if idade >= 16:
        return "Pode votar"
    else:
        return "Não pode votar"

# Missão 3: Recuperando o Sistema de Notas / Classifica a nota do aluno


def classificar_nota(nota):
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota < 90:
        return "Muito bem, você tirou B."
    elif 70 <= nota < 80:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota < 70:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."

# Missão 4: Restaurando a Identificação de Números / Soma dois números


def somar_numeros(a, b):
    return a + b

# Missão 5: Recuperando o Cofre de Segurança / Verifica se a senha está correta


def verificar_senha(senha):
    senha_correta = "Python123"
    if senha == senha_correta:
        return "Acesso permitido"
    else:
        return "Acesso negado"

# Missão 6: Reforçando a Segurança e a Contagem do Sistema / Conta de 1 a 10


def contar_numeros():
    i = 1
    while i <= 10:
        print(i)
        i += 1

# Missão 7: Organizando a Lista de Números / Ordena uma lista de números


def ordenar_lista():
    numeros = [8, 3, 10, 1, 5]
    return sorted(numeros)

# Missão 8: Acessando os Registros de Alunos / Acessa o primeiro e último registro


def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    return alunos[0], alunos[-1]

# Missão 9: Calculando Dobro de um Número / Retorna o dobro de um número


def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"

# Missão 10: Contando Letras em um Nome


def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"


# Testes
if __name__ == "__main__":
    print(verificar_aprovacao(8))
    print(verificar_votacao(16))
    print(classificar_nota(85))
    print(somar_numeros(4, 5))
    print(verificar_senha("Python123"))
    contar_numeros()
    print(ordenar_lista())
    print(acessar_registros())
    print(dobro(5))
    print(contar_letras("Ana"))
