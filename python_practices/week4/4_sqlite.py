import sqlite3

bag = sqlite3.connect("a.vt")
# Tabloya bağlandık

cursor = bag.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)")
bag.commit()

bag.close()