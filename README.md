# FisioControl

Sistema web de gestão clínica desenvolvido com foco em UI/UX e metodologia Scrum.

## Objetivo
Gerenciar pacientes, consultas e acompanhamento clínico.

## Tecnologias/Ferramentas
- Figma
- GitHub Projects
- Flask
- MySQL (mariadb)
- AWS 
- Scrum

## Estrutura do Projeto
- Wireframes
- Mockups
- Protótipo
- Documentação Scrum
- MVP

## Funcionalidades
- Cadastro de pacientes
- Agenda
- Histórico clínico
- Controle financeiro

# Como executar
- Instalação
1. Clonar o projeto
git clone <repositorio>
cd fisiocontrol
2. Criar ambiente virtual
python -m venv .venv
3. Ativar ambiente

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate
4. Instalar dependências
pip install -r requirements.txt
5. Criar banco de dados
flask db upgrade
6. Executar aplicação
flask run
