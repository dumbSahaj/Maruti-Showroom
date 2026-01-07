# Maruti-Showroom
The Car Showroom Management System is a Python-based, terminal-driven application developed as a school project to simulate the basic operations of a car showroom. The main objective of this project is to help a car showroom dealer efficiently manage car inventory and handle sales transactions using a simple and user friendly command line interface

# Requirements 

```bash
pip install tqdm
```

 
## Project Overview

The Maruti Car Showroom Management System is a console-based Python application designed to simulate the operations of a car showroom.
It allows users to:

- Purchase cars from the company

- Sell cars to customers

- View showroom stock

- Store and view customer details

- Maintain showroom balance automatically

This project uses file handling, dictionaries, functions, loops, and modules to manage data efficiently.

## Technologies & Modules Used

**Python 3**

- `time` – for delays and loading effects

- `os` – for directory and file handling

- `pickle` – for data storage and retrieval

- `tqdm` – for loading/progress bars

- `logos` – custom module for ASCII art and menus

## Features

**1 Purchase Cars (Company Stock)**

-  Purchase cars from the manufacturer

- Stock quantity increases

- Balance decreases based on purchase price

**2 Sell Cars to Customers**

- Display available cars

- View detailed specifications

- Apply 18% GST

- Generate bill/invoice

- Store customer details securely

**3 View Showroom Stock**

- Displays all available cars and quantities

- Shows current showroom balance

**4 View Customer Details**

- Displays customer name, Aadhaar number, phone number, and purchased car

**5 Data Persistence**

- Uses pickle files to save:

- Stock data

- Customer details

- Showroom balance

- Data remains intact even after program exit

## How to Run the Project
**Step 1:** Install Required Module
`pip install tqdm`

**Step 2:** Run the Program
`python main.py`


⚠️ Note:

- The program creates a folder C:/maruti automatically.

- Make sure you have permission to create folders on the C: drive.
 ## First-Time Setup

**On first run:**

- A showroom directory is created

- Initial balance is set to ₹10,00,00,000

- Stock quantities are initialized to zero
## Learning Outcomes

- File handling with pickle

- Modular programming

- Menu-driven programs

- Real-world simulation using Python

- Data persistence techniques

## Author

Name: **Sahaj Saxena**

