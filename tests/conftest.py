import pytest
from http.server import HTTPServer
from src.web_app import MyServer
from main import hostName, serverPort
import threading # Для запуска сервера в фоновом потоке
import time

@pytest.fixture(scope="module", autouse=True)
def server_instance():
    """Фикстура для запуска сервера в отдельном потоке на время тестов"""
    # noinspection PyTypeChecker
    server = HTTPServer((hostName, serverPort), MyServer)
    thread = threading.Thread(target=server.serve_forever) # Создаем поток, где целью (target) является запуск сервера
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Даем серверу время на запуск
    yield
    server.shutdown()