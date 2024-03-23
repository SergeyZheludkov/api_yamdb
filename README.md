### Проект YaMDB  

## Описание
YaMDB - это API собирающий отзывы пользователей на различные произведения. Произведения разделены по категориям, например таким как Книги и Музыка, также произведениям присваиваются жанры по которым также удобно найти небходимое. Произведения, Жанры и Категории добавляются администраторами проекта. Каждый зарегистрированный пользователь может добавлять отзывы, есть также и функционал комментариев для возможности обсудить тот или иной отзыв. Для незарегестрированных пользователей доступно лишь чтение. Пользователи блягодаря своим отзывам формируют рейтинг произведений, который формируется из среднего значения оценок выставленных во всех отзывах.

## Используемые технологии:

- django
- DRF
- Simple JWT

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladimirNagibin/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить пакетный менеджер и зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Загрузить тестовые данные:

```
python manage.py load_data
```
(ключ -e (--erase) позволяет предварительно очистить таблицы)

## Регистрация пользователей
Пользователь отправляет POST-запрос с параметрами username, email на эндпоинт: /api/v1/auth/signup/
При полученный корректных данных YaMDB отправляет на почту письмо с кодом подтверждения
Пользователь отправляет POST-запрос с параметрами username, confirmation_code на эндпоинт: /api/v1/auth/token/ и получает JWT-token который ему необходимо будет отправлять вместе с запросом.

## Примеры запросов к API

### Произведения
Получение списка всех произведений - GET запрос на эндпоинт: /api/v1/titles/

Добавление произведения (доступно только для администратора) - POST запрос на эндпоинт: /api/v1/titles/ 

Получение информации о конкретном произведении - GET запрос на эндпоинт: /api/v1/titles/{titles_id}/ 

Редактирование данных произведения (доступно только для администратора)- PATCH запрос на эндпоинт: /api/v1/titles/{titles_id}/ 

Удаление произведения (доступно только для администратора)- DELETE запрос на эндпоинт: /api/v1/titles/{titles_id}/ 

### Жанры
Получение списка всех жанров - GET запрос на эндпоинт: /api/v1/genres/

Добавление жанра (доступно только для администратора) - POST запрос на эндпоинт: /api/v1/genres/

Удаление жанра (доступно только для администратора) - DELETE запрос на эндпоинт: /api/v1/genres/{slug}/

### Категории
Получение списка всех категорий - GET запрос на эндпоинт: /api/v1/categories/

Добавление категории (доступно только для администратора) - POST запрос на эндпоинт: /api/v1/categories/

Удаление катиегорр (доступно только для администратора) - DELETE запрос на эндпоинт: /api/v1/categories/{slug}/

### Отзывы
Получение списка всех отзывов - GET запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/

Добавление нового отзыва (доступно только для аутентифицированного пользователя) - POST запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/

Получение конкретного отзыва - GET запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/

Редактирование отзыва (доступно для автора, администратора, модератора)- PATCH запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/

Удаление отзыва (доступно для автора, администратора, модератора)- DELETE запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/

### Комментарии
Получение списка всех комментариев к отзыву - GET запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/comments/

Добавление комментария к отзыву (доступно только для аутентифицированного пользователя) - POST запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/comments/

Получение конкретного комментария к отзыву - GET запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

Редактирование комментария (доступно для автора, администратора, модератора)- PATCH запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

Удаление комментария (доступно для автора, администратора, модератора)- DELETE запрос на эндпоинт: /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

### Работа с пользователями
Получение списка всех пользователей (доступно только для администратора) - GET запрос на эндпоинт: /api/v1/users/

Добавление пользователя (доступно только для администратора) - POST запрос на эндпоинт: /api/v1/users/

Получение конкретного пользователя по username (доступно только для администратора) - GET запрос на эндпоинт: /api/v1/users/{username}/

Изменение данных пользователя (доступно только для администратора) - PATCH запрос на эндпоинт: /api/v1/users/{username}/

Удаление пользователя (доступно только для администратора) - DELET запрос на эндпоинт: /api/v1/users/{username}/

Получение данных своей учетной записи (доступно для любого авторизованного пользователя) - GET запрос на эндпоинт: /api/v1/users/me/

Редактирование данных своей учетной записи (доступно для любого авторизованного пользователя) PATCH запрос на эндпоинт: /api/v1/users/me/

Более подробные данные: http://127.0.0.1:8000/redoc/

## Авторы проекта
- Владимир Нагибин (Github: [@VladimirNagibin](https://github.com/VladimirNagibin/))
- Сергей Желудков (Github: [@SergeyZheludkov](https://github.com/SergeyZheludkov/))
- Вадим Трахимец (Github: [@Tantal25](https://github.com/Tantal25/))
