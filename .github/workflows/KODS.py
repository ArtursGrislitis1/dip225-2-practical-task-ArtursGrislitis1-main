import pandas # Importē pandas bibliotēku 

# Nolasīt datus no Excel faila
fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # Izmanto pandas lasīšanas funkciju, lai importētu datus no Excel faila
info_list = fails.values.tolist() # Pārveido datus par sarakstu

# Ievadīt reģiona nosaukumu
get_info = input('Kāds reģions?') # Pieprasa lietotājam ievadīt reģiona nosaukumu

# Atrast reģiona ID
reg_id = 0 # Inicializē mainīgo reg_id ar vērtību 0
for row in info_list: # Iterē cauri katrai rindai info_list sarakstā
    if row[1] == get_info: # Pārbauda, vai ievadītais reģiona nosaukums sakrīt ar kādas rindas 2. kolonnas vērtību
        reg_id = row[0] # Ja sakrīt, iestata reg_id kā šīs rindas 1. kolonnas vērtību
        break # Iziet no cikla, kad reģiona ID ir atrasts

if reg_id == 0: # Ja reg_id paliek 0, tas nozīmē, ka reģions nav atrasts
    print('0') # Izdrukā ziņojumu, ka reģions nav atrasts
    exit() # Iziet no programmas

# Nolasīt datus no CSV faila
CleanData = pandas.read_csv('data.csv').values.tolist() # Izmanto pandas lasīšanas funkciju, lai importētu datus no CSV faila, un pārveido tos par sarakstu

# Aprēķināt ģeogrāfisko punktu skaitu
geo_count = [] # Inicializē tukšu sarakstu geo_count
for line in CleanData: # Iterē cauri katrai rindai CleanData sarakstā
    if line[1] == reg_id: # Pārbauda, vai rindas 2. kolonnas vērtība sakrīt ar reg_id
        geo_count.append(int(line[3])) # Ja sakrīt, pievieno rindas 4. kolonnas vērtību (konvertētu uz veselu skaitli) geo_count sarakstam

print(sum(geo_count)) # Izdrukā geo_count saraksta vērtību summu
