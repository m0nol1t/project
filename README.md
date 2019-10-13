## Проект по разработке платформы для объединения музыкантов в коллективы и их коммуникации
	
_**Участники проекта**: Андреев Александр, Гришкевич Константин, Ницевич Владислав, Ряполова Екатерина, Субботин Сергей_

***

### Идея проекта

Сервис должен помочь начинающим исполнителям опубликовать свои композиции и
собрать свой коллектив, позволить уже состоявщимся коллективам найти новых людей
в команду.

***

### Функционал
* **Сбор музыкальной команды**
* Регистрация новых пользователей
* Добавление композиции (также клипов) в базу
* Поиск по имени исполнителя/названию композиции
* Сортировка музыкальных записей 
* Рейтинговая система для композиций
* Рейтинг пользователей
* Прослушивание композиций/просмотр клипов
* Поиск объявлений(поиск по рейтингу, по роли в группе)
* Коммуникативные функции (чат и тд)
* Тематические статьи

***

### Требования
Реализовать бэк-энд составляющую для следующих пунктов:
* Система оценок композиций должна позволить начинающим музыкантам заявить о себея среди
других исполнителей. 
* Доска объявлений должна предоставлять возможность как музыканту найти группу,
так и группе найти музыканта.
* Должна быть предоставлена база всех загруженных композиций с возможностью добавления новых и их прослушивания.
* Рейтинг музыканта должен определяться исходя из оценок на его публикации (композиции, статьи).
* Необходимо введение системы тегов для поиска необходимых публикаций.

### Сущности
##### Необходимо заполнить
| Сущность            | 1                   | 2                    | 3                | 4             | 5    | 6     | 7                | 8       |
| ------------------- | ------------------- | -------------------- | ---------------- | ------------- | ---- | ----- | ---------------- | ------- |
| **Пользователь**    | __Логин__           | Имя                  | Дата регистрации | Дата рождения | Инфо | email | _Номер телефона_ | _Город_ |
| **Песня**           | Название            | Исполнитель          | Дилтельность     | Теги          |      |       |                  |         |
| **Группа**          | Название            | Члены группы         | Теги             |               |      |       |                  |         |
| **Член группы**     | __Группа(id)__      | __Пользователь(id)__ |                  |               |      |       |                  |         |
| **Лич. Сообщение**  | __Отправитель(id)__ | __Получатель(id)__   | Текст            |               |      |       |                  |         |
| **Статья**          | __Создатель(id)__   | Теги                 | Название         | Текст         |      |       |                  |         |
| **Запись о поиске** | __Создатель(id)__   | ?(Нужно заполнить)                    |                  |               |      |       |                  |         |
| **Комментарий**     | __Пост(id)__        | *Предок(id)*         | Текст            |               |      |       |                  |         |