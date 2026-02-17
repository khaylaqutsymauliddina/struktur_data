class FixedArray:
    def __init__(self, capacity):
        """
        Membuat array dengan kapasitas tetap.
        Semua elemen awal bernilai None.
        """
        if capacity <= 0:
            raise ValueError("Kapasitas harus lebih dari nol")
        
        self.capacity = capacity
        self.elements = [None] * capacity

    def __len__(self):
        return self.capacity

    def __getitem__(self, pos):
        if pos < 0 or pos >= self.capacity:
            raise IndexError("Index tidak tersedia")
        return self.elements[pos]

    def __setitem__(self, pos, value):
        if pos < 0 or pos >= self.capacity:
            raise IndexError("Index tidak tersedia")
        self.elements[pos] = value

    def fill_all(self, value):
        """Mengisi semua elemen dengan nilai tertentu."""
        for i in range(self.capacity):
            self.elements[i] = value

    def __iter__(self):
        for item in self.elements:
            yield item


# =============================
# Contoh Penggunaan
# =============================

data = FixedArray(4)

print("Ukuran array:", len(data))

# Mengisi nilai
data[0] = 8
data[1] = 16
data[2] = 24

print("\nIsi array setelah pengisian:")
for item in data:
    print(item)

print("\nNilai pada index ke-2:", data[2])

# Mengisi ulang seluruh elemen
data.fill_all(5)

print("\nIsi array setelah diisi ulang:")
for item in data:
    print(item)