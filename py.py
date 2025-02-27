import json

# Cargar el JSON
data = [
    
]

# Modificar el campo "FECHA REGISTRO" para que solo contenga el año
for entry in data:
    fecha = entry["FECHA REGISTRO"]
    if "T" in fecha:  # Si la fecha tiene formato ISO (con hora)
        entry["FECHA REGISTRO"] = fecha.split("-")[0]  # Extraer solo el año
    else:  # Si la fecha tiene formato "MM/DD/YYYY HH:MM:SS AM/PM"
        entry["FECHA REGISTRO"] = fecha.split("/")[2].split(" ")[0]  # Extraer solo el año

    # Renombrar el campo "GÉNERO" a "GENERO" sin tilde
    if "GÉNERO" in entry:
        entry["GENERO"] = entry.pop("GÉNERO")

# Guardar el JSON modificado
with open("emprendimiento_juvenil_modificado.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON modificado guardado con éxito.")
