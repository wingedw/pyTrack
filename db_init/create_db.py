import sqlite3


def main():
    conn = sqlite3.connect('../pytrack.db')
    cursor = conn.cursor()
    # Employee_details table created in the database employee
    cursor.execute("""CREATE TABLE Users (Id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    First_Name varchar, 
                    Last_Name varchar, 
                    Status varchar, 
                    Level varchar)""")
    cursor.execute("""CREATE TABLE Issues (Id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    Subject varchar,
                    Description varchar, 
                    Issue_Type varchar, 
                    Priority varchar,
                    Category varchar,
                    Status varchar,
                    Project varchar,
                    Assignee varchar,
                    Version integer,
                    Time_Estimate integer,
                    Due_Date date,
                    Created_date date)""")
    conn.close()


if __name__ == "__main__":
    main()
