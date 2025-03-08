import os
import time

def is_valid_number(value):
    """
    Verifica si una cadena representa un número válido.

    Parámetros:
        value (str): La cadena a verificar.

    Retorna:
        bool: True si es un número válido, False en caso contrario.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def compute_statistics_from_files(folder_path, output_file):
    """
    Lee múltiples archivos en la carpeta especificada, calcula estadísticas
    descriptivas y guarda los resultados en un archivo de salida.

    Parámetros:
        folder_path (str): Ruta de la carpeta con los archivos de prueba.
        output_file (str): Nombre del archivo donde se guardarán los resultados.
    """
    result_lines = []
    start_time = time.time()

    for filename in sorted(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    numbers = [float(line.strip()) for line in file if is_valid_number(line.strip())]

                if not numbers:
                    result_lines.append(f"{filename}: No contiene datos válidos.\n")
                    continue

                # Cálculo de estadísticas
                n = len(numbers)
                mean = sum(numbers) / n
                numbers.sort()
                median = numbers[n // 2] if n % 2 != 0 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2
                mode = max(set(numbers), key=numbers.count)
                variance = sum((x - mean) ** 2 for x in numbers) / n
                stddev = variance ** 0.5

                # Guardar resultados
                result_lines.append(
                    f"{filename} - Media: {mean:.2f}, Mediana: {median:.2f}, Moda: {mode:.2f}, "
                    f"Varianza: {variance:.2f}, Desviación estándar: {stddev:.2f}\n"
                )

            except FileNotFoundError:
                result_lines.append(f"Error: No se encontró el archivo {filename}\n")
            except Exception as e:
                result_lines.append(f"Error procesando {filename}: {e}\n")

    elapsed_time = time.time() - start_time
    result_lines.append(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos\n")

    # Escribir resultados en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(result_lines)

    print(f"Resultados guardados en {output_file}")

# Llamar a la función con la carpeta de archivos de prueba
compute_statistics_from_files("P1", "ResultadosEstadisticas.txt")
