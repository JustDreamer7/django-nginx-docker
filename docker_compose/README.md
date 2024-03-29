# Проектное задание: Docker-compose


## Для Linux OS:

1) Клонируйте репозиторий на ваш компьютер.
2) Зайдите в папку cd ${your_path_to_repository}/new_admin_panel_sprint_2/docker_compose
3) **Сбор и запуск:** docker-compose -f docker-compose.yml up -d --build
4) **Работает на:** 0.0.0.0:80
5) **Остановка:** docker-compose stop




Приступим к улучшению сервиса в области DevOps. Настройте запуск всех компонентов системы — Django, Nginx и Postgresql — с использованием docker-compose.

Для упрощения выполнения задания мы подготовили проект, где настроена работа связки Django + uWSGI + Nginx + Docker. Вы можете взять его за основу, но его придётся дополнительно доработать, чтобы подключить Postgres, а также устранить мелкие ошибки в конфигурировании Django: например, debug = True или отсутствие настроек чтения переменных окружения.

Сама заготовка уже показывает админку с примером одного метода API. Однако статика не собирается, миграций нет, конфиги Nginx, uWSGI и Docker, возможно, придётся подправить.

Если вы считаете, что всё нужно сделать по-другому, воспользуйтесь пустой заготовкой проекта и напишите его самостоятельно.

**Требования к работе:**

Напишите dockerfile для Django.

Для настройки Nginx можно пользоваться наработками из этой темы, но ревьюеры будут запускать ваше решение. Перед сдачей проекта убедитесь, что всё работает правильно.

Уберите версию Nginx из заголовков. Версии любого ПО лучше скрывать от посторонних глаз, чтобы вашу админку случайно не взломали. Найдите необходимую настройку в официальной документации и проверьте, что она работает корректно. Убедиться в этом можно с помощью «Инструментов разработчика» в браузере.

Отдавайте статические файлы Django через Nginx, чтобы не нагружать сервис дополнительными запросами. Перепишите location таким образом, чтобы запросы на /admin шли без поиска статического контента. То есть, минуя директиву try_files $uri @backend;.

**Подсказки и советы:**

Теории на платформе должно быть достаточно для понимания принципов конфигурирования. Если у вас появятся какие-то вопросы по параметрам, ищите ответы в официальной документации.

Для выполнения задачи про /admin нужно посмотреть порядок поиска location.

Для работы со статикой нужно подумать, как залить данные в файловую систему контейнера с Nginx.

Для задания дана базовая структура, которой можно пользоваться.

При настройке docker-compose важно проверять пути до папок. Большинство проблем связанно именно с этим.