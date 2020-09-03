import sqlite3


comm = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email ='update@update.com'"
update_cursor = comm.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print("\nAre connections the same: {}\n".format(update_cursor.connection == comm))

update_cursor.connection.commit()
update_cursor.close()

for row in comm.execute("SELECT * FROM contacts"):
    print(row)

comm.close()