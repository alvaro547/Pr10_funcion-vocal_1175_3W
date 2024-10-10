print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_vocal(caracter):
    """
    Verifica si un carácter es una vocal.

    Parameters:
    caracter (str): Un carácter a verificar.

    Returns:
    bool: True si el carácter es una vocal, False de lo contrario.
    
    Example:
    >>> es_vocal('a')
    True
    >>> es_vocal('b')
    False
    >>> es_vocal('E')
    True
    """
    # Definir las vocales (en minúsculas y mayúsculas)
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    
    # Verificar si el carácter está en la lista de vocales
    return caracter in vocales

# Ejemplo de uso
if __name__ == "__main__":
    print(es_vocal('a'))  # Debería imprimir True
    print(es_vocal('b'))  # Debería imprimir False
    print(es_vocal('E'))  # Debería imprimir True
