input_bilangan = int(input("Masukkan bilangan yang akan di Tentukan : "))

if input_bilangan > 0 and input_bilangan %2 == 1:
    print(f"{input_bilangan} adalah bilangan Positif (Ganjil)")
elif input_bilangan > 0 and input_bilangan %2 == 0:
    print(f"{input_bilangan} adalah bilangan Positif (Genap)")
elif input_bilangan < 0 and input_bilangan %2 == 1:
    print(f"{input_bilangan} adalah bilangan Negatif (Ganjil)")
elif input_bilangan < 0 and input_bilangan %2 == 0:
    print(f"{input_bilangan} adalah bilangan Negatif (Genap)")
else:
    print(f"{input_bilangan} adalah bilangan Netral")