import math

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def jarakTerdekatStrip(strip, d, pasangan_terdekat):
    print(f"    [Strip diurutkan berdasarkan Y]: {strip}")
    min_jarak = d
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_jarak:
                jarak_antar = jarak(strip[i], strip[j])
                print(f"    Bandingkan (strip): {strip[i]} - {strip[j]} = {jarak_antar:.6f}")
                if jarak_antar < min_jarak:
                    min_jarak = jarak_antar
                    pasangan_terdekat[0] = (strip[i], strip[j])
            else:
                break
    return min_jarak

def minDistUtil(titik, kiri, kanan, pasangan_terdekat, level=0):
    indentasi = "  " * level
    if kanan - kiri <= 2:
        print(f"{indentasi}Brute force: {titik[kiri:kanan]}")
        min_jarak = float('inf')
        for i in range(kiri, kanan):
            for j in range(i + 1, kanan):
                d = jarak(titik[i], titik[j])
                print(f"{indentasi}  Jarak {titik[i]} - {titik[j]} = {d:.6f}")
                if d < min_jarak:
                    min_jarak = d
                    pasangan_terdekat[0] = (titik[i], titik[j])
        return min_jarak

    mid = (kiri + kanan) // 2
    mid_x = titik[mid][0]
    print(f"{indentasi}Divide: kiri={titik[kiri:mid]}, kanan={titik[mid:kanan]} (mid_x = {mid_x})")

    jarak_kiri = minDistUtil(titik, kiri, mid, pasangan_terdekat, level + 1)
    jarak_kanan = minDistUtil(titik, mid, kanan, pasangan_terdekat, level + 1)

    d = min(jarak_kiri, jarak_kanan)
    print(f"{indentasi}Jarak minimum kiri={jarak_kiri:.6f}, kanan={jarak_kanan:.6f}, sementara d = {d:.6f}")

    strip = []
    for i in range(kiri, kanan):
        if abs(titik[i][0] - mid_x) < d:
            strip.append(titik[i])
    print(f"{indentasi}Strip dekat mid_x ({mid_x}) dengan lebar {d:.6f}: {strip}")

    strip_jarak = jarakTerdekatStrip(strip, d, pasangan_terdekat)
    print(f"{indentasi}Jarak minimum di strip: {strip_jarak:.6f}")

    return min(d, strip_jarak)

def jarakTerdekat(titik):
    titik.sort(key=lambda point: point[0])
    pasangan_terdekat = [None]
    hasil = minDistUtil(titik, 0, len(titik), pasangan_terdekat)
    return hasil, pasangan_terdekat[0]



titik = [
    [-72, -63], [29, -57], [-66, -25], [-5, -84], [13, 73],
    [-30, 91], [83, -96], [7, 43], [71, 2]
]
hasil_jarak, pasangan = jarakTerdekat(titik)
print(f'\nJarak terdekat: {hasil_jarak:.6f}')
print(f'Pasangan titik terdekat: {pasangan[0]} dan {pasangan[1]}')
