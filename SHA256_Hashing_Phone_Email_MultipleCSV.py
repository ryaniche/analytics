import csv
import hashlib
import os

def hash_csv_and_save_new_file(input_file_path, output_file_path):
    with open(input_file_path, mode='r', encoding='utf-8', errors='ignore') as infile, open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        # Write new headers to the output file
        csv_writer.writerow(['PHONE', 'EMAIL'])

        # Skip the header row in the input file
        next(csv_reader)

        for row in csv_reader:
            # Assuming the first column is 'phone' and the second is 'email'
            phone, email = row[0], row[1]
            
            # Hash the phone
            phone_hash = hashlib.sha256(phone.encode()).hexdigest()
            
            # Check if email is "XNA", if so treat it as null (empty string), else hash it
            if email == "XNA":
                email_hash = ''
            else:
                email_hash = hashlib.sha256(email.encode()).hexdigest()
            
            # Write the phone hash and the email hash (or empty string) to the new file
            csv_writer.writerow([phone_hash, email_hash])

import datetime

def process_folder(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get today's date in the format YYYYMMDD
    today_str = datetime.datetime.now().strftime('%Y%m%d')

    # List all CSV files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            input_file_path = os.path.join(input_folder, file)
            
            # Construct output file path by including today's date, original file name, and '_Hashed'
            output_file_name = f"{today_str}_{file.split('.')[0]}_Hashed.csv"
            output_file_path = os.path.join(output_folder, output_file_name)
            
            # Process the file
            hash_csv_and_save_new_file(input_file_path, output_file_path)
            print(f"Processed {input_file_path} -> {output_file_path}")

# Replace these paths with your actual folder paths
input_folder = 'C:\\Users\\linh.nguyenv14\\Desktop\\BAU_WeeklyHashing_Input'
output_folder = 'C:\\Users\\linh.nguyenv14\\Desktop\\BAU_WeeklyHashing_Output'

process_folder(input_folder, output_folder)
