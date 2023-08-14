# Курс API веб-сервисов от dvmn.org 
# Урок 3.
`main.py` получает в качестве аргумента url. Если введеный url в формате коротких ссылок bit.ly, то выведется кол-во кликов по ссылке за всё время. В другом случае программа попытается сократить ссылку посредствои API bit.ly. Если сократить ссылку невозможно, будет выведен текст с ошибкой.
## Переменные окружения .env
Файл `.env` необходимо сохранить в корневую директорию проекта, рядом с файлом `main.py`
Заполнить файл в соотетствии:
ПЕРЕМЕННАЯ = значение
`BITLY_ACCESS_TOKEN` - токен сервиса bit.ly
## Установка
Python3 должен быть уже установлен.
1. Клоинруйте проект командой и перейдите в директорию проекта
 ```bash
git clone https://github.com/d3rr0m/dvmn_api_3.git
```
```bash
cd dvmn_api_3
```
2. Установите виртуальное окружение.
```bash
python -m venv venv
```
3. Активируйте только что созданное виртуальное окружение.
```bash
$ source venv/bin/activate
```
либо
```bash
venv\Scripts\activate.bat
```
4. Использую pip установите необходимые пакеты
```bash
pip install -r requirements.txt
```
## Запуск
`python main.py url`, где url - параметр командой строки. Передавайте в нем адрес сайта для получения сокращенной ссылки или вывода кол-ва кликов по уже существующей короткой ссылке.
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
