# CSC6302 Week 5 Project

This is a Python-based GUI app that manages the Merrimack River Cruise (MRC) MySQL database. It provides funtionality for interacting with the database.

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- tabulate
- tkinter

## Project Structure

- ReganMRCapplication
    - view.py
    - BLL.py
    - DAL.py
    - README.md

## Install Dependencies

On macOS:

```bash
pip3 install mysql-connector-python tabulate tkinter
```

## Running the Application

 On macOS, start the application by opening the terminal, navigating to the project directory, and running the following command:

```bash
python3 view.py
```

The interface will prompt you to enter the password for the MRC database to establish a connection. You may need to change the username, host, or port input as well.

You can then select options from menu to run the application. Ensure proper formatting of inputs, especially for date and time inputs (yyyy-mm-dd hh:mm:ss).

## Author

This project was created by Danny Regan as part of Professor Amanda Menier's Database Principles course at Merrimack College.