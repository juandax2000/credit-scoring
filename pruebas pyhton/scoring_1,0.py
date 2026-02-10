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


# 1. Base de datos
clientes = {
    "juan":   {"edad": 25, "ingreso": 2800, "deuda": 400,  "historial": 8, "compras": 12},
    "ana":    {"edad": 19, "ingreso": 1200, "deuda": 900,  "historial": 4, "compras": 3},
    "carlos": {"edad": 40, "ingreso": 5000, "deuda": 1500, "historial": 9, "compras": 25},
    "maria":  {"edad": 32, "ingreso": 3500, "deuda": 200,  "historial": 6, "compras": 18}
}

# 2. Función lógica
def evaluar_credito(nombre, monto, base_datos):
    nombre = nombre.strip().lower()
    if nombre in base_datos:
        c = base_datos[nombre]
        limite_deuda = c['ingreso'] * 0.40

        # --- CAMBIO AQUÍ: Regla de oro ---
        # Si el monto es mayor al ingreso, se rechaza de inmediato o resta muchos puntos
        if monto > c['ingreso'] * 2: # Por ejemplo, nadie puede pedir más del doble de lo que gana
            return f"❌ RECHAZADO: El monto de {monto} es demasiado alto para sus ingresos."

        reglas = [
            c['edad'] >= 21,
            c['ingreso'] >= monto * 2,
            c['deuda'] < limite_deuda,   
            c['historial'] >= 7,
            c['compras'] > 10
        ]

        penalizaciones = [
            c['deuda'] > c['ingreso'] * 0.5,
            c['historial'] < 5,
            monto > c['ingreso'] 
        ]

        puntos_finales = sum(reglas) - sum(penalizaciones)

        if puntos_finales >= 3:
            return f"✅ APROBADO: {nombre.upper()} puede recibir {monto} (Puntos: {puntos_finales})"
        elif 1 <= puntos_finales <= 2:
            return f"⚠️ REVISIÓN: El crédito de {monto} para {nombre.upper()} requiere aval (Puntos: {puntos_finales})"
        else:
            return f"❌ RECHAZADO: Puntuación insuficiente para {monto} (Puntos: {puntos_finales})"
    else:
        return f"Error: '{nombre}' no encontrado."

# 3. Interacción con el usuario
cliente_digitado = input('Escribe tu nombre: ')

# Usamos try para manejar posibles errores al escribir el número
try:
    monto_solicitado = float(input('¿Qué monto deseas solicitar? '))
    
    # Llamada a la función con ambos inputs
    resultado = evaluar_credito(cliente_digitado, monto_solicitado, clientes)
    print(resultado)

except ValueError:
    print("Error: Por favor, ingresa un número válido para el monto.")
