# Image_reconcililation

We need a way to identify and keep track of a customer's identity across multiple purchases.
We know that orders on FluxKart.com will always have either an email or phoneNumber in the checkout event.
Need to keep the track of the collected contact information in a relational database table named Contact.

One customer can have multiple Contact rows in the database against them. All of the rows are linked together
with the oldest one being treated as "primary” and the rest as “secondary” .

Contact rows are linked if they have either of email or phone as common.

For example:

If a customer placed an order with
email=lorraine@hillvalley.edu & phoneNumber=123456
and later came back to place another order with
email=mcfly@hillvalley.edu & phoneNumber=123456 ,
database will have the following rows:

![image](https://github.com/user-attachments/assets/9058c3db-1f5e-45f8-a58a-458d8b381986)

You are required to design a web service with an endpoint /identify that will receive HTTP POST requests with
JSON body.

![image](https://github.com/user-attachments/assets/4445cb53-e61a-49d5-9470-3e694bc826c7)


How to Install and Run the Project:- [Run in any IDE with python installed]
Here we are not using any external module and library that needs to be imported.
Run these commands in order to migrate model's fields into Database.

#python commands:-
python manage.py makemigrations
python manage.py migrate

#To start the server:-
python manage.py runserver

APi Endpoint:- http://127.0.0.1:8000/identify/

Admin Endpoint:- http://127.0.0.1:8000/admin/

username:- admin, 
Password:- admin123

We must have valid json payload for api.
