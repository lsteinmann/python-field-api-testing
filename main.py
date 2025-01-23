
# json.dumps(): Converts a Python object into a JSON string. / konvertiert einen Python Objekt in eine JSON Zeichenkette
# json.loads(): Converts a JSON string into a Python object. / konvertiert eine JSON Zeichenkette in ein Python Objekt
#---------------------------------------------------------------------------------------------------------------------------------------------

import requests
import json

username = input("Enter username: ")
password = input("Enter password: ")
url = f"http://{username}:{password}@localhost:3001"
notworking = input("Is Field running? (Y/N) : ")


print("---------------------|")

#Fehlerbehandlung
while notworking == "n" or notworking == "N" or notworking == "":
    try:
        print("Field does not working\nPlease try again")  
        notworking = input("Is Field running? (Y/N) : ")
                                                            #Ab hier muss noch weiter gearbeitet werden
    except :                                                   
        print("Field is working")
        
# Zeige alle Datenbanken an
dbs = requests.get(f"{url}/_all_dbs").json()

#blendet "_repliicator" aus, da diese Datenbank nicht angezeigt werden soll
print("--------------------°")
for db in dbs:
    if db !="_replicator": 
        print(f"{db}")

# Benutzer wählt eine Datenbank aus
selected_db = (input("\nSelect database: "))

# Zeige alle Dokumente der ausgewählten Datenbank an
print(requests.get(f"{url}/{selected_db}/_all_docs").json())