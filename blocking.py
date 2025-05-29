import json
import random

def get_blocking_members(setlist_name: str, center_name: str, data_json: dict):
    # Ambil data berdasarkan setlist dan center
    setlist_data = data_json.get(setlist_name)
    
    if not setlist_data:
        print("Setlist tidak ditemukan.")
        return
    
    centers = setlist_data["Centers"]
    
    # Mencari center yang sesuai
    for center in centers:
        if center["Center"].lower() == center_name.lower():
            used_members = set()

            # Mengumpulkan anggota dari setiap blocking
            for blocking_level in range(2, 17):  # Blocking dari 2 sampai 16
                blocking_key = f"Blocking {blocking_level}"
                
                if blocking_key in center:
                    members = center[blocking_key].split(", ")
                    random.shuffle(members)  # Acak urutan anggota
                    
                    # Pilih anggota yang belum digunakan
                    unique_member = next((member for member in members if member not in used_members), None)
                    
                    if unique_member:
                        print(f"{blocking_key} : {unique_member}")
                        used_members.add(unique_member)  # Tambahkan anggota yang sudah digunakan

            return

def get_ramune_blocking_members(center_name: str, data_json: dict):
    # Ambil data berdasarkan setlist "Cara Meminum Ramune"
    setlist_data = data_json.get("Cara Meminum Ramune")
    
    if not setlist_data:
        print("Setlist 'Cara Meminum Ramune' tidak ditemukan.")
        return
    
    centers = setlist_data["Centers"]
    
    # Mencari center yang sesuai
    for center in centers:
        if center.get("Yellow", "").lower() == center_name.lower():
            used_members = set()
            
            # Mengumpulkan anggota dari setiap blocking berdasarkan warna
            for blocking_color, members in center.items():
                if blocking_color == "Yellow":  # Skip Yellow (center name itself)
                    continue
                
                # Pisahkan anggota berdasarkan koma
                members_list = members.split(", ")
                random.shuffle(members_list)  # Acak urutan anggota
                
                # Pilih anggota yang belum digunakan
                unique_member = next((member for member in members_list if member not in used_members), None)
                
                if unique_member:
                    print(f"{blocking_color} : {unique_member}")
                    used_members.add(unique_member)  # Tambahkan anggota yang sudah digunakan
            
            return
    
    print("Center tidak ditemukan.")

def main():
    # Membaca data JSON dari file
    try:
        with open('list_blocking.json', 'r') as file:
            data_json = json.load(file)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return
    except json.JSONDecodeError:
        print("Error dalam membaca file JSON. Pastikan format JSON benar.")
        return

    # Mengambil input dari pengguna
    setlist_input = input("Masukkan nama setlist : ").strip()
    
    if setlist_input.lower() == "cara meminum ramune":
        center_input = input("Masukkan nama center (Yellow): ").strip()
        get_ramune_blocking_members(center_input, data_json)
    else:
        center_input = input("Masukkan nama center: ").strip()
        get_blocking_members(setlist_input, center_input, data_json)


if __name__ == "__main__":
    main()
