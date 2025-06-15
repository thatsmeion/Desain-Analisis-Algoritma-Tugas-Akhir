import math
import time

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bruteForceJarakTerdekat(titik):
    min_jarak = float('inf')
    pasangan_terdekat = (None, None)

    n = len(titik)
    for i in range(n):
        for j in range(i + 1, n):
            d = jarak(titik[i], titik[j])
            if d < min_jarak:
                min_jarak = d
                pasangan_terdekat = (titik[i], titik[j])
    return min_jarak, pasangan_terdekat

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
hasil_jarak, pasangan = bruteForceJarakTerdekat(titik)
end_time = time.perf_counter()
print(f'\n[Brute Force]')
print(f'Jarak terdekat: {hasil_jarak:.6f}')
print(f'Pasangan titik terdekat: {pasangan[0]} dan {pasangan[1]}')
print(f'Waktu eksekusi: {(end_time - start_time):.6f} detik')
