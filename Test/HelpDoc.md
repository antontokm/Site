# Вспомоготальная документация к тест кейсам

## Проверка пользователя в бд

Предусловие:

* Пользователь залогинен под аккауном с ролью админстратор

Данные:

* Логин и пароль взять из ?

1. Зайти на сайт /admin/auth/user/
2. Перейти по ссылке /admin/auth/user/
3. Убедиться в наличии пользователя.

## Логин в аккаунт обычного пользователя

Предусловие:

* Не быть залогиненым на сайте.
* Убедится что пользователь присутствет в бд.  Проверка пользователя в базе данных. [Документация для проверки](HelpDoc.md).

Данные:

* login:Test1
* password:1qaz@WSX3edc$RFV  

Шаги:

1. Зайти на сайт по ссылке [Локальный сервер](TestCaseLink.md).
2. В хедере кликнуть по кнопке log in.  
3. Ввести логин в строку Username из данных.
4. Ввести пароль в строку Password из данных.
5. Кликнуть по кнопке log in.