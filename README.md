# TeamCityInDocker
ОБЯЗАТЕЛЬНО К УСТАНОВКЕ:
- На агенте обязательно должен быть установлен docker.

TeamCity_builds - пример Build для реализации задачи вызова REST API TeamCity из docker контейнера и получения результата из него.
- BuildDockerContainer - построение образа с текущим снапшотом репозитория и запуск контейнера;
- GetResultContainer - вызов REST API TeamCity и получение результата из контейнера.

PythonTest - пример реализации репозитория с python тестами.
- dockerfile - файл для построения образа в котором будут запущены тесты;
- main.py - пример теста на python с использованием allure-report;
- requirements.txt - перечень используемых библиотек для тестов. Будут установлены при сборке образа docker.
- run.sh - bash скрипт для запуска тестов и вызова Rest API TeamCity для вызова дальнейшей обработки результатов тестирования.