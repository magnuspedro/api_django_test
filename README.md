# HOW TO USE

## Follow the comands

To build the project:
    
```docker 
docker-compose build
```
To migrate the datebase:
```docker 
docker-compose run --rm app sh -c "python manage.py migrate"
```
To create A super user:
```docker 
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
To strat the server:
```docker
docker-compose up
```
GO to the page:

**localhost:8000/api/user/token**

The page will generate a toke for the super user, download the ModHeader exteantion for the browser and put a request reader.

In the first fild type **Authorization**
In the secound type **Token [YOUR TOKEN]**

