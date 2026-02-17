import time

# Dimensi grid
BARIS = 5
KOLOM = 6

# 0 = mati, 1 = hidup
dunia = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

def cetak(dunia):
    for r in range(BARIS):
        for c in range(KOLOM):
            simbol = "O" if dunia[r][c] == 1 else "."
            print(simbol, end=" ")
        print()
    print("-" * 15)

def jumlah_tetangga(dunia, r, c):
    hitung = 0
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            
            rr = r + dr
            cc = c + dc
            
            if 0 <= rr < BARIS and 0 <= cc < KOLOM:
                if dunia[rr][cc] == 1:
                    hitung += 1
                    
    return hitung

def update(dunia):
    papan_baru = [[0]*KOLOM for _ in range(BARIS)]
    
    for r in range(BARIS):
        for c in range(KOLOM):
            tetangga = jumlah_tetangga(dunia, r, c)
            
            if dunia[r][c] == 1:
                papan_baru[r][c] = 1 if tetangga in [2,3] else 0
            else:
                papan_baru[r][c] = 1 if tetangga == 3 else 0
    
    return papan_baru

# Simulasi
generasi = 0
while generasi < 4:
    print("=== Generasi", generasi, "===")
    cetak(dunia)
    dunia = update(dunia)
    time.sleep(1)
    generasi += 1