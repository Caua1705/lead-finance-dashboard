def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_porcentagem(valor):
    return f"{valor:.2f}%"

def formatar_unidade(valor):
    if valor < 100:
        return f"{valor:02d}"
    else:
        return f"{valor:,}".replace(",", ".")