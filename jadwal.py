def combine(arr, r):
    from math import factorial
    
    n = len(arr)
    
    # Fungsi untuk menghitung C(n, r)
    def combinations_count(n, r):
        if r > n:
            return 0
        return factorial(n) // (factorial(r) * factorial(n - r))

    result = []
    
    # Menggunakan backtracking untuk menghasilkan kombinasi
    def backtrack(start, path):
        if len(path) == r:
            result.append(path)
            return
        for i in range(start, n):
            backtrack(i + 1, path + [arr[i]])

    backtrack(0, [])
    
    # Menghitung jumlah kombinasi yang dihasilkan
    total_combinations = combinations_count(n, r)
    print(f"Jumlah kombinasi yang mungkin: {total_combinations}")
    
    return result

def main():
    # Input
    arr = input("Masukkan kemungkinan hari pertunjukkan (pisahkan dengan spasi): ").split()
    
    # Menyimpan elemen dalam daftar dengan tipe data yang sesuai
    typed_arr = []
    for item in arr:
        # Konversi ke integer
        try:
            typed_arr.append(int(item))
            continue
        except ValueError:
            pass
        
        # Konversi ke float
        try:
            typed_arr.append(float(item))
            continue
        except ValueError:
            pass
        
        # Jika bukan integer atau float, simpan sebagai string
        typed_arr.append(item)
    
    r = int(input("Berapa kali JKT48 ingin tampil pada minggu ini? : "))
    
    # Menghasilkan kombinasi
    combinations_result = combine(typed_arr, r)
    
    # Menampilkan hasil
    for combo in combinations_result:
        print(combo)

if __name__ == "__main__":
    main()
