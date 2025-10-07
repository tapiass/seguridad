from collections import Counter

def contar_letras(texto):
    conteo = Counter()
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            conteo[letra] += 1
    return conteo

def reemplazar_letra(texto, letra_original, letra_nueva):
    texto_modificado = texto.replace(letra_original.lower(), letra_nueva.lower())
    texto_modificado = texto_modificado.replace(letra_original.upper(), letra_nueva.upper())
    return texto_modificado

def imprimir_mensajesecreto(texto):
    print("\n===== MENSAJE SECRETO ACTUALIZADO =====")
    vista = texto[:1000]  # mostrar solo los primeros 1000 caracteres si es muy largo
    print(vista)
    print("========================================\n")

def imprimir_frecuencias(texto):
    conteo = contar_letras(texto)
    print("Frecuencia de cada letra (de mayor a menor):")
    for letra, frecuencia in conteo.most_common():
        print(f"'{letra}': {frecuencia}")
    print("------------------------------------------\n")

def main():
    # ------------------- TEXTO CIFRADO -------------------
    texto_original = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE.
"""

    mensaje_secreto = texto_original  # copia del texto original

    print("\n=== TEXTO CIFRADO INICIAL ===")
    imprimir_mensajesecreto(mensaje_secreto)

    while True:
        imprimir_frecuencias(mensaje_secreto)

        letra_cambiar = input("Ingrese la letra que desea cambiar (0 para salir): ").lower()

        if letra_cambiar == '0':
            break

        if not letra_cambiar.isalpha() or len(letra_cambiar) != 1:
            print("Entrada inválida. Por favor, ingrese una letra válida.\n")
            continue

        conteo_letras = contar_letras(mensaje_secreto)
        if letra_cambiar not in conteo_letras:
            print("La letra no está presente en el texto.\n")
            continue

        letra_nueva = input("Ingrese la letra por la que desea reemplazar: ").lower()
        if not letra_nueva.isalpha() or len(letra_nueva) != 1:
            print("Entrada inválida. Por favor, ingrese una letra válida.\n")
            continue

        mensaje_secreto = reemplazar_letra(mensaje_secreto, letra_cambiar, letra_nueva)

        imprimir_mensajesecreto(mensaje_secreto)

    # Guardar resultado final
    with open('mensajesecreto.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(mensaje_secreto)

    print("El mensaje secreto modificado se ha guardado en 'mensajesecreto.txt'.")

if __name__ == "__main__":
    main()
