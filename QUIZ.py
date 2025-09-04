
# Quiz 1
# Cálculo del consumo y almacenamiento de agua en un edificio


# variables generadas:
print("Cálculo del consumo y almacenamiento de agua en un edificio")

consumo_persona = float(input("Ingrese el consumo promedio por persona (Litro/día): "))
personas = int(input("Ingrese la cantidad de personas en el edificio: "))
cap_tanque = float(input("Ingrese la capacidad de cada tanque (Litro): "))
eficiencia = float(input("Ingrese la eficiencia del tanque (ejemplo 0.90 para 90%): "))
dias_inactivos = int(input("Ingrese la cantidad de días de inactividad por año: "))
area_total = float(input("Ingrese el área disponible para tanques (m²): "))
area_por_tanque = float(input("Ingrese el área que ocupa cada tanque (m²): "))

# Cálculos:
dias_año = 365
dias_planificados = dias_año + dias_inactivos

# Consumo total diario:
consumo_total_dia = consumo_persona * personas

# Consumo anual:
consumo_total_anual = consumo_total_dia * dias_planificados

# Capacidad efectiva de cada tanque considerando la eficiencia:
cap_efectiva_tanque = cap_tanque * eficiencia

# Cantidad de tanques que caben en el área disponible:
tanques_por_area = area_total / area_por_tanque

# Consumo necesario para cubrir los días de inactividad:
consumo_reserva = consumo_total_dia * dias_inactivos


# Capacidad total de todos los tanques que caben en el área:
cap_total_area = tanques_por_area * cap_efectiva_tanque

# Días que se pueden cubrir con todos los tanques instalados:
cobertura_dias = cap_total_area / consumo_total_dia

#Resultados:
print(" Los calculos son los siguientes: ")
print("Consumo total diario calculado:", consumo_total_dia, "litros")
print("Consumo total anual calculado:", consumo_total_anual, "litros")
print("Capacidad efectiva por tanque:", cap_efectiva_tanque, "litros")
print("Tanques que caben en el área disponible:", tanques_por_area)
print("Capacidad total de todos los tanques:", cap_total_area, "litros")
print("Consumo necesario durante", dias_inactivos, "días sin recolección:", consumo_reserva, "litros")
print("Con el área disponible, los tanques pueden cubrir aproximadamente", cobertura_dias, "días de consumo.")

