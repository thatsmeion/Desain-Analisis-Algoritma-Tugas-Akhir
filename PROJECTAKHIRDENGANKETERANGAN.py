import math
import time

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def jarakTerdekatStrip(strip, d, pasangan_terdekat):
    print(f"    [Strip diurutkan berdasarkan Y]: {strip}")
    min_jarak = d
    strip.sort(key=lambda point: point[1]) #lambda untuk mengurutkan berdasarkan value tertentu, disini berdasarkan sumbu y
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

def rekursifJarakTerdekat(titik, kiri, kanan, pasangan_terdekat, level=0):
    indentasi = "  " * level
    if kanan - kiri <= 2: #ini base case
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

    mid = (kiri + kanan) // 2 #ini divide
    mid_x = titik[mid][0]
    print(f"{indentasi}Divide: kiri={titik[kiri:mid]}, kanan={titik[mid:kanan]} (mid_x = {mid_x})")

    jarak_kiri = rekursifJarakTerdekat(titik, kiri, mid, pasangan_terdekat, level + 1) #ini rekursif
    jarak_kanan = rekursifJarakTerdekat(titik, mid, kanan, pasangan_terdekat, level + 1) #ini rekursif

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
    titik.sort(key=lambda point: point[0]) #lambda disini untuk mengurutkan berdasarkan value koordinat x
    pasangan_terdekat = [None]
    hasil = rekursifJarakTerdekat(titik, 0, len(titik), pasangan_terdekat)
    return hasil, pasangan_terdekat[0]



titik = [
    [5, 12], [10, 20], [12, 17], [15, 24], [20, 20],
    [22, 25], [25, 22], [30, 18], [33, 27], [35, 30],
    [37, 29], [40, 38], [42, 35], [45, 33], [48, 39],
    [50, 40], [52, 44], [53, 42], [55, 45], [58, 47],
    [60, 50], [61, 49], [63, 53], [65, 55], [66, 54],
    [67, 57], [68, 56], [70, 60], [71, 59], [72, 62],
    [73, 61], [75, 65], [76, 63], [77, 66], [78, 67],
    [80, 70], [81, 69], [83, 71], [84, 72], [85, 74],
    [86, 73], [87, 75], [88, 76], [89, 78], [90, 80],
    [92, 82], [93, 83], [95, 85], [97, 87], [100, 90]
]

start_time = time.perf_counter()
hasil_jarak, pasangan = jarakTerdekat(titik)
end_time = time.perf_counter()  

print(f'\nJarak terdekat: {hasil_jarak:.6f}')
print(f'Pasangan titik terdekat: {pasangan[0]} dan {pasangan[1]}')
print(f'Waktu eksekusi: {(end_time - start_time):.6f} detik')