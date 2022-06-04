Описание hack.py
==================
Этот скрипт сделан в учебных целях для курса [Девман](http://dvmn.org/). Скрипт позволяет изменять запси в базе данных
[Сайта электронного дневника](https://github.com/devmanorg/e-diary). Если вы планируете использовать этот сайт, его необходимо
предварительно развернуть у себя на сервере. Также вам понадобится база данных для него. Информацию о том, как это сделать, смотрите по
[ссылке](https://github.com/devmanorg/e-diary/blob/master/README.md)

Подготовка к работе
---
Файл со скриптом следует положить в основную папку сайта на сервер. Необходимо, чтобы он лежал в той же папке, что и файл
`manage.py`.

Запуск скрипта и работа с ним
---
1. Необходимо открыть коммандную строку в основной папке сервера и запустить интерактивную консоль коммандой
    ```python
       python manage.py shell 
    ```
   Вы увидите сообщение, похожее на это:
    ```commandline
        Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> 
    ```
2. После этого следует запустить файл со скриптом
    ```commandline
        >>>  exec(open('hack.py', encoding='utf-8').read())
    ```
3. Следуйте инструкциям в консоли. Когда скрипт закончит работу, вы увидите такое сообщение:
    ```commandline
        Записи для "Полное имя ученика" исправлены. Похвала по "Название предмета" добавлена
    ```
4. Если вы ввели несуществующее имя или в имени была опечатка, то вы получите следующее сообщение:
    ```commandline
        CRITICAL Ученика с таким именем нет. Проверьте правильность написания
    ```
   В этом случае, повторите все действия начиная с пункта 1.


5. Если в базе данных много похожих имен, то вы получите следующее сообщение:
    ```commandline
        CRITICAL Много похожих имён. Ввведите одно из них
        Воронцова Иванна Рубеновна 1В
        Русакова Иванна Рубеновна 2А
        Королева Иванна Артемовна 2В
        г-жа Власова Иванна Аскольдовна 2В

    ```
   В этом случае скопируйте нужное вам имя из списка и повторите все действия начиная с пункта 1. Номер и буква класса выводятся
    для того, чтобы точно найти имя нужного ученика. Их копировать и вводить не надо.


6. Если в базе данных нет урока с названием, которое вы ввели, то вы получите следующее сообщение:
    ```commandline
        CRITICAL Такого урока нет у этого ученика
        Вот правильные названия уроков:
        Краеведение
        География
        Математика
        Изобразительное искусство
        Основы безопасности жизнедеятельности (ОБЖ)

    ```
   В этом случае скопируйте нужное вам название из списка и повторите все действия начиная с пункта 1.

