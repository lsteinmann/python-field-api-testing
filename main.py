# json.dumps(): Converts a Python object into a JSON string. / konvertiert einen Python Objekt in eine JSON Zeichenkette
# json.loads(): Converts a JSON string into a Python object. / konvertiert eine JSON Zeichenkette in ein Python Objekt
#---------------------------------------------------------------------------------------------------------------------------------------------

import requests
import json

status_code = True
url = "http://localhost:3001"
check_status = False

def check_status():
    print("Checking status...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Field Desktop is running")
            return response.status_code
        else:
            print(f"Field Desktop returned status code: {response.status_code}")
            return response.status_code
    except requests.ConnectionError:
        print("Field Desktop is not running")
        return False

if not check_status():
    print("Please start Field Desktop before continuing")
    exit() 

username = input("Enter username: ")
password = input("Enter password: ")

url = f"http://{username}:{password}@localhost:3001"

print("---------------------|")

# Zeige alle Datenbanken an
dbs = requests.get(f"{url}/_all_dbs").json()

#blendet "_repliicator" aus, da diese Datenbank nicht angezeigt werden soll
print("--------------------°")
for db in dbs:
    if db !="_replicator": 
        print(f"{db}")

# Benutzer wählt eine Datenbank aus
select_db = (input("\nSelect database: "))

# Zeige alle Dokumente der ausgewählten Datenbank an
print(requests.get(f"{url}/{select_db}/_all_docs").json())