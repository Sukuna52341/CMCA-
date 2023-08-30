import mysql.connector

# Function to establish a database connection
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="#Chelsey1234",
        database="books"
    )
    return mydb

# Function to display available books
def display_available_books():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bookt")
    rows = mycursor.fetchall()
    print("Available Books:")
    for row in rows:
        print(row)
    mycursor.close()
    mydb.close()

# Function to search for a book by title or author
def search_book():
    keyword = input("Enter the book title or author: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM bookt WHERE title LIKE %s OR author LIKE %s"
    mycursor.execute(sql, ('%' + keyword + '%', '%' + keyword + '%'))
    results = mycursor.fetchall()
    if len(results) > 0:
        print("Search Results:")
        for row in results:
            print(row)
    else:
        print("No results found")
    mycursor.close()
    mydb.close()

# Function to add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    category = input("Enter the book category: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "INSERT INTO bookt (title, author, category) VALUES (%s, %s, %s)"
    val = (title, author, category)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Book added successfully")
    mycursor.close()
    mydb.close()

# Function to delete a book
def delete_book():
    book_id = input("Enter the book ID to delete: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "DELETE FROM bookt WHERE id = %s"
    val = (book_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Book deleted successfully")
    mycursor.close()
    mydb.close()

# Function to update a book
def update_book():
    book_id = input("Enter the book ID to update: ")
    title = input("Enter the new book title: ")
    author = input("Enter the new author name: ")
    category = input("Enter the new book category: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "UPDATE bookt SET title = %s, author = %s, category = %s WHERE id = %s"
    val = (title, author, category, book_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Book updated successfully")
    mycursor.close()
    mydb.close()

# Function for the librarian menu
def librarian_menu():
    while True:
        print("\nLibrarian Menu:")
        print("1. Display available books")
        print("2. Search for a book")
        print("3. Add a book")
        print("4. Delete a book")
        print("5. Update a book")
        print("6. Add a book category")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_available_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            add_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            add_book_category()
        elif choice == "7":
            break
        else:
            print("Invalid choice")

# Function for the lecturer menu
def lecturer_menu():
    while True:
        print("\nLecturer Menu:")
        print("1. Display available books")
        print("2. Search for a book")
        print("3. Request a book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_available_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            request_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# Function for the student menu
def student_menu():
    while True:
        print("\nStudent Menu:")
        print("1. Display available books")
        print("2. Search for a book")
        print("3. Request a book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_available_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            request_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# Function to request a book
def request_book():
    book_id = input("Enter the book ID to request: ")
    user_id = input("Enter your user ID: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "INSERT INTO requests (book_id, user_id) VALUES (%s, %s)"
    val = (book_id, user_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Book requested successfully")
    mycursor.close()
    mydb.close()

# Function to add a book category
def add_book_category():
    category = input("Enter the book category to add: ")
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "INSERT INTO categories (name) VALUES (%s)"
    val = (category,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Book category added successfully")
    mycursor.close()
    mydb.close()

# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. Librarian Login")
    print("2. Lecturer Login")
    print("3. Student Login")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "lib" and password == "libpass":
            print("Login successful")
            librarian_menu()
        else:
            print("Invalid username or password")
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "lec" and password == "lecpass":
            print("Login successful")
            lecturer_menu()
        else:
            print("Invalid username or password")
    elif choice == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "stud" and password == "studpass":
            print("Login successful")
            student_menu()
        else:
            print("Invalid username or password")
    elif choice == "4":
        break
    else:
        print("Invalid choice")