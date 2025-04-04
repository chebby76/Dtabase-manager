import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",  # replace with your MySQL username
        password="your_password",  # replace with your MySQL password
        database="my_database"
    )

def add_user(name, email):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    cursor.close()
    db.close()
    print("User  added successfully.")

def view_users():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    for (id, name, email) in cursor.fetchall():
        print(f"ID: {id}, Name: {name}, Email: {email}")
    cursor.close()
    db.close()

def update_user(user_id, name, email):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    db.commit()
    cursor.close()
    db.close()
    print("User  updated successfully.")

def delete_user(user_id):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    cursor.close()
    db.close()
    print("User  deleted successfully.")

def main():
    while True:
        print("\nDatabase Manager")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            view_users()
        elif choice == '3':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_user(user_id, name, email)
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
