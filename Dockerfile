# Estágio de build
FROM python:3.10-slim AS builder

# Instala o Poetry
RUN pip install poetry

# Define o diretório de trabalho
WORKDIR /app

# Configura o Poetry para criar o ambiente virtual no diretório do projeto
RUN poetry config virtualenvs.in-project true

# Copia os arquivos de dependência e instala as dependências
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Estágio final
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o ambiente virtual do estágio de build para o estágio final
COPY --from=builder /app/.venv /app/.venv

# Ativa o ambiente virtual
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código da aplicação
COPY . .

# Expõe a porta
EXPOSE 8001

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]