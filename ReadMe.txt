Address for static HTML content:
http://127.0.0.1:8000/restaurant/

Address for Menu Items:
http://127.0.0.1:8000/restaurant/menu

Address for Booking:
http://127.0.0.1:8000/restaurant/booking/tables

Address for User Registration:
http://127.0.0.1:8000/auth/users

Address for Token Login:
http://127.0.0.1:8000/auth/token/login

Address for Token Logout:
http://127.0.0.1:8000/auth/token/logout

Address for Admin:
http://127.0.0.1:8000/admin
- Username: admin
- Password: password



Insomnia API Tests:

1.  API to get Token:
  POST Method
  http://127.0.0.1:8000/restaurant/api-token-auth/
  - Body - Form Data:
    username = testuser
    password = coursera

or

  POST Method
  http://127.0.0.1:8000/auth/token/login
  - Body - Form Data:
    username = testuser
    password = coursera
  
  
2.  API to Get Menu Item List (Authentication Required):
  GET Method
  http://127.0.0.1:8000/restaurant/menu
  - Use Bearer Token from Token API (1.) in Insomnia Auth Tab (Prefix = Token)
  
  
3.  API to Add New Menu Item (Authentication Required):
  POST Method
  http://127.0.0.1:8000/restaurant/menu/
  - Use JSON in the Body with template below
    {
      "id" : number above 1,
      "Title" : "menu name",
      "Price" : "2 decimal price",
      "Inventory" : integer
    }
  - Use Bearer Token from Token API (1.) in Insomnia Auth Tab (Prefix = Token)
  
  
4.  API to Edit Existing Item (Authentication Required):
  PUT Method
  http://127.0.0.1:8000/restaurant/menu/#id_of_the_item_to_edit
  - Use JSON in the Body with template below
    {
      "Title" : "menu name",
      "Price" : "2 decimal price",
      "Inventory" : integer
    }
  - Use Bearer Token from Token API (1.) in Insomnia Auth Tab (Prefix = Token)
  
  
5.  API to Delete Menu Item (Authentication Required):
  DELETE Method
  http://127.0.0.1:8000/restaurant/menu/#id_of_the_item_to_delete
  - Use Bearer Token from Token API (1.) in Insomnia Auth Tab (Prefix = Token)


6. API to Get Booking List (Authentication Required):
  GET Method
  http://127.0.0.1:8000/restaurant/booking/tables
  - Use Bearer Token from Token API (1.) in Insomnia Auth Tab (Prefix = Token)
