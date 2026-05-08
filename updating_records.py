import pyodbc
import customtkinter

# Setup appearance for the GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x500")
app.title("Update Table")

# Entry for table name, ID, and Name
entry_table_name = customtkinter.CTkEntry(app, placeholder_text="Table name")
entry_table_name.place(relx=0.2, rely=0.1)

entry_id = customtkinter.CTkEntry(app, placeholder_text="ID")
entry_id.place(relx=0.2, rely=0.2)

entry_name = customtkinter.CTkEntry(app, placeholder_text="Name")
entry_name.place(relx=0.2, rely=0.3)


def update():
    try:
        # Establish database connection
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=RITHUL-DESKTOP\\EDUREKA;' +
                                    'database=company;' +
                                    'Trusted_Connection=yes')
        connection.autocommit = True
        cursor = connection.cursor()

        # Check if the record exists first
        cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
        data = cursor.fetchone()  # Fetch a single record

        if data:
            # If data exists, perform the update
            cursor.execute(f"UPDATE {entry_table_name.get()} "
                           f"SET name = '{entry_name.get()}' "
                           f"WHERE id = {entry_id.get()}")
            info_label.configure(text="Update Completed")
        else:
            info_label.configure(text="ID not found!")

    except pyodbc.Error as ex:
        print("Failed", ex)
        info_label.configure(text="Failed")


update_button = customtkinter.CTkButton(app, text="Update",
                                        command=update,
                                        fg_color="red")
update_button.place(relx=0.1, rely=0.4)


def select():
    try:
        # Establish database connection
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=RITHUL-DESKTOP\\EDUREKA;' +
                                    'database=company;' +
                                    'Trusted_Connection=yes')
        cursor = connection.cursor()

        # Fetch the record with the specified ID
        cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")

        data = cursor.fetchone()  # Fetch only one record

        if data:
            info_label.configure(text=f"ID: {data[0]}, Name: {data[1]}")
        else:
            info_label.configure(text="No data found")

    except pyodbc.Error as ex:
        print("Failed", ex)
        info_label.configure(text="Failed")


select_button = customtkinter.CTkButton(app, text="Select",
                                        command=select,
                                        fg_color="green")
select_button.place(relx=0.55, rely=0.4)

info_label = customtkinter.CTkLabel(app, text="INFO", font=('Arial', 25))
info_label.place(relx=0.2, rely=0.5)

app.mainloop()
