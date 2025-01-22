
# json.dumps(): Converts a Python object into a JSON string. / konvertiert einen Python Objekt in eine JSON Zeichenkette
# json.loads(): Converts a JSON string into a Python object. / konvertiert eine JSON Zeichenkette in ein Python Objekt
#---------------------------------------------------------------------------------------------------------------------------------------------

import requests
from colorama import init,Fore,Style

username = input("Enter username: ")
password = input("Enter password: ")
url = f"http://{username}:{password}@localhost:3001"
notworking = True

#---------------------------------------------------------------------------------------------------------------------------------------------

# raise ConnectionRefusedError
# print("Connection refused")

#--------------------------------------------------------------------------------------------------------------------------------------------

# Zeige alle Datenbanken an
dbs = requests.get(f"{url}/_all_dbs").json()

#blendet "_repliicator" aus, da diese Datenbank nicht angezeigt werden soll
print("--------------------")
for db in dbs:
    if db !="_replicator": 
        name = db
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+f"{name}"+Style.RESET_ALL)

# Benutzer wählt eine Datenbank aus
selected_db = (input("\nSelect database: "))
   
# Zeige alle Dokumente der ausgewählten Datenbank an
print(requests.get(f"{url}/{selected_db}/_all_docs").json())

#----------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------

# #Fehlerbehandlung
# while notworking:
#     try:
#         print("--------------------")
#         quit()
#     except ConnectionRefusedError:
#         print("Connection refused. Please check your credentials and try again.")
#         quit()
#     except requests.exceptions.ConnectionError:
#         print("Connection error. Please check your network connection and try again.")
#         quit()
#     except requests.exceptions.Timeout:
#         print("Request timed out. Please try again later.")
#         quit()

#-----------------------------------------------------------------------------------------------------------------------------------------------      
