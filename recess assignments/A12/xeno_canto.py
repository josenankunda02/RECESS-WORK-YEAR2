print('this will give a list with duplicates')
"""import requests

url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = [recording["sp"] for recording in data["recordings"]]
        print(species_list)
else:
    print("Error: Unable to fetch data from the API.")
"""

print('this will give a list without duplicates')
"""
import requests

url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"] for recording in data["recordings"]})
        print(species_list)
else:
    print("Error: Unable to fetch data from the API.")
"""


print('this will give a list without duplicates in the csv file')

"""
import requests
import csv

url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"] for recording in data["recordings"]})

        # Specify the file path for the CSV file
        csv_file_path = "species_list.csv"

        # Write the species_list to the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Species"])  # Write header row
            writer.writerows([[species] for species in species_list])  # Write species names row by row

        print("Data saved to CSV file successfully.")
else:
    print("Error: Unable to fetch data from the API.")
"""



print('please modify this to so that you be creative enough to do more with the API https://xeno-canto.org/explore/api \nbecause the trick is on playing around with the query parameters')