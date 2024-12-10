import couchdb


adr = 'localhost:3001'
pwd = 'A12345'

# Verbindung zur CouchDB-Instanz herstellen (passe die URL an)
couch = couchdb.Server('http://qgis:' + pwd + '@' + adr)

# Datenbank auswählen oder erstellen
db_name = 'idai-field'
try:
    db = couch[db_name]
except couchdb.http.ResourceNotFound:
    db = couch.create(db_name)

# Dokument hinzufügen
doc = {'name': 'Burak D', 'alter': 36, 'stadt': 'Istanbul'}
db.save(doc)

# Dokument nach ID abrufen
doc_id = doc['_id']  # Die ID wird beim Speichern automatisch vergeben
retrieved_doc = db[doc_id]
print(retrieved_doc)

# Dokument aktualisieren
retrieved_doc['alter'] = 36
db.save(retrieved_doc)

# Alle Dokumente ausgeben
for doc in db:
    print(doc)

# Dokument löschen
db.delete(retrieved_doc)

# Einfache Abfrage (alle Dokumente mit "Istanbul" finden)
for doc in db:
    if 'stadt' in doc and doc['stadt'] == 'Istanbul':
        print(doc)

# View erstellen (für effizientere Abfragen)
# (Erstelle zuerst eine Design-Dokument mit einer Map-Funktion in CouchDB)
design_doc = db.save({'views': {'by_city': {'map': 'function(doc) { if (doc.stadt) { emit(doc.stadt, doc); } }'}}})

# View verwenden
view_results = db.view(design_doc['id'] + '/by_city')
for row in view_results:
    print(row.key, row.value)