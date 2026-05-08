import pyodbc
import customtkinter

# Setup appearance for the GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x500")
app.title("Delete Data")

# Entry for table name and ID
entry_table_name = customtkinter.CTkEntry(app, placeholder_text="Table name")
entry_table_name.place(relx=0.2, rely=0.1)

entry_id = customtkinter.CTkEntry(app, placeholder_text="ID")
entry_id.place(relx=0.2, rely=0.2)


def select():
    try:
        # Establish database connection
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=RITHUL-DESKTOP\\EDUREKA;' +
                                    'database=master;' +
                                    'Trusted_Connection=yes')

        cursor = connection.cursor()

        a = 0
        # Correct SQL query with proper spaces
        query = f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}"
        cursor.execute(query)

        for data in cursor:
            a = 1
            info_label.configure(text=f"{data[0]} {data[1]}")
        if a == 0:
            info_label.configure(text="No Data")

    except pyodbc.Error as ex:
        print("Failed!", ex)
        info_label.configure(text="No Table")


# Button to trigger the select operation
select_button = customtkinter.CTkButton(app, text="Select", command=select, fg_color="green")
select_button.place(relx=0.2, rely=0.3)


def delete():
    try:
        # Establish database connection
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=RITHUL-DESKTOP\\EDUREKA;' +
                                    'database=master;' +
                                    'Trusted_Connection=yes')

        cursor = connection.cursor()

        # Delete the record based on table name and ID
        query = f"DELETE FROM {entry_table_name.get()} WHERE id = {entry_id.get()}"
        cursor.execute(query)
        connection.commit()

        info_label.configure(text="Data Deleted")

    except pyodbc.Error as ex:
        print("Failed!", ex)
        info_label.configure(text="Delete Failed")


# Button to trigger the delete operation
delete_button = customtkinter.CTkButton(app, text="Delete", command=delete, fg_color="red")
delete_button.place(relx=0.2, rely=0.4)

info_label = customtkinter.CTkLabel(app, text="Company")
info_label.place(relx=0.2, rely=0.5)

app.mainloop()
