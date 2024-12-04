
# Python-library namens 'couchdb', die dafür da ist, die API der couchDB anzusprechen
# vorher: pip install couchdb
import couchdb
import pandas as pd
import numpy as np
import json
#from couchdbkit import Server
import cloudant
import requests


# Wenn Field läuft, dann findest du sie unter: 
# http://localhost:3001/_utils/
# Name ist egal, Passwort ist das Passwort, dass du in Field Desktop unter "Einstellungen" für den eigenen Synchronisationsdienst gesetzt hast
# 6
#print('hello')

# Das ist unsere Adresse für die CouchDB
adr = 'localhost:3001'
# Das ist jetzt unser Passwort
pwd = 'A12345'
# Hier definieren wir mit der couchdb-library die Verbindung
# Schau dir das hier an: https://github.com/djc/couchdb-python/
# und das hier: https://couchdb-python.readthedocs.io/en/latest/
# Du siehst schon: Das wird nicht mehr gepflegt und wir sollten es daher eigentlich nicht benutzen! 
fieldConnection = couchdb.Server('http://qgis:' + pwd + '@' + adr) # das "qgis" ist dabei der Benutzername

# leerer projects-array
projects = []
# Was ist da überhaupt drin:
# https://couchdb-python.readthedocs.io/en/latest/client.html#server
# This class behaves like a dictionary of databases. For example, to get a list of database names on the server, you can simply iterate over the server object.

# Suchen wir nach irgendwas, das field identifiziert um sicherzugehen, dass wir die richtige db haben:
#print("print(fieldConnection.config()) : ")
#print(fieldConnection.config())

# okay, der Pfad würde helfen: 
#print("..... if ... ")
if "idai-field" in fieldConnection.config()['log']['file']:
    #print('Connected.', 'Can now access Field Desktops project databases.')
    # für j
    # now we iterate over the server object
    for prj in fieldConnection:
        if str(prj) != "_replicator":
            projects.append(str(prj))

#df = pd.read_csv("task.py")
#print(df)

fd = pd.read_csv("orte.csv")
print(fd)

#erstellen einer datenframe mit zufälligen zahlen
data = {'spalteA': np.random.rand(100),
'spalteB': np.random.randint(1,100,100)}
df = pd.DataFrame(data)

#speichere die dataframe als CSV
df.to_csv("meineDaten.csv",index=False)
print(df)

#print(projects)


# Schritt 1, Problem gelöst! 
