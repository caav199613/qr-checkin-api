import json
import qrcode

# Archivo de entrada (txt con tu JSON)
INPUT_FILE = "generador_qr/datos.txt"
# Carpeta de salida para los QRs
OUTPUT_DIR = "generador_qr/qrs/"

def generar_qrs():
    # Leer archivo
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)  # Parsear como JSON

    # Recorrer cada objeto en el arreglo
    for i, estudiante in enumerate(data, start=1):
        # Convertir el objeto a string JSON para meterlo en el QR
        qr_data = json.dumps(estudiante, ensure_ascii=False)

        # Crear QR
        qr = qrcode.QRCode(
            version=1,  # tamaño automático si lo dejas en None
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Generar imagen
        img = qr.make_image(fill_color="black", back_color="white")

        # Nombre del archivo: usa numero_identificacion si existe
        filename = estudiante.get("numero_identificacion", f"qr_{i}") + ".png"
        img.save(OUTPUT_DIR + filename)

        print(f"✅ QR generado: {filename}")

if __name__ == "__main__":
    generar_qrs()
