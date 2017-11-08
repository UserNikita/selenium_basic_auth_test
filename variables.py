"""
Переменные для запуска тестов
"""

BROWSERMOB_PROXY_PATH = 'C:\\Users\\user\\Programs\\browsermob-proxy-2.1.4' \
                        '\\bin\\browsermob-proxy.bat'
# Путь к bat файлу для запуска сервера browsermob_proxy

PROXY_PORT = 8080  # Порт для прокси сервера

DOMAIN = 'auth-demo.aerobatic.io'  # Домен тестируемого сайта

PROTOCOL = 'https://'  # Протокол по которому доступен сайт

START_URL = PROTOCOL + DOMAIN  # Полный адрес сайта для тестирования

USERNAME = 'aerobatic'  # Логин под которым необходимо войти

PASSWORD = 'aerobatic'  # Пароль для входа на сайт
