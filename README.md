# RentSmart — Sistema de Orçamento de Locação

Projeto acadêmico desenvolvido em Python para a imobiliária fictícia **R.M. Imóveis**, como parte das atividades de Algorithmic Thinking (AT) e Introduction to Object-Oriented Programming (IOOP), aplicando lógica de programação e conceitos básicos de Programação Orientada a Objetos.

## Objetivo do projeto

O RentSmart foi criado para facilitar a elaboração de orçamentos de locação. O sistema recebe as características do imóvel escolhido pelo cliente, calcula o valor do aluguel com seus adicionais e possíveis descontos, apresenta a taxa contratual separadamente e gera um arquivo CSV com a projeção dos pagamentos durante 12 meses.

## Funcionalidades

- Cadastro das informações do imóvel pelo terminal.
- Cálculo do aluguel para apartamento, casa e estúdio.
- Adicional por segundo quarto em apartamentos e casas.
- Adicional de garagem para apartamentos e casas.
- Opção de pacote de duas vagas para estúdios e inclusão de vagas extras.
- Desconto de 5% para apartamentos quando o cliente informa que não possui crianças.
- Taxa contratual de R$ 2.000,00, com opção de parcelamento de 1 a 5 vezes.
- Exibição separada do aluguel mensal e da taxa contratual.
- Geração automática de um CSV com a projeção dos 12 meses.
- Validação de algumas respostas para evitar opções inválidas.

## Tecnologias utilizadas

- **Python 3**
- Biblioteca `csv`, utilizada para criar o arquivo de projeção.
- Programação Orientada a Objetos: classes, objetos, atributos, métodos e herança.

Não é necessário instalar bibliotecas externas, pois o projeto utiliza recursos que já acompanham o Python.

## Regras de negócio

### Apartamento

- Valor inicial para 1 quarto: **R$ 700,00**.
- Adicional para 2 quartos: **R$ 200,00**.
- Garagem: **R$ 300,00**.
- Quando o cliente informa que não possui crianças, é aplicado desconto de **5% sobre o valor do aluguel após os adicionais**.

### Casa

- Valor inicial para 1 quarto: **R$ 900,00**.
- Adicional para 2 quartos: **R$ 250,00**.
- Garagem: **R$ 300,00**.
- Não possui o desconto de 5% aplicado aos apartamentos.

### Estúdio

- Valor inicial: **R$ 1.200,00**.
- Pacote opcional com duas vagas: **R$ 250,00**.
- Cada vaga extra, quando o pacote é escolhido: **R$ 60,00**.

### Taxa contratual

- Valor total: **R$ 2.000,00**.
- Pode ser parcelada em até **5 vezes** (de 1 a 5 parcelas).
- A taxa contratual é exibida separadamente do valor mensal do aluguel.

## Organização das classes

O código está organizado em classes para separar as regras de cada tipo de imóvel e as funções do orçamento:

- **`Imovel`**: classe principal que guarda informações básicas, como quantidade de quartos e valor-base, e possui métodos utilizados pelos outros tipos de imóvel.
- **`Apartamento`**: herda características de `Imovel` e calcula os adicionais de quarto e garagem, além do desconto de 5% quando aplicável.
- **`Casa`**: herda características de `Imovel` e calcula os adicionais de quarto e garagem.
- **`Estudio`**: herda características de `Imovel` e calcula o valor do pacote de vagas e das vagas extras.
- **`Orcamento`**: reúne o imóvel escolhido, calcula o aluguel final, apresenta o resumo dos valores e gera o arquivo CSV.

O programa também utiliza funções para receber respostas de sim ou não, validar algumas entradas e iniciar a execução principal.

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Salve o arquivo `rentsmart.py` em uma pasta do computador.
3. Abra essa pasta no Visual Studio Code.
4. No menu superior, selecione **Terminal > Novo Terminal**.
5. No terminal, execute:

```bash
python rentsmart.py
```

No Windows, se o comando acima não funcionar, tente:

```powershell
py rentsmart.py
```

6. Responda às perguntas exibidas no terminal para escolher o imóvel e montar o orçamento.

## Arquivo CSV gerado

Ao finalizar o orçamento, o programa cria o arquivo **`projecao_rentsmart.csv`** na pasta em que o programa foi executado.

O arquivo apresenta uma linha para cada um dos 12 meses e contém as seguintes informações:

- Mês da projeção;
- Valor do aluguel;
- Parcela da taxa contratual;
- Total previsto para o mês.

A taxa contratual aparece somente nos meses correspondentes à quantidade de parcelas escolhida. Nos meses seguintes, o valor dessa parcela fica zerado. O arquivo pode ser aberto no Excel ou em outro programa de planilhas. Caso os dados apareçam em uma única coluna, importe o CSV utilizando o delimitador **ponto e vírgula (`;`)**.

## Exemplo de teste

Para testar o cálculo do desconto, utilize as seguintes respostas:

- Tipo de imóvel: apartamento;
- Quantidade de quartos: 2;
- Garagem: sim;
- Cliente sem crianças: sim;
- Parcelamento da taxa contratual: 5 vezes.

### Resultado esperado

| Descrição | Valor |
|---|---:|
| Aluguel inicial | R$ 700,00 |
| Adicional do segundo quarto | R$ 200,00 |
| Adicional de garagem | R$ 300,00 |
| Subtotal | R$ 1.200,00 |
| Desconto de 5% | - R$ 60,00 |
| **Aluguel mensal final** | **R$ 1.140,00** |
| Taxa contratual | R$ 2.000,00 |
| Parcelamento | 5 x R$ 400,00 |

## Considerações finais

O desenvolvimento do RentSmart permitiu praticar conceitos de lógica de programação e Orientação a Objetos em uma situação próxima de um problema real. A divisão do código em classes ajuda a organizar as regras de cada imóvel e facilita futuras alterações no sistema.

Este projeto foi desenvolvido para fins acadêmicos.
