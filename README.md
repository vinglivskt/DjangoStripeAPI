Задача
------

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* 	Django Модель Item с полями (name, description, price)
* 	API с двумя методами:
* 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса;
* 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id).

Бонусные задачи:
---------------
* 	Запуск используя Docker ✅
* 	Использование environment variables ✅
* 	Просмотр Django Моделей в Django Admin панели ✅
* 	Запуск приложения на удаленном сервере, доступном для тестирования: http://127.0.0.1:8000/ ✅
* 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
* 	Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
* 	Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
* 	Реализовать не Stripe Session, а Stripe Payment Intent.

Api ключи:
-------------------------

https://dashboard.stripe.com/apikeys

Запуск
------

```
git clone https://github.com/vinglivskt/DjangoStripeAPI.git
cd DjangoStripeAPI
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Главная страница: http://localhost:8000/

Запуск Docker
-------------

```
git clone https://github.com/vinglivskt/DjangoStripeAPI.git
cd DjangoStripeAPI
docker-compose up -d
```
Главная страница: http://localhost:8000/
#### Остановка Docker:
```
docker-compose stop
```


