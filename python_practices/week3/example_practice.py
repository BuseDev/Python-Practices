"""
kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini
de bu toplamdan çıkaran ve geri döndüren python fonksiyonu yaz
"""


def polindrom(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(polindrom(10, 101, 55, 40, 9009))