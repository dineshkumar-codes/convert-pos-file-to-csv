import csv
import os

# Define the column widths for the fixed-width file
COL_WIDTHS = [12, 12, 8]

# Define the starting positions for each column
START_POS = [26, 41, 56]


for file in os.listdir():
    if os.path.isfile(file) and file.endswith('.pos'):
        with open(file, 'r') as f:
            # Advance the iterator to skip the first 10 rows
            for i in range(10):
                next(f)
            
            data = []
            for line in f:
                # Extract the values from each line based on the defined column widths and starting positions
                values = []
                for start, width in zip(START_POS, COL_WIDTHS):
                    value = line[start:start+width].strip()
                    values.append(value)  
                    
                # Append the extracted latitude, longitude and height values to a variable
                data.append({'latitude': values[0], 'longitude': values[1], 'height': values[2]})
        
        # Create CSV file and write the values 
        if not os.path.exists("./output"):
            os.mkdir("./output")
            with open(f'./output/{os.path.splitext(file)[0]}.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['latitude', 'longitude', 'height'])
                writer.writeheader()
                writer.writerows(data)
        else:
            with open(f'./output/{os.path.splitext(file)[0]}.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['latitude', 'longitude', 'height'])
                writer.writeheader() 
                writer.writerows(data)