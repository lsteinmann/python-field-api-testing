# json.dumps(): Converts a Python object into a JSON string. / konvertiert einen Python Objekt in eine JSON Zeichenkette
# json.loads(): Converts a JSON string into a Python object. / konvertiert eine JSON Zeichenkette in ein Python Objekt
#---------------------------------------------------------------------------------------------------------------------------------------------

import requests
import json

notworking = False
status_code = True
url = "http://localhost:3001"

def Statusueberpruefung ():  
    try: 
        field_status = requests.get(url).json()
    except: 
        notworking = True

    if notworking == True:
        print("Server nicht erreichbar")
    else:
        print(field_status["status"])

if Statusueberpruefung == 200: 
    print("Request was successful!") 
    print(Statusueberpruefung.json()) 
else:
    print("Something went wrong!")

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