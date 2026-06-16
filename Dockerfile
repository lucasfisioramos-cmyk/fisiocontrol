FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copia e instala dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Variáveis para rodar o Flask
ENV FLASK_APP=app:create_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

# Inicia com o servidor de desenvolvimento do Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
