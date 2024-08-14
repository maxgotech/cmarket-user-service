# CMARKET-USER-SERVICE
Пользовательский микросервис в проекте CoursesMarketplace

## Используемые технологии:
- Flask 3
- SQLAlchemy 2
- Pytest
- MySQL

## Документация
Доступна по [ссылке](https://documenter.getpostman.com/view/25915575/2sA3kVn2wn#1e959e1c-da2b-46f3-979f-61a8435e1bb1)


## Установка
1. Установить Docker и запустить
2. Скачать файлы проекта на ПК
3. Для запуска в терминале директории проекта прописать команду:
```
docker compose up -d
```
4. Для выключения прописать команду:
```
docker stop $(docker ps -q)
```

> [!TIP]
> Для просмотра базы данных можно использовать phphmyadmin.

phpmyadmin: http://127.0.0.1:8080/ или http://localhost:8080/
  - пользователь: root
  - пароль: root