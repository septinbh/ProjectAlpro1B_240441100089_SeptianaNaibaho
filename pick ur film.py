data_pengguna = {}
playlist = {}

film_info = {
    "The Conjuring": {"info": "Film tentang pasangan Warren yang membantu keluarga Perron menghadapi gangguan supernatural di rumah mereka di Rhode Island.", "genre": "Horror", "sutradara": "James Wan"},
    "The Godfather": {"info": "Film tentang keluarga mafia dan perjuangan mereka.", "genre": "Drama", "sutradara": "Francis Ford Coppola"},
    "Avengers": {"info": "Film tentang superhero yang bekerja sama untuk menyelamatkan dunia.", "genre": "Action", "sutradara": "Joss Whedon"},
    "Titanic": {"info": "Film drama romantis tentang tragedi kapal Titanic.", "genre": "Romance", "sutradara": "James Cameron"},
    "Parasite": {"info": "Film thriller tentang kesenjangan sosial di Korea Selatan.", "genre": "Thriller", "sutradara": "Bong Joon-ho"},
    "Jumanji": {"info": "Film ini berkisah tentang papan permainan ajaib yang memiliki kekuatan untuk menghidupkan tantangan yang ada di dalamnya.", "genre": "Komedi", "sutradara": "Jake Kasdan"},
    "Tarzan": {"info": "Film tentang seorang pria yang dibesarkan oleh kera di hutan Afrika dan kemudian berusaha menemukan jati dirinya di antara dua dunia: dunia alam liar yang membesarkannya dan dunia manusia yang menjadi asal-usulnya.", "genre": "Petualangan", "sutradara": "Chris Buck"},
    "True Beauty": {"info": "Film menceritakan tentang siswi SMA yang tidak percaya diri dengan penampilannya.", "genre": "Romance", "sutradara": "Lee Je-kyoo"},
    "Squid Game": {"info": "Sekelompok orang yang mengikuti permainan bertahan hidup untuk memenangkan hadiah uang tunai.", "genre": "Action", "sutradara": "Hwang Dong-hyuk"},
    "5 cm": {"info": "Lima remaja yang menjalin persahabatan selama 5 tahun lamanya dan merasa jenuh kemudian mereka memutuskan untuk berpisah tidak berkomunikasi selama 3 bulan.", "genre": "Petualangan", "sutradara": "Rizal Mantovani"},
    "Joker": {"info": "Menceritakan tentang seseorang badut pesta yang tersakiti dan memutuskan untuk menjadi jahat dan membuat kekacauan.", "genre": "Thriller", "sutradara": "Todd Phillips"},
    "Sewu Dino": {"info": "Tentang seorang yang kesulitan ekonomi, memutuskan untuk bekerja kepada keluarga kaya dan merawat cucu keluarga yang terkena santet.", "genre": "Horror", "sutradara": "Kimo Stamboel"}
}

rekomendasi_film = {
    "Horror": ["The Conjuring", "Sewu Dino"],
    "Drama": ["The Godfather"],
    "Action": ["Avengers", "Squid Game"],
    "Romance": ["Titanic", "True Beauty"],
    "Thriller": ["Parasite", "Joker"],
    "Komedi": ["Jumanji"],
    "Petualangan": ["Tarzan", "5 cm"]
}

# Data pengguna dan playlist awal
data_pengguna = {}
playlist = {}

def tambah_pengguna():
    username = input("Masukkan username: ")
    if username in data_pengguna:
        print("Username sudah ada.")
    else:
        ID = input("Masukkan ID: ")
        data_pengguna[username] = ID
        playlist[username] = []  
        
        print(f"Pengguna {username} berhasil ditambahkan.")

def lihat_pengguna():
    if not data_pengguna:
        print("Tidak ada data pengguna yang terdaftar.")
    else:
        print("Daftar pengguna:")
        for username, ID in data_pengguna.items():
            print(f"Username: {username}, ID: {ID}")

def tambah_film(username):
    if username not in playlist:
        print("Username tidak ditemukan")
        return
    film = input("Masukkan nama film yang ingin ditambahkan ke playlist: ")
    if film not in film_info:
        print("Film tidak ditemukan dalam database info film")
    else:
        if film not in playlist[username]:
            playlist[username].append(film)
            print(f"Film '{film}' berhasil ditambahkan ke playlist {username}")
        else:
            print(f"Film '{film}' sudah ada di playlist {username}")

def lihat_playlist(username):
    if username not in playlist:
        print("Username tidak ditemukan")
        return
    if not playlist[username]:
        print("Playlist kosong")
    else:
        print("Daftar film dalam playlist:")
        for film in playlist[username]:
            print(f"- {film}")

def lihat_info_film_admin():
    print("Daftar Info Film:")
    for film, details in film_info.items():
        print(f"- {film}:")
        print(f"  Genre: {details['genre']}")
        print(f"  Sutradara: {details.get('sutradara', 'Tidak tersedia')}")
        print(f"  Deskripsi: {details['info']}")

def cari_film():
    film = input("Masukkan nama film yang ingin dicari: ")
    if film in film_info:
        details = film_info[film]
        print(f"Informasi Film '{film}':")
        print(f"Genre: {details['genre']}")
        print(f"Sutradara: {details.get('sutradara', 'Tidak tersedia')}")
        print(f"Deskripsi: {details['info']}")
    else:
        print("Film tidak ditemukan dalam database.")

def rekomendasi_film_berdasarkan_genre():
    print("Pilih genre untuk rekomendasi film:")
    for idx, genre in enumerate(rekomendasi_film.keys(), start=1):
        print(f"{idx}. {genre}")
    
    pilihan = input("Masukkan nomor genre: ")
    
    if not pilihan.isdigit():
        print("Harap masukkan nomor yang valid")
        return
    
    pilihan = int(pilihan)
    genre_list = list(rekomendasi_film.keys())
    
    if 1 <= pilihan <= len(genre_list):
        genre = genre_list[pilihan - 1]
        print(f"Rekomendasi Film Genre {genre}:")
        for film in rekomendasi_film[genre]:
            print(f"- {film}")
    else:
        print("Pilihan tidak valid")

def hapus_film(username):
    if username not in playlist:
        print("Username tidak ditemukan")
        return
    if not playlist[username]:
        print("Playlist kosong, tidak ada film yang dapat dihapus")
        return
    
    print("Daftar film dalam playlist:")
    for idx, film in enumerate(playlist[username], start=1):
        print(f"{idx}. {film}")
    
    pilihan = input("Pilih nomor film yang ingin dihapus: ")
    
    if not pilihan.isdigit():
        print("Harap masukkan nomor yang valid")
        return
    
    pilihan = int(pilihan)
    if 1 <= pilihan <= len(playlist[username]):
        film = playlist[username].pop(pilihan - 1)
        print(f"Film '{film}' berhasil dihapus dari playlist {username}")
    else:
        print("Pilihan tidak valid")
def edit_film():
    film = input("Masukkan nama film yang ingin diedit: ")
    if film not in film_info:
        print("Film tidak ditemukan dalam database.")
        return
    
    print("Masukkan informasi baru untuk film ini:")
    info_baru = input("Deskripsi: ")
    genre_baru = input("Genre: ")
    sutradara_baru = input("Sutradara: ")

    if info_baru:
        film_info[film]['info'] = info_baru
    if genre_baru:
        film_info[film]['genre'] = genre_baru
    if sutradara_baru:
        film_info[film]['sutradara'] = sutradara_baru

    print(f"Informasi film '{film}' berhasil diperbarui.")

def menu_admin():
    while True:
        print("\nMenu Admin")
        print("1. Tambah Pengguna")
        print("2. Lihat Daftar Pengguna")
        print("3. Lihat Info Film")
        print("4. Edit Film")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_pengguna()
        elif pilihan == "2":
            lihat_pengguna()
        elif pilihan == "3":
            lihat_info_film_admin()
        elif pilihan == "4":
            edit_film()
        elif pilihan == "5":
            print("Keluar dari menu admin")
            break
        else:
            print("Opsi tidak valid, silakan pilih lagi")


def menu_user():
    username = input("Masukkan username: ")
    if username not in data_pengguna:
        print("Username tidak ditemukan")
        return

    while True:
        print("Menu User")
        print("1. Lihat Playlist")
        print("2. Tambah Film ke Playlist")
        print("3. Hapus Film dari Playlist")
        print("4. Cari Film")
        print("5. Rekomendasi Film Berdasarkan Genre")
        print("6. Info film")
        print("7. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5/6/7): ")

        if pilihan == "1":
            lihat_playlist(username)
        elif pilihan == "2":
            tambah_film(username)
        elif pilihan == "3":
            hapus_film(username)
        elif pilihan == "4":
            cari_film()
        elif pilihan == "5":
            rekomendasi_film_berdasarkan_genre()
        elif pilihan == "6":
            lihat_info_film_admin()
        elif pilihan == "7":
            print("Keluar dari menu user")
            break
        else:
            print("Opsi tidak valid, silakan pilih lagi")

def menu_utama():
    while True:
        print("\nMenu Utama")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            print("Login sebagai Admin")
            menu_admin()
        elif pilihan == "2":
            print("Login sebagai User")
            menu_user()
        elif pilihan == "3":
            print("Keluar dari program Pick ur film.")
            break
        else:
            print("Opsi tidak valid, silakan pilih lagi.")

menu_utama()