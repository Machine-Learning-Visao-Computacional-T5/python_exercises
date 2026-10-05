"""Execute no terminal: python exemplo_main.py (ou python3)."""

def calcular_subtotal(preco, quantidade):
    return preco * quantidade

def com_desconto(preco, percentual=10):
    return preco * (1 - percentual / 100)

def resumo_compra(preco, quantidade):
    subtotal = calcular_subtotal(preco, quantidade)
    total = com_desconto(subtotal)
    return {"subtotal": subtotal, "total": total}

def main():
    resultado = resumo_compra(20, 3)
    return resultado

if __name__ == "__main__":
    resultado_programa = main()
    print(resultado_programa)
