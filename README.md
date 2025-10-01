1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Ketika beberapa selector CSS menargetkan elemen HTML yang sama, browser akan menerapkan gaya berdasarkan hierarki prioritas yang disebut spesifisitas. Urutan dari prioritas tertinggi ke terendah adalah: !important (yang akan mengesampingkan semua aturan lain), inline styles (atribut style di dalam tag HTML), ID selectors (contoh: #header), class, attribute, and pseudo-class selectors (contoh: .tombol, [type="text"], :hover), dan yang terendah adalah type selectors (contoh: h1, p). Jika dua selector memiliki spesifisitas yang sama, maka aturan yang didefinisikan paling akhir di dalam file CSS-lah yang akan diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design menjadi konsep yang sangat penting dalam pengembangan web karena memastikan sebuah aplikasi dapat memberikan pengalaman pengguna (UX) yang optimal di berbagai ukuran layar, mulai dari desktop hingga smartphone. Dengan semakin banyaknya pengguna yang mengakses internet melalui perangkat mobile, situs yang tidak responsif akan sulit dinavigasi, memaksa pengguna untuk melakukan pinch-and-zoom, dan sering kali menyebabkan mereka meninggalkan situs tersebut. Desain yang responsif tidak hanya meningkatkan kepuasan pengguna tetapi juga menjadi faktor penting dalam peringkat mesin pencari (SEO). Sebagai contoh, situs berita seperti The Guardian menerapkan responsive design dengan sangat baik; tata letaknya berubah dari multi-kolom di desktop menjadi satu kolom yang mudah digulir di ponsel. Sebaliknya, contoh situs yang belum responsif adalah beberapa situs akademik atau pemerintah yang lebih tua, di mana saat dibuka di ponsel, tampilannya sama persis seperti di desktop, dengan teks yang sangat kecil dan sulit dibaca.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin, border, dan padding adalah komponen fundamental dari CSS box model yang mengatur ruang di sekitar sebuah elemen HTML. Perbedaannya terletak pada posisi dan fungsinya: padding adalah ruang transparan di dalam elemen, yang menciptakan jarak antara konten (teks/gambar) dengan border. Border adalah garis yang mengelilingi padding dan konten, yang bisa diatur ketebalan, gaya, dan warnanya. Sementara itu, margin adalah ruang transparan di luar border, yang berfungsi untuk menciptakan jarak antara elemen tersebut dengan elemen lain di sekitarnya. Ketiganya dapat diimplementasikan dengan mudah dalam CSS, sebagai contoh: .box { margin: 20px; border: 2px solid black; padding: 15px; }


4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid adalah dua modul tata letak modern di CSS yang berfungsi untuk mengatur dan menyelaraskan elemen secara efisien. Flexbox adalah sistem tata letak satu dimensi, yang sangat ideal untuk mendistribusikan ruang dan menyusun item dalam satu baris atau satu kolom. Kegunaannya sangat terasa saat membuat komponen seperti navigation bar, menyelaraskan item di dalam sebuah kartu (card), atau secara mudah menengahkan elemen secara vertikal. Di sisi lain, Grid Layout adalah sistem tata letak dua dimensi yang mengontrol baris dan kolom secara bersamaan. Hal ini membuatnya sangat kuat untuk merancang tata letak halaman web secara keseluruhan, seperti mengatur posisi header, sidebar, konten utama, dan footer dalam sebuah struktur kisi yang kompleks dan terprediksi.



5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Membuat Fitur Edit
a. kita harus membuat fungsi edit_product terlebih dahulu di dalam views.py
``` python
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
```

b. lalu buat edit_news.html, dan kondigurasikan ke dalam urls.py (import dan masukkan ke dalam url pattern). Hubungkan njuga dengan main.html

Membuat Fitur Delete
a. kita harus membuat fungsi delete di views
```python
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

b. masukan html bagian delete di bagian main.html, serta konfigurasikan di dalam urls.py (import dan masukkan ke dalama url pattern)

Mendesign
a. menambahkan tailwind di dalam base.html
b. 