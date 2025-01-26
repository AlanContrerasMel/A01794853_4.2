"""
Programa para contar la frecuencia de palabras en múltiples archivos de texto.

Uso:
    python wordCount.py

Este programa busca archivos que comiencen con "TC" en la carpeta actual,
cuenta las palabras en cada archivo y guarda los resultados en WordCountResults.txt.
"""

import os
import time


def count_words_from_file(filename):
    """
    Cuenta la frecuencia de cada palabra en un archivo de texto.

    Parámetros:
        filename (str): Nombre del archivo de entrada.

    Retorna:
        dict: Diccionario con las palabras como claves y su frecuencia como valores.
    """
    word_count = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower().strip(".,!?\"'()[]{}")
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encontró.")
    except Exception as error:
        print(f"Error inesperado en '{filename}': {error}")
    
    return word_count


def process_word_count():
    """
    Procesa todos los archivos que comiencen con 'TC', cuenta las palabras,
    y guarda los resultados en un archivo de salida.
    """
    start_time = time.time()
    result_lines = []
    found_files = False

    script_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in sorted(os.listdir(script_dir)):
        if filename.startswith("TC") and filename.endswith(".txt"):
            found_files = True
            file_path = os.path.join(script_dir, filename)
            word_counts = count_words_from_file(file_path)
            result_lines.append(f"Resultados para {filename}:\n")
            for word, count in sorted(word_counts.items()):
                result_lines.append(f"{word}: {count}\n")
            result_lines.append("\n")

    if not found_files:
        result_lines.append("No se encontraron archivos de texto para procesar.\n")

    elapsed_time = time.time() - start_time
    result_lines.append(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos\n")

    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.writelines(result_lines)

    print("Resultados guardados en WordCountResults.txt")


if __name__ == "__main__":
    process_word_count()
print("Archivos en la carpeta:", os.listdir())
