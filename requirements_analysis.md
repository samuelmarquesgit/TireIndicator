# Análise de Requisitos - Projeto Tirindicator (Indicar Pneu)

## 1. Entendimento do Problema

O projeto **Tirindicator** é uma aplicação web Full-Stack cujo objetivo é:
- Permitir cadastro de clientes
- Permitir cadastro de veículos do cliente
- Permitir cadastro de pneus que o cliente utiliza
- Utilizar dados técnicos de veículos para indicar o pneu ideal

O sistema deve ajudar o cliente a escolher pneus adequados, pois muitos usuários não sabem qual pneu comprar.

---

## 2. Praticabilidade e Implementabilidade

Sim, o software é totalmente implementável devido a três fatores técnicos principais:

### 2.1 Disponibilidade de dados automotivos
Existem bases de dados públicas ou comerciais contendo Marca, Modelo, Ano, Motorização e Medidas de pneus.
- **Fontes possíveis**: API Tabela FIPE (Dados de veículos), Kaggle datasets, bases de fabricantes.

### 2.2 Dados de pneus
As dimensões seguem um padrão universal. Exemplo: `205/55 R16 91V`
- **205**: largura
- **55**: perfil
- **R16**: aro
- **91**: índice de carga
- **V**: velocidade

### 2.3 Tecnologia escolhida
A stack é adequada para um MVP:
- **Backend**: FastAPI, SQLAlchemy, Pydantic.
- **Frontend**: Streamlit.
- **Banco**: SQLite (inicial).

---

## 3. O que é necessário para enunciar os requisitos

### 3.1 Levantamento com stakeholders
Entrevistas com gestores, equipe de vendas, clientes e especialistas para entender o processo de escolha e dúvidas comuns.

### 3.2 Benchmark
Análise de sistemas existentes como Pneustore, Pirelli, Michelin e Mercado Livre.

### 3.3 Modelagem de domínio
Identificar entidades principais: Cliente, Veículo, Pneus, Fabricante, Modelo, Histórico de KM.

### 3.4 Casos de uso
Definir fluxos de cadastro, consulta, recomendação e relatórios.

### 3.5 Regras de negócio
Base do algoritmo de recomendação (limites de carga, velocidade e tipo de uso).

---

## 4. Requisitos Funcionais (RF)

- **RF01 – Cadastro de Clientes**: Nome, email, status (ativo/inativo).
- **RF02 – Cadastro de Veículos**: Marca, modelo, ano, motorização, categoria.
- **RF03 – Base de Dados Automotiva**: Todas as marcas, modelos e anos.
- **RF04 – Cadastro de Pneus do Cliente**: Tipo, marca, medida, data de instalação, KM atual.
- **RF05 – Recomendação de Pneus**: Sugestões baseadas no veículo, uso e medidas.
- **RF06 – Consulta de Pneus**: Pesquisa por marca, modelo de veículo ou medida.
- **RF07 – Histórico de Quilometragem**: Registro de KM atual para estimar desgaste.
- **RF08 – Relatórios**: Pneus recomendados, instalados e previsão de troca.
- **RF09 – Interface de Consulta**: Facilitar descoberta do pneu correto via dados do veículo.

---

## 5. Requisitos Não Funcionais (RNF)

- **RNF01 – Desempenho**: Respostas em menos de 2 segundos.
- **RNF02 – Escalabilidade**: Permitir migração para PostgreSQL/Cloud.
- **RNF03 – Segurança**: Proteção de dados, criptografia e autenticação.
- **RNF04 – Usabilidade**: Interface simples para usuários leigos.
- **RNF05 – Disponibilidade**: Mínima de 99%.
- **RNF06 – Manutenibilidade**: Clean Architecture e Documentação.

---

## 6. Modelo Conceitual de Dados

**Cliente** → possui → **Veículo** → utiliza → **Pneus**

Outras entidades incluem Fabricante, Modelo e Ano (Veículo/Pneu).

---

## 7. Algoritmo de Recomendação (Conceito)

1. **Identificar veículo**: Marca, Modelo, Ano.
2. **Consultar tabela técnica**: Veículo → Medida recomendada.
3. **Filtrar pneus disponíveis**: Marca, preço, avaliação.
4. **Retornar melhores opções**.

---

## 8. Estimativas (MVP)

- **Tempo Total**: ~13 semanas (3 meses).
- **Custo Aproximado**: ~R$ 60.000,00 (considerando 500h a R$ 120/h).

---

## 9. Validação dos Requisitos

- **Revisão com Stakeholders**: Validação da lógica de negócio.
- **Protótipo**: Testes de usabilidade (Figma/Streamlit).
- **Casos de Teste**: Cenários reais (ex: Corolla 2018 -> 205/55 R16).
- **Testes de Aceitação**: Checklist de funcionalidades core.

---

## 10. Riscos e Melhorias

- **Riscos**: Falta de base automotiva, dados incorretos, recomendação errada.
- **Melhorias**: IA de recomendação, app mobile, integração direta com lojas e comparação de preços.
