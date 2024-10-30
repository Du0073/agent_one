from configs.agents import project_agent
from swarm.repl import run_demo_loop
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

if __name__ == "__main__":
    context_variables = {
        #"excel_file": "data/Cursos_rutas_escuelas.xlsx",
        "excel_file": "/home/asus/Hacky Platzi 2024/agent_jaky/data/Cursos_rutas_escuelas.xlsx",
        "openai_api_key": os.getenv("OPENAI_API_KEY")  # Cargar la clave desde las variables de entorno
    }
    run_demo_loop(project_agent, context_variables=context_variables, debug=True)
