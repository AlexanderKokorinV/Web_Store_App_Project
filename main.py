from http.server import HTTPServer

from src.web_app import MyServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

if __name__ == "__main__":
    # noinspection PyTypeChecker
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен: http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()  # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
    except (
        KeyboardInterrupt
    ):  # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Сервер остановлен.")
