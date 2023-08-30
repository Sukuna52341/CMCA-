CommandLine Simple Library Management System

The Library Management System is a Python program that allows different users, such as librarians, lecturers, and students, to interact with a library database. Users can perform various operations like displaying available books, searching for books, adding books, deleting books, updating books, requesting books, and adding book categories.

Requirements

Python 3.x
mysql-connector-python package
Installation and Setup
Install Python: If you don't have Python installed, you can download it from the official Python website and follow the installation instructions specific to your operating system.

Install mysql-connector-python: Open a command prompt or terminal and run the following command to install the required package:


Copy
pip install mysql-connector-python
```

Database Setup: Before running the program, you need to set up a MySQL database and configure the connection details in the code. Follow these steps:

Install and configure MySQL Server.
Create a new database named "books".
Create the required tables by executing the following SQL script or using a MySQL client:
sql
Copy
CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  category VARCHAR(255)
);

CREATE TABLE requests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  book_id INT,
  user_id INT,
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255)
);
Update Database Connection Details: In the Python code, locate the connect_to_database() function and modify the connection details according to your MySQL configuration. Update the user, password, and database fields as necessary.

Usage
Run the Program: Open a command prompt or terminal, navigate to the directory where the Python script is located, and run the following command:

Copy
python main1.py
User Login: The program will display a login menu. Enter the appropriate credentials for the desired user type:

Librarian: Username = "lib", Password = "libpass"
Lecturer: Username = "lec", Password = "lecpass"
Student: Username = "stud", Password = "studpass"
Menu Options: After successful login, the user will see a menu with different options. Choose the desired option by entering the corresponding number.

Perform Operations: Depending on the selected menu option, follow the prompts to perform operations like displaying available books, searching for books, adding books, deleting books, updating books, requesting books, or adding book categories.

Exit: To exit the program, select the "Exit" option from the main menu.

Contributing
Contributions to this Library Management System project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
# CMCA-
