# User Administration

This app allows you to manage users and their IBAN, you will login as a Administrator of users, you only can edit/delete users that you created. 

---
## Setup


This is a docker based application, so you will need docker installed in your machine.

To install it you can go to the official documentation: [here](https://docs.docker.com/install/)

Once, you have docker installed, you can just run:

    make server

You can see all the availables commands with:

    make help

---
## Linting

We lint the application with isort and pylint, just run the following command:
    
    make pylint

---
## Test
We use pytest-django to run the tests. Test files names start with test_*.py

To run all the tests, we can just run:

    make test

This creates a new container which will be destroyed after the test command ends.

---
## Contributing
>If you have any doubts or any improvement, you can just open an issue or create a pull request, also you can contact me on: 

>**juanmigabarron@gmail.com**