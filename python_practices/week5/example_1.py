"""
1 - veri isimli bir klasör oluşturun
2 - zip dosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştirin
4 - bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""

import os
import zipfile
import pandas as pd
import sqlite3

all_files = os.listdir("veri")
pandas_csv_list = []
for csv_dosya in all_files:
    veri = pd.read_csv("veri/" + csv_dosya)
    del veri["volume"]
    pandas_csv_list.append(veri)

associated_csvs = pd.concat(pandas_csv_list)
associated_csvs.to_csv('hepsi.csv', index=False)

"""
pariteler ---> tablo ismi
id  -----> otomatik artan
otime ----> datetime

________________________
open 
high      -----> float
low       
close 
________________________
"""


if not os.path.exists("veri"):...

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST parite("
                +"id INTEGER PRIMARY KEY AUTOINCREMENT, "
                +"otime DATETIME, open FLOAT, "
                +"high FLOAT, low FLOAT, close FLOAT);")

cursor.execute("INSERT INTO parite(otime, open, high, low, close) VALUES(NULL, 2022-01-01 03:00:00, 46216.93000000, 46731.39000000, 46208.37000000, 46656.13000000)")
bag.commit()
bag.close()
records = pd.read_csv("hepsi.csv")