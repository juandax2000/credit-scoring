#📊 Reglas del banco

#El banco calcula un puntaje de aprobación basado en las siguientes condiciones.

#Cada regla cumplida suma 1 punto.

#🧮 Reglas financieras

#1️⃣ La edad debe ser mayor o igual a 21
#2️⃣ El ingreso debe ser al menos 2 veces el monto solicitado
#3️⃣ La deuda debe ser menor al 40% del ingreso
#4️⃣ El historial debe ser mayor o igual a 7
#5️⃣ El cliente debe tener más de 10 compras registradas

#⚖️ Reglas de riesgo

#6️⃣ Si la deuda es mayor a 50% del ingreso → se resta 1 punto
#7️⃣ Si el historial es menor a 5 → se resta 1 punto
#8️⃣ Si el monto solicitado es mayor al ingreso → se resta 1 punto

#🏁 Decisión final

#Después de sumar y restar puntos:

#• Si el puntaje ≥ 3 → Crédito aprobado
#• Si el puntaje es 1 o 2 → Crédito en revisión
#• Si el puntaje ≤ 0 → Crédito rechazado

clientes = {
    'juan': {'edad': 25, 'ingreso': 2800, 'deuda': 400},
    'ana': {'edad': 17, 'ingreso': 1500, 'deuda': 100},
    'carlos': {'edad': 35, 'ingreso': 4000, 'deuda': 1200}
}



clientes = {
    'juan': {'compras': 5,  'devoluciones': 0, 'monto': 1200},
    'ana': {'compras': 2,  'devoluciones': 1, 'monto': 300},
    'carlos': {'compras': 20, 'devoluciones': 8, 'monto': 8000}
}
cliente_digitado = "carlos"
datos = clientes.get(cliente_digitado)

deteccion = {
    'Devoluciones': 3,
    'Monto': 5000,
    'Compras': 15
}

if datos is None:
    print(f"El cliente {cliente_digitado} NO existe.")
else:
    print(f"Cliente encontrado: {cliente_digitado} {datos}")
    
    Devoluciones_ok = datos['devoluciones'] > deteccion['Devoluciones']    
    Monto_ok = datos['monto'] > deteccion['Monto']    
    Compras_ok = datos['compras'] > deteccion['Compras']  
      
    puntos_fraude = sum([Devoluciones_ok, Monto_ok, Compras_ok])
    
    if puntos_fraude >= 2:
        print(f'el cliente {cliente_digitado} es sospechoso de fraude') 
    else:
        print(f'cliente {cliente_digitado} normal')