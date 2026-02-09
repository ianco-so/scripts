import random

# Dicionário de temas com palavras relacionadas em português
TEMAS = {
    "cafeteria":    ["cafe",    "leite",    "acucar",   "xicara",   "bolo",     "padaria",  "canela",       "grao",     "bule"],
    "praia":        ["sol",     "mar",      "areia",    "onda",     "ferias",   "coqueiro", "concha",       "brisa",    "verao"],
    "espaco":       ["estrela", "planeta",  "galaxia",  "cometa",   "foguete",  "orbita",   "cosmos",       "astro",    "lua"],
    "tecnologia":   ["codigo",  "dados",    "rede",     "nuvem",    "mouse",    "teclado",  "chip",         "pixel",    "sistema"],
    "floresta":     ["arvore",  "folha",    "riacho",   "passaro",  "trilha",   "sombra",   "vento",        "terra",    "raiz"],
    "musica":       ["ritmo",   "melodia",  "som",      "acorde",   "pauta",    "palco",    "instrumento",  "eco",      "nota"]
}

def gerar_senha_tematica(num_palavras=3, incluir_numero=True):
    # Escolhe um tema aleatório
    tema_escolhido = random.choice(list(TEMAS.keys()))
    palavras_tema = TEMAS[tema_escolhido]
    
    # Garante que não vamos pedir mais palavras do que existem no tema
    qtd = min(num_palavras, len(palavras_tema))
    
    # Sorteia as palavras sem repetição
    palavras_sorteadas = random.sample(palavras_tema, qtd)
    
    # Junta as palavras com hífen
    senha = "-".join(palavras_sorteadas)
    
    # Opcional: adiciona um número aleatório ao final para aumentar a segurança
    if incluir_numero:
        numero = random.randint(10, 99)
        senha += f"-{numero}"
        
    return senha, tema_escolhido

def gerar():
    # --- GERANDO EXEMPLOS ---
    print("🔒 Senhas Geradas:\n")
    for _ in range(5):
        senha, tema = gerar_senha_tematica(num_palavras=3, incluir_numero=True)
        print(f"• Senha: {senha:<30} (Tema: {tema})")

if __name__ == "__main__":
    gerar()