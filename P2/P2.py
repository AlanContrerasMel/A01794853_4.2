"""
Módulo para convertir números de múltiples archivos a sus representaciones
binaria y hexadecimal, y almacenar los resultados en un archivo de salida.

Uso:
    python P2.py
"""

import os
import time


def to_binary(number):
    """
    Convierte un número entero a su representación binaria.

    Parámetros:
        number (int): Número a convertir.

    Retorna:
        str: Representación binaria del número.
    """
    binary_str = ""
    while number > 0:
        binary_str = str(number % 2) + binary_str
        number //= 2
    return binary_str if binary_str else "0"


def to_hexadecimal(number):
    """
    Convierte un número entero a su representación hexadecimal.

    Parámetros:
        number (int): Número a convertir.

    Retorna:
        str: Representación hexadecimal del número.
    """
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    while number > 0:
        hex_str = hex_chars[number % 16] + hex_str
        number //= 16
    return hex_str if hex_str else "0"


def convert_numbers():
    """
    Lee múltiples archivos en la carpeta actual, los convierte a binario
    y hexadecimal, y guarda los resultados en un archivo de salida.
    """
    start_time = time.time()
    result_lines = []

    current_folder = os.path.dirname(os.path.abspath(__file__))

    for filename in sorted(os.listdir(current_folder)):
        if filename.startswith("TC") and filename.endswith(".txt"):
            file_path = os.path.join(current_folder, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        try:
                            number = int(line.strip())
                            binary = to_binary(number)
                            hexadecimal = to_hexadecimal(number)
                            result = f"{filename} - {number}: binario={binary}, hexadecimal={hexadecimal}\n"
                            print(result.strip())
                            result_lines.append(result)
                        except ValueError:
                            error_msg = f"{filename}: Dato inválido ignorado: {line.strip()}\n"
                            print(error_msg.strip())
                            result_lines.append(error_msg)
            except FileNotFoundError:
                error_msg = f"Error: No se encontró el archivo {filename}\n"
                print(error_msg.strip())
                result_lines.append(error_msg)
            except Exception as error:
                error_msg = f"Error inesperado procesando {filename}: {error}\n"
                print(error_msg.strip())
                result_lines.append(error_msg)

    elapsed_time = time.time() - start_time
    result_lines.append(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos\n")

    with open("ConvertionResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.writelines(result_lines)

    print("Resultados guardados en ConvertionResults.txt")


if __name__ == "__main__":
    convert_numbers()
