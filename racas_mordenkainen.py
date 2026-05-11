from livromordekainen import livro_mostrar_racas_mordenkainen, livro_racas_mordenkainen

def escolher_raca_mordenkainen(ficha):

    racas = livro_racas_mordenkainen()

    livro_mostrar_racas_mordenkainen(racas)

    mordenkainen = int(input("Digite a raça de seu personagem (Use a pagina do livro como resposta, EX: 6 (Aarakocra): "))

    match mordenkainen:

        case 1:
            ficha["raca"] = "Aarakocra"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_aarakocra = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_aarakocra}"
            tamanho_aarakocra = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_aarakocra < 100:
                tamanho_aarakocra = tamanho_aarakocra * 100
            ficha["tamanho"] = f"{tamanho_aarakocra}"
            peso_aarakocra = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_aarakocra} kg"
            ficha["deslocamento"] = "9 m"
            ficha["voo"] = "Deslocamento de voo igual ao deslocamento de caminhada, mas nao pode usar armadura media ou pesada"
            ficha["especialista"] = "Garras causam 1d6 + For de dano cortante e pode conjurar lufada de vento a partir do nivel 3"
            print(f"Raça escolhida: [{mordenkainen}] Aarakocra")

        case 2:
            ficha["raca"] = "Aasimar"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_aasimar = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_aasimar}"
            tamanho_aasimar = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_aasimar < 100:
                tamanho_aasimar = tamanho_aasimar * 100
            ficha["tamanho"] = f"{tamanho_aasimar}"
            peso_aasimar = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_aasimar} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Resistencia a dano radiante e necrotico, maos curativas e revelacao celestial"
            print(f"Raça escolhida: [{mordenkainen}] Aasimar")

        case 3:
            ficha["raca"] = "Bugurso"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_bugurso = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_bugurso}"
            tamanho_bugurso = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_bugurso < 100:
                tamanho_bugurso = tamanho_bugurso * 100
            ficha["tamanho"] = f"{tamanho_bugurso}"
            peso_bugurso = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_bugurso} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Alcance maior em ataques corpo a corpo no seu turno, furtividade natural e dano extra contra alvo surpreso"
            print(f"Raça escolhida: [{mordenkainen}] Bugurso")

        case 4:
            ficha["raca"] = "Centauro"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_centauro = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_centauro}"
            tamanho_centauro = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_centauro < 100:
                tamanho_centauro = tamanho_centauro * 100
            ficha["tamanho"] = f"{tamanho_centauro}"
            peso_centauro = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_centauro} kg"
            ficha["deslocamento"] = "12 m"
            ficha["especialista"] = "Tipo feerico, cascos como ataque natural e investida"
            ficha["proficiencias"] = "Uma entre Adestrar Animais, Medicina, Natureza ou Sobrevivencia"
            print(f"Raça escolhida: [{mordenkainen}] Centauro")

        case 5:
            ficha["raca"] = "Duergar"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_duergar = int(input("Qual a idade de seu personagem? (Max +- 350): "))
            ficha["idade"] = f"{idade_duergar}"
            tamanho_duergar = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_duergar < 100:
                tamanho_duergar = tamanho_duergar * 100
            ficha["tamanho"] = f"{tamanho_duergar}"
            peso_duergar = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_duergar} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Visao no escuro superior, resistencia contra veneno, vantagem contra encantamento/atordoamento e magia duergar"
            print(f"Raça escolhida: [{mordenkainen}] Duergar")

        case 6:
            ficha["raca"] = "Duplicante"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_duplicante = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_duplicante}"
            tamanho_duplicante = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_duplicante < 100:
                tamanho_duplicante = tamanho_duplicante * 100
            ficha["tamanho"] = f"{tamanho_duplicante}"
            peso_duplicante = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_duplicante} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Pode mudar aparencia, voz e forma corporal, mantendo o mesmo tipo basico de corpo"
            ficha["proficiencias"] = "Duas entre Enganação, Intuição, Intimidação e Persuasão"
            print(f"Raça escolhida: [{mordenkainen}] Duplicante")

        case 7:
            ficha["raca"] = "Eladrin"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_eladrin = int(input("Qual a idade de seu personagem? (Max +- 750): "))
            ficha["idade"] = f"{idade_eladrin}"
            tamanho_eladrin = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_eladrin < 100:
                tamanho_eladrin = tamanho_eladrin * 100
            ficha["tamanho"] = f"{tamanho_eladrin}"
            peso_eladrin = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_eladrin} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Ancestralidade feerica, transe e passo feerico ligado a estações"
            print(f"Raça escolhida: [{mordenkainen}] Eladrin")

        case 8:
            ficha["raca"] = "Elfo Marinho"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_elfo_marinho = int(input("Qual a idade de seu personagem? (Max +- 750): "))
            ficha["idade"] = f"{idade_elfo_marinho}"
            tamanho_elfo_marinho = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_elfo_marinho < 100:
                tamanho_elfo_marinho = tamanho_elfo_marinho * 100
            ficha["tamanho"] = f"{tamanho_elfo_marinho}"
            peso_elfo_marinho = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_elfo_marinho} kg"
            ficha["deslocamento"] = "9 m"
            ficha["nado"] = "9 m"
            ficha["especialista"] = "Respira ar e agua, resistencia a dano gelido, transe e comunicação limitada com feras aquaticas"
            print(f"Raça escolhida: [{mordenkainen}] Elfo Marinho")

        case 9:
            ficha["raca"] = "Fada"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_fada = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_fada}"
            tamanho_fada = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_fada < 100:
                tamanho_fada = tamanho_fada * 100
            ficha["tamanho"] = f"{tamanho_fada}"
            peso_fada = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_fada} kg"
            ficha["deslocamento"] = "9 m"
            ficha["voo"] = "Deslocamento de voo igual ao deslocamento de caminhada, mas nao pode usar armadura media ou pesada"
            ficha["especialista"] = "Tipo feerico e magia de fada"
            print(f"Raça escolhida: [{mordenkainen}] Fada")

        case 10:
            ficha["raca"] = "Firbolg"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_firbolg = int(input("Qual a idade de seu personagem? (Max +- 500): "))
            ficha["idade"] = f"{idade_firbolg}"
            tamanho_firbolg = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_firbolg < 100:
                tamanho_firbolg = tamanho_firbolg * 100
            ficha["tamanho"] = f"{tamanho_firbolg}"
            peso_firbolg = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_firbolg} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Magia firbolg, passo oculto, fala com animais e plantas e corpo poderoso"
            print(f"Raça escolhida: [{mordenkainen}] Firbolg")

        case 11:
            ficha["raca"] = "Genasi"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_genasi = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_genasi}"
            tamanho_genasi = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_genasi < 100:
                tamanho_genasi = tamanho_genasi * 100
            ficha["tamanho"] = f"{tamanho_genasi}"
            peso_genasi = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_genasi} kg"
            ficha["deslocamento"] = "9 m"
            subraca_genasi = int(input("Voce deseja qual tipo de Genasi? (1- Agua, 2- Ar, 3- Fogo, 4- Terra): "))
            if subraca_genasi == 1:
                ficha["SubRaça"] = "Genasi da Agua"
                ficha["nado"] = "9 m"
                ficha["especialista"] = "Respira ar e agua, resistencia a acido e magias de agua"
            elif subraca_genasi == 2:
                ficha["SubRaça"] = "Genasi do Ar"
                ficha["especialista"] = "Pode prender a respiração indefinidamente e possui magias de ar"
            elif subraca_genasi == 3:
                ficha["SubRaça"] = "Genasi do Fogo"
                ficha["especialista"] = "Visao no escuro, resistencia a fogo e magias de fogo"
            else:
                ficha["SubRaça"] = "Genasi da Terra"
                ficha["especialista"] = "Caminha por terreno dificil de terra/pedra com facilidade e possui magias de terra"
            print(f"Raça escolhida: [{mordenkainen}] Genasi")

        case 12:
            ficha["raca"] = "Githyanki"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_githyanki = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_githyanki}"
            tamanho_githyanki = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_githyanki < 100:
                tamanho_githyanki = tamanho_githyanki * 100
            ficha["tamanho"] = f"{tamanho_githyanki}"
            peso_githyanki = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_githyanki} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Conhecimento astral, resistencia psionica e magias githyanki"
            print(f"Raça escolhida: [{mordenkainen}] Githyanki")

        case 13:
            ficha["raca"] = "Githzerai"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_githzerai = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_githzerai}"
            tamanho_githzerai = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_githzerai < 100:
                tamanho_githzerai = tamanho_githzerai * 100
            ficha["tamanho"] = f"{tamanho_githzerai}"
            peso_githzerai = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_githzerai} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Disciplina mental, resistencia psiquica e magias githzerai"
            print(f"Raça escolhida: [{mordenkainen}] Githzerai")
        case 14:
            ficha["raca"] = "Goblin"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_goblin = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_goblin}"
            tamanho_goblin = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_goblin < 100:
                tamanho_goblin = tamanho_goblin * 100
            ficha["tamanho"] = f"{tamanho_goblin}"
            peso_goblin = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_goblin} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Tipo feerico, furia dos pequenos, pode esconder-se ou desengajar como ação bonus"
            print(f"Raça escolhida: [{mordenkainen}] Goblin")

        case 15:
            ficha["raca"] = "Golias"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_golias = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_golias}"
            tamanho_golias = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_golias < 100:
                tamanho_golias = tamanho_golias * 100
            ficha["tamanho"] = f"{tamanho_golias}"
            peso_golias = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_golias} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Corpo poderoso, resistencia ao frio e pode reduzir dano recebido com resistencia de pedra"
            ficha["proficiencias"] = "Atletismo"
            print(f"Raça escolhida: [{mordenkainen}] Golias")

        case 16:
            ficha["raca"] = "Harengon"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_harengon = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_harengon}"
            tamanho_harengon = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_harengon < 100:
                tamanho_harengon = tamanho_harengon * 100
            ficha["tamanho"] = f"{tamanho_harengon}"
            peso_harengon = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_harengon} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Tipo feerico, bonus em iniciativa, salto de coelho e sentidos leporinos"
            ficha["proficiencias"] = "Percepção"
            print(f"Raça escolhida: [{mordenkainen}] Harengon")

        case 17:
            ficha["raca"] = "Hobgoblin"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_hobgoblin = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_hobgoblin}"
            tamanho_hobgoblin = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_hobgoblin < 100:
                tamanho_hobgoblin = tamanho_hobgoblin * 100
            ficha["tamanho"] = f"{tamanho_hobgoblin}"
            peso_hobgoblin = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_hobgoblin} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Tipo feerico, sorte de muitos e ajuda como ação bonus com benefícios extras"
            print(f"Raça escolhida: [{mordenkainen}] Hobgoblin")

        case 18:
            ficha["raca"] = "Kenku"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_kenku = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_kenku}"
            tamanho_kenku = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_kenku < 100:
                tamanho_kenku = tamanho_kenku * 100
            ficha["tamanho"] = f"{tamanho_kenku}"
            peso_kenku = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_kenku} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Recordação kenku, imitação de sons e vantagem para duplicar escrita ou objetos"
            ficha["proficiencias"] = "Duas pericias à sua escolha"
            print(f"Raça escolhida: [{mordenkainen}] Kenku")

        case 19:
            ficha["raca"] = "Kobold"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_kobold = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_kobold}"
            tamanho_kobold = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_kobold < 100:
                tamanho_kobold = tamanho_kobold * 100
            ficha["tamanho"] = f"{tamanho_kobold}"
            peso_kobold = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_kobold} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Grito draconico e legado kobold"
            print(f"Raça escolhida: [{mordenkainen}] Kobold")

        case 20:
            ficha["raca"] = "Povo-Lagarto"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_povo_lagarto = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_povo_lagarto}"
            tamanho_povo_lagarto = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_povo_lagarto < 100:
                tamanho_povo_lagarto = tamanho_povo_lagarto * 100
            ficha["tamanho"] = f"{tamanho_povo_lagarto}"
            peso_povo_lagarto = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_povo_lagarto} kg"
            ficha["deslocamento"] = "9 m"
            ficha["nado"] = "9 m"
            ficha["especialista"] = "Mordida natural, armadura natural, segurar folego e mordida faminta"
            ficha["proficiencias"] = "Duas entre Adestrar Animais, Medicina, Natureza, Percepção, Furtividade ou Sobrevivencia"
            print(f"Raça escolhida: [{mordenkainen}] Povo-Lagarto")

        case 21:
            ficha["raca"] = "Minotauro"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_minotauro = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_minotauro}"
            tamanho_minotauro = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_minotauro < 100:
                tamanho_minotauro = tamanho_minotauro * 100
            ficha["tamanho"] = f"{tamanho_minotauro}"
            peso_minotauro = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_minotauro} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Chifres como arma natural, investida com chifres e empurrão com chifres"
            ficha["proficiencias"] = "Uma entre Intimidação ou Persuasão"
            print(f"Raça escolhida: [{mordenkainen}] Minotauro")

        case 22:
            ficha["raca"] = "Orc"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_orc = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_orc}"
            tamanho_orc = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_orc < 100:
                tamanho_orc = tamanho_orc * 100
            ficha["tamanho"] = f"{tamanho_orc}"
            peso_orc = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_orc} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Disparada agressiva, corpo poderoso e resistencia implacavel"
            print(f"Raça escolhida: [{mordenkainen}] Orc")

        case 23:
            ficha["raca"] = "Satiro"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_satiro = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_satiro}"
            tamanho_satiro = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_satiro < 100:
                tamanho_satiro = tamanho_satiro * 100
            ficha["tamanho"] = f"{tamanho_satiro}"
            peso_satiro = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_satiro} kg"
            ficha["deslocamento"] = "10,5 m"
            ficha["especialista"] = "Tipo feerico, resistencia magica, saltos alegres e chifres como arma natural"
            ficha["proficiencias"] = "Atuação e Persuasão, além de um instrumento musical"
            print(f"Raça escolhida: [{mordenkainen}] Satiro")

        case 24:
            ficha["raca"] = "Elfo Marinho"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_elfo_marinho = int(input("Qual a idade de seu personagem? (Max +- 750): "))
            ficha["idade"] = f"{idade_elfo_marinho}"
            tamanho_elfo_marinho = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_elfo_marinho < 100:
                tamanho_elfo_marinho = tamanho_elfo_marinho * 100
            ficha["tamanho"] = f"{tamanho_elfo_marinho}"
            peso_elfo_marinho = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_elfo_marinho} kg"
            ficha["deslocamento"] = "9 m"
            ficha["nado"] = "9 m"
            ficha["especialista"] = "Respira ar e agua, resistencia a dano gelido, transe e comunicação limitada com feras aquaticas"
            print(f"Raça escolhida: [{mordenkainen}] Elfo Marinho")

        case 25:
            ficha["raca"] = "Shadar-kai"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_shadar_kai = int(input("Qual a idade de seu personagem? (Max +- 750): "))
            ficha["idade"] = f"{idade_shadar_kai}"
            tamanho_shadar_kai = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_shadar_kai < 100:
                tamanho_shadar_kai = tamanho_shadar_kai * 100
            ficha["tamanho"] = f"{tamanho_shadar_kai}"
            peso_shadar_kai = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_shadar_kai} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Ancestralidade feerica, transe, resistencia necrotica e benção da rainha corvo"
            print(f"Raça escolhida: [{mordenkainen}] Shadar-kai")

        case 26:
            ficha["raca"] = "Metamorfo"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_metamorfo = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_metamorfo}"
            tamanho_metamorfo = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_metamorfo < 100:
                tamanho_metamorfo = tamanho_metamorfo * 100
            ficha["tamanho"] = f"{tamanho_metamorfo}"
            peso_metamorfo = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_metamorfo} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Pode transformar parcialmente o corpo, ganhando PV temporarios e beneficios conforme o tipo"
            subraca_metamorfo = int(input("Voce deseja qual tipo de Metamorfo? (1- Pele de Besta, 2- Passo Longo, 3- Dente Longo, 4- Caça Selvagem): "))
            if subraca_metamorfo == 1:
                ficha["SubRaça"] = "Pele de Besta"
                ficha["atributo da subRaça"] = "Durante a transformação recebe bonus na CA"
            elif subraca_metamorfo == 2:
                ficha["SubRaça"] = "Passo Longo"
                ficha["atributo da subRaça"] = "Durante a transformação aumenta deslocamento"
            elif subraca_metamorfo == 3:
                ficha["SubRaça"] = "Dente Longo"
                ficha["atributo da subRaça"] = "Durante a transformação ganha ataque de presas"
            else:
                ficha["SubRaça"] = "Caça Selvagem"
                ficha["atributo da subRaça"] = "Durante a transformação melhora rastreamento e evita vantagem contra voce"
            print(f"Raça escolhida: [{mordenkainen}] Metamorfo")

        case 27:
            ficha["raca"] = "Tabaxi"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_tabaxi = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_tabaxi}"
            tamanho_tabaxi = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_tabaxi < 100:
                tamanho_tabaxi = tamanho_tabaxi * 100
            ficha["tamanho"] = f"{tamanho_tabaxi}"
            peso_tabaxi = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_tabaxi} kg"
            ficha["deslocamento"] = "9 m"
            ficha["escalada"] = "9 m"
            ficha["especialista"] = "Agilidade felina, garras como arma natural e sentidos felinos"
            ficha["proficiencias"] = "Percepção e Furtividade"
            print(f"Raça escolhida: [{mordenkainen}] Tabaxi")

        case 28:
            ficha["raca"] = "Tortle"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_tortle = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_tortle}"
            tamanho_tortle = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_tortle < 100:
                tamanho_tortle = tamanho_tortle * 100
            ficha["tamanho"] = f"{tamanho_tortle}"
            peso_tortle = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_tortle} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Armadura natural, casco defensivo, garras e prender respiração"
            ficha["proficiencias"] = "Sobrevivencia"
            print(f"Raça escolhida: [{mordenkainen}] Tortle")

        case 29:
            ficha["raca"] = "Tritao"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_tritao = int(input("Qual a idade de seu personagem? (Max +- 200): "))
            ficha["idade"] = f"{idade_tritao}"
            tamanho_tritao = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_tritao < 100:
                tamanho_tritao = tamanho_tritao * 100
            ficha["tamanho"] = f"{tamanho_tritao}"
            peso_tritao = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_tritao} kg"
            ficha["deslocamento"] = "9 m"
            ficha["nado"] = "9 m"
            ficha["especialista"] = "Respira ar e agua, resistencia a dano gelido e magias de controle do ar e agua"
            print(f"Raça escolhida: [{mordenkainen}] Tritao")

        case 30:
            ficha["raca"] = "Yuan-ti"
            ficha["atributo da raça"] = "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes"
            idade_yuan_ti = int(input("Qual a idade de seu personagem? (Max +- 100): "))
            ficha["idade"] = f"{idade_yuan_ti}"
            tamanho_yuan_ti = float(input("Qual o tamanho do seu personagem?: "))
            if tamanho_yuan_ti < 100:
                tamanho_yuan_ti = tamanho_yuan_ti * 100
            ficha["tamanho"] = f"{tamanho_yuan_ti}"
            peso_yuan_ti = float(input("Qual o peso do seu personagem?: (Coloque em kg e use apenas numeros): "))
            ficha["peso"] = f"{peso_yuan_ti} kg"
            ficha["deslocamento"] = "9 m"
            ficha["especialista"] = "Resistencia a veneno, vantagem contra veneno, visão no escuro e magia serpentina"
            print(f"Raça escolhida: [{mordenkainen}] Yuan-ti")
