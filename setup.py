import os
import subprocess

def create_virtual_env():
    subprocess.run(["python", "-m", "venv", "venv"])

def install_dependencies():
    subprocess.run([os.path.join("venv", "Scripts", "pip"), "install", "-r", "requirements.txt"])

def main():
    if not os.path.exists("requirements.txt"):
        return
    
    create_virtual_env()
    install_dependencies()

if __name__ == "__main__":
    main()
