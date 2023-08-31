nome = []
idade = []
genero = []
media_idade = 0
soma_idade = 0
homem_velho = 0
nome_homem = ''
mulher_nova = 0
nome_mulher = ''

for pessoas in range(0,4):
    lista_nome = str(input('Digite o nome da {}º pessoa: '.format(pessoas+1)))
    lista_idade = int(input('Digite a idade da {}º pessoa:  '.format(pessoas+1)))
    lista_genero = str(input('Digite o gênero da {}º pessoa:(M/F)  '.format(pessoas+1))).upper()
    print("-"*80)
    nome.append(lista_nome)
    idade.append(lista_idade)
    genero.append(lista_genero)
    soma_idade = soma_idade + lista_idade
    media_idade = soma_idade/len(idade)

    if pessoas == 1 and lista_genero == 'M': 
        homem_velho = lista_idade
        nome_homem = lista_nome
    if lista_genero == 'M' and lista_idade > homem_velho:
        homem_velho = lista_idade
        nome_homem = lista_nome
    if lista_genero == 'F' and lista_idade < 20:
        lista_idade = mulher_nova
        nome_mulher = lista_nome

print(nome, idade, genero, media_idade)
print('A media da idade é {} anos. O homem mais velho é {} e tem {} anos, e a mulher com menos de 20 anos é {}'.format(media_idade, nome_homem, homem_velho, nome_mulher))
