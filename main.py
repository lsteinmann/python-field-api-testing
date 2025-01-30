# json.dumps(): Converts a Python object into a JSON string. / konvertiert einen Python Objekt in eine JSON Zeichenkette
# json.loads(): Converts a JSON string into a Python object. / konvertiert eine JSON Zeichenkette in ein Python Objekt
#---------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json

status_code = True
url = "http://localhost:3001"
check_status = False

# def check_status():
#     print("Checking status...")
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print("Field Desktop is running")
#             return response.status_code
#         else:
#             print(f"Field Desktop returned status code: {response.status_code}")
#             return response.status_code
#     except requests.ConnectionError:
#         print("Field Desktop is not running")
#         return False

# if not check_status():
#     print("Please start Field Desktop before continuing")
#     exit() 

username = input("Enter username: ")
password = input("Enter password: ")

url = f"http://{username}:{password}@localhost:3001"

# Zeige alle Datenbanken an
dbs = requests.get(f"{url}/_all_dbs").json()

#blendet "_repliicator" aus, da diese Datenbank nicht angezeigt werden soll
print("--------------------")
for db in dbs:
    if db !="_replicator": 
        print(f"{db}")
print("--------------------")

#Benutzer wählt eine Datenbank aus
select_db = (input("\nSelect database: "))

# Hier definieren wir einen 'query' für die Datenbank. Wie das funktioniert kannst du
# auch unter localhost:3001/_utils ausprobieren, indem du dort auf ein Datenbankprojekt klickst und dann 
# links 'Run a Query with Mango' auswählst. 
# Das ist hier dokumentiert: https://docs.couchdb.org/en/stable/api/database/find.html#
# Aber auch ChatGPT kann dir erklären, wie genau das funktioniert. Du musst dafür nur das Datenmodell von Field
# ganz gut verstehen (= alles, was innerhalb von "resource" ist).
                                                                    #TODO hier ein Auswahlmenü erstellen-liste erstellt, nun muss  nur noch die Auswahl geschrieben werden
query = {
    "selector": {
        "_id": {
      "$gt": "0"
    }
  }
}

# Spiel auch hiermal mal herum, um unterschiedliche DInge herauszubekommen oder andere Anfragen zu stellen
# es ist wichtig, dass du lernst, wie diese queries funktionieren, da wir ohne die das plugin nicht bauen
# können

# Hier schicken wir dann statt mit get() nun mit post() eine besondere Anfrage an die API
# das ist der query, den wir oben geschrieben haben
response = requests.post(f'{url}/{select_db}/_find', json = query)

# das muss mit "post" passieren, weil wir ja nicht nur sehen wollen, was unter einer bestimmten 
# Adresse *immer* angezeigt wird, sondern wir mit pouchdb reden wollen, d.h. 
# wir "schicken" auch etwas (den query) an pouchdb

# Hier machen wir den response zu einem python dictionary:
result = response.json()
print("--------------------")

# Und nun versuch mal, alle "documents" da raus zu bekommen und dann aus allen 
# documents irgendwas, das du sehen möchtest, in der Konsole anzeigen zu lassen: 

docs = result["docs"]

for doc in docs:
    print(doc["_id"][:10])
print("--------------------")

select_query = (input("\nSelect query: "))
print(docs[int(select_query)])

