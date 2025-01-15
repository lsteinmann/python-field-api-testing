#http://localhost:3001/_all_dbs

import couchdb
import getpass
from colorama import init,Fore,Style
#import sys

init()

adr = 'localhost:3001'
pwd = getpass.getpass("put your pwd: ")
print("the password is :", pwd)

db_name = input("Please enter the identifier of your project database: ")

# resource = 'testprojekt-2'

#notworking = True

notworking = 1
max_tries = 3

while notworking <= max_tries :

# Verbindung zur CouchDB-Instanz herstellen (passe die URL an)
    couch = couchdb.Server('http://qgis:' + pwd + '@' + adr)
# Datenbank auswählen oder erstellen

# def fehlermeldungen(meldungen): /TODO

    try:
        if db_name == "":
            raise couchdb.http.ResourceNotFound
        elif db_name == " ":
            raise couchdb.http.ResourceNotFound
        else:
            print(db_name)
            db = couch[db_name]

# das Script kontrolliert stoppen sofern das Projekt nicht existiert.    
    except couchdb.http.ResourceNotFound: 
        print("Project " + Fore.RED + Style.BRIGHT + db_name + Style.RESET_ALL +
        " does not exist or there is an empty space."+"\n"+"These are the project databases available on the server: ")
        for item in couch:
            if item != "_replicator":   # Versuch mal, dafür zu sorgen, dass "_replicator" nicht angezeigt wird!
                                        #_replicator wird nicht mehr angezeigt
            
            #ändert die Farbe und macht die Schrift fett um es besser lesen zu können...
                name= item      
                print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{name}{Style.RESET_ALL}")
                # quit()
                notworking += 1
                continue
        else:
            quit()
        
# wird ausgelöst wenn es zu keiner bestimmten Exception gehört 
    except RuntimeError as e:
        print(f"{Fore.RED}there is an Error: {str(e)}{Style.RESET_ALL}")
        erneut_versuchen = input("Do you want to try again? (Y/N): ")
        if erneut_versuchen.lower() != 'y':
            print("the Program is stopping...")
            quit()
        else:
            print("the program is starting again...")
            continue
        
# das einloggen ist nicht möglich, weil das Passwort falsch ist.
    except couchdb.http.Unauthorized:       
        print("Password is wrong")
        pwd = getpass.getpass("put your pwd again: ")

# der Server hat irgendwelche probleme
    except couchdb.http.ServerError:
        print("ServerError")
        quit()

# tritt auf wenn es zu einem SystemFehler kommt / das heißt im Python Interpreter
    except SystemError:
        print("There is a System Error")
        quit()

# kann auftreten wenn der Benutzer auf zwei verschiedene Typen drückt / str und int
    except TypeError:
        print("please just using letters")
        quit()

# kann auftreten wenn Sonderzeichen etc. verwenden sollten
    except UnicodeError:
        print("Please use the formal Letters")
        quit()

# wenn Field nicht läuft soll dieser block fragen ob es läuft oder nicht
    except ConnectionRefusedError:
        
        trying = input("Is Field running? (Y/N) : ")
        if trying == "y" or trying == "Y" :
            print("Trying again...")
        elif trying == "":
            print("This is an empty space. Trying again...")
        else: 
            print("Field is not running.")
            quit()    
    else:
        notworking = 4


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
        print(retrieved_doc['resource']['identifier'])
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