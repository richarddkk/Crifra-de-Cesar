def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado

def quebrar_cifra_cesar(cifrado):
    for deslocamento in range(1, 26):
        texto_decifrado = cifra_cesar(cifrado, -deslocamento)
        print(f"Deslocamento {deslocamento}: {texto_decifrado}")

texto_cifrado = "Rod Pxqgr"
quebrar_cifra_cesar(texto_cifrado)
