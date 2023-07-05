# Тестовое задание

В данном репозитории представлено тестовое задание, которое включает работу с регулярными выражениями и выполнение HTTP-запросов.

## Регулярные выражения

Для проверки регулярных выражений были разработаны функции-валидаторы и написаны тесты.

## HTTP-запросы

Для проверки корректности выполнения HTTP-запросов был использован фейковый API [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/). Были написаны mock-тесты.

## Установка и запуск проекта

Чтобы запустить проект, выполните следующие шаги:

1. Склонируйте репозиторий:

   ```shell
   git clone https://github.com/Shadowmoses1314/Regular_expression_and_query.git
   ```

2. Перейдите в каталог проекта:

   ```shell
   cd Regular_expression_and_query
   ```

3. Создайте и активируйте виртуальное окружение:

   ```shell
   python -m venv env
   source env/Scripts/activate
   ```

4. Обновите pip:

   ```shell
   python -m pip install --upgrade pip
   ```

5. Установите зависимости:

   ```shell
   pip install -r requirements.txt
   ```

6. Запустите тесты:

   ```shell
   pytest
   ```

7. Запустить подробные тесты:

   ```shell
   pytest -v
   ```
