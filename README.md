APP-RESTAURANTE
# Documentação do Aplicativo Restaurante

## Visão Geral
Este aplicativo de linha de comando, desenvolvido em Python, foi criado para ajudar o gerenciamento básico financeiro e de clientes de um restaurante. Ele permite a inserção mensal de dados de receita, gasto e número de clientes, e gera resumos com totais e médias anuais.

## Funcionalidades

- Adicionar dados mensais:
  - Receita mensal (renda em reais).
  - Gasto mensal (despesas em reais).
  - Número de clientes mensais.
- Calcular totais anuais:
  - Receita anual (soma das receitas mensais).
  - Gasto anual (soma dos gastos mensais).
  - Total de clientes atendidos no ano (soma dos clientes mensais).
- Calcular médias mensais:
  - Receita média mensal.
  - Gasto médio mensal.
  - Número médio mensal de clientes.
- Mostrar resumo estatístico com meses registrados e os valores acima.

## Estrutura do Código

### Classe `RestaurantApp`
- **Atributos:**
  - `monthly_revenues`: lista de floats, armazena receitas mensais.
  - `monthly_expenses`: lista de floats, armazena gastos mensais.
  - `monthly_clients`: lista de inteiros, armazena número de clientes mensais.

- **Métodos principais:**
  - `add_monthly_data(revenue, expense, clients)`: adiciona os dados mensais.
  - `total_annual_revenue()`: retorna a soma das receitas mensais.
  - `total_annual_expense()`: retorna a soma dos gastos mensais.
  - `total_annual_clients()`: retorna a soma dos clientes mensais.
  - `show_stats()`: exibe um resumo formatado com totais e médias anuais.

### Função `main()`
- Executa um loop que apresenta um menu interativo.
- Permite ao usuário inserir dados, mostrar estatísticas ou sair do aplicativo.
- Valida entradas do usuário para garantir valores coerentes.

## Como Executar

1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Salve o código em um arquivo chamado `restaurant_app.py`.
3. No terminal ou prompt de comando, navegue até a pasta onde o arquivo está salvo.
4. Execute o comando:

   ```bash
   python restaurant_app.py
