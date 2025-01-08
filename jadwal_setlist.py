from math import factorial

def combine(arr, r):
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
    
    return result, total_combinations

def main():
    # Input kemungkinan hari pertunjukan
    days = input("Masukkan kemungkinan hari pertunjukkan (pisahkan dengan spasi): ").split()
    
    # Input setlist JKT48
    setlist = input("Masukkan setlist-setlist JKT48 yang sedang aktif (pisahkan dengan koma): ").split(",")
    
    # Menghapus spasi di sekitar setiap item dalam setlist
    setlist = [item.strip() for item in setlist]
    
    # Input jumlah hari dan setlist yang dipilih
    r_days = int(input("Berapa kali JKT48 ingin tampil pada minggu ini? : "))
    r_setlist = int(input("Berapa banyak setlist yang ingin dipilih? : "))
    
    # Menghasilkan kombinasi hari dan setlist
    combinations_days, total_days = combine(days, r_days)
    combinations_setlist, total_setlist = combine(setlist, r_setlist)
    
    # Menghitung total kombinasi hari * kombinasi setlist
    total_combinations = total_days * total_setlist
    print(f"\nTotal kombinasi : {total_combinations}")
    
    # Menampilkan hasil kombinasi
    print("\nKombinasi untuk jadwal dan setlist:\n")
    for day_combo in combinations_days:
        for setlist_combo in combinations_setlist:
            # Gabungkan hari dan setlist
            combined = list(zip(day_combo, setlist_combo))
            
            # Pastikan tidak ada elemen yang sama
            if len(set(day_combo)) == len(day_combo) and len(set(setlist_combo)) == len(setlist_combo):
                # Format output dengan kurung siku
                formatted_output = [f"[{day} - {song}]" for day, song in combined]
                print(" ".join(formatted_output))  # Gabungkan output menjadi satu string

if __name__ == "__main__":
    main()