print("=" * 50)
print("     KASIR MINIMARKET - CEK DISKON MEMBER")
print("=" * 50)

nama_pembeli = input("Nama Pelanggan\t\t\t: ")
print(nama_pembeli)
input_kartu = input("Punya Kartu Member? (y/t)\t: ").strip().lower()
print(input_kartu)

try:
  total_belanja = int(
      input("Masukkan Total Belanja (Rp)\t: Rp ").replace(".", "").replace(",", "")
  )
  print(total_belanja)
except ValueError:
  total_belanja = 0

punya_kartu_member = True if input_kartu == 'y' else False
dapat_diskon = punya_kartu_member

print("\n" + "=" * 50)
print("                STRUK PENGECEKAN")
print("=" * 50)
print(f"Pelanggan        : {nama_pembeli}")
print(f"Kartu Member     : {'ADA' if punya_kartu_member else 'TIDAK ADA'}")
print(f"Total Belanja    : Rp {total_belanja:,}".replace(",", "."))
print("-" * 50)

if dapat_diskon:
  print(
      f"Hasil            : Selamat {nama_pembeli}, Anda berhak mendapatkan"
      " diskon member! "
  )
else:
  print(f"Hasil            : Maaf {nama_pembeli},")
  print("                   kamu tidak mendapatkan diskon")
  print("                   khusus untuk pemilik kartu member.")

print("=" * 50)