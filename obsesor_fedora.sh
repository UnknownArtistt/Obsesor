#!/bin/bash

# Función para instalar pip
install_pip() {
    if ! command -v pip &>/dev/null; then
        echo "pip no está instalado. Instalando pip..."
        sudo dnf install -y python3-pip
    else
        echo "pip ya está instalado."
    fi
}

# Función para instalar paquetes necesarios
install_packages() {
    echo "Instalando paquetes necesarios..."
    sudo pip3 install pyfiglet tqdm
}

# Función para ejecutar el programa
run_program() {
    echo "Ejecutando Obsesor..."
    python3 obsesor.py
}

# Ejecutar funciones
install_pip
install_packages
run_program
