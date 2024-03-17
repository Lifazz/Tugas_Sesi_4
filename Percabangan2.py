input_a = int(input("Masukan Bilangan a :"))
input_b = int(input("Masukan Bilangan b :"))
input_c = int(input("Masukan bilangan c :"))

if input_b > input_a and input_b > input_a :
    print(f"{input_a} lebih Kecil dari {input_b} dan {input_c} ")
elif input_a > input_b and input_c > input_b :
    print(f"{input_b} Lebih Kecil dari {input_a} dan {input_c} ")
else :
    print(f"{input_c} Lebih Kecil dari {input_a} dan {input_b}")
    