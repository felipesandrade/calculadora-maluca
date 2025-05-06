from abc import ABC, abstractmethod

# É possível implementar uma classe q permite definir a regra de construção de outras classes
# Classe de Interface
class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass
# Define a regra de construção
# Quando herdamos uma classe de interface que contém métodos abstratos, somos obrigados a implementar esses métodos novamente
class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f"Email message - {message}")


class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f"SMS message - {message}")

class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender


    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)

# Injeção de dependência -> colocar uma classe dentro da outra
obj = Notificator(EmailNotificationSender())
obj.send('Olá Mundo')
    