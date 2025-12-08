import sys
import os

# Directorio raíz del proyecto (carpeta tarea-3-hebs095)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar al PYTHONPATH si no está ya incluido
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
