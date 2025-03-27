from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Percorso immagine template
TEMPLATE_PATH = "ricetta_ssn.png"  # Assicurati che sia caricato nella root
FONT_PATH = "arial.ttf"  # Può essere assente, fallback su font di default
CSV_PATH = "partecipanti.csv"

# Posizione del testo sulla ricetta
POS_NOME = (170, 220)
FONT_SIZE = 36

# Inizializza file CSV se non esiste
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "nome", "accompagnatore"])

@app.route("/genera", methods=["POST"])
def genera_ricetta():
    nome = request.form.get("nome", "Nome Sconosciuto").upper()
    accompagnatore = request.form.get("accompagnatore") == "1"

    # Aggiungi +1 se ha selezionato accompagnatore
    if accompagnatore:
        nome += " +1"

    # Carica immagine e font
    img = Image.open(TEMPLATE_PATH).convert("RGB")
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(img)
    draw.text(POS_NOME, nome, font=font, fill="red")

    # Salva in memoria
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Salva nome nel CSV
    with open(CSV_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), nome, "SI" if accompagnatore else "NO"])

    return send_file(buffer, mimetype='image/png', download_name=f"ricetta_{nome.replace(' ', '_')}.png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
