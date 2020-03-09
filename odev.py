cinsiyet = input("Cinsiyetinizi giriniz: ")
yas = int(input("Yasınızı giriniz: "))
kilo = int(input("Kilonuzu giriniz: "))
boy = int(input("Boyunuzu giriniz(cm): "))
boy = boy/100
indeks = kilo/(boy*boy)
print ("Indeks: " , indeks)
if yas < 18:
    print("Ergen")
elif yas < 65:
    print("Genc")
elif yas < 74:
    print("Genç-Yasli")
elif yas < 84:
    print("Yasli")
elif yas >= 85:
    print("Cok Yasli")
if indeks < 18.5:
    print("Zayıf")
elif indeks < 25:
    print("Sağlıklı")
elif indeks < 30:
    print("Fazla Kilolu")
elif indeks < 35:
    print("1. derece obez")
elif indeks < 40:
    print("2. derece obez")
elif indeks >= 40:
    print("3. derece morbid obez")
if cinsiyet == "erkek":
    erkek = 50 + (2.3 * (((boy*100)/2.54) - 60))
    ideal = (kilo) - (erkek)
    print("Ideal kilonuz yaklaşık: " , round(erkek) , " dir.")
    if ideal > 0:
        print("Yaklaşık " , round(ideal) , " kilo vermeniz gerek.")
    elif ideal < 0:
        print("Yaklaşık " , round(abs(ideal)) , " kilo almanız gerek.")
elif cinsiyet == "kadın":
    kadın = 45.5 + (2.3 * (((boy*100)/2.54) - 60))
    ideal = (kilo) - (kadın)
    print("Ideal kilonuz yaklaşık: " , round(kadın) , " dir.")
    if ideal > 0:
        print("Yaklaşık " , round(ideal) , " kilo vermeniz gerek.")
    elif ideal < 0:
        print("Yaklaşık " , round(abs(ideal)) , " kilo almanız gerek.")