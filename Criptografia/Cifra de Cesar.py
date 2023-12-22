def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado

texto_original = "Ola Mundo"
deslocamento = 3
texto_cifrado = cifra_cesar(texto_original, deslocamento)

print(f"Texto Original: {texto_original}")
print(f"Texto Cifrado: {texto_cifrado}")
