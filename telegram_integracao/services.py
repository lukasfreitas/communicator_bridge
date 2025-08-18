import logging
import requests

# Configuração do logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Crie uma instância de logger
logger = logging.getLogger(__name__)

class TelegramApiClient:

    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        # Use o logger na classe
        self.logger = logging.getLogger(self.__class__.__name__)

    def Post(self, endpoint, data=None) -> dict:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Enviando requisição POST para: {url}")
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            self.logger.debug(f"Requisição POST bem-sucedida. Status: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            data = response.json()
            self.logger.error(f"Erro na requisição para {url}: {data.get("description", str(e))}")
            return None
        
    def setWebhook(self, url, secret) -> dict:
        
        self.logger.debug(f"Configurando webhook para: {url}")
        ngrok_url = "https://8f50f3e698fa.ngrok-free.app/telegram-integracao/webhook/"
        data = {"url": ngrok_url, "secret_token": secret}
        response = self.Post("setWebhook", data)
        if response and response.get("ok"):
            self.logger.debug("Webhook configurado com sucesso.")
        else:
            self.logger.error("Falha ao configurar o webhook.")
        return response if response else None
    

    def sendMessage(self, msg:str) -> dict:
        self.logger.debug(f"Enviando mensagem: {msg}")
        data = {"text": msg}
        response = self.Post("sendMessage", data)
        if response and response.get("ok"):
            self.logger.debug("Mensagem enviada com sucesso.")
        else:
            self.logger.error("Falha ao enviar a mensagem.")
        return response if response else None