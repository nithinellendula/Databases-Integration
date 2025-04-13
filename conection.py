import mysql.connector as my
import cx_Oracle as cx
import psycopg2 as pg

def insert_data(db, db_config, tbl, data):
    cnt = None
    try:
        if db == 'mysql':
            cnt = my.connect(**db_config)
            cursor = cnt.cursor()
        elif db == 'postgres':
            cnt = pg.connect(**db_config)
            cursor = cnt.cursor()
        elif db == 'oracle':
            cnt = cx.connect(**db_config)
            cursor = cnt.cursor()
        else:
            raise ValueError("Enter correct database type")

        # Loop through each row of data and insert into the destination table
        for row in data:
            print(f"Inserting row: {row}")  # Debug: Print the row being inserted

            # For Oracle, make sure to match column names and number of placeholders
            if db == 'oracle':
                # Assuming columns in 'student' table are 'id, name, address, marks'
                cursor.execute(f"INSERT INTO {tbl} (sid, sname, saddress, marks) VALUES (:1, :2, :3, :4)", row)
            else:
                # For MySQL/PostgreSQL, assuming same columns for 'student' table
                cursor.execute(f"INSERT INTO {tbl} (sid, sname, saddress, marks) VALUES (%s, %s, %s, %s)", row)

        # Commit the transaction
        cnt.commit()

    except (my.Error, cx.Error, pg.Error) as e:
        print("Value Error:", e)
    finally:
        if cnt:
            cursor.close()
            cnt.close()

def select_data(db, db_config, tbl):
    try:
        # Establish connection based on the database type
        if db == 'mysql':
            cnt = my.connect(**db_config)
            cursor = cnt.cursor()
        elif db == 'postgres':
            cnt = pg.connect(**db_config)
            cursor = cnt.cursor()
        elif db == 'oracle':
            cnt = cx.connect(**db_config)
            cursor = cnt.cursor()
        else:
            raise ValueError("Enter correct database type")

        # Execute the query and fetch results
        cursor.execute(f"SELECT * FROM {tbl}")
        res = cursor.fetchall()
        return res
    except (my.Error, cx.Error, pg.Error) as e:
        print("Value Error:", e)
        return None
    finally:
        if cnt:
            cursor.close()
            cnt.close()


def tnsfr_data(s, s_config, d, d_config, tbl):
    # Fetch data from source database
    src = select_data(s, s_config, tbl)
    if src is None:
        print("Data not fetched")
    else:
        print(f"Fetched data: {src}")  # Debug: Print the data being fetched
        # Insert data into destination database
        insert_data(d, d_config, tbl, src)

        # Query the destination table to confirm the transfer
        transferred_data = select_data(d, d_config, tbl)
        if transferred_data:
            print(f"Transferred Data from {tbl}:")
            for row in transferred_data:
                print(row)
        else:
            print("No data found in the destination table.")


def main():
    my_config = {
        'host': "localhost",
        'user': "root",
        'password': "root",
        'database': "db1"
    }
    pg_config = {
        'host': "localhost",
        'user': 'postgres',
        'password': "post",
        'database': "db1"
    }
    cx_config = {
        'user': 'system',
        'password': "root",
        'dsn': cx.makedsn('localhost', 1521, service_name='ORCL')  # Example service name
    }

    # Input for source and destination database
    src_db = input("Source databases are 1.mysql\n2.postgres\n3.oraclemysql\nEnter database: ").lower()
    dest_db = input("Destination Database are 1.mysql\n2.Postgres\n3.Oracleoracle\nEnter database: ").lower()
    table = input("Enter Table name: ")

    # Assign configuration based on user input
    try:
        if src_db == 'mysql':
            src_config = my_config
        elif src_db == 'postgres':
            src_config = pg_config
        elif src_db == 'oracle':
            src_config = cx_config
        else:
            print("Invalid source database selection")
            return
    except (my.Error, pg.Error, cx.Error) as e:
        print("Error while setting source config:", e)
        return

    try:
        if dest_db == 'mysql':
            dest_config = my_config
        elif dest_db == 'postgres':
            dest_config = pg_config
        elif dest_db == 'oracle':
            dest_config = cx_config
        else:
            print("Invalid destination database selection")
            return
    except (my.Error, pg.Error, cx.Error) as e:
        print("Error while setting destination config:", e)
        return

    # Transfer data from source to destination
    tnsfr_data(src_db, src_config, dest_db, dest_config, table)


if __name__ == "__main__":
    main()
