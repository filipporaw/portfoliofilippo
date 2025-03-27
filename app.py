
from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import io
import csv
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Percorsi e configurazione
FONT_PATH = "Mayonice.ttf"
CSV_PATH = "partecipanti.csv"
TEMPLATE_BASENAME = "ricetta_ssn"
TEMPLATE_OPTIONS = [f"{TEMPLATE_BASENAME}{i}.png" for i in range(1, 8)]
POS_NOME = (215, 320)
FONT_SIZE = 36

# Carica font
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
except:
    font = ImageFont.load_default()

# Inizializza CSV se non esiste
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "nome", "accompagnatore"])

@app.route("/genera", methods=["POST"])
def genera_ricetta():
    nome = request.form.get("nome", "Nome Sconosciuto").upper()
    accompagnatore = request.form.get("accompagnatore") == "1"
    if accompagnatore:
        nome += " +1"

    # Seleziona un template casuale
    template_file = random.choice(TEMPLATE_OPTIONS)
    img = Image.open(template_file).convert("RGB")

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    # Disegna il nome
    draw = ImageDraw.Draw(img)
    draw.text(POS_NOME, nome, font=font, fill="black")

    # Scrive l'immagine in memoria
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Log nel CSV
    with open(CSV_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), nome, "SI" if accompagnatore else "NO"])

    return send_file(buffer, mimetype='image/png', download_name=f"ricetta_{nome.replace(' ', '_')}.png")


@app.route("/partecipanti")
def scarica_csv():
    return send_file(CSV_PATH, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
