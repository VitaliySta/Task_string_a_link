## Запуск приложения
- Склонируйте репозиторий:  
``` git clone <название репозитория> ```    
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите poetry:
``` pip install poetry ```
- Установите зависимости:   
``` poetry install ```
- Запуск приложения:   
``` python main.py ```
- Запуск тестов:
``` pytest ```

## Работа приложения
- Введите целое число - количество строк, котрые необходимо проверить
- Ввведите строки
- В процессе ввода строк можно изменить первоначальное количество строк:
  - введите '+' затем число, на которое необходимо увеличить количество вводимых строк
  - введите '-' затем число, на которое необходимо уменьшить количество вводимых строк


Время выполнения - 1 час