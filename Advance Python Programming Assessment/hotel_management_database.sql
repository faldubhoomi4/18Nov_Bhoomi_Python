CREATE database hotel_management;
USE hotel_management;
CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    check_in_date DATE,
    check_out_date DATE,
    total_bill DECIMAL(10, 2)
);

