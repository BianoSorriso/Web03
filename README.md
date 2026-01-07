# Sobre a ONG Felicidade Compartilhada

A ONG Felicidade Compartilhada é uma organização social que nasceu em 2013 com o objetivo de criar oportunidades para a sociedade conhecer instituições carentes e oferecer tempo e amor aos abrigados. A organização se dedica a incentivar, instruir, capacitar e motivar pessoas a se tornarem voluntárias em seus projetos. 

# Site da ONG Felicidade Compartilhada

Este repositório contém o código-fonte do site institucional da ONG Felicidade Compartilhada, desenvolvido em equipe como parte de um projeto de extensão universitária da Universidade UniLaSalle RJ.

## Objetivo
O objetivo deste projeto é desenvolver uma aplicação web para a ONG, com intuito de arrecadar fundos e aumentar sua visibilidade online. A plataforma destaca a missão da organização e os impactos positivos que causa na vida de moradores de rua e pessoas vulneráveis, e visa divulgar a importância de que pessoas façam doações para ajudar essas pessoas. A aplicação web oferecerá informações detalhadas sobre os programas e eventos da ONG, além de opções para doações online, permitindo que apoiadores contribuam diretamente. Com um design atraente e funcional, buscamos engajar visitantes e criar uma rede de apoio sólida para a causa, promovendo a transparência e incentivando a participação da comunidade.

## Funcionalidades do Projeto

- 📋 **Cadastro de Voluntários:** Armazenar e visualizar informações dos beneficiários atendidos.
- 🔄 **Atualização de Dados:** Manter o registro dos voluntários sempre atualizado.
- ❌ **Exclusão de Registros:** Remover registros de voluntários inativos ou desatualizados.
- 🔍 **Consulta Rápida:** Localizar voluntários e seus históricos de participações na ONG.
- 💰 **Doações Online:** Possibilidade de usuários realizarem doações via PIX.

## Tecnologias Utilizadas

- **Django** como framework principal.
- **DbSqlite** para gerenciamento do banco de dados.

## Como Executar


1. Clone o repositório:
    ```bash
    git clone https://github.com/RoGamer97/SiteONG-TrabalhoWebIII.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd SiteONG-TrabalhoWebIII/ONG_FelicidadeCompartilhada
    ```

3. Crie o ambiente virtual
 
    **IMPORTANTE:** Faça este passo apenas na **primeira vez** que for rodar o projeto!
      ```bash
      python -m venv venv
      ```
      
4. Ative o ambiente virtual:
    - No Windows (cmd ou PowerShell):
      ```
      .\venv\Scripts\activate
      ```
      
    - No Linux/Mac:
      ```bash
      source venv/bin/activate
      ```
      
5. Instale as dependências
   
   **IMPORTANTE:** Faça este passo apenas na **primeira vez** que for rodar o projeto!
   
    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações:

    **IMPORTANTE:** Faça este passo apenas na **primeira vez** que for rodar o projeto!
   
    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

# Equipe

A equipe é composta por alunos que colaboraram no desenvolvimento deste projeto:

- **Rodrigo de Moraes Lorenzatto**  
- **Fabiano dos Santos Gomes Bastos**  
- **Pierre Batista do Amaral**  
- **Guilherme Ornellas Chagas**  
- **Wilson da Silva Prata Junior**

## Agradecimento especial 

Vocês que foram essenciais para que pudéssemos construir algo que realmente fizesse a diferença.

- **Aron Barbosa**
- **Pedro Azeredo**