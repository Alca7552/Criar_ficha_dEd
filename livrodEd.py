def livro_racas_dEd():

    racas = {
        1: {
            "nome": "Anão",
            "info": [
                "Atributos: Constituição +2",
                "Idade: vivem em média cerca de 350 anos",
                "Tamanho: Médio, geralmente entre 1,20 m e 1,50 m",
                "Deslocamento: 7,5 m",
                "Visão no escuro: 18 m",
                "Resiliência Anã: vantagem contra veneno e resistência a dano de veneno",
                "Treinamento Anão em Combate: machado de batalha, machadinha, martelo leve e martelo de guerra",
                "Ferramentas: proficiência com uma ferramenta de artesão",
                "Especialização em Rochas: bônus melhorado em testes de História ligados a pedra"
            ],
            "subracas": {
                1: ["Anão da Colina", "Sabedoria +1", "PV máximo aumenta em 1 por nível"],
                2: ["Anão da Montanha", "Força +2", "Proficiência com armaduras leves e médias"]
            }
        },

        2: {
            "nome": "Elfo",
            "info": [
                "Atributos: Destreza +2",
                "Idade: podem viver cerca de 750 anos",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Sentidos Aguçados: proficiência em Percepção",
                "Ancestralidade Feérica: vantagem contra encantamento e não dorme por magia",
                "Transe: descansa meditando por 4 horas"
            ],
            "subracas": {
                1: ["Alto Elfo", "Inteligência +1", "Treinamento com espada longa, espada curta, arco longo e arco curto", "Recebe 1 truque de mago"],
                2: ["Elfo da Floresta", "Sabedoria +1", "Deslocamento 10,5 m", "Pode se esconder melhor em ambiente natural"],
                3: ["Elfo Negro / Drow", "Carisma +1", "Visão no escuro superior", "Sensibilidade à luz solar", "Magias drow"]
            }
        },

        3: {
            "nome": "Halfling",
            "info": [
                "Atributos: Destreza +2",
                "Idade: vivem em média cerca de 150 anos",
                "Tamanho: Pequeno",
                "Deslocamento: 7,5 m",
                "Sortudo: ao tirar 1 no d20, pode rolar novamente",
                "Bravura: vantagem contra ficar amedrontado",
                "Agilidade Halfling: pode atravessar espaço de criatura maior"
            ],
            "subracas": {
                1: ["Pés-leves", "Carisma +1", "Pode se esconder atrás de criaturas maiores"],
                2: ["Robusto", "Constituição +1", "Vantagem contra veneno e resistência a dano de veneno"]
            }
        },

        4: {
            "nome": "Humano",
            "info": [
                "Atributos: +1 em todos os atributos",
                "Idade: padrão humano",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Versatilidade: raça simples e equilibrada"
            ],
            "subracas": {}
        },

        5: {
            "nome": "Draconato",
            "info": [
                "Atributos: Força +2 e Carisma +1",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Ancestralidade Dracônica: escolhe um tipo de dragão",
                "Arma de Sopro: ataque elemental baseado na ancestralidade",
                "Resistência a Dano: resistência ao tipo de dano da ancestralidade"
            ],
            "subracas": {}
        },

        6: {
            "nome": "Gnomo",
            "info": [
                "Atributos: Inteligência +2",
                "Idade: podem viver vários séculos",
                "Tamanho: Pequeno",
                "Deslocamento: 7,5 m",
                "Visão no escuro: 18 m",
                "Esperteza Gnômica: vantagem em testes de Int, Sab e Car contra magia"
            ],
            "subracas": {
                1: ["Gnomo da Floresta", "Destreza +1", "Conhece o truque Ilusão Menor", "Pode se comunicar de forma simples com animais pequenos"],
                2: ["Gnomo das Rochas", "Constituição +1", "Conhecimento de artífice", "Pode criar pequenos dispositivos mecânicos"]
            }
        },

        7: {
            "nome": "Meio-Elfo",
            "info": [
                "Atributos: Carisma +2 e +1 em dois atributos à escolha",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Ancestralidade Feérica: vantagem contra encantamento e não dorme por magia",
                "Versatilidade em Perícia: proficiência em duas perícias à escolha"
            ],
            "subracas": {}
        },

        8: {
            "nome": "Meio-Orc",
            "info": [
                "Atributos: Força +2 e Constituição +1",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Ameaçador: proficiência em Intimidação",
                "Resistência Implacável: ao cair a 0 PV, pode ficar com 1 PV uma vez por descanso longo",
                "Ataques Selvagens: acerto crítico corpo a corpo causa dano extra"
            ],
            "subracas": {}
        },

        9: {
            "nome": "Tiefling",
            "info": [
                "Atributos: Carisma +2 e Inteligência +1",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Resistência Infernal: resistência a dano de fogo",
                "Legado Infernal: recebe magias raciais conforme sobe de nível"
            ],
            "subracas": {}
        }
    }

    return racas

def livro_mostrar_racas_dEd(racas, titulo="RAÇAS"):

    print(f"\n========== {titulo} ==========\n")

    for numero, dados in racas.items():
        print(f"[{numero}] {dados['nome']}")
        print("")

def livro_mostrar_info_raca(raca):

    print(f"\n========== {raca['nome'].upper()} ==========\n")

    for info in raca["info"]:
        print(f"- {info}")

    if raca["subracas"]:

        escolha_sub = int(input("\nVoce deseja ver as Sub-Raças? (1- Sim, 2- Nao): "))

        if escolha_sub == 1:

            print("\n========== SUB-RAÇAS ==========\n")

            for numero, sub in raca["subracas"].items():
                print(f"[{numero}] {sub[0]}")

            escolha_sumario_subraca = int(input("\nQual Sub-Raça voce deseja ver?: "))

            if escolha_sumario_subraca in raca["subracas"]:

                sub = raca["subracas"][escolha_sumario_subraca]

                print(f"\n----- {sub[0].upper()} -----\n")

                for detalhe in sub[1:]:
                    print(f"- {detalhe}")

            else:
                print("Sub-raça inválida.")

def livro_lista_dEd(ficha):

    racas = livro_racas_dEd()

    while True:
        sumario = int(input("Aqui voce ira ver a lista das 9 raças do Livro do Jogador de D&D. Voce deseja (1- Continuar, 2- Voltar): "))

        if sumario == 2:
            break

        livro_mostrar_racas_dEd(racas)

        escolha_sumario = int(input("\nDeseja visualizar alguma raça em especifico? Digite o numero da raça ou 0 para voltar: "))

        if escolha_sumario == 0:
            break

        if escolha_sumario not in racas:
            print("Raça inválida.")
            continue

        livro_mostrar_info_raca(racas[escolha_sumario])

        input("\nPressione Enter para voltar ao sumário...")
