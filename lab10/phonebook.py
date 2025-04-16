import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="eca11aec3e2b"
)

cur = conn.cursor()

while True:
    print("Phonebook")
    print("1. Add name and phone")
    print("2. Show all")
    print("3. Exit")
    print("4. Update info")
    print("5. Delete info")
    choice = input("Choose number: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s);", (name, phone))
        conn.commit()
        print("Info added.")
    elif choice == "2":
        cur.execute("SELECT * FROM PhoneBook;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif choice == "3":
        cur.close()
        conn.close()
        print("Bye!")
        break
    elif choice == "4":
        name = input("Write old name: ")
        new_name = input("New name : ")
        new_phone = input("New phone : ")

        if new_name:
            cur.execute("UPDATE PhoneBook SET first_name = %s WHERE first_name = %s;", (new_name, name))
        if new_phone:
            cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s;", (new_phone, new_name or name))

        conn.commit()
        print("Info updated.")
    elif choice == "5":
        name = input("Enter name to delete: ")
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s AND phone = %s;", (name, phone))
        conn.commit()
        print("Info deleted.")
    elif choice == "6":
        import csv
        with open("contacts.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row["first_name"]
                    phone = row["phone"]
                    cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s);", (name, phone))
                conn.commit()
                print("CSV data uploaded.")

