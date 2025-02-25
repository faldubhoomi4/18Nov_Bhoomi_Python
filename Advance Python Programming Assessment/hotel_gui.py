import tkinter as tk
from tkinter import messagebox
from hotel_management import HotelManagement
from datetime import datetime

class HotelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.hm = HotelManagement()

        # Create the interface elements here
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Guest Name")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_address = tk.Label(self.root, text="Address")
        self.label_address.grid(row=1, column=0)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=1, column=1)

        self.label_check_in = tk.Label(self.root, text="Check-in Date (YYYY-MM-DD)")
        self.label_check_in.grid(row=2, column=0)
        self.entry_check_in = tk.Entry(self.root)
        self.entry_check_in.grid(row=2, column=1)

        self.label_total_bill = tk.Label(self.root, text="Total Bill")
        self.label_total_bill.grid(row=3, column=0)
        self.entry_total_bill = tk.Entry(self.root)
        self.entry_total_bill.grid(row=3, column=1)

        self.check_in_button = tk.Button(self.root, text="Check In", command=self.check_in_guest)
        self.check_in_button.grid(row=4, column=1)

        self.display_button = tk.Button(self.root, text="Display Guests", command=self.display_guests)
        self.display_button.grid(row=5, column=1)

        self.checkout_button = tk.Button(self.root, text="Check Out", command=self.check_out_guest)
        self.checkout_button.grid(row=6, column=1)

        self.remove_button = tk.Button(self.root, text="Remove Guest", command=self.remove_guest)
        self.remove_button.grid(row=7, column=1)

        self.remove_button = tk.Button(self.root, text="Exit", command=self.exit_guest)
        self.remove_button.grid(row=8, column=1)

    def check_in_guest(self):
        try:
            name = self.entry_name.get()
            address = self.entry_address.get()
            check_in_date = self.entry_check_in.get()
            total_bill = float(self.entry_total_bill.get())

            if not name or not address or not check_in_date:
                messagebox.showerror("Error", "All fields are required!")
                return

            # Validate date format
            try:
                datetime.strptime(check_in_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
                return

            self.hm.check_in(name, address, check_in_date, total_bill)
            messagebox.showinfo("Success", "Guest checked in successfully!")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid total bill.")
    
    def display_guests(self):
        self.hm.display_guests()

    def check_out_guest(self):
        try:
            guest_id = int(self.entry_name.get())  # For simplicity, assume the user enters guest ID
            check_out_date = datetime.now().strftime("%Y-%m-%d")
            total_bill = float(self.entry_total_bill.get())

            self.hm.check_out(guest_id, check_out_date, total_bill)
            messagebox.showinfo("Success", "Guest checked out successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def remove_guest(self):
        guest_id = int(self.entry_name.get())  # Assume guest ID is input
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this guest?")
        if confirmation:
            self.hm.remove_guest(guest_id)
            messagebox.showinfo("Success", "Guest removed successfully.")

    def exit_guest(self):
        exit()

    def close(self):
        self.hm.close_db()

def main():
    root = tk.Tk()
    gui = HotelGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
