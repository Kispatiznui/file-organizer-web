import json
import os
from organizer.core import (
    organizar_archivos,
    limpiar_duplicados,
    organizar_por_fecha
)

def load_config():
    with open("config.json") as f:
        return json.load(f)

def process_files(path, mode):
    # 🔥 Validación de existencia real
    if not os.path.exists(path):
        return False, "❌ Path does not exist"

    try:
        config = load_config()

        if mode == "organize":
            organizar_archivos(path, config)

        elif mode == "clean":
            limpiar_duplicados(path)

        elif mode == "date":
            organizar_por_fecha(path)

        else:
            return False, "❌ Invalid mode selected"

        return True, f"✅ Operation '{mode}' completed successfully"

    except Exception as e:
        return False, f"❌ Error: {str(e)}”


