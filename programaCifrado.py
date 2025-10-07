from collections import Counter

# ------------------- TEXTO CIFRADO -------------------

cyphertext = """
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

# ------------------- FUNCIONES -------------------

def calcular_frecuencias(texto):
    letras = [ch.lower() for ch in texto if ch.isalpha()]
    total = len(letras)
    conteo = Counter(letras)
    return {letra: (conteo[letra] / total) * 100 for letra in conteo}

def mapa_inicial(texto):
    frecuencias_es = {
        'a': 11.96, 'b': 0.92, 'c': 2.92, 'd': 6.87, 'e': 16.78,
        'f': 0.52, 'g': 0.73, 'h': 0.89, 'i': 4.15, 'j': 0.30,
        'k': 0.0, 'l': 8.37, 'm': 2.12, 'n': 7.01, 'ñ': 0.29,
        'o': 8.69, 'p': 2.776, 'q': 1.53, 'r': 4.94, 's': 7.88,
        't': 3.31, 'u': 4.80, 'v': 0.39, 'w': 0.0, 'x': 0.06,
        'y': 1.54, 'z': 0.15
    }

    frec_texto = calcular_frecuencias(texto)
    letras_texto = sorted(frec_texto, key=frec_texto.get, reverse=True)
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")

    for letra in alfabeto:
        if letra not in letras_texto:
            letras_texto.append(letra)

    letras_es = [l for l, _ in sorted(frecuencias_es.items(), key=lambda x: -x[1])]
    return dict(zip(letras_texto, letras_es))

def sustituir(texto, equivalencias):
    resultado = []
    for c in texto:
        if c.isalpha():
            nuevo = equivalencias.get(c.lower(), c)
            resultado.append(nuevo.upper() if c.isupper() else nuevo)
        else:
            resultado.append(c)
    return ''.join(resultado)

def imprimir_mapa(mapa):
    print("\nSustituciones actuales:")
    for k in sorted(mapa):
        print(f"{k} → {mapa[k]}")
    print("-" * 35)

def ajustar_mapa(mapa, texto):
    print("\nIntroduce cambios con el formato  letra_cifrada=letra_real  (ej: q=e)")
    print("Escribe 'salir' o 'q' para terminar.\n")

    while True:
        imprimir_mapa(mapa)
        descifrado = sustituir(texto, mapa)
        print("\nTexto descifrado (vista previa):\n")
        print(descifrado[:1000])
        print("\n----------------------------")

        entrada = input("Cambio: ").strip().lower()
        if entrada in ("salir", "q"):
            break

        if "=" not in entrada or len(entrada) != 3:
            print("Formato no válido. Ejemplo correcto:  k=e")
            continue

        cifrada, real = entrada.split("=")

        # Evitar duplicados
        for k, v in mapa.items():
            if v == real:
                mapa[k] = mapa[cifrada]
        mapa[cifrada] = real

        print(f"Actualizado: {cifrada} → {real}\n")
        print("\nTexto actualizado:\n")
        print(sustituir(texto, mapa)[:1000])
        print("\n----------------------------")

    print("\n=== RESULTADO FINAL ===\n")
    print(sustituir(texto, mapa))

# ------------------- EJECUCIÓN -------------------

if __name__ == "__main__":
    mapa = mapa_inicial(cyphertext)
    ajustar_mapa(mapa, cyphertext)
