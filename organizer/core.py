 import os
import shutil
import logging
from datetime import datetime
from organizer.utils import get_extension, ensure_directory, is_valid_file


def get_category(extension, config):
    for category, extensions in config.items():
        if extension in [ext.lower() for ext in extensions]:
            return category
    return "others"


def organizar_archivos(ruta, config):
    if not os.path.exists(ruta):
        raise ValueError("Invalid path")

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if is_valid_file(ruta_completa):
            extension = get_extension(archivo)
            categoria = get_category(extension, config)

            destino = os.path.join(ruta, categoria)
            ensure_directory(destino)

            destino_final = os.path.join(destino, archivo)

            try:
                shutil.move(ruta_completa, destino_final)
                logging.info(f"Moved: {archivo} → {categoria}")
            except Exception as e:
                logging.error(f"Error moving {archivo}: {e}")


def limpiar_duplicados(ruta):
    if not os.path.exists(ruta):
        raise ValueError("Invalid path")

    vistos = set()

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if is_valid_file(ruta_completa):
            if archivo in vistos:
                try:
                    os.remove(ruta_completa)
                    logging.info(f"Deleted duplicate: {archivo}")
                except Exception as e:
                    logging.error(f"Error deleting {archivo}: {e}")
            else:
                vistos.add(archivo)


def organizar_por_fecha(ruta):
    if not os.path.exists(ruta):
        raise ValueError("Invalid path")

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if is_valid_file(ruta_completa):
            try:
                timestamp = os.path.getmtime(ruta_completa)
                fecha = datetime.fromtimestamp(timestamp).strftime("%Y-%m")

                destino = os.path.join(ruta, fecha)
                ensure_directory(destino)

                shutil.move(ruta_completa, os.path.join(destino, archivo))
                logging.info(f"Moved: {archivo} → {fecha}")

            except Exception as e:
                logging.error(f"Error processing {archivo}: {e}")

