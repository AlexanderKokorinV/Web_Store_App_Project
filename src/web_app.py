# Импорт встроенной библиотеки для работы веб-сервера
import os
from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        # 1. Читаем содержимое из файла
        try:
            # Получаем путь к папке, где лежит web_app.py (папка src)
            base_dir = os.path.dirname(os.path.abspath(__file__))
            # Формируем путь: выходим из src и заходим в html_files
            file_path = os.path.join(base_dir, "..", "html_files", "contacts.html")
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            # 2. Отправляем успешный ответ
            self.send_response(200)  # Отправка кода ответа
            self.send_header(
                "Content-type", "text/html; charset=utf-8"
            )  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(html_content, "utf-8"))  # Тело ответа

        except FileNotFoundError:
            # Если файл не найден, отправляем ошибку 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("Файл contacts.html не найден", "utf-8"))

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""

        # 1. Определяем длину сообщения
        content_length = int(self.headers["Content-Length"])

        # 2. Читаем "сырые" данные из тела запроса
        body = self.rfile.read(content_length)

        # 3. Печатаем в консоль сервера
        print(f"Получены данные формы: {body}")

        # 4. Отвечаем браузеру
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes("Данные получены и напечатаны в консоль!", "utf-8"))
