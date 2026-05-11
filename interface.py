import json
import os
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

#Eu ainda nao sei direito mexer com o tkinter e tal, entao esse codigo foi feito por ia e eu vou utiliza-lo para aprender sobre tkinter
#ah mas por que entao voce ta upando no git?
#nao tem um motivo especifico n, é mais para deixar salvo e ir dando commit conforme eu vou aprendendo sobre, tambem para melhor compartilhaçao com meu amiguinhos c:
#Mas o resto foi feito por mim, no caso os outros arquivos, apenas esse interface foi feito por ia

PASTA_FICHAS = "fichas"

RACAS_DND = {
    "Anão": {
        "atributo da raça": "+2 Con",
        "deslocamento": "7,5 m",
        "proficiencias": "Machados de batalha, machadinhas, martelos leves e martelos de guerra + ferramenta de artesão à sua escolha",
        "especialista": "Testes de Int(Hist) adicionam 2x bônus de proficiência no teste",
        "subracas": {
            "Anões da Colina": "Sab +1 e HP +1",
            "Anões da Montanha": "For +2 e Prof. Armaduras leves"
        }
    },
    "Elfo": {
        "atributo da raça": "+2 Des",
        "deslocamento": "9 m",
        "proficiencias": "Perícia Percepção",
        "especialista": "Vantagem em testes de resistência contra ser enfeitiçado por magia e não pode ser colocado para dormir magicamente",
        "subracas": {
            "Altos Elfos": "Int +1 e proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos",
            "Elfos da Floresta": "Sab +1, proficiência com espadas longas, espadas curtas, arcos longos e arcos curtos, deslocamento 10,5 m",
            "Elfos Negros": "Car +1, proficiência com rapieiras, espadas curtas e bestas de mão, Sensibilidade à Luz Solar e Magia Drow"
        }
    },
    "Halfling": {
        "atributo da raça": "+2 Des",
        "deslocamento": "7,5 m",
        "proficiencias": "Nenhuma proficiência racial obrigatória",
        "especialista": "Quando tirar 1 em um d20 para ataque, teste ou resistência, pode rolar novamente e usar o novo resultado",
        "subracas": {
            "Pés-leves": "Car +1 e pode tentar se esconder atrás de criaturas maiores",
            "Robustos": "Con +1 e vantagem contra veneno"
        }
    },
    "Humano": {
        "atributo da raça": "+1 em todos os atributos",
        "deslocamento": "9 m",
        "proficiencias": "Nenhuma proficiência racial obrigatória",
        "especialista": "Humanos são versáteis e recebem +1 em todos os atributos",
        "subracas": {}
    },
    "Draconato": {
        "atributo da raça": "+2 For e +1 Car",
        "deslocamento": "9 m",
        "proficiencias": "Nenhuma proficiência racial obrigatória",
        "especialista": "Possui arma de sopro e resistência ao tipo de dano da ancestralidade dracônica",
        "subracas": {}
    },
    "Gnomo": {
        "atributo da raça": "+2 Int",
        "deslocamento": "7,5 m",
        "proficiencias": "Nenhuma proficiência racial obrigatória",
        "especialista": "Vantagem em testes de resistência de Int, Sab e Car contra magia",
        "subracas": {
            "Gnomo da Floresta": "Des +1 e conhece o truque Ilusão Menor",
            "Gnomo das Rochas": "Con +1 e proficiência dobrada em testes de história ligados a itens mágicos, alquímicos ou tecnológicos"
        }
    },
    "Meio-Elfo": {
        "atributo da raça": "+2 Car e +1 em dois atributos à escolha",
        "deslocamento": "9 m",
        "proficiencias": "Duas perícias à sua escolha",
        "especialista": "Vantagem contra ser enfeitiçado por magia e não pode ser colocado para dormir magicamente",
        "subracas": {}
    },
    "Meio-Orc": {
        "atributo da raça": "+2 For e +1 Con",
        "deslocamento": "9 m",
        "proficiencias": "Perícia Intimidação",
        "especialista": "Quando cair a 0 PV, pode cair a 1 PV uma vez antes de precisar de descanso longo",
        "critico": "Ao causar acerto crítico com ataque corpo a corpo, adiciona um dado extra de dano da arma",
        "subracas": {}
    },
    "Tiefling": {
        "atributo da raça": "+2 Car e +1 Int",
        "deslocamento": "9 m",
        "proficiencias": "Nenhuma proficiência racial obrigatória",
        "especialista": "Resistência a dano de fogo",
        "magia infernal": "Conhece Taumaturgia. Em níveis maiores ganha acesso a Repreensão Infernal e Escuridão usando Carisma",
        "subracas": {}
    }
}

RACAS_MORDENKAINEN = {
    "Aarakocra": {"extra": "Voo igual ao deslocamento de caminhada, mas não pode usar armadura média ou pesada. Garras 1d6 + For."},
    "Aasimar": {"extra": "Resistência a dano radiante e necrótico, mãos curativas e revelação celestial."},
    "Bugurso": {"extra": "Alcance maior em ataques corpo a corpo no seu turno, furtividade natural e dano extra contra alvo surpreso."},
    "Centauro": {"extra": "Tipo feérico, cascos como ataque natural e investida.", "deslocamento": "12 m"},
    "Duergar": {"extra": "Visão no escuro superior, resistência contra veneno, vantagem contra encantamento/atordoamento e magia duergar."},
    "Duplicante": {"extra": "Pode mudar aparência, voz e forma corporal.", "proficiencias": "Duas entre Enganação, Intuição, Intimidação e Persuasão"},
    "Eladrin": {"extra": "Ancestralidade feérica, transe e passo feérico ligado a estações."},
    "Fada": {"extra": "Tipo feérico, voo e magia de fada."},
    "Firbolg": {"extra": "Magia firbolg, passo oculto, fala com animais e plantas e corpo poderoso."},
    "Genasi da Água": {"extra": "Respira ar e água, resistência a ácido e magias de água.", "nado": "9 m"},
    "Genasi do Ar": {"extra": "Pode prender a respiração indefinidamente e possui magias de ar."},
    "Genasi do Fogo": {"extra": "Visão no escuro, resistência a fogo e magias de fogo."},
    "Genasi da Terra": {"extra": "Caminha por terreno difícil de terra/pedra com facilidade e possui magias de terra."},
    "Githyanki": {"extra": "Conhecimento astral, resistência psíquica e magias githyanki."},
    "Githzerai": {"extra": "Disciplina mental, resistência psíquica e magias githzerai."},
    "Goblin": {"extra": "Tipo feérico, fúria dos pequenos, pode esconder-se ou desengajar como ação bônus."},
    "Golias": {"extra": "Corpo poderoso, resistência ao frio e pode reduzir dano recebido com resistência de pedra.", "proficiencias": "Atletismo"},
    "Harengon": {"extra": "Tipo feérico, bônus em iniciativa, salto de coelho e sentidos leporinos.", "proficiencias": "Percepção"},
    "Hobgoblin": {"extra": "Tipo feérico, sorte de muitos e ajuda como ação bônus com benefícios extras."},
    "Kenku": {"extra": "Recordação kenku, imitação de sons e vantagem para duplicar escrita ou objetos.", "proficiencias": "Duas perícias à sua escolha"},
    "Kobold": {"extra": "Grito dracônico e legado kobold."},
    "Povo-Lagarto": {"extra": "Mordida natural, armadura natural, segurar fôlego e mordida faminta.", "nado": "9 m"},
    "Minotauro": {"extra": "Chifres como arma natural, investida com chifres e empurrão com chifres."},
    "Orc": {"extra": "Disparada agressiva, corpo poderoso e resistência implacável."},
    "Sátiro": {"extra": "Tipo feérico, resistência mágica, saltos alegres e chifres como arma natural.", "deslocamento": "10,5 m"},
    "Elfo Marinho": {"extra": "Respira ar e água, resistência a dano gélido, transe e comunicação limitada com feras aquáticas.", "nado": "9 m"},
    "Shadar-kai": {"extra": "Ancestralidade feérica, transe, resistência necrótica e bênção da Rainha Corvo."},
    "Metamorfo": {"extra": "Pode transformar parcialmente o corpo, ganhando PV temporários e benefícios conforme o tipo."},
    "Tabaxi": {"extra": "Agilidade felina, garras como arma natural e sentidos felinos.", "escalada": "9 m", "proficiencias": "Percepção e Furtividade"},
    "Tortle": {"extra": "Armadura natural, casco defensivo, garras e prender respiração.", "proficiencias": "Sobrevivência"},
    "Tritão": {"extra": "Respira ar e água, resistência a dano gélido e magias de controle do ar e água.", "nado": "9 m"},
    "Yuan-ti": {"extra": "Resistência a veneno, vantagem contra veneno, visão no escuro e magia serpentina."}
}

class App:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Criador de Fichas RPG")
        self.janela.geometry("850x620")
        self.janela.minsize(760, 560)
        self.ficha = {}
        self.arquivo_aberto = None

        self.cor_fundo = "#1f1f2e"
        self.cor_card = "#2d2d44"
        self.cor_texto = "#f2f2f2"
        self.cor_botao = "#6c63ff"
        self.cor_botao_escuro = "#4d47c3"

        self.janela.configure(bg=self.cor_fundo)
        self.tela_menu()

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def card(self):
        frame = tk.Frame(self.janela, bg=self.cor_card, padx=30, pady=25)
        frame.pack(expand=True, fill="both", padx=35, pady=35)
        return frame

    def titulo(self, frame, texto):
        tk.Label(frame, text=texto, bg=self.cor_card, fg=self.cor_texto, font=("Arial", 24, "bold")).pack(pady=(0, 20))

    def subtitulo(self, frame, texto):
        tk.Label(frame, text=texto, bg=self.cor_card, fg="#ccccdd", font=("Arial", 12)).pack(pady=(0, 20))

    def botao(self, frame, texto, comando):
        tk.Button(
            frame,
            text=texto,
            command=comando,
            bg=self.cor_botao,
            fg="white",
            activebackground=self.cor_botao_escuro,
            activeforeground="white",
            relief="flat",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(pady=8, fill="x")

    def entrada(self, frame, texto):
        tk.Label(frame, text=texto, bg=self.cor_card, fg=self.cor_texto, font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 3))
        campo = tk.Entry(frame, font=("Arial", 12), relief="flat")
        campo.pack(fill="x", ipady=7)
        return campo

    def tela_menu(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Criador de Fichas RPG")
        self.subtitulo(frame, "Sistema de criação, salvamento, abertura e edição de fichas em JSON")
        self.botao(frame, "Criar nova ficha", self.tela_nome)
        self.botao(frame, "Gerenciar fichas", self.tela_gerenciar)
        self.botao(frame, "Sair", self.janela.destroy)

    def tela_nome(self):
        self.limpar_tela()
        self.ficha = {}
        frame = self.card()
        self.titulo(frame, "Nova ficha")
        nome = self.entrada(frame, "Nome do personagem")

        def continuar():
            if nome.get().strip() == "":
                messagebox.showwarning("Aviso", "Digite um nome para o personagem.")
                return
            self.ficha["nome"] = nome.get().strip()
            self.tela_livro()

        self.botao(frame, "Continuar", continuar)
        self.botao(frame, "Voltar", self.tela_menu)

    def tela_livro(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Escolha o livro")

        def dnd():
            self.ficha["livro"] = "D&D Livro do Jogador"
            self.tela_escolher_raca("dnd")

        def mordenkainen():
            self.ficha["livro"] = "Mordenkainen"
            self.tela_escolher_raca("mordenkainen")

        self.botao(frame, "D&D Livro do Jogador", dnd)
        self.botao(frame, "Mordenkainen", mordenkainen)
        self.botao(frame, "Voltar", self.tela_nome)

    def tela_escolher_raca(self, tipo):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Escolha a raça")

        lista_frame = tk.Frame(frame, bg=self.cor_card)
        lista_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(lista_frame, bg=self.cor_card, highlightthickness=0)
        scrollbar = tk.Scrollbar(lista_frame, orient="vertical", command=canvas.yview)
        conteudo = tk.Frame(canvas, bg=self.cor_card)

        conteudo.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=conteudo, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        racas = RACAS_DND if tipo == "dnd" else RACAS_MORDENKAINEN

        for nome_raca, dados in racas.items():
            def escolher(raca=nome_raca, info=dados):
                self.ficha["raca"] = raca
                self.ficha["atributo da raça"] = info.get("atributo da raça", "+2 em um atributo e +1 em outro, ou +1 em tres atributos diferentes")
                self.ficha["deslocamento"] = info.get("deslocamento", "9 m")

                if "proficiencias" in info:
                    self.ficha["proficiencias"] = info["proficiencias"]
                if "especialista" in info:
                    self.ficha["especialista"] = info["especialista"]
                if "critico" in info:
                    self.ficha["critico"] = info["critico"]
                if "magia infernal" in info:
                    self.ficha["magia infernal"] = info["magia infernal"]
                if "extra" in info:
                    self.ficha["especialista"] = info["extra"]
                if "nado" in info:
                    self.ficha["nado"] = info["nado"]
                if "escalada" in info:
                    self.ficha["escalada"] = info["escalada"]

                if tipo == "dnd" and info.get("subracas"):
                    self.tela_subraca(info["subracas"])
                else:
                    self.tela_dados_fisicos()

            tk.Button(
                conteudo,
                text=nome_raca,
                command=escolher,
                bg="#3b3b5c",
                fg="white",
                activebackground=self.cor_botao,
                activeforeground="white",
                relief="flat",
                font=("Arial", 11, "bold"),
                padx=12,
                pady=8,
                cursor="hand2"
            ).pack(fill="x", pady=4)

        self.botao(frame, "Voltar", self.tela_livro)

    def tela_subraca(self, subracas):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Escolha a sub-raça")

        for nome_subraca, atributo in subracas.items():
            def escolher(sub=nome_subraca, atr=atributo):
                self.ficha["SubRaça"] = sub
                self.ficha["atributo da subRaça"] = atr
                self.tela_dados_fisicos()

            self.botao(frame, nome_subraca, escolher)

        self.botao(frame, "Sub-raça personalizada", self.tela_subraca_personalizada)
        self.botao(frame, "Voltar", self.tela_livro)

    def tela_subraca_personalizada(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Sub-raça personalizada")
        nome = self.entrada(frame, "Nome da sub-raça personalizada")
        atributo = self.entrada(frame, "Atributos/efeitos da sub-raça")

        def continuar():
            self.ficha["SubRaça"] = nome.get().strip()
            self.ficha["atributo da subRaça"] = atributo.get().strip()
            self.tela_dados_fisicos()

        self.botao(frame, "Continuar", continuar)

    def tela_dados_fisicos(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Dados físicos")

        idade = self.entrada(frame, "Idade")
        tamanho = self.entrada(frame, "Tamanho em cm ou metros. Ex: 175 ou 1.75")
        peso = self.entrada(frame, "Peso em kg")

        def continuar():
            if idade.get().strip() == "" or tamanho.get().strip() == "" or peso.get().strip() == "":
                messagebox.showwarning("Aviso", "Preencha idade, tamanho e peso.")
                return

            self.ficha["idade"] = idade.get().strip()
            self.ficha["tamanho"] = tamanho.get().strip()
            self.ficha["peso"] = peso.get().strip() + " kg"
            self.tela_confirmar()

        self.botao(frame, "Continuar", continuar)
        self.botao(frame, "Voltar", self.tela_livro)

    def tela_confirmar(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Confirmar ficha")

        texto = tk.Text(frame, height=18, bg="#202033", fg="white", font=("Consolas", 11), relief="flat")
        texto.pack(fill="both", expand=True)

        for chave, valor in self.ficha.items():
            texto.insert("end", f"{chave:<25}: {valor}\n")

        texto.configure(state="disabled")

        self.botao(frame, "Salvar ficha", self.salvar_ficha)
        self.botao(frame, "Voltar ao menu", self.tela_menu)

    def salvar_ficha(self):
        if not os.path.exists(PASTA_FICHAS):
            os.mkdir(PASTA_FICHAS)

        nome_base = self.ficha.get("nome", "ficha").replace(" ", "_").lower()
        nome_arquivo = simpledialog.askstring("Salvar ficha", "Nome do arquivo:", initialvalue=nome_base)

        if not nome_arquivo:
            return

        caminho = os.path.join(PASTA_FICHAS, nome_arquivo + ".json")

        if os.path.exists(caminho):
            confirmar = messagebox.askyesno("Arquivo existente", "Esse arquivo já existe. Deseja substituir?")
            if not confirmar:
                return

        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self.ficha, arquivo, ensure_ascii=False, indent=4)

        messagebox.showinfo("Sucesso", "Ficha salva com sucesso!")
        self.tela_menu()

    def tela_gerenciar(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Gerenciar fichas")

        if not os.path.exists(PASTA_FICHAS):
            os.mkdir(PASTA_FICHAS)

        arquivos = [a for a in os.listdir(PASTA_FICHAS) if a.endswith(".json")]

        if not arquivos:
            self.subtitulo(frame, "Nenhuma ficha encontrada.")
            self.botao(frame, "Voltar", self.tela_menu)
            return

        lista = tk.Listbox(frame, font=("Arial", 12), bg="#202033", fg="white", selectbackground=self.cor_botao, relief="flat")
        lista.pack(fill="both", expand=True, pady=10)

        for arquivo in arquivos:
            lista.insert("end", arquivo)

        def abrir():
            selecao = lista.curselection()
            if not selecao:
                messagebox.showwarning("Aviso", "Escolha uma ficha para abrir.")
                return
            arquivo = arquivos[selecao[0]]
            self.abrir_ficha(arquivo)

        def excluir():
            selecao = lista.curselection()
            if not selecao:
                messagebox.showwarning("Aviso", "Escolha uma ficha para excluir.")
                return
            arquivo = arquivos[selecao[0]]
            confirmar = messagebox.askyesno("Excluir", f"Deseja excluir {arquivo}?")
            if confirmar:
                os.remove(os.path.join(PASTA_FICHAS, arquivo))
                self.tela_gerenciar()

        self.botao(frame, "Abrir ficha", abrir)
        self.botao(frame, "Excluir ficha", excluir)
        self.botao(frame, "Voltar", self.tela_menu)

    def abrir_ficha(self, arquivo):
        caminho = os.path.join(PASTA_FICHAS, arquivo)

        with open(caminho, "r", encoding="utf-8") as f:
            self.ficha = json.load(f)

        self.arquivo_aberto = caminho
        self.tela_visualizar_ficha()

    def tela_visualizar_ficha(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Ficha aberta")

        texto = tk.Text(frame, height=18, bg="#202033", fg="white", font=("Consolas", 11), relief="flat")
        texto.pack(fill="both", expand=True)

        for chave, valor in self.ficha.items():
            texto.insert("end", f"{chave:<25}: {valor}\n")

        texto.configure(state="disabled")

        self.botao(frame, "Editar ficha", self.tela_editar_ficha)
        self.botao(frame, "Voltar", self.tela_gerenciar)

    def tela_editar_ficha(self):
        self.limpar_tela()
        frame = self.card()
        self.titulo(frame, "Editar ficha")

        campos = {}
        canvas = tk.Canvas(frame, bg=self.cor_card, highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        conteudo = tk.Frame(canvas, bg=self.cor_card)

        conteudo.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=conteudo, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for chave, valor in self.ficha.items():
            tk.Label(conteudo, text=chave, bg=self.cor_card, fg=self.cor_texto, font=("Arial", 10, "bold")).pack(anchor="w", pady=(8, 2))
            entrada = tk.Entry(conteudo, font=("Arial", 11), relief="flat")
            entrada.insert(0, str(valor))
            entrada.pack(fill="x", ipady=5)
            campos[chave] = entrada

        def salvar_edicao():
            for chave, entrada in campos.items():
                self.ficha[chave] = entrada.get()

            with open(self.arquivo_aberto, "w", encoding="utf-8") as arquivo:
                json.dump(self.ficha, arquivo, ensure_ascii=False, indent=4)

            messagebox.showinfo("Sucesso", "Ficha editada com sucesso!")
            self.tela_visualizar_ficha()

        tk.Button(
            conteudo,
            text="Salvar alterações",
            command=salvar_edicao,
            bg=self.cor_botao,
            fg="white",
            relief="flat",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(fill="x", pady=15)

        tk.Button(
            conteudo,
            text="Voltar",
            command=self.tela_visualizar_ficha,
            bg="#3b3b5c",
            fg="white",
            relief="flat",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(fill="x", pady=5)


if __name__ == "__main__":
    janela = tk.Tk()
    app = App(janela)
    janela.mainloop()
