clients = [" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "", 
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES", "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "]

# deberia imprimir esto
# Lista limpia de clientes al realizar todas las operaciones:
# ['Alejandro González', 'Ana López', 'Andrés Ocampo', 'Carlos Mendes', 'Claudia Torres', 'Damián Castillo', 'Gabriela Ruíz', 'Juan Pérez', 'Laura Ramos', 'Luis Rodríguez', 'Maria Martínez', 'Miguel Ángel', 'Monica Herrera', 'Patricia Vega', 'Pedro Gómez', 'Ricardo Fernández', 'Sandra Morales']


def clean_espacios(name):
    """limpia los espacios extras del nombre del cliente si no es """
    if name:
        name = name.strip() #elimina los espacios al inicio y al final
        name = ' '.join(name.split()) #elimina los espacios extras entre palabras
        return name #retorna el nombre limpio
    else: 
        return None

def conv_tit (name):
    """convierte el nombre a titulo, primera letra con mayuscula y el resto en minusculas"""
    if name:
        name = name.title() #convierte el nombre a titulo
        return name #retorna el nombre en titulo
    else:
        return None


def clean_list(clients):
    clients_cleaned =[] #creo una lista vacia donde voy a guardar la lista corregida
    for data in clients:
        name_cleaned=clean_espacios (data) 
        if name_cleaned: #osea si no es vacio
            name_cleaned= conv_tit (name_cleaned)
            clients_cleaned.append (name_cleaned) #agrego el nombre ya limpio y procesado a la lista
    return clients_cleaned #devuelvo la lista limpia

print(clean_list(clients)) #imprimo el resultado de la funcion

