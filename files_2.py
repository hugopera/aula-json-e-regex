import os
import json as manipjson

filepath = R"D:\dev\PI0925\python\dicionario.json"

dicpessoa = {}

if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        dicpessoa = manipjson.load(file)

sair = 0

while sair != -1:
    print("MENU: ")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Gravar file")
    print("5 - Sair sem guardar")
    opc = input("Opção: ")

    match opc:
        case "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            morada = input("Morada: ")

            dicpessoa[nome] = {"idade": idade, "morada": morada}

        case "2":
            for nome in dicpessoa:
                print(nome, dicpessoa[nome])

        case "3":
            nome = input("Nome: ")

            if nome in dicpessoa:
                del dicpessoa[nome]

        case "4":
            with open(filepath, "w", encoding="utf-8") as file:
                manipjson.dump(dicpessoa, file, indent=4, ensure_ascii=False)
            break

        case "5":
            sair = -1
            break

        case _:
            print("Opção inválida")