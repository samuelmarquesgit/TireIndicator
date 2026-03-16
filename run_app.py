import subprocess
import time
import sys
import os

def run():
    print("Iniciando Tirindicator...")
    
    # Define os caminhos
    python_exe = os.path.join("venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
         python_exe = "python" # fallback

    # Inicia o Backend (FastAPI)
    print("Iniciando API (Backend)...")
    backend_proc = subprocess.Popen([python_exe, "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080"])
    
    # Espera um pouco para garantir que a API subiu
    time.sleep(3)
    
    # Inicia o Frontend (Streamlit)
    print("Iniciando Interface (Frontend)...")
    try:
        frontend_proc = subprocess.run([python_exe, "-m", "streamlit", "run", "frontend/main.py"])
    except KeyboardInterrupt:
        print("\nFinalizando processos...")
        backend_proc.terminate()

if __name__ == "__main__":
    run()
