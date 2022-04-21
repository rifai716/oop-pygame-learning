# Langkah 1
# sertakan library pygame
import pygame
from komponen.bentuk_grafik import Shape
from komponen.gambar import Gambar
# inisialisasi library untuk pertama kalinya
pygame.init()

# Langkah 2
# mengatur halaman
ukuran = (700, 400)
tampilan = pygame.display.set_mode(ukuran)

shape = Shape(tampilan)
gambar = Gambar(tampilan)

# Langkah 3
# membuat variabel untuk looping control
selesai = False
# membuat variabel untuk mengatur limit FPS
waktu = pygame.time.Clock()
# membuat variabel warna
PUTIH = (0xFF, 0xFF, 0xFF)
# looping game utama
while not selesai:
  # untuk menangkap segala sesuatu yang dilakukan pengguna
  for event in pygame.event.get():
    # apabila pengguna melakukan klik tombol close window
    if event.type == pygame.QUIT:
      selesai = True
  
  # hapus semua tampilan yang tampil dilayar, digantikan dengan warna putih
  tampilan.fill(PUTIH)
  # ---- PROGRAM LAINNYA BISA DILETAKAN DISINI --- #
  gambar.draw()
  shape.kotak()
  shape.garis()
  # update tampilan
  pygame.display.flip()
  # limit FPS menjadi 60
  waktu.tick(60)

# keluar dari looping dan keluar dari pygame
pygame.quit()
