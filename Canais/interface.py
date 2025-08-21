
from abc import ABC, abstractmethod

from telegram_integracao.services import TelegramApiClient

class CanalInterface(ABC):
    @abstractmethod
    def enviar_mensagem(self, chat_id, texto):
        pass

    @abstractmethod
    def configurar_webhook(self, url):
        pass

class TelegramInterface(CanalInterface):

    def __init__(self, client: TelegramApiClient):
        """
        Inicializa a interface com uma instância de TelegramApiClient.
        """
        self.client = client

    def enviar_mensagem(self, chat_id, texto):
        # A lógica para enviar a mensagem via o cliente
        return self.client.sendMessage(chat_id=chat_id, text=texto)

    def configurar_webhook(self, url: str, secret: str = None) -> dict:
        # A lógica para configurar o webhook via o cliente
        return self.client.setWebhook(url=url, secret=secret)