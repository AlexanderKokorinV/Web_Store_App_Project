from main import hostName, serverPort
import requests

def test_get_contacts():
    """Тест успешного получения страницы контактов"""
    url = f"http://{hostName}:{serverPort}/"
    response = requests.get(url)

    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
    assert "Контакты" in response.text  # Проверяем наличие заголовка в HTML

def test_post_data():
    """Тест отправки данных через POST"""
    url = f"http://{hostName}:{serverPort}/"
    data = {
        "user_name": "TestUser",
        "user_email": "test@example.com",
        "user_message": "Hello from tests!"
    }
    response = requests.post(url, data=data)

    assert response.status_code == 200
    # Если do_POST возвращает текст подтверждения:
    assert "Данные получены" in response.text