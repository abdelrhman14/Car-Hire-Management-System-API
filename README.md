# Car-Hire-Management-System-API
![ERD  Car Hire Management System  (1)](https://user-images.githubusercontent.com/42601017/222050740-f3997cf4-6167-476b-80fd-f89569b274c0.png)

1- An Endpoint to get all Customer : http://127.0.0.1:5000/retrieve_all_customer/

2- An Endpoint to get Customer : http://127.0.0.1:5000/customer/<int:customer_id>/

3- An Endpoint to Create Customer : http://127.0.0.1:5000/add_customer/

4- An Endpoint to Create Update : http://127.0.0.1:5000/update_customer/<int:customer_id>

5- An Endpoint to Create Delete : http://127.0.0.1:5000//del_customer/<int:customer_id>/

### Lib:

1- pip -3 -m venv venv

2- pip install flask

3- pip install pycopg2

4- python -m pip freez > requirments.txt

5 - python app.py \ flask run
