from db_connection import DatabaseConnection
from datetime import datetime

class HotelManagement:
    def __init__(self):
        self.db = DatabaseConnection()

    def check_in(self, name, address, check_in_date, total_bill):
        self.db.insert_guest(name, address, check_in_date, total_bill)

    def display_guests(self):
        guests = self.db.get_all_guests()
        for guest in guests:
            print(f"ID: {guest[0]}, Name: {guest[1]}, Address: {guest[2]}, Check-in Date: {guest[3]}, Bill: {guest[5]}")

    def check_out(self, guest_id, check_out_date, total_bill):
        self.db.update_checkout(guest_id, check_out_date, total_bill)

    def remove_guest(self, guest_id):
        self.db.delete_guest(guest_id)

    def close_db(self):
        self.db.close()
