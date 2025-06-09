def obter_dados_inss(salario):
    if salario <= 1518.00:
        return 0.075, 0.00
    elif salario <= 2793.88:
        return 0.09, 22.77
    elif salario <= 4190.84:
        return 0.12, 106.59
    elif salario <= 8157.41:
        return 0.14, 190.40
    else:
        return None, 951.62  

def calcular_inss(salario):
    aliquota, deducao = obter_dados_inss(salario)
    if aliquota is None:
        return "Teto", deducao
    valor = salario * aliquota - deducao
    return f"{aliquota*100:.1f}", valor

def obter_dados_ir(base):
    if base <= 2259.20:
        return 0.00, 0.00
    elif base <= 2826.65:
        return 0.075, 169.44
    elif base <= 3751.05:
        return 0.15, 381.44
    elif base <= 4664.68:
        return 0.225, 662.77
    else:
        return 0.275, 896.00

def calcular_ir(base):
    aliquota, deducao = obter_dados_ir(base)
    valor = base * aliquota - deducao
    if valor < 10.00:
        valor = 0.00
    return f"{aliquota*100:.1f}", valor

def processar_salario(salario):
    aliq_inss, val_inss = calcular_inss(salario)
    base_ir = salario - val_inss
    aliq_ir, val_ir = calcular_ir(base_ir)
    liquido = salario - val_inss - val_ir
    return {
        "bruto": salario,
        "aliq_inss": aliq_inss,
        "val_inss": val_inss,
        "base_ir": base_ir,
        "aliq_ir": aliq_ir,
        "val_ir": val_ir,
        "liquido": liquido
    }

def imprimir_e_gravar(resultados):
    cabecalho = f"{'Bruto':>10} {'AliqINSS':>9} {'Val.INSS':>9} {'Base I.R.':>10} {'AliqIR':>7} {'Val.IR':>9} {'Liquido':>10}"
    print(cabecalho)
    with open("CALCULOS.TXT", "w") as f:
        f.write(cabecalho + "\n")
        for r in resultados:
            linha = f"{r['bruto']:10.2f} {r['aliq_inss']:>9} {r['val_inss']:9.2f} {r['base_ir']:10.2f} {r['aliq_ir']:>7} {r['val_ir']:9.2f} {r['liquido']:10.2f}"
            print(linha)
            f.write(linha + "\n")
        print("Fim dos dados")
        f.write("Fim dos dados\n")

def ler_salarios():
    salarios = []
    while True:
        try:
            valor = float(input("Digite o salário bruto (0 para sair): "))
            if valor == 0:
                break
            salarios.append(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return salarios

def main():
    salarios = ler_salarios()
    calculos = [processar_salario(s) for s in salarios]
    calculos.sort(key=lambda x: x["bruto"])
    imprimir_e_gravar(calculos)

if __name__ == "__main__":
    main()


