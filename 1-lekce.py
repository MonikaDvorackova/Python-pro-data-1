
# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známky z daného předmětu. pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematika a dějepis). Vypiš obsah slovníku pomocí funkce print(.)


schoolReport = {"Český jazyk": 1, "Matematika": 2, "Dějepis": 3}
print(schoolReport)


# Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů: 

sales = {
  "Zkus mě chytit": 4165, 
  "Vrah zavolá v deset": 5681, 
  "Zločinný steh": 2565,
}

# Zkopíruj si slovník do svého programu. Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena  na trh a je tedy prodáno "0" kusů. U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o "100".

sales = {
  "Zkus mě chytit": 4165,
  "Vrah zavolá v deset": 5681,
  "Zločinný steh": 2665, 
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100

# kontrola:
print(sales)


# V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

# Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na `int`!
# Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text `"Bohužel nevyhráváš nic."` Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.
# Odeber výhru pro daný lístek ze slovníku, abychom tam evidovali pouze nevydané ceny.


tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

number = int(input("Zadejte číslo lístku: "))
if number in tombola:
  # Zde je jedna věc, co jsem neřekl v kurzu. Funkce pop odstraní hodnotu ze slovníku
  # a tuto odstraňovanou hodnotu vrací, můžeme ji tedy uložit do proměnné a nemusíme načítat
  # výhru pomocí hranatých závorek.
  win = tombola.pop(number)
  print(f"Vyhráváš: {win}.")
else:
  print("Bohužel nevyhráváš nic.")
  
  
# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, 
# které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, 
# zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. 
# Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."


passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name = input("Zadej jméno: ")
if name in passwords:
  password = input("Zadej heslo: ")
  if password == passwords[name]:
    print("Smíš vstoupit.")
  else:
    password = input("Nesprávné heslo. Zadej heslo znovu: ")
    if password == passwords[name]:
      print("Smíš vstoupit.")
    else:
      print("Neznáš heslo, vstup zakázán.")
else:
  print("Nejsi na seznamu hostů.")
