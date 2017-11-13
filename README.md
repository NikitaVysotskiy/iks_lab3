Інтеграційні програмні системи
Практична робота 3
Системи автоматизації збірки, автоматичні тести, рецензування
коду та безперервна інтеграція.
Робота присвячена організації процесу розробки у вашому репозиторії.

Скопіювати проект на локальну машину:

git clone https://github.com/NikitaVysotskiy/iks_lab3.git

Для запуску проекту потрібно налаштувати оточення. 
Необхідне програмне забезпечення:
- Python3
- Virtualenv
- Virtualenvwrapper (http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

Створення віртуального оточення і встановлення необхідних пакетів python:

- $ mkvirtualenv -p python3 <env_name>

- $ workon <env_name>

- $ cd <path_to_project_root>

- $ pip install -r requirements.txt

Кожного разу при встановленні нових пакетів потрібно активувати віртуальне оточення командою "workon"
Після встановлення потрібно додавати зміни у файл requirements.txt

- $ pip freeze > requirements.txt  
