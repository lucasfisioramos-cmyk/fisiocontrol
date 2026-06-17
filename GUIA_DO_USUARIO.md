# fisioControl - Guia de Instalação e Execução

Este guia explica, de forma simples e direta, como baixar, configurar e rodar o **fisioControl** na sua máquina utilizando o Docker.

---

## Pré-requisitos

Antes de começar, você precisará ter instalado na sua máquina:

1. **Git**: Para clonar o repositório do projeto.
2. **Docker**: Para gerenciar os containers do sistema.
3. **Docker Compose**: Para subir a aplicação e o banco de dados juntos.

 *Nota para usuários Linux (Ubuntu/Debian):* Certifique-se de que o seu usuário tem permissão para rodar o Docker ou utilize `sudo` antes dos comandos do Docker.

---

## 🚚 1. Como Baixar o Projeto

Abra o terminal do seu computador e execute o comando abaixo para clonar o repositório:

```bash
git clone [https://github.com/lucasfisioranos-cmyk/fisiocontrol.git](https://github.com/lucasfisioramos-cmyk/fisiocontrol.git)
```

---

Após baixar entre na pasta do projeto:

```bash
cd fisiocontrol
```

---

## 2. Configurar o arquivo 
O sistema utiliza variaveis de ambiente para 
proteger dados sensiveis, e credenciais do banco de dados 
- ​Abra o arquivo .env.exemplo em seu editor de texto de preferência modifique o nome para .env e configure as credenciais do sistema:
```
# Configurações do Banco de Dados (MariaDB)
DB_PASSWORD=sua_senha_root_aqui
DB_NAME=fisiocontrol
DB_USER=fisiouser
DB_PASS=sua_senha_usuario_aqui

# Configurações do Flask
FLASK_ENV=development
FLASK_DEBUG=1
```

---

##3. Como Subir os Containers
Com o Docker instalado e o arquivo .env configurado, subir o sistema é extremamente simples. Rode o comando abaixo na raiz do projeto:

```bash
docker compose up -d --build
```

---

### 4. Como Acessar pelo Navegador
Assim que o comando anterior terminar, o sistema estará online!
- Abra o seu navegador de preferência e digite o endereço correspondente de onde o sistema está rodando:
  http://localhost:5000

## 5. Como Parar o Sistema
Se você precisar pausar ou desligar os serviços para liberar memória do seu computador, utilize o seguinte comando:

```bash
docker compose down
```
- Este comando encerra a execução do Flask e do MariaDB com segurança, mantendo os dados salvos no volume local para a próxima vez que você iniciar o sistema.
