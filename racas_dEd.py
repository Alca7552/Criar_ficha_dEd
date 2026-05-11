def escolher_raca_dEd(ficha):

    dEd = int(input("Digite a raça de seu personagem (Use a pagina do livro como resposta, EX: 18 (Anão): "))

    match dEd:

        case 18:
            ficha["raca"] = "Anao"
            ficha["atributo da raça"] = "+2 Con"
            idade_anao = int(input("Qual a idade de seu personagem? (Max +- 350): "))
            if idade_anao > 400:
                print("Anões nao vivem muito mais do que 350 anos")
            else:
                ficha["idade"] = f"{idade_anao}"
            tamanho_anao = float(input("Qual o tamanho do seu personagem? (Max 160): "))
            if tamanho_anao < 100:
                tamanho_anao = tamanho_anao * 100

            if tamanho_anao > 160:
                print("Um anão tem por volta de 1,20 até 1,50 metros")
            else:
                ficha["tamanho"] = f"{tamanho_anao}"
            peso_anao = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_anao} kg"
            ficha["deslocamento"] = "7,5 m"
            ficha["proficiencias"] = " machados de batalha, machadinhas, martelos leves e martelos de guerra + ferramenta de artesão à sua escolha"
            ficha["especialista"] = "testes de Int(Hist) add 2x bonus de prof. no teste"
            subraca_anao = int(input("Voce deseja qual subRaça para seu personagem? (1- Anões da colina, 2- Anões da montanha, 3- Personalizada): "))
            if subraca_anao == 1:
                ficha["SubRaça"] = "Anões da Colina"
                ficha["atributo da subRaça"] = "Sab +1 e Hp +1"
            elif subraca_anao == 2:
                ficha["SubRaça"] = "Anões da montanha"
                ficha["atributo da subRaça"] = "For +2 e Prof. Armaduras leves"
            else:
                subraca_anao_personalizada = input("Digite qual sera o nome da subRaça personalizada: ")
                subraca_anao_personalizada_atributos = int(input("Digite de qual das subRaças de anoes voce quer os atributos: (1- Anões da Colina, 2- Anões da montanha): "))
                if subraca_anao_personalizada_atributos == 1:
                    ficha["atributo da subRaça"] = "Sab +1 e Hp +1"
                else:
                    ficha["atributo da subRaça"] = "For +2 e Prof. Armaduras leves"
                ficha["SubRaça"] = f"{subraca_anao_personalizada}"
            print(f"Raça escolhida: [{dEd}] Anão")
        case 21:
            ficha["raca"] = "Elfo"
            ficha["atributo da raça"] = "+2 Des"
            idade_elfo = int(input("Qual a idade de seu personagem? (Max +- 750): "))
            if idade_elfo > 800:
                print("Elfos nao vivem muito mais do que 750 anos")
            else:
                ficha["idade"] = f"{idade_elfo}"
            tamanho_elfo = float(input("Qual o tamanho do seu personagem? (Max 180): "))
            if tamanho_elfo < 100:
                tamanho_elfo = tamanho_elfo * 100

            if tamanho_elfo > 180:
                print("Um elfo tem por volta de 1,50 até 1,80 metros")
            else:
                ficha["tamanho"] = f"{tamanho_elfo}"
            peso_elfo = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_elfo} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Pericia Percepção"
            ficha["especialista"] = "Vantagem em testes de resistencia a ser enfeitiçado por magias e nao pode ser colocado para dormir"
            subraca_elfo = int(input("Voce deseja qual subRaça para seu personagem? (1- Altos elfos, 2- Elfos da floresta, 3- Elfos negros, 4- Personalizada): "))
            if subraca_elfo == 1:
                ficha["SubRaça"] = "Altos elfos"
                ficha["atributo da subRaça"] = "Int +1 e proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos"
                ficha["truque"] = "um truque à sua escolha, da lista de truques do mago. Inteligência é a habilidade usado para conjurar este truque"
            elif subraca_elfo == 2:
                ficha["SubRaça"] = "Elfos da floresta"
                ficha["atributo da subRaça"] = "Sab +1 e Você possui proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos"
                ficha["deslocamento"] = "10,5 m"
            elif subraca_elfo == 3:
                ficha["SubRaça"] = "Elfos negros"
                ficha["atributo da subRaça"] = "Car +1 e Você possui proficiência com rapieiras, espadas curtas e bestas de mão"
                ficha["desvantagem"] = "Sensibilidade a luz Solar"
                ficha["Magia drow"] = "Você possui o truque globos de luz. Quando você alcança o 3° nível, você pode conjurar a magia fogo das fadas. Quando você alcança o 5° nível, você pode conjurar escuridão. Você precisa terminar um descanso longo para poder conjurar as magias desse traço novamente. Carisma é sua habilidade chave para conjurar essas magias"
            else:
                subraca_elfo_personalizada = input("Digite qual sera o nome da subRaça personalizada: ")
                subraca_elfo_personalizada_atributos = int(input("Digite de qual das subRaças de anoes voce quer os atributos: (1- Altos elfos, 2- Elfos da floresta, 3- Elfos negros): "))
                if subraca_elfo_personalizada_atributos == 1:
                    ficha["atributo da subRaça"] = "Int +1 e proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos"
                    ficha["truque"] = "um truque à sua escolha, da lista de truques do mago. Inteligência é a habilidade usado para conjurar este truque"
                elif subraca_elfo_personalizada_atributos == 2:
                    ficha["atributo da subRaça"] = "Sab +1 e Você possui proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos"
                    ficha["deslocamento"] = "10,5 m"
                else:
                    ficha["atributo da subRaça"] = "Car +1 e Você possui proficiência com rapieiras, espadas curtas e bestas de mão"
                    ficha["desvantagem"] = "Sensibilidade a luz Solar"
                    ficha["Magia drow"] = "Você possui o truque globos de luz. Quando você alcança o 3° nível, você pode conjurar a magia fogo das fadas. Quando você alcança o 5° nível, você pode conjurar escuridão. Você precisa terminar um descanso longo para poder conjurar as magias desse traço novamente. Carisma é sua habilidade chave para conjurar essas magias"
                ficha["SubRaça"] = f"{subraca_elfo_personalizada}"
            print(f"Raça escolhida: [{dEd}] Elfo")
        case 26:
            ficha["raca"] = "Halfling"
            ficha["atributo da raça"] = "+2 Des"
            idade_halfling = int(input("Qual a idade de seu personagem? (Max +- 150): "))
            if idade_halfling > 180:
                print("Halflings raramente vivem muito mais do que 150 anos")
            else:
                ficha["idade"] = f"{idade_halfling}"
            tamanho_halfling = float(input("Qual o tamanho do seu personagem? (Max 100): "))
            if tamanho_halfling < 100:
                tamanho_halfling = tamanho_halfling * 100
            if tamanho_halfling > 100:
                print("Um halfling tem por volta de 90 centimetros")
            else:
                ficha["tamanho"] = f"{tamanho_halfling}"
            peso_halfling = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_halfling} kg"
            ficha["deslocamento"] = "7,5 m"
            ficha["proficiencias"] = "Nenhuma proficiência racial obrigatória"
            ficha["especialista"] = "Quando tirar 1 em um d20 para ataque, teste ou resistencia, pode rolar novamente e usar o novo resultado"
            subraca_halfling = int(input("Voce deseja qual subRaça para seu personagem? (1- Pés-leves, 2- Robustos, 3- Personalizada): "))
            if subraca_halfling == 1:
                ficha["SubRaça"] = "Pés-leves"
                ficha["atributo da subRaça"] = "Car +1 e pode tentar se esconder atras de criaturas maiores"
            elif subraca_halfling == 2:
                ficha["SubRaça"] = "Robustos"
                ficha["atributo da subRaça"] = "Con +1 e vantagem contra veneno"
            else:
                subraca_halfling_personalizada = input("Digite qual sera o nome da subRaça personalizada: ")
                subraca_halfling_personalizada_atributos = int(input("Digite de qual das subRaças de halfling voce quer os atributos: (1- Pés-leves, 2- Robustos): "))
                if subraca_halfling_personalizada_atributos == 1:
                    ficha["atributo da subRaça"] = "Car +1 e pode tentar se esconder atras de criaturas maiores"
                else:
                    ficha["atributo da subRaça"] = "Con +1 e vantagem contra veneno"
                ficha["SubRaça"] = f"{subraca_halfling_personalizada}"
            print(f"Raça escolhida: [{dEd}] Halfling")

        case 29:
            ficha["raca"] = "Humano"
            ficha["atributo da raça"] = "+1 em todos os atributos"
            idade_humano = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_humano}"
            tamanho_humano = float(input("Qual o tamanho do seu personagem? (Max 200): "))
            if tamanho_humano < 100:
                tamanho_humano = tamanho_humano * 100
            ficha["tamanho"] = f"{tamanho_humano}"
            peso_humano = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_humano} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Nenhuma proficiência racial obrigatória"
            ficha["especialista"] = "Humanos sao versateis e recebem +1 em todos os atributos"
            print(f"Raça escolhida: [{dEd}] Humano")

        case 32:
            ficha["raca"] = "Draconato"
            ficha["atributo da raça"] = "+2 For e +1 Car"
            idade_draconato = int(input("Qual a idade de seu personagem? (Max +- 80): "))
            ficha["idade"] = f"{idade_draconato}"
            tamanho_draconato = float(input("Qual o tamanho do seu personagem? (Max 210): "))
            if tamanho_draconato < 100:
                tamanho_draconato = tamanho_draconato * 100
            ficha["tamanho"] = f"{tamanho_draconato}"
            peso_draconato = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_draconato} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Nenhuma proficiência racial obrigatória"
            ficha["ancestralidade draconica"] = input("Escolha a ancestralidade draconica do personagem: ")
            ficha["especialista"] = "Possui arma de sopro e resistencia ao tipo de dano da ancestralidade draconica"
            print(f"Raça escolhida: [{dEd}] Draconato")

        case 35:
            ficha["raca"] = "Gnomo"
            ficha["atributo da raça"] = "+2 Int"
            idade_gnomo = int(input("Qual a idade de seu personagem? (Max +- 500): "))
            ficha["idade"] = f"{idade_gnomo}"
            tamanho_gnomo = float(input("Qual o tamanho do seu personagem? (Max 120): "))
            if tamanho_gnomo < 100:
                tamanho_gnomo = tamanho_gnomo * 100
            ficha["tamanho"] = f"{tamanho_gnomo}"
            peso_gnomo = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_gnomo} kg"
            ficha["deslocamento"] = "7,5 m"
            ficha["proficiencias"] = "Nenhuma proficiência racial obrigatória"
            ficha["especialista"] = "Vantagem em testes de resistencia de Int, Sab e Car contra magia"
            subraca_gnomo = int(input("Voce deseja qual subRaça para seu personagem? (1- Gnomo da floresta, 2- Gnomo das rochas, 3- Personalizada): "))
            if subraca_gnomo == 1:
                ficha["SubRaça"] = "Gnomo da floresta"
                ficha["atributo da subRaça"] = "Des +1 e conhece o truque ilusao menor"
            elif subraca_gnomo == 2:
                ficha["SubRaça"] = "Gnomo das rochas"
                ficha["atributo da subRaça"] = "Con +1 e proficiência dobrada em testes de historia ligados a itens magicos, alquimicos ou tecnologicos"
            else:
                subraca_gnomo_personalizada = input("Digite qual sera o nome da subRaça personalizada: ")
                subraca_gnomo_personalizada_atributos = int(input("Digite de qual das subRaças de gnomo voce quer os atributos: (1- Gnomo da floresta, 2- Gnomo das rochas): "))
                if subraca_gnomo_personalizada_atributos == 1:
                    ficha["atributo da subRaça"] = "Des +1 e conhece o truque ilusao menor"
                else:
                    ficha["atributo da subRaça"] = "Con +1 e proficiência dobrada em testes de historia ligados a itens magicos, alquimicos ou tecnologicos"
                ficha["SubRaça"] = f"{subraca_gnomo_personalizada}"
            print(f"Raça escolhida: [{dEd}] Gnomo")

        case 38:
            ficha["raca"] = "Meio-Elfo"
            ficha["atributo da raça"] = "+2 Car e +1 em dois atributos à escolha"
            idade_meio_elfo = int(input("Qual a idade de seu personagem? (Max +- 180): "))
            ficha["idade"] = f"{idade_meio_elfo}"
            tamanho_meio_elfo = float(input("Qual o tamanho do seu personagem? (Max 190): "))
            if tamanho_meio_elfo < 100:
                tamanho_meio_elfo = tamanho_meio_elfo * 100
            ficha["tamanho"] = f"{tamanho_meio_elfo}"
            peso_meio_elfo = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_meio_elfo} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Duas perícias à sua escolha"
            ficha["especialista"] = "Vantagem contra ser enfeitiçado por magia e nao pode ser colocado para dormir magicamente"
            print(f"Raça escolhida: [{dEd}] Meio-Elfo")

        case 40:
            ficha["raca"] = "Meio-Orc"
            ficha["atributo da raça"] = "+2 For e +1 Con"
            idade_meio_orc = int(input("Qual a idade de seu personagem? (Max +- 75): "))
            ficha["idade"] = f"{idade_meio_orc}"
            tamanho_meio_orc = float(input("Qual o tamanho do seu personagem? (Max 210): "))
            if tamanho_meio_orc < 100:
                tamanho_meio_orc = tamanho_meio_orc * 100
            ficha["tamanho"] = f"{tamanho_meio_orc}"
            peso_meio_orc = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_meio_orc} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Pericia Intimidação"
            ficha["especialista"] = "Quando cair a 0 PV, pode cair a 1 PV uma vez antes de precisar de descanso longo"
            ficha["critico"] = "Ao causar acerto critico com ataque corpo a corpo, adiciona um dado extra de dano da arma"
            print(f"Raça escolhida: [{dEd}] Meio-Orc")

        case 42:
            ficha["raca"] = "Tiefling"
            ficha["atributo da raça"] = "+2 Car e +1 Int"
            idade_tiefling = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_tiefling}"
            tamanho_tiefling = float(input("Qual o tamanho do seu personagem? (Max 190): "))
            if tamanho_tiefling < 100:
                tamanho_tiefling = tamanho_tiefling * 100
            ficha["tamanho"] = f"{tamanho_tiefling}"
            peso_tiefling = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_tiefling} kg"
            ficha["deslocamento"] = "9 m"
            ficha["proficiencias"] = "Nenhuma proficiência racial obrigatória"
            ficha["especialista"] = "Resistencia a dano de fogo"
            ficha["magia infernal"] = "Conhece taumaturgia. Em niveis maiores ganha acesso a repreensao infernal e escuridao usando Carisma"
            print(f"Raça escolhida: [{dEd}] Tiefling")