import json
import os
from racas_dEd import escolher_raca_dEd
from racas_mordenkainen import escolher_raca_mordenkainen
from livrodEd import livro_lista_dEd, livro_racas_dEd
from livromordekainen import livro_lista_mordenkainen, livro_racas_mordenkainen

ficha = {}

racasdEd = livro_racas_dEd()
racasmordenkainen = livro_racas_mordenkainen()


def main():
        
    while True:
        try:

            resposta = int(input("O que voce deseja fazer? (1- Criar uma nova ficha, 2- gerenciar fichas, 3- Livro, 0- Sair): "))

            if resposta == 1:
                while True:
                    try:
                        nome_ficha = input("Digite o nome de seu personagem: ")
                        ficha["nome"] = nome_ficha
                        classe_ficha = int(input("Qual classe voce quer? (1- d&d basico, 2- d&d MORDENKAINEN, 0- Voltar): "))

                        if classe_ficha == 1:
                            escolher_raca_dEd(ficha)
                                    
                        elif classe_ficha == 2:
                            escolher_raca_mordenkainen(ficha)
                        else:
                            pass

                        nome_arquivo = input("Digite o nome que voce deseja para o arquivo que sua ficha ira ser salvo (Ex: ficha1): ")
                        nome_final = nome_arquivo + ".json"
          
                        if os.path.exists(nome_final):
                            print(f"AVISO: O arquivo '{nome_final}' ja existe!")
                            escolha_subArquivo = int(input("Voce deseja criar um novo arquivo com o mesmo nome? (1- Sim, 2- Nao)  (Ira excluir o arquivo anterior): "))

                            if escolha_subArquivo == 1:

                                with open(nome_final, "w", encoding='utf-8') as Arquivo:
                                    json.dump(ficha, Arquivo, ensure_ascii=False, indent=4)

                                print(f"Arquivo '{nome_final}' substituido com sucesso")

                            else:
                                pass
                        else:
                            with open(nome_final, "w", encoding='utf-8') as Arquivo:
                                    json.dump(ficha, Arquivo, ensure_ascii=False, indent=4)

                            print(f"Arquivo '{nome_final}' criado com sucesso")

                        escolha1 = int(input("Voce deseja criar outra ficha? (1- Sim, 2- Nao): "))

                        if escolha1 == 1:
                            pass
                        else:
                            break
                        print(f"Arquivo '{nome_final}' criado com sucesso")

                    except ValueError:
                        print("Erro: Por favor, digite algo antes de pressionar Enter")

            elif resposta == 2:
                arquivos_json = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]

                if len(arquivos_json) == 0:
                    print("Nenhuma ficha encontrada.")
                else:
                    print("\nFichas encontradas:\n")

                    for i, arquivo in enumerate(arquivos_json):
                        print(f"{i + 1}- {arquivo}")

                    escolha_arquivo = int(input("\nDigite o numero da ficha que deseja abrir, ou 0 para voltar: "))

                    if escolha_arquivo == 0:
                        pass
                    elif escolha_arquivo > len(arquivos_json):
                        print("Opção invalida")
                    else:
                        arquivo_escolhido = arquivos_json[escolha_arquivo - 1]

                        with open(arquivo_escolhido, "r", encoding="utf-8") as Arquivo:
                            ficha_aberta = json.load(Arquivo)

                        print("\n========== FICHA ==========\n")

                        for chave, valor in ficha_aberta.items():
                            print(f"{chave.capitalize():<25}: {valor}")

                        print("\n===========================\n")

                        editar = int(input("Voce deseja editar essa ficha? (1- Sim, 2- Nao): "))

                        if editar == 1:
                            print("\nCampos da ficha:\n")

                            campos = list(ficha_aberta.keys())

                            for i, campo in enumerate(campos):
                                print(f"{i + 1}- {campo}: {ficha_aberta[campo]}")

                            escolha_campo = int(input("\nDigite o numero do campo que deseja editar, ou 0 para cancelar: "))

                            if escolha_campo == 0:
                                print("Edição cancelada.")
                            elif escolha_campo > len(campos):
                                print("Campo invalido.")
                            else:
                                campo_escolhido = campos[escolha_campo - 1]
                                novo_valor = input(f"Digite o novo valor para '{campo_escolhido}': ")

                                ficha_aberta[campo_escolhido] = novo_valor

                                with open(arquivo_escolhido, "w", encoding="utf-8") as Arquivo:
                                    json.dump(ficha_aberta, Arquivo, ensure_ascii=False, indent=4)

                                print("Ficha atualizada com sucesso.")

            elif resposta == 3:
                livro_main = int(input("Voce deseja ver o livro de (1- D&D, 2- MORDENKAINEN): "))

                if livro_main == 1:
                    livro_lista_dEd(ficha)
            elif resposta == 0:
                print("saindo...")
                print("")
                break
            else:
                print("Opçao invalida")

        except ValueError:
            print("Erro: Por favor, digite algo antes de pressionar Enter")

if __name__ == "__main__":
    main()
