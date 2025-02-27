# Quotes Scraper

Этот проект представляет собой парсер для сайта [https://quotes.toscrape.com/](https://quotes.toscrape.com/), который извлекает цитаты и авторов и сохраняет их в файл `quotes.json`.

## Структура проекта
├── scraper.py
├── requirements.txt
└── README.md

## Установка

1. Создайте виртуальное окружение:

    ```sh
    python -m venv venv
    ```

2. Активируйте виртуальное окружение:

    ```sh
    # Windows
    venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

## Использование

Запустите скрипт `scraper.py`:

```sh
python scraper.py
```

