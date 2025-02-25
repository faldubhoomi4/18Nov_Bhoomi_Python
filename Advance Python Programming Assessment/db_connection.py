import pymysql

class DatabaseConnection:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",      # replace with your MySQL username
            password="Bhoomi@4599",      # replace with your MySQL password
            database="hotel_management"
        )
        self.cursor = self.conn.cursor()

    def insert_guest(self, name, address, check_in_date, total_bill):
        query = "INSERT INTO guests (name, address, check_in_date, total_bill) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, address, check_in_date, total_bill))
        self.conn.commit()

    def get_all_guests(self):
        query = "SELECT * FROM guests"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_guest(self, guest_id):
        query = "DELETE FROM guests WHERE guest_id = %s"
        self.cursor.execute(query, (guest_id,))
        self.conn.commit()

    def update_checkout(self, guest_id, check_out_date, total_bill):
        query = "UPDATE guests SET check_out_date = %s, total_bill = %s WHERE guest_id = %s"
        self.cursor.execute(query, (check_out_date, total_bill, guest_id))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
