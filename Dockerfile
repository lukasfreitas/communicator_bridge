# Estágio de build
FROM python:3.10-slim as builder

# Instala o Poetry
RUN pip install poetry

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência e instala as dependências
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Estágio final
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia as dependências do estágio de build
# COPY --from=builder /app/.venv /.venv

# Ativa o ambiente virtual
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código da aplicação
COPY . .

# Expõe a porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]