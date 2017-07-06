# rss_news

Загружаем зависимости в venv
pip3 install -r requirements.txt

Подключаем необходимые модули

INSTALLED_APPS = [
    ...
    'rss_news',
    'bootstrap3',
    ...
]

из корня проекта
python3 manage.py collectstatic
