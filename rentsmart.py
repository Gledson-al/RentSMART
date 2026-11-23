"""
RentSmart - Sistema de Orçamento de Locação

Execução:
    python rentsmart.py

O programa calcula o aluguel, apresenta a taxa contratual separadamente
e gera um CSV com a projeção dos 12 meses.
"""


import csv


# Valor da taxa contratual
TAXA_CONTRATUAL = 2000


# Classe principal dos imóveis
class Imovel:
    def __init__(self, quartos, valor_base):
        self.quartos = quartos
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base

    def calcular_adicionais(self):
        return 0

    def calcular_desconto(self):
        return 0

    def descricao(self):
        return "Imóvel"


# Classe Apartamento
class Apartamento(Imovel):
    def __init__(self, quartos, garagem, sem_criancas):
        super().__init__(quartos, 700)
        self.garagem = garagem
        self.sem_criancas = sem_criancas

    def calcular_adicionais(self):
        adicional = 0

        if self.quartos == 2:
            adicional += 200

        if self.garagem:
            adicional += 300

        return adicional

    def calcular_desconto(self):
        if self.sem_criancas:
            return (self.valor_base + self.calcular_adicionais()) * 0.05
        return 0

    def descricao(self):
        return "Apartamento"


# Classe Casa
class Casa(Imovel):
    def __init__(self, quartos, garagem):
        super().__init__(quartos, 900)
        self.garagem = garagem

    def calcular_adicionais(self):
        adicional = 0

        if self.quartos == 2:
            adicional += 250

        if self.garagem:
            adicional += 300

        return adicional

    def descricao(self):
        return "Casa"


# Classe Estudio
class Estudio(Imovel):
    def __init__(self, pacote_vagas, vagas_extras):
        super().__init__(0, 1200)
        self.pacote_vagas = pacote_vagas
        self.vagas_extras = vagas_extras

    def calcular_adicionais(self):
        adicional = 0

        if self.pacote_vagas:
            adicional = 250 + (self.vagas_extras * 60)

        return adicional

    def descricao(self):
        return "Estúdio"


# Classe responsável pelo orçamento
class Orcamento:
    def __init__(self, imovel, parcelas):
        self.imovel = imovel
        self.parcelas = parcelas

    def calcular_aluguel_final(self):
        valor = self.imovel.valor_base
        valor += self.imovel.calcular_adicionais()
        valor -= self.imovel.calcular_desconto()

        return round(valor, 2)

    def calcular_parcela(self, mes):
        if mes <= self.parcelas:
            valor = TAXA_CONTRATUAL / self.parcelas

            # Ajusta a última parcela para fechar R$ 2.000
            if mes == self.parcelas:
                return round(
                    TAXA_CONTRATUAL - (round(valor, 2) * (self.parcelas - 1)),
                    2
                )

            return round(valor, 2)

        return 0

    def mostrar_orcamento(self):
        print("\n========== ORÇAMENTO RENTSMART ==========")
        print("Imóvel:", self.imovel.descricao())
        print("Valor base: R$ {:.2f}".format(self.imovel.valor_base))
        print("Adicionais: R$ {:.2f}".format(
            self.imovel.calcular_adicionais()
        ))
        print("Desconto: R$ {:.2f}".format(
            self.imovel.calcular_desconto()
        ))

        print("-----------------------------------------")
        print("ALUGUEL MENSAL: R$ {:.2f}".format(
            self.calcular_aluguel_final()
        ))

        print("-----------------------------------------")
        print("Taxa contratual: R$ 2000,00")
        print("Parcelamento:", self.parcelas, "vez(es)")
        print("Valor aproximado da parcela: R$ {:.2f}".format(
            round(TAXA_CONTRATUAL / self.parcelas, 2)
        ))
        print("=========================================")

    def gerar_csv(self):
        arquivo = open(
            "projecao_rentsmart.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        )

        escritor = csv.writer(arquivo, delimiter=";")

        escritor.writerow([
            "Mes",
            "Aluguel",
            "Taxa contratual",
            "Total do mes"
        ])

        for mes in range(1, 13):
            aluguel = self.calcular_aluguel_final()
            parcela = self.calcular_parcela(mes)
            total = aluguel + parcela

            escritor.writerow([
                mes,
                "{:.2f}".format(aluguel).replace(".", ","),
                "{:.2f}".format(parcela).replace(".", ","),
                "{:.2f}".format(total).replace(".", ",")
            ])

        arquivo.close()

        print("\nArquivo CSV gerado com sucesso!")


# Função para receber respostas sim ou não
def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).lower()

        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Digite apenas s ou n.")


# Programa principal
def main():
    print("=========================================")
    print("       RENTSMART - R.M IMOVEIS")
    print("=========================================")

    print("\nEscolha o tipo de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    while True:
        tipo = input("Digite a opção: ")

        if tipo in ["1", "2", "3"]:
            break

        print("Opção inválida. Tente novamente.")

    if tipo == "1":
        while True:
            quartos = input("Quantidade de quartos (1 ou 2): ")

            if quartos in ["1", "2"]:
                quartos = int(quartos)
                break

            print("Escolha 1 ou 2 quartos.")

        garagem = perguntar_sim_nao("Deseja garagem? (s/n): ")

        sem_criancas = perguntar_sim_nao(
            "O cliente não possui crianças? (s/n): "
        )

        imovel = Apartamento(quartos, garagem, sem_criancas)

    elif tipo == "2":
        while True:
            quartos = input("Quantidade de quartos (1 ou 2): ")

            if quartos in ["1", "2"]:
                quartos = int(quartos)
                break

            print("Escolha 1 ou 2 quartos.")

        garagem = perguntar_sim_nao("Deseja garagem? (s/n): ")

        imovel = Casa(quartos, garagem)

    else:
        pacote = perguntar_sim_nao(
            "Deseja o pacote de duas vagas por R$ 250? (s/n): "
        )

        vagas_extras = 0

        if pacote:
            while True:
                try:
                    vagas_extras = int(input("Quantidade de vagas extras: "))

                    if 0 <= vagas_extras <= 20:
                        break

                    print("Digite um número entre 0 e 20.")

                except ValueError:
                    print("Digite um número inteiro.")

        imovel = Estudio(pacote, vagas_extras)

    while True:
        try:
            parcelas = int(input(
                "\nParcelamento da taxa contratual (1 a 5): "
            ))

            if 1 <= parcelas <= 5:
                break

            print("Escolha de 1 a 5 parcelas.")

        except ValueError:
            print("Digite um número inteiro.")

    # Criação do orçamento
    orcamento = Orcamento(imovel, parcelas)

    # Exibição dos valores
    orcamento.mostrar_orcamento()

    # Geração da planilha CSV
    orcamento.gerar_csv()


# Inicia o programa
if __name__ == "__main__":
    main()
