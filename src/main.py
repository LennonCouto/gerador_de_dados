import names
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import random


# Dicionário com departamentos e cargos possíveis
departamentos = {
    "vendas": ["Vendedor Jr", "Vendedor Pleno", "Gerente de Vendas"],
    "rh": ["Estagiário de RH", "Analista de RH", "Gerente de RH"],
    "ti": ["Suporte Técnico", "Desenvolvedor", "Gerente de TI"],
    "financeiro": ["Assistente Financeiro", "Analista Financeiro", "Gerente Financeiro"]
}

# Faixas salariais por cargo
salarios = {
    "Estagiário de RH": (800, 1800),
    "Analista de RH": (2500, 5000),
    "Gerente de RH": (9000, 16000),
    "Vendedor Jr": (1500, 3000),
    "Vendedor Pleno": (3000, 6000),
    "Gerente de Vendas": (7000, 15000),
    "Suporte Técnico": (1800, 3500),
    "Desenvolvedor": (3500, 10000),
    "Gerente de TI": (12000, 25000),
    "Assistente Financeiro": (1500, 3000),
    "Analista Financeiro": (3000, 8000),
    "Gerente Financeiro": (10000, 20000)
}


# Data atual formatada
def data_atual_formatada():
    return datetime.now().strftime("%d-%m-%Y_%H-%M")

# Gera uma data aleatoria


def gerar_random_date():
    start = datetime(2020, 1, 1)
    end = datetime.now()
    delta_days = (end - start).days
    random_day = random.randint(0, delta_days)
    return (start + timedelta(days=random_day)).date()


# Gera um numero de telefone fictício
def gerar_phone():
    dd = random.randint(11, 99)
    return f"({dd}) 9{random.randint(90000000, 100000000)}"


# Gera um email fictício
def gerar_email(nome):
    partes = nome.lower().split(" ")
    if len(partes) > 1:
        return f"{partes[0]}.{partes[1][0]}@gmail.com"
    else:
        return f"{partes[0]}@gmail.com"


def gerar_salario(cargo):
    minimo, maximo = salarios.get(cargo, (1500, 9000))
    return round(random.uniform(minimo, maximo), 2)


def gerador_dados(count, departamento):
    dados = []
    cargos = departamentos.get(departamento)

    for i in range(count):
        nome = names.get_full_name()
        cargo = random.choice(cargos)

        # Guarda os dados criados em dicionário
        dados.append({
            "Nome": nome,
            "Telefone": gerar_phone(),
            "E-mail": gerar_email(nome),
            "Departamento": departamento.title(),
            "Cargo": cargo,
            "Salário": gerar_salario(cargo),
            "Data de registro": gerar_random_date()
        })
    return dados


def salvar_dados(dados, departamento):
    pasta_atual = Path(__file__).resolve().parent.parent
    (pasta_atual / 'Dados_gerados').mkdir(exist_ok=True)

    df = pd.DataFrame(dados)     # Cria o DataFrame
    df.to_excel(pasta_atual / 'Dados_gerados' /
                f'arquivo_{departamento}_{data_atual_formatada()}.xlsx', index=False)

    print("✅ Dados criado com sucesso!")


def main():
    while True:
        try:
            count = int(input("Quantos dados deseja gerar? "))
            if count <= 0:
                print("Valor inválido. Digite um número maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número valido!")

    print("Departamentos disponiveis:", ", ".join(departamentos.keys()))
    departamento = input("Escolha um departamento: ").lower().strip()

    if departamento not in departamentos:
        print("Departamento invalido. Usando automaticamente Ti")
        departamento = 'ti'

    dados = gerador_dados(count, departamento)
    salvar_dados(dados, departamento)


if __name__ == "__main__":
    main()
