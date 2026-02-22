from flask import Flask, request
import requests
import json
import os
from openai import OpenAI

app = Flask(__name__)

# =========================
# =========================
# 🚀 PROCESOS, FLUJOS Y EDGE CASES ULTRA-COMPLETOS
# =========================

# Proceso de escalamiento por formatos no compatibles
def detectar_formato_no_compatible(tipo, numero):
    if tipo not in ["text", "image", "audio"]:
        escalar_a_humano(numero, f"Formato no compatible: {tipo}")
        enviar_mensaje(numero, "He detectado un formato que no puedo procesar automáticamente. Un agente humano te ayudará en breve.")
        registrar_evento("formato_no_compatible", tipo, "Escalado a humano", numero)
        return True
    return False

# Proceso de atención urgente
def atender_urgente(numero):
    enviar_mensaje(numero, "Procesaré tu pedido con prioridad. El tiempo estimado es 20 minutos.")
    registrar_evento("urgente", "Atención urgente", "Prioridad dada", numero)

# Proceso de promociones y combos
def informar_promociones(numero):
    promo = "Hoy tenemos la promo Combo Familiar: S/49. Pizza grande + bebida + postre."
    enviar_mensaje(numero, promo)
    registrar_evento("promociones", "Consulta de promociones", promo, numero)

# Proceso de feedback instantáneo
def solicitar_feedback(numero):
    enviar_mensaje(numero, "¿Cómo calificarías tu experiencia hoy? (Excelente/Buena/Regular/Mala)")
    registrar_evento("feedback", "Solicitud de feedback", "Feedback solicitado", numero)

# Proceso de actualización automática (simulado)
def auto_actualizar():
    actualizar_conocimiento()
    registrar_evento("actualización", "Auto-actualización", "Conocimiento actualizado", "sistema")

# Proceso de crisis y saturación
def detectar_crisis(numero, motivo):
    enviar_mensaje(numero, f"Estamos experimentando una situación especial. Un agente humano te atenderá en breve. Motivo: {motivo}")
    registrar_evento("crisis", motivo, "Escalado a humano por crisis", numero)

# Proceso de validación de stock
def validar_stock(productos, menu):
    agotados = []
    for item in productos:
        nombre = item["nombre"].lower()
        if nombre not in menu:
            agotados.append(nombre)
    return agotados

# Proceso de sugerencia alternativa
def sugerir_alternativas(numero, agotados, menu):
    alternativas = [k for k in menu.keys() if k not in agotados][:3]
    mensaje = f"Los productos {', '.join(agotados)} no están disponibles. Te sugiero: {', '.join(alternativas)}"
    enviar_mensaje(numero, mensaje)
    registrar_evento("alternativas", f"Agotados: {agotados}", mensaje, numero)

# Proceso de registro de reclamos
def registrar_reclamo(numero, mensaje):
    enviar_mensaje(numero, "Tu reclamo ha sido registrado. Un agente humano te atenderá en breve.")
    registrar_evento("reclamo", mensaje, "Reclamo registrado", numero)

# Proceso de aprendizaje continuo
def aprendizaje_continuo():
    # Simulación: analizar eventos y mejorar procesos
    if os.path.exists("eventos.json"):
        with open("eventos.json", "r") as f:
            eventos = json.load(f)
        # Aquí se podría analizar y ajustar protocolos
    registrar_evento("aprendizaje", "Análisis de eventos", "Protocolos mejorados", "sistema")
# =========================
# 🧩 MODULARIZACIÓN AVANZADA Y PROCESOS
# =========================

# Registro de errores, feedback y aprendizaje automático
def registrar_evento(tipo, mensaje, respuesta, numero):
    evento = {
        "fecha": str(__import__('datetime').datetime.now()),
        "tipo": tipo,
        "mensaje": mensaje,
        "respuesta": respuesta,
        "numero": numero
    }
    if not os.path.exists("eventos.json"):
        eventos = []
    else:
        with open("eventos.json", "r") as f:
            eventos = json.load(f)
    eventos.append(evento)
    with open("eventos.json", "w") as f:
        json.dump(eventos, f, indent=4)

# Validaciones contextuales
def validar_direccion(direccion):
    if not direccion or len(direccion) < 5:
        return False
    return True

def validar_pedido(productos):
    return len(productos) > 0

# Escalamiento automático
def escalar_a_humano(numero, motivo):
    enviar_mensaje(numero, f"Un agente humano te atenderá en breve. Motivo: {motivo}")
    registrar_evento("escalamiento", motivo, "Escalado a humano", numero)

# Actualización automática (simulada)
def actualizar_conocimiento():
    # Aquí se podría consultar una API o fuente externa para actualizar el .txt
    pass

# Respuestas personalizadas
def respuesta_personalizada(perfil, base):
    if perfil == "nuevo":
        return base + " ¡Bienvenido! ¿Te gustaría conocer nuestras promociones?"
    elif perfil == "frecuente":
        return base + " ¡Gracias por tu preferencia! Promo VIP disponible."
    elif perfil == "VIP":
        return base + " ¡Atención preferencial! ¿Deseas algo especial hoy?"
    elif perfil == "reclamante":
        return base + " Lamentamos el inconveniente. Te ofrecemos una solución inmediata."
    else:
        return base
# 🔐 CONFIGURACION
# =========================

WHATSAPP_TOKEN = "PEGA_AQUI_TU_WHATSAPP_TOKEN"
PHONE_NUMBER_ID = "PEGA_AQUI_TU_PHONE_NUMBER_ID"
OPENAI_API_KEY = "PEGA_AQUI_TU_OPENAI_KEY"
GOOGLE_MAPS_API_KEY = "PEGA_AQUI_TU_GOOGLE_MAPS_KEY"

DIRECCION_LOCAL = "PEGA_AQUI_DIRECCION_REAL_DEL_RESTAURANTE"

client = OpenAI(api_key=OPENAI_API_KEY)

# =========================
# 📂 BASE DE DATOS LOCAL
# =========================

def cargar_pedidos():
    if not os.path.exists("pedidos.json"):
        return {}
    with open("pedidos.json", "r") as f:
        return json.load(f)

def guardar_pedidos(data):
    with open("pedidos.json", "w") as f:
        json.dump(data, f, indent=4)

# =========================
# 📖 CARGAR MENU DESDE TXT
# =========================

def cargar_menu():
    menu = {}
    with open("base_conocimiento.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line and "km" not in line.lower():
                nombre, precio = line.strip().split("|")
                menu[nombre.strip().lower()] = float(precio.strip())
    return menu

# =========================
# 🧠 INTERPRETAR MENSAJE
# =========================

def cargar_conocimiento():
    with open("base_conocimiento.txt", "r", encoding="utf-8") as f:
        return f.read()

def interpretar_mensaje(texto):
    conocimiento = cargar_conocimiento()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
Eres una IA ultra-resiliente para Pizza Dypsi. Usa la siguiente fuente de conocimiento para responder, siguiendo todos los protocolos, procesos, instrucciones, edge cases, ejemplos y respuestas modelo:
---
{conocimiento}
---
Devuelve SOLO JSON con este formato:
{{
  "productos": [{{"nombre": "", "cantidad": 0}}],
  "direccion": "",
  "confirmar": false,
  "respuesta": ""
}}
Incluye en 'respuesta' la respuesta exacta que debe enviar la IA según el protocolo.
"""
            },
            {"role": "user", "content": texto}
        ]
    )
    return response.choices[0].message.content

# =========================
# 📍 CALCULAR DISTANCIA
# =========================

def calcular_distancia(destino):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={DIRECCION_LOCAL}&destinations={destino}&key={GOOGLE_MAPS_API_KEY}"
    r = requests.get(url).json()
    metros = r["rows"][0]["elements"][0]["distance"]["value"]
    return metros / 1000

def calcular_delivery(km):
    if km <= 3:
        return 5
    elif km <= 6:
        return 8
    else:
        return 12

# =========================
# 🖼 ANALIZAR IMAGEN
# =========================

def analizar_imagen(url_imagen):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "¿Qué comida es esta?"},
                {"type": "image_url", "image_url": {"url": url_imagen}}
            ]
        }]
    )
    return response.choices[0].message.content

# =========================
# 🎤 TRANSCRIBIR AUDIO
# =========================

def transcribir_audio(url_audio):
    audio = requests.get(url_audio, headers={
        "Authorization": f"Bearer {WHATSAPP_TOKEN}"
    })
    with open("audio.ogg", "wb") as f:
        f.write(audio.content)
    with open("audio.ogg", "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text

# =========================
# 📤 ENVIAR MENSAJE
# =========================

def enviar_mensaje(numero, texto):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    requests.post(url, headers=headers, json=data)

# =========================
# 🔔 WEBHOOK
# =========================

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json
    mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]
    numero = mensaje["from"]

    pedidos = cargar_pedidos()
    menu = cargar_menu()

    # Detectar formatos no compatibles
    if detectar_formato_no_compatible(mensaje["type"], numero):
        return "ok", 200

    texto_usuario = ""
    if mensaje["type"] == "text":
        if "urgente" in mensaje["text"]["body"].lower():
            atender_urgente(numero)
        if "promo" in mensaje["text"]["body"].lower():
            informar_promociones(numero)
        if "reclamo" in mensaje["text"]["body"].lower():
            registrar_reclamo(numero, mensaje["text"]["body"])
        texto_usuario = mensaje["text"]["body"]
    elif mensaje["type"] == "image":
        media_id = mensaje["image"]["id"]
        media = requests.get(
            f"https://graph.facebook.com/v18.0/{media_id}",
            headers={"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
        ).json()
        texto_usuario = analizar_imagen(media["url"])
    elif mensaje["type"] == "audio":
        media_id = mensaje["audio"]["id"]
        media = requests.get(
            f"https://graph.facebook.com/v18.0/{media_id}",
            headers={"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
        ).json()
        texto_usuario = transcribir_audio(media["url"])

    interpretado = interpretar_mensaje(texto_usuario)
    try:
        datos = json.loads(interpretado)
    except Exception as e:
        enviar_mensaje(numero, "No entendí tu mensaje, ¿puedes repetirlo?")
        registrar_evento("error", texto_usuario, str(e), numero)
        escalar_a_humano(numero, "Error de interpretación")
        return "ok", 200

    if numero not in pedidos:
        pedidos[numero] = {"productos": {}, "direccion": ""}

    # Validar pedido y dirección
    if not validar_pedido(datos["productos"]):
        enviar_mensaje(numero, "No detecté productos válidos. ¿Puedes detallar tu pedido?")
        registrar_evento("validación", texto_usuario, "Pedido inválido", numero)
        solicitar_feedback(numero)
        return "ok", 200

    if not validar_direccion(datos["direccion"]):
        enviar_mensaje(numero, "¿Me confirmas tu dirección exacta?")
        registrar_evento("validación", texto_usuario, "Dirección inválida", numero)
        solicitar_feedback(numero)
        return "ok", 200

    # Validar stock
    agotados = validar_stock(datos["productos"], menu)
    if agotados:
        sugerir_alternativas(numero, agotados, menu)
        registrar_evento("stock", f"Agotados: {agotados}", "Alternativas sugeridas", numero)
        solicitar_feedback(numero)
        return "ok", 200

    # Agregar productos
    for item in datos["productos"]:
        nombre = item["nombre"].lower()
        cantidad = item["cantidad"]
        if nombre in menu:
            pedidos[numero]["productos"][nombre] = cantidad

    # Guardar dirección
    if datos["direccion"]:
        pedidos[numero]["direccion"] = datos["direccion"]

    guardar_pedidos(pedidos)

    # Calcular total si hay productos
    subtotal = 0
    for producto, cantidad in pedidos[numero]["productos"].items():
        subtotal += menu[producto] * cantidad

    perfil = "nuevo" if len(pedidos[numero]["productos"]) == 1 else "frecuente"

    if pedidos[numero]["direccion"]:
        km = calcular_distancia(pedidos[numero]["direccion"])
        delivery = calcular_delivery(km)
        total = subtotal + delivery

        respuesta = datos.get("respuesta", "")
        if not respuesta:
            base = f"""
🍕 PIZZA DYPSI

Resumen de pedido:

{pedidos[numero]["productos"]}

Subtotal: S/ {subtotal}
Delivery: S/ {delivery}
Total: S/ {total}

¿Confirmas tu pedido?
"""
            respuesta = respuesta_personalizada(perfil, base)
        registrar_evento("atención", texto_usuario, respuesta, numero)
        solicitar_feedback(numero)
    else:
        respuesta = datos.get("respuesta", "") or "Perfecto 🙌 ¿Me envías tu dirección para calcular el delivery?"
        registrar_evento("atención", texto_usuario, respuesta, numero)
        solicitar_feedback(numero)

    enviar_mensaje(numero, respuesta)
    aprendizaje_continuo()
    auto_actualizar()
    return "ok", 200


if __name__ == "__main__":
    app.run(port=5000)