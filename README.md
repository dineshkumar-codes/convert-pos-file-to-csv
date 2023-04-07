# convert-pos-file-to-csv
Extracts latitude, longitude, and height values from POS file (generated after post-processing) and saves it to a CSV file. 

## purpose
This python script generates CSV file from POS file (which is generated after post-processing using emlid studio). This script saves lot of time by automating the csv generation where previously this process was done manually using excel. Later the generated csv file is plotted on google earth along with kml to check the mapped area is fully covered.

## how to use?
Edit the **width size** (number of characters) and **starting position** according to your POS file

Width size - In the sample.pos file there are 12 characters for Latitude and Longitude values, and 8 characters for height. 

 `COL_WIDTHS = [12,12,8]`

Starting position - Latitude value starts after `26` characters from the left corner. Similarly Longitude - `41` and Height - `56`

`START_POS = [26,41,56]`

Keep the POS file in the same directory and run the script. It will create a new folder named "output" and adds the CSV file.
