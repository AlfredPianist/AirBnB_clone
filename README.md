# AirBnB_clone
![Foo](https://raw.githubusercontent.com/AlfredPianist/AirBnB_clone/master/img/65f4a1dd9c51265f49d0.png)
## Description

This project is a limited clone of the AirBnB website. And, this release
is only focused on the data storage engine.

In the last version, the expected clone will have:

* A command interpreter to manipulate data without a visual interface / Status: In proccess.
* A website (the front-end) that shows the final product to everybody / Status: To do.
* A database or files that store data (data = objects) / Status: To do.
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them) / Status: To do

---

## Console
This is a command interpreter to manipulate data without
a visual interface (perfect for development and debugging).

### How to use

- **No interactive mode:**

    ```
    $ echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) 
    $
    ```

- **Interactive mode:**

    ```
    $ ./console.py
    ```

    On this mode the console displays a prompt wating for input:

    ```
    $ ./console.py
    (hbnb) 
    ```

    To exit enter the command `quit`, or input an EOF signal 
    (`ctrl-D`).

    ```
    $ ./console.py
    (hbnb) quit
    $
    ```

    ```
    $ ./console.py
    (hbnb) EOF
    $
    ```

### Commands

This console supports the folow commands:

- **create:** `create <class>`
- **show:** `show <class> <id>` or `<class>.show(<id>)`
- **destroy:** `destroy <class> <id>` or `<class>.destroy(<id>)`
- **all:** `all` or `all <class>` or `<class>.all()`
- **count:** `count <class>` or `<class>.count()`
- **update:** `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(<id>, <attribute dictionary>)`

---

## Authors

* **Alfredo Delgado Moreno** - [AlfredPianist](https://github.com/AlfredPianist)
* **Jaime Andres Aricapa** - [Jaricapa-holberton](https://github.com/Jaricapa-holberton)