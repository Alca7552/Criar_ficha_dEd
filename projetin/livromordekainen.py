def livro_racas_mordenkainen():

    racas = {
        1: {
            "nome": "Aarakocra",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Voo: deslocamento de voo igual ao deslocamento de caminhada",
                "Restrição: não pode voar usando armadura média ou pesada",
                "Garras: pode usar as garras como ataque natural",
                "Magia: recebe magia ligada ao ar em nível maior"
            ]
        },

        2: {
            "nome": "Aasimar",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Resistência: dano radiante e necrótico",
                "Mãos Curativas: pode curar uma criatura tocada",
                "Revelação Celestial: forma especial temporária com efeito celestial"
            ]
        },

        3: {
            "nome": "Bugurso",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Alcance Longo: ataques corpo a corpo têm alcance maior no seu turno",
                "Construção Poderosa: conta como maior para carregar peso",
                "Ataque Surpresa: causa dano extra contra criatura surpreendida"
            ]
        },

        4: {
            "nome": "Centauro",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Médio",
                "Deslocamento: 12 m",
                "Cascos: pode usar os cascos como ataque natural",
                "Investida: após se mover em linha reta, pode atacar com os cascos",
                "Proficiência: uma entre Adestrar Animais, Medicina, Natureza ou Sobrevivência"
            ]
        },

        5: {
            "nome": "Duergar",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Visão no escuro superior",
                "Resiliência Duergar: vantagem contra certas condições e resistência a veneno",
                "Magia Duergar: recebe magias raciais como aumentar/reduzir e invisibilidade"
            ]
        },

        6: {
            "nome": "Duplicante",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Mudança de Forma: pode alterar aparência, voz e detalhes físicos",
                "Instintos Duplicantes: recebe proficiência em duas perícias sociais",
                "Proficiências sugeridas: Enganação, Intuição, Intimidação ou Persuasão"
            ]
        },

        7: {
            "nome": "Eladrin",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Elfo",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Ancestralidade Feérica: vantagem contra encantamento",
                "Transe: descansa meditando",
                "Passo Feérico: teleporte curto com efeito baseado na estação escolhida"
            ]
        },

        8: {
            "nome": "Elfo Astral",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Elfo",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Transe: descansa meditando",
                "Passo Estelar: teleporte curto",
                "Conhecimento Astral: ganha proficiências temporárias após o descanso"
            ]
        },

        9: {
            "nome": "Fada",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Pequeno",
                "Deslocamento: 9 m",
                "Voo: possui deslocamento de voo",
                "Restrição: não pode voar usando armadura média ou pesada",
                "Magia de Fada: recebe magias raciais feéricas"
            ]
        },

        10: {
            "nome": "Firbolg",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Magia Firbolg: recebe magias ligadas à natureza e disfarce",
                "Passo Oculto: pode ficar invisível brevemente",
                "Construção Poderosa: conta como maior para carregar peso",
                "Fala com animais e plantas de forma limitada"
            ]
        },

        11: {
            "nome": "Genasi",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Existem quatro tipos principais: Água, Ar, Fogo e Terra"
            ],
            "subracas": {
                1: ["Genasi da Água", "Nado 9 m", "Respira ar e água", "Resistência a ácido", "Magias ligadas à água"],
                2: ["Genasi do Ar", "Pode prender a respiração indefinidamente", "Resistência a relâmpago", "Magias ligadas ao ar"],
                3: ["Genasi do Fogo", "Visão no escuro", "Resistência a fogo", "Magias ligadas ao fogo"],
                4: ["Genasi da Terra", "Caminha melhor por terreno difícil de terra ou pedra", "Magias ligadas à terra"]
            }
        },

        12: {
            "nome": "Githyanki",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Conhecimento Astral: ganha proficiência temporária após descanso",
                "Resistência Psíquica: resistência a dano psíquico",
                "Magia Githyanki: recebe magias raciais psíquicas"
            ]
        },

        13: {
            "nome": "Githzerai",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Disciplina Mental: vantagem contra encantamento ou medo",
                "Resistência Psíquica: resistência a dano psíquico",
                "Magia Githzerai: recebe magias raciais defensivas/psíquicas"
            ]
        },

        14: {
            "nome": "Goblin",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Pequeno",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Fúria dos Pequenos: causa dano extra contra criaturas maiores",
                "Escapada Ágil: pode desengajar ou esconder-se como ação bônus"
            ]
        },

        15: {
            "nome": "Golias",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Construção Poderosa: conta como maior para carregar peso",
                "Resistência ao Frio: resistência a dano gélido",
                "Resistência de Pedra: pode reduzir dano recebido",
                "Proficiência: Atletismo"
            ]
        },

        16: {
            "nome": "Harengon",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Sentidos Leporinos: proficiência em Percepção",
                "Pé de Lebre: bônus em iniciativa",
                "Salto de Coelho: pode saltar como ação bônus"
            ]
        },

        17: {
            "nome": "Hobgoblin",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Sorte de Muitos: pode receber bônus em falhas dependendo de aliados próximos",
                "Ajuda Feérica: melhora a ação Ajudar como ação bônus"
            ]
        },

        18: {
            "nome": "Kenku",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Recordação Kenku: melhora testes com perícias treinadas",
                "Imitação: pode imitar sons e vozes",
                "Duplicação Especializada: vantagem para copiar escrita ou objetos",
                "Proficiências: duas perícias à escolha"
            ]
        },

        19: {
            "nome": "Kobold",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Pequeno",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Grito Dracônico: pode conceder vantagem contra inimigos próximos",
                "Legado Kobold: escolhe um benefício racial adicional"
            ]
        },

        20: {
            "nome": "Povo-Lagarto",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Nado: 9 m",
                "Mordida: ataque natural",
                "Armadura Natural: proteção baseada na pele resistente",
                "Segurar Fôlego: consegue ficar bastante tempo sem respirar",
                "Mordida Faminta: pode ganhar PV temporários mordendo inimigos",
                "Proficiências: duas entre perícias ligadas a sobrevivência e natureza"
            ]
        },

        21: {
            "nome": "Minotauro",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Chifres: ataque natural",
                "Investida com Chifres: pode atacar após avançar",
                "Empurrão com Chifres: pode empurrar criatura após ataque",
                "Proficiência: uma entre Intimidação ou Persuasão"
            ]
        },

        22: {
            "nome": "Orc",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Disparada Agressiva: aproxima-se rapidamente como ação bônus",
                "Construção Poderosa: conta como maior para carregar peso",
                "Resistência Implacável: pode evitar cair a 0 PV uma vez por descanso longo"
            ]
        },

        23: {
            "nome": "Sátiro",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Feérico",
                "Tamanho: Médio",
                "Deslocamento: 10,5 m",
                "Chifres: ataque natural",
                "Resistência Mágica: vantagem contra magias",
                "Saltos Alegres: melhora saltos",
                "Proficiências: Atuação, Persuasão e um instrumento musical"
            ]
        },

        24: {
            "nome": "Elfo Marinho",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Elfo",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Nado: 9 m",
                "Visão no escuro: 18 m",
                "Respira ar e água",
                "Resistência a dano gélido",
                "Transe: descansa meditando",
                "Comunicação limitada com criaturas aquáticas"
            ]
        },

        25: {
            "nome": "Shadar-kai",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tipo: Elfo",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Resistência a dano necrótico",
                "Transe: descansa meditando",
                "Bênção da Rainha Corvo: teleporte curto com defesa temporária"
            ]
        },

        26: {
            "nome": "Metamorfo",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Transformação: muda parcialmente o corpo e ganha PV temporários",
                "Tipo de transformação define benefícios adicionais"
            ],
            "subracas": {
                1: ["Pele de Besta", "Durante a transformação recebe bônus na CA"],
                2: ["Passo Longo", "Durante a transformação aumenta o deslocamento"],
                3: ["Dente Longo", "Durante a transformação ganha ataque de presas"],
                4: ["Caça Selvagem", "Melhora rastreamento e dificulta vantagem contra você"]
            }
        },

        27: {
            "nome": "Tabaxi",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Escalada: 9 m",
                "Visão no escuro: 18 m",
                "Agilidade Felina: pode aumentar muito o movimento por um turno",
                "Garras: ataque natural",
                "Proficiências: Percepção e Furtividade"
            ]
        },

        28: {
            "nome": "Tortle",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Armadura Natural: possui proteção natural alta",
                "Casco Defensivo: pode entrar no casco para aumentar defesa",
                "Garras: ataque natural",
                "Prender Respiração: consegue ficar bastante tempo sem respirar",
                "Proficiência: Sobrevivência"
            ]
        },

        29: {
            "nome": "Tritão",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio",
                "Deslocamento: 9 m",
                "Nado: 9 m",
                "Respira ar e água",
                "Resistência a dano gélido",
                "Magias ligadas a ar e água",
                "Comunicação limitada com criaturas aquáticas"
            ]
        },

        30: {
            "nome": "Yuan-ti",
            "info": [
                "Atributos: +2 em um atributo e +1 em outro, ou +1 em três atributos diferentes",
                "Tamanho: Médio ou Pequeno",
                "Deslocamento: 9 m",
                "Visão no escuro: 18 m",
                "Resistência a veneno",
                "Vantagem contra veneno",
                "Resistência Mágica: vantagem contra magias",
                "Magia Serpentina: recebe magias raciais"
            ]
        }
    }
    return racas

def livro_mostrar_racas_mordenkainen(racas, titulo="RAÇAS MORDENKAINEN"):

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

def livro_lista_mordenkainen(ficha):

    racas = livro_racas_mordenkainen()

    while True:
        sumario = int(input("Aqui voce ira ver a lista das 30 raças do Livro de MORDENKAINEN. Voce deseja (1- Continuar, 2- Voltar): "))

        if sumario == 2:
            break

        livro_mostrar_racas_mordenkainen(racas)

        escolha_sumario = int(input("\nDeseja visualizar alguma raça em especifico? Digite o numero da raça ou 0 para voltar: "))

        if escolha_sumario == 0:
            break

        if escolha_sumario not in racas:
            print("Raça inválida.")
            continue

        livro_mostrar_info_raca(racas[escolha_sumario])

        input("\nPressione Enter para voltar ao sumário...")