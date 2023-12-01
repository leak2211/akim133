import sqlite3

db = "base.sqlite"
connection = sqlite3.connect(db)
cursor = connection.cursor()
cursor.execute('''SELECT Name FROM Track 
                LEFT JOIN 'InvoiceLine' ON InvoiceLine.TrackId=Track.TrackId 
                LEFT JOIN 'Invoice' ON InvoiceLine.InvoiceId=Invoice.InvoiceId WHERE CustomerId = 6 ''')

results = cursor.fetchall()

for results in results:
    print(str(results)[1:-1])