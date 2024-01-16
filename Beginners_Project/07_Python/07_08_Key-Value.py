# Exercise 1
# Create a dictionary with keys and values
my_dict = {
    "First name": "Casper",
    "Last name": "Velzen",
    "Job title": "Learning coach",
    "Company": "Techgrounds"
}

# Loop over the dictionary and print every key-value pair
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Exercise 2
    
import csv
import os

# Function to get user information
def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    job_title = input("Enter your job title: ")
    company = input("Enter your company: ")
    return {
        "First name": first_name,
        "Last name": last_name,
        "Job title": job_title,
        "Company": company
    }

# Function to write information to a CSV file
def write_to_csv(data):
    file_exists = os.path.isfile("user_info.csv")

    with open("user_info.csv", mode="a", newline="") as csv_file:
        fieldnames = ["First name", "Last name", "Job title", "Company"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created

        writer.writerow(data)

# Get user information
user_info = get_user_info()

# Write user information to a CSV file
write_to_csv(user_info)
