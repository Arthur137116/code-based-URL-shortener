import random
import string
import webbrowser

urls = {}

def gerar_codigo():
    letras = string.ascii_letters + string.digits
    return "".join(random.choice(letras) for i in range(5))

while True:
    print("\nEncurtador de URL's")
    print("\n1. Gerar um codigo")
    print("2. Abrir um codigo")
    print("3. Sair")

    escolha = input("O que você deseja fazer? ").strip().lower()

    if escolha == "1" or escolha == "Gerar um codigo".strip().lower():
        link_longo = input('Digite o URL: ').strip()
        if not link_longo:
            print('Digite um link válido! ')
            continue

        else: 
            codigo = gerar_codigo()
            urls[codigo] = link_longo
            print(f'Sucesso! Seu código é {codigo}')
        
    

    elif escolha == '2' or  escolha == "Abrir um codigo".strip().lower():
        codigo_digitado = input('Digite seu código: ').strip()
        if codigo_digitado in urls:
            link_longo = urls[codigo_digitado]
            print('Redirecionando para o Link Original!')
            webbrowser.open(link_longo)

        else:
            print('Código não encontrado')


    elif escolha == "3" or escolha == "Sair".lower().strip():
        print("Até a próxima!")
        break

    else:
        print('Escolha um opção válida! ')