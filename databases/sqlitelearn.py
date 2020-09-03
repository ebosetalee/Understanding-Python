import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")

# db.execute(
#     "INSERT INTO IF NOT EXITS contacts (name, phone, email) VALUES('Tim', 6474872, 'tims@gmail.com')")

# db.execute("INSERT INTO contacts VALUES('Brian', 23879723, 'brian@gmail')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# for row in cursor:
#     print(row)
# Note: cursor works only once; thus, the need to run the query again.
print("--"* 40)

# use the cursor more than once, you can put it to a list:
# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)


cursor.close()
db.commit()
db.close

# cursors is a generator i.e iterable by generating the
# next value  

db = sqlite3.connect("contacts.sqlite")

for row in db.execute("SELECT * FROM contacts"):
    print(row)

update_sql = "UPDATE contacts SET email ='update@update.com' WHERE contacts.phone = 23879723"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.close()
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*40)

db.close()
# Nothing prints because using Insert or update doesn't stop permanently.
# Thus, we need to commit the changes.