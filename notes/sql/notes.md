# SQL Commands

Cleaning up tables
> .mode columns

> .headers yes


## Selecting with conditions
> SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";

> SELECT * FROM flights WHERE origin LIKE "%a%";

returns any rows with there is an "a" within the origin column

## Editing a table

- UPDATE flights
SET duration = 430
WHERE origin = "New York">
AND destination = "London";

- DELETE FROM flights WHERE destination = "Tokyo";

## SQL Clauses
- LIMIT
- ORDER BY
- GROUP BY
- HAVING

# Foreign Keys

## Many-to-Many table relationship

Example:

### **people**
| id      | first | last    |
| :---        |    :----:   |          ---: |
| 1      | Harry       | Potter   |
| 2   | Ron        | Weasley      |

### **passengers**
| person_id      | flight_id | 
| :---        |    :----:   |         
| 1      | 1       | 
| 2   | 1        | 
| 2   | 4       | 

- Each flight maps to two different airports (destination and origin)
- Any airport may appear on many different flights
- Any person can be on multiple different flights
- Any flight may have multiple people

## Joining tables

> SELECT first, origin, destination
>   
> &nbsp;&nbsp;&nbsp;&nbsp;FROM flights JOIN passengers
>
> &nbsp;ON passengers.flight_id = flights.id

Overall result will be the same as the original table with columns (name, origin, destination), but access will be easier

# CREATE INDEX
 - makes it easier to search for a value that you expect to be looking up often
> CREATE INDEX name_index ON passengers (last);

# Race Conditions
 - when multiple events are occuring at the same time
 - danger when multiple users try to update the same database entry at the same

 # Django Models

## 1. Within models.py

> from django.db import models
>
> class Flight(models.Model):
>
> &nbsp;&nbsp;&nbsp;   origin = models.CharField(max_length=64)
>
> &nbsp;&nbsp;&nbsp;   destination = models.CharField(max_length=64)
>
> &nbsp;&nbsp;&nbsp;   duration = models.IntegerField

## 2. Make migrations
- Within the cmd
> python manage.py makemigrations
- Creates a file within migrations/

## 3. Apply migrations
> python manage.py migrate

## 4. Interacting with database using django abstractions

### 1. Within the cmd
> python manage.py shell

### 2. Within the shell
> from <appname\>.models import <classname\>
* Example: 
> from flights.models import Flight
>
> f = Flight(origin="New York", destination="London", duration=415)
> 
> f.save()

## 5. Viewing objects
> Flight.objects.all()

### Renaming object
> def __str__(self):
> &nbsp;&nbsp;&nbsp; return f"{self.id}: {self.origin} to {self.destination}"

### Accessing object properties
> flights = Flight.objects.all()
>
> flight = flights.first()
>
> flight.id
>
> flight.destination
>
> flight.delete

### More properties using foreign keys
> jfk = Airport(code="JFK", city="New York")
>
> lhr = ...
>
> jfk.save()
> f = Flight(origin=jfk, destination=lhr, duration=415)
> 
> f.save()
>
> f.origin
>
> f.origin.city OR f.origin.code
>
> lhr.arrivals.all()

# Filtering objects
> Airport.objects.filter(city="New York").first()
>
> Airport.objects.get(city="New York")

# Importing images
https://drive.google.com/uc?export=view&id=[image_id]
