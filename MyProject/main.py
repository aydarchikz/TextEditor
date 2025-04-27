import subprocess
from create_window import *

def install_dependencies():
    try:
        subprocess.check_call(["python", "-m", "pip", "install", "-r", "requirements.txt"])
        print("Зависимости установлены успешно!")
    except subprocess.CalledProcessError:
        print("Ошибка установки зависимостей.")
    
def run_project():
    text_editor = CreateTextEditor()
    
if __name__ == "__main__":
    install_dependencies()
    run_project()
