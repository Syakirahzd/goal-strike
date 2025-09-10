**Implementasi Aplikasi GoalStrike**

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
   a. Membuat sebuah proyek Django baru
   1) Membuat repository di Github
   2) Melakukan clone repository ke local
   3) Menginisiasi virtual environment python di repo dengan python -m venv env dan diaktifkan dengan source env/bin/activate
   4) Membuat requirements.txt dan melakukan instalasi secara rekursif dengan pip install -r requirements.txt
   5) Inisiasli proyek django dengan django-admin startproject goasl_strike .
   6) Membuat .env dan .env.prod dan melakukan konfirgurasi databse dan credentials.
   7) Melakukan modifikasi pada settings.py untuk menambahkan environment variables, setting ALLOWED_HOSTS untuk mengizinkan host yang dapat deploy, menambahkan konfigurasi PRODUCTION, dan menyesuaikan konfigurasi DATABASES.
   8) Setelahnya lakukan migrasi dengan python manage.py migrate
   
   b. Membuat aplikasi dengan nama main pada proyek
   1) Membuat aplikasi dengan python manage.py startapp main
   2) Menambahkan daftar aplikasi main pada INSTALLED_APPS di settings.py
      
   c. Melakukan Routing pada proyek agar dapat menjalankan aplikasi main
   1) Menginisiasikan main pada INSTALLED_APPS di settings.py
   2) Buat urls.py pada aplikasi main
   3) Menginisiasikan root ke halaman views.py untuk bisa menjalankan aplikasi
  
   d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribute
   1) import models dari django ke dalam models.py
   2) membuat class Product dengan parameter models.Model
   3) Melakukan inisiasi variable yang sesuai dengan atribut wajib yang telah didefinisikan.
      variabel: name, price, description, thumbnail, category, is_featured
         
   e. Membuat fungsi views.py dan dikembalikan dalam template HTML
   1) Membuat fungsi def show_main(request) pada views.py
   2) Dalam show_main, berikan return berupa render dengan parameter request, main.html, db.
   3) Buat folder templates yang berisi index.html dalam apps main, dan buat tampilan html di dalamnya.
  
   f. Membuat routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
   1) Inisiasi nama app dan pathnya pada urls.py di aplikasi main
   2) Import path dan include pada urls.py di folder project, lalu tambahkan route main di sana dengan path([route], include('main.urls')) untuk menampilkan aplikasi
  
   g. Melakukan deployment ke PWS
   1) Membuat project di PWS
   2) Menyalin credentials berupa username dan password
   3) Menginisiasikan environs sesuai dengan .env.prods
   4) Menambahkan remote pws ke project dengan git remote add pws https://pbp.cs.ui.ac.id/syakirah.zahra/goalstrike
   5) Lalu push project ke PWS dengan git add, commit, dan git push pws master
   6) Selanjutnya akan diminta username dan password, masukan sesuai dengan yang telah diberikan diawal
   7) Push project dan secara otomatis akan terdeploy

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
<img width="586" height="928" alt="Django" src="https://github.com/user-attachments/assets/715833b5-bd63-4720-b254-5f45c28592de" />

3. Jelaskan peran settings.py dalam proyek Django!
   settings.py merupakan tempat untuk melakukan konfigurasi project, dalam file tersebut kita dapat melakukan penyesuaian untuk project atau aplikasi yang kita buat, termasuk pengaturan environment, deployment, dan lain-lain.
     
4. Bagaimana cara kerja migrasi database di Django?
   Migrasi di django merupakan cara untuk membuat perubahan kepada model yang telah dibuat ke schema database.
   Cara kerja migrasi:
   a. makemigrations, untuk membuat migrasi baru berdasarkan perubahan yang dibuat terhadap model
   b. migrate, untuk memasang/melepas migrasi yg dibuat
   Secara singkat migrasi bekerja dengan cara membuat tabel, ataupun kolom baru berdasarkan model yang dibuat atau attribute yang ditambah

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Django adalah framework Python yang sering disebut sebagai "batteries-included". Artinya, Django memiliki banyak fitur bawaan yang siap pakai, sehingga kita bisa langsung fokus membangun aplikasi tanpa perlu menginstal banyak tambahan fitur. Dengan banyaknya fitur yang siap pakai dan struktur yang jelas, Django memungkinkann pemula menhasilkan aplikasi yang dapat digunakan dalam waktu singkat. Django juga merpuakan proyek Python gratis sehingga cocok untuk mahasiswa yang ingin belajar. Selain itu, di mata kuliah PBP ini kita diharapkan untuk membangun sebuah aplikasi berbasis web dengan Python. Django adalah salah satu framework web yang palimg populer untuk pengembangan aplikasi Python.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
   Tutorial 1 disampaikan dengan sangat jelas sehingga mudah dipahami. Beban tugas yang diberikan juga proporsional, sehingga saya dapat lebih banyak meluangkan waktu untuk benar-benar memahami materi, bukan hanya sekadar mengikuti instruksi. Hal ini membuat proses belajar menjadi lebih efektif. Selain itu, Tutorial 1 juga sangat membantu saya dalam menyelesaikan Tugas 2.

Terima kasih tim Asdos.

Referensi:
Tim Dosen PBP. (n.d.). *Introduction to the Internet and Web Framework* [PowerPoint slides]. Fakultas Ilmu Komputer, Universitas Indonesia.

Tim Pengajar Pemrograman Berbasis Platform PBP. (2025, 27 Agustus). *Tutorial 0: Konfigurasi dan Instalasi Git dan Django* [Halaman web]. Fakultas Ilmu Komputer, Universitas Indonesia. Diakses tanggal 10 September 2025, dari pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-0

Tim Pengajar Pemrograman Berbasis Platform PBP. (2025, 21 Agustus). *Tutorial 1: Pengenalan Aplikasi Django dan Model-View-Template (MVT) pada Django* [Halaman web]. Fakultas Ilmu Komputer, Universitas Indonesia. Diakses tanggal 10 September 2025, dari pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-1

Django Software Foundation. (n.d.). *Django: The web framework for perfectionists with deadlines*. Diakses tanggal 10 September 2025, dari https://www.djangoproject.com/

Amazon Web Services. (2024). *Apa itu Django?*. Diakses pada 10 September 2025, dari aws.amazon.com/id/what-is/django/
