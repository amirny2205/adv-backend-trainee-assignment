# adv-backend-trainee-assignment
выполнение вот этого тестового задания : https://github.com/avito-tech/adv-backend-trainee-assignment
запуск осуществляется просто : docker-compose up


## описание архитектуры сервиса
 Джанго коммуницирует с базой данных Postgres через ORM; клиент отправляет http запросы на django, получает ответы в формате JSON.



## описание методов сервиса:
здесь 3 эндпоинта:

### ad_list/

тип запроса: GET

выдаёт список объявлений, по 10 на страницу.

принимает параметр page в адресную строку, например ad_list/?page=2

принимает параметр ordering, к нему значения : price и creation_date; например:

?ordering=price

?ordering=-creation_date

принимает параметр fields, в него можно прописать значения description,photos,id:
?fields=description,photos

### ad_detail/(id)/ 

тип запроса: GET

выдаёт конкретное объявление

принимает параметр fields, в него можно прописать значения description,photos,id:
?fields=description,photos

### ad_create/

тип запроса: POST

создаёт объявление, в теле ожидает следующее:

title(не больше 200 символов), description(не больше 1000 символов), photos(список в формате json, не более 3-х фото), price



