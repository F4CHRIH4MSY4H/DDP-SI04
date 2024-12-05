from Gempa import *

# membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.4)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.8)


# Info Gempa
print('## Gempa Bumi Info ##')
print()
gempa1.dampak() # Memanggil Gempa dampak()

print()
print('## Gempa Bumi Info ##')
print()
gempa2.dampak() # Memanggil Method dampak

print()
print('## Gempa Bumi Info ##')
print()
gempa3.dampak() # Memanggil Method dampak

print()
print('## Gempa Bumi Info ##')
print()
gempa4.dampak() # Memanggil Method dampak

print()
print('## Gempa Bumi Info ##')
print()
gempa5.dampak() # Memanggil Method dampak