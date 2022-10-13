# adv-backend-trainee-assignment
выполнение вот этого тестового задания : https://github.com/avito-tech/adv-backend-trainee-assignment

здесь 3 эндпоинта:

### ad_list/

выдаёт список объявлений, по 10 на страницу.

принимает параметр page в адресную строку, например ad_list/?page=2





### ad_detail/(id)/ 
выдаёт конкретное объявление

### ad_create/
создаёт объявление, в теле ожидает следующее:

title(не больше 200 символов), description(не больше 1000 символов), photos(список в формате json, не более 3-х фото), price

