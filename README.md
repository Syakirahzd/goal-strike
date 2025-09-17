**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery merupakan proses inti yang memastikan sebuah platform dapat berjalan dengan optimal. Mekanisme ini berperan dalam menjamin data tersalurkan dengan aman dan efisien di antara berbagai elemen, seperti server, basis data, maupun antarmuka pengguna. Tanpa adanya sistem tersebut, informasi tidak akan tersampaikan ke pengguna atau layanan lain secara tepat waktu, yang pada akhirnya dapat menurunkan fungsionalitas, kinerja, serta kualitas pengalaman pengguna pada platform.


**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Walaupun memiliki beberapa keterbatasan, JSON secara umum dipandang lebih unggul dan lebih populer dibandingkan XML karena tiga faktor, yaitu:

a. Sederhana dan Ringkas: Struktur JSON yang minimalis membuatnya lebih mudah dipahami dan ditulis baik oleh manusia maupun mesin. Berbeda dengan XML yang menggunakan banyak tag pembuka dan penutup, JSON lebih efisien sehingga ukuran file menjadi lebih kecil, penggunaan bandwidth berkurang, dan proses transfer data berlangsung lebih cepat.

b. Kecepatan Pemrosesan: Parsing JSON cenderung lebih cepat dibandingkan XML. Dalam konteks aplikasi yang sering bertukar data, seperti API, hal ini berpengaruh besar terhadap kinerja sistem dan kenyamanan pengguna.

c. Integrasi Native: Karena formatnya serupa dengan objek JavaScript, JSON dapat diproses langsung tanpa perlu library tambahan yang rumit. Hal ini membuat penerapannya pada aplikasi web menjadi lebih praktis.

Walaupun XML tetap memiliki kelebihan, seperti validasi skema dan dukungan namespace, JSON dianggap lebih relevan untuk kebutuhan modern karena menawarkan kecepatan, efisiensi, serta kemudahan integrasi yang sangat penting, terutama pada aplikasi berbasis web.


**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

is_valid() adalah method pada form Django yang digunakan untuk memvalidasi data yang dikirimkan pengguna. Method ini akan memeriksa apakah data dalam form (biasanya berasal dari request.POST) sudah sesuai dengan aturan yang ditentukan di dalam ProductForm, seperti jenis data, panjang karakter, serta kelengkapan field wajib.

Apabila seluruh data sesuai dengan aturan, is_valid() akan mengembalikan nilai True sehingga data dapat diproses lebih lanjut, misalnya disimpan ke dalam database. Namun, jika ada data yang tidak valid pada satu atau beberapa field, method ini akan mengembalikan nilai False sekaligus memberikan pesan error yang relevan.

Dengan kata lain, is_valid() berfungsi sebagai gerbang utama yang menjaga aplikasi agar hanya menerima data yang valid. Mekanisme ini memastikan integritas data dan keamanan aplikasi tetap terjamin, karena mencegah masuknya input yang salah ataupun berpotensi membahayakan.


**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

csrf_token adalah fitur keamanan penting di Django yang digunakan untuk melindungi form dari serangan CSRF (Cross-Site Request Forgery). Token ini berupa nilai unik yang disisipkan ke setiap form, dengan tujuan memastikan bahwa permintaan yang dikirim ke server benar-benar berasal dari form sah di aplikasi kita, bukan dari situs lain yang berbahaya.

Secara sederhana, serangan CSRF terjadi ketika seorang pengguna yang sedang login di situs kita tanpa sadar mengunjungi situs berbahaya milik penyerang. Situs tersebut dapat memaksa browser pengguna mengirimkan permintaan ke server kita. Karena browser otomatis melampirkan cookie sesi yang valid, tanpa adanya token verifikasi, server tidak mampu membedakan apakah request berasal dari sumber asli atau dari pihak berbahaya. Akibatnya, server bisa saja memproses perintah penyerang, misalnya mengubah data pengguna atau melakukan aksi yang merugikan. Alur serangan CSRF dapat dijelaskan sebagai berikut:

a. Pengguna login ke aplikasi kita dan browser menyimpan session cookie yang menandakan pengguna sudah terotentikasi.

b. Penyerang membuat situs berbahaya yang berisi form tersembunyi untuk mengirim request ke URL aplikasi kita.

c. Pengguna yang masih login di aplikasi kita dan membuka situs berbahaya. Browser secara otomatis menjalankan form tersembunyi tersebut tanpa sepengetahuan pengguna.

Jika tidak ada csrf_token yang divalidasi, Django akan menganggap request tersebut sah karena dikirim oleh pengguna yang terotentikasi, lalu memprosesnya (misalnya menambahkan produk ke keranjang atau mengubah data).

Dengan adanya csrf_token, Django dapat memverifikasi bahwa setiap permintaan memang berasal dari form resmi aplikasi, sehingga serangan CSRF dapat dicegah.


**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

a. kita membuat direktori baru bernama template di dalam direktori utama. di dalam template tersebut, buat base.html sebagai kerangka umum dan hubungkan base.html ini dengan settings.py agar base.html terdeteksi sebagai berkas template

b. Kita ke direktori template yang ada di dalam direktori main, edit berkas main.html

c. Masih di dalam direktori main, kita tambahkan berkas forms.py 
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
```

d. buka berkas views.py dalam direktori main dan tambahkan import dan fungsi fungsi fungsi yang dibutuhkan

```python
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product


# Create your views here.
def show_main(request):
    product_list = Product.objects.all()

    context = {
        'title' : '== GoalStrike ==',
        'npm': '2406353950',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP D',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_product()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
```
e. buka berkas urls.py di dalam main, tambahkan urlpatterns nya
```python
path('create-product/', create_product, name='create_product'),
path('product/<str:id>/', show_product, name='show_product'),
```

f. update berkas main.html buat beberapa berkas di dalam direktori template (main/template)
main.html
```html
<h1>GoalStrike</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

<a href="{% url 'main:create_product' %}">
  <button>+ Add Product</button>
</a>

<hr>

{% if not product_list %}
<p>Belum ada product dalam GoalStrike.</p>
{% else %}

{% for product in product_list %}
<div>
  <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>

  <p> Rp {{ product.price }} |
    {{ product.get_category_display }}</b>{% if product.is_featured %} | 
    <b>Featured</b>{% endif %}{% if product.is_news_hot %} | 
    <b>Hot</b>{% endif %} | Views: {{ product.product_views }}</p>

  {% if product.thumbnail %}
  <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
  <br />
  {% endif %}

  <p>{{ product.description|truncatewords:25 }}...</p>

  <p><a href="{% url 'main:show_product' product.id %}"><button>Detail Product</button></a></p>
</div>

<hr>
{% endfor %}

{% endif %}
```

create_product
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add PRODUCT" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

product_detail
```html
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

<h1>{{ product.name }}</h1>
<p> Rp {{ product.price }}|
    <b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
    <b>Featured</b>{% endif %}{% if product.is_product_hot %} | 
    <b>Hot</b>{% endif %} | Views: {{ product.product_views }}</p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
<br /><br />
{% endif %}

<p>{{ product.description }}</p>

{% endblock content %}
```

g. buka settings.py dan tambahkan entri url proyek 
```python
CSRF_TRUSTED_ORIGINS = [
    "https://syakirah-zahra-goalstrike.pbp.cs.ui.ac.id",
    "https://pbp.cs.ui.ac.id/syakirah.zahra/goalstrike/"
]
```

h. jalankan proyek dengan python manage.py runserver

i. mengembalikan data dalam bentuk xml, dengan membuka views.py, tambahkan import 
```python
from django.http import HttpResponse
from django.core import serializers
```
dan tambahkna juga fungsi
```python
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
```
lalu buka urls.py, lengkapi import dan path yang sesuai. jalankan proyek dengan  http://localhost:8000/xml/

j. mengembalikan data dalam bentuk json, dengan membuka views.py dan tambahkan fungsi
```python
def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")
```
lalu buka urls.py, lengkapi import dan path yang sesuai. jalankan proyek dengan  http://localhost:8000/json/

l. mengembalikan data dalam bentuk xml berdasarkan id dengan menambahkan fungsi di dalam views.py 
```python
def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
```
lalu lengkapi urls.py dengan impoert dan path yang sesuai. jalankan proyek dengan  http://localhost:8000/xml/[news_id]/

m. mengembalikan data dalam bentuk json berdasarkan id dengan menambahkan fungsi di dalam views.py 
```python
def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
```
lalu lengkapi urls.py dengan impoert dan path yang sesuai. jalankan proyek dengan  http://localhost:8000/json/[news_id]/

**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**

Saya bisa mengerjakan tutorial dengan baik. Dokumen tutorial rapi dan terstruktur, saya bisa memahami materi dengan baik. Tutorial yang di berikan juga sangat membantu saya dalam menyelesaikan tugas 3 ini. Terima kasih Tim Asdos.

**Hasil API Call dengan Postman**

XML

<img width="1920" height="1080" alt="Screenshot (999)" src="https://github.com/user-attachments/assets/7b47d88e-22b2-4ec8-9cb6-58da7eca21c1" />

JSON

<img width="1920" height="1080" alt="Screenshot (1000)" src="https://github.com/user-attachments/assets/4b283402-cdef-4c0b-9258-2d0dfe01af97" />


XML with ID

<img width="1920" height="1080" alt="Screenshot (1001)" src="https://github.com/user-attachments/assets/ab2685b0-fd81-4c98-bbfe-2c8efe80bcca" />


JSON with ID

<img width="1920" height="1080" alt="Screenshot (1002)" src="https://github.com/user-attachments/assets/9ae722aa-e516-4673-be0c-612703045659" />
