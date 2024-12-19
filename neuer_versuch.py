import couchdb

adr = 'localhost:3001'
pwd = input("put your pwd: ")
db_name = 'idai-field'
ressource = 'testprojekt-2'

notworking = True

while notworking:
# Verbindung zur CouchDB-Instanz herstellen (passe die URL an)
    couch = couchdb.Server('http://qgis:' + pwd + '@' + adr)
# Datenbank auswählen oder erstellen

# def fehlermeldungen(meldungen): /TODO

    try:
        db = couch[db_name]

# Hier wäre dann sinnvoll, das Script kontrolliert zu stoppen sofern das Projekt nicht existiert.    
    except couchdb.http.ResourceNotFound:   
        print("Project does not exist.")

# das einloggen ist nicht möglich, weil das Passwort falsch ist.
    except couchdb.http.Unauthorized:       
        print("Password is wrong")
        pwd = input("put your pwd again: ")

# der Server hat irgendwelche probleme
    except couchdb.http.ServerError:
        print("ServerError")
        quit()

# wenn Field nicht läuft soll dieser block fragen ob es läuft oder nicht
    except ConnectionRefusedError:
        print("is Field running ? "+ "\n" + "yes or no ?")
        trying = input(": ")
        if trying == "yes":
            print("try again")
        elif trying == "":
            print("there is an empty space")
        else: 
            trying == "no"
            print("Field doesnt running")
            break    
    else:
        notworking = False


print(db)
print("-------------")
# Gut - jetzt macht das Script danach natürlich weiter und wirft andere Fehler...
# Du könntest recherchieren, wie man das Script dann im Falle eines Fehler an dieser Stelle stoppt
# oder sogar um einen Input in der Command-Line bittet, zB nach einem neuen Passwort - falls das falsche eingegeben wurde! 

# Dokument hinzufügen
# Das wollen wir nicht machen, da wir ja nur auf die Projektdatenbank, die schon existiert, zugreifen wollen!
# doc = {}
# db.save(doc)

# Dokument nach ID abrufen
# doc_id = doc['_id']  # Die ID wird beim Speichern automatisch vergeben
# retrieved_doc = db[doc_id]
# print(retrieved_doc)

# Dokument aktualisieren
# retrieved_doc['alter'] = 36
# db.save(retrieved_doc)

# Wir wollen keine neuen docs erstellen und abrufen, sondern nur schon bestehende docs angucken!

# Alle Dokumente ausgeben
for docid in db:
    print(docid)
    retrieved_doc = db[docid]
# print(retrieved_doc)
    
# print("Und jetzt nur die 'resource' in dem Document:")
# print(retrieved_doc['resource'])

# print("Und jetzt nur die 'identifier' aus jedem Document:")
# print('Ein identifier in der Datenbank:')
# print(retrieved_doc['resource']['identifier'])
                                                        
# Das hier wird nicht funktionieren, weil es nicht überall funktioniert: 
# Versuch mal einen Weg zu finden, wie du zB mit try (wie oben) diesen Fehler umgehen kannsT!
    try:
        print(retrieved_doc['resource']['description'])
    except: 
        print("resource has no description")
    finally:
        print("------------------------------------\n")

# Lesetipp: Dictionaries / dict in Python und wie man auf keys etc. zugreift

# Einfache Abfrage (alle Dokumente mit "Istanbul" finden)
# for doc in db:
#    if 'stadt' in doc and doc['stadt'] == 'Istanbul':
#       print(doc)

# View erstellen (für effizientere Abfragen)
# (Erstelle zuerst eine Design-Dokument mit einer Map-Funktion in CouchDB)
#design_doc = db.save({'views': {'by_city': {'map': 'function(doc) { if (doc.stadt) { emit(doc.stadt, doc); } }'}}})
# Design docs sind eine andere, etwas kompliziertere Sache, die du für's Erste ignorieren solltest.

# View verwenden
# view_results = db.view(design_doc['id'] + '/by_city')
# for row in view_results:
#    print(row.key, row.value)



#    while not couchdb : 
#        print("is Field running ?")
#        answer= input("yes or no ? : ")#

#        if answer == "yes":
#            print("try again : ")#
#
#        elif answer == "no":
#            couchdb = True
#            print("Field doesnt running")