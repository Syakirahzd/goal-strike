**1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**

AuthenticationForm adalah form bawaan Django yang digunakan untuk login. Form ini otomatis menyediakan field username dan password, serta sudah memvalidasi data terhadap model User. Kelebihannya adalah sudah terintegrasi dengan sistem autentikasi Django. Mudah dipakai, tidak perlu membuat form login manual, lalu secara default sudah menghandle validasi username username dan password. Namun tetap saja pastia da kekurangannya, yaitu terbatas hanya untuk login username dan password. Sulit dikustomisasi jika ingin menambah field tambahan. Tampilannya standar sehingga kurang menarik perhatian.


**2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**

Autentikasi adalah proses memastikan identitas pengguna, contohnya login dengan username dan password. Kalau otorisasu adalah proses menetukan hak akses setelah identitas diketahui, contohnya hanya admiin yang boleh menghapus produk. Django mengatur ini dengan @login_required atau @permission_required.


**3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**


Kelebihan dari cookies adalah tidak membebani server karena data disimpan di browser, mudah digunakan untuk menyimpan preferensi user. Namun kekurangannya adalah kurang aman karena bisa saja dimodifikasi oleh user, ukurannya terbatas, dan tidak coock untuk data sensitif.


Session memiliki beberapa kelebihan, di antaranya data disimpan di server sehingga lebih aman dibanding cookies, mampu menyimpan data dalam jumlah yang lebih besar, serta terintegrasi langsung dengan Django melalui request.session. Namun, session juga memiliki kekurangan, yaitu dapat membebani server karena semua data pengguna tersimpan di sisi server, dan pada aplikasi berskala besar biasanya membutuhkan mekanisme tambahan untuk scaling, seperti penggunaan database session store atau cache server.


**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**


Cookies tidak sepenuhnya aman secara default karena dapat dicuri melalui serangan XSS (Cross-Site Scripting), dicegat lewat sniffing jika tidak menggunakan HTTPS, serta dimodifikasi secara langsung oleh pengguna. Risiko yang mungkin muncul dari kelemahan ini antara lain session hijacking dan pencurian data login. Untuk mengatasinya, Django menyediakan beberapa mekanisme keamanan, seperti penggunaan HttpOnly cookie agar tidak dapat diakses lewat JavaScript, opsi Secure cookie agar hanya dikirim melalui HTTPS, middleware CSRF protection (CsrfViewMiddleware), serta enkripsi dan signing pada session cookies sehingga tidak bisa dimodifikasi tanpa menjadi invalid.


**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

a. Pertama, kita perlu membuat fungsi dan form register dengan membuka views.py yang ada pada subdirektori main pada proyek kamu. Tambahkan import UserCreationForm dan messages pada bagian paling atas

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

b. Tambahkan fungsi register ke dalam views.py

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

c. Masih di dalam direktori main, kita tambahkan berkas forms.py 

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
```

d. Buat berkas html dalam mian/template dengan nama register.html

```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

e. buka berkas urls.py di dalam main, tambahkan import dan urlpatterns nya
```python
from main.views import register
...
path('register/', register, name='register'),
```

f. Lalu kita perlu membuat fungsi login dengan menambahkan import di views.py dan tambahkanjuga usungsi login_user di dalamnya

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

...
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

h. Selanjut kita perlu membuat berkas HTML baru dengan nama login.html di dalam direktori main/templates

```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

i. Buka urls.py dalam direktori main, lalu tambahkan import dan urlpatterns
```python
from main.views import login_user
...
path('login/', login_user, name='login'),
```

j. Selanjutnya kita membuat fungsi logout dengan menambahkan import dan fungsi logout_user di views.py dalam direktori main
```python
from django.contrib.auth import authenticate, login, logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
lalu tambahkan juga kode html di main.html untuk tombol logout

```html
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

l. Setelah membuat fungsi dan kode html, kita perlu menghubungkannya dengan urls.py 
```python
from main.views import logout_user
...
path('logout/', logout_user, name='logout'),
```

m. Kita juga perlu merestriksikan akses halaman main dan product detail
dengan mengimport login_required di dalam views.py
```python
from django.contrib.auth.decorators import login_required
...
...
@login_required(login_url='/login')
def show_main(request):
...
@login_required(login_url='/login')
def show_news(request):
...
```

n. kita juga perlu menggunakan data dati cookies dengan melakukan log out terlebih dahulu dan buka kemabli views.py dan tambahkan import 
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
ubah kode bagian login_user untuk menyimpan cookies baru bernama last_login
```python
if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
```
pada fungsi show_main, tambahkan potongan kode username dan last_login
```python
 context = {
        'title': '== GoalStrike ==',
        'npm': '2406353950',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP D',
        'product_list': product_list,
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
```

lalu ubah fungsi log_out user menjadi
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
masukan juga potongan kode di main.html untuk menampilkan terakhir login


o. Menhubungkan models product dan user. kita perlu membuka models.py pada direktori main dan menambahkan import dan potongan kode
```python
from django.contrib.auth.models import User
...
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```
lalu lakukan python manage.py makemigrations dan python manage.py migrate

p. buka kembali views dan ubah potongan creat product menjadi ini
```python
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```

modifikasi juga fungsi show_main menjadi ini
```python
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'title': '== GoalStrike ==',
        'npm': '2406353950',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP D',
        'product_list': product_list,
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)
```

tambahkan kode html di main.html untuk menampilkan tombol all article dan my article

berikut isi main.html saya
```htmml
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

<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>

<h2>Welcome, {{ username }}!</h2>
<h5>Sesi terakhir login: {{ last_login }}</h5>

<a href="?filter=all">
    <button type="button">All Articles</button>
</a>
<a href="?filter=my">
    <button type="button">My Articles</button>
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

dan ini isi dari product_detail.html saya
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

{% if product.user %}
    <p>Author: {{ product.user.username }}</p>
{% else %}
    <p>Author: Anonymous</p>
{% endif %}

{% endblock content %}

{% endblock content %}
```


ini adalah tampilan untuk user syakirah 
<img width="1890" height="868" alt="image" src="https://github.com/user-attachments/assets/87bd427d-1a2c-4bac-ace6-81f59da31855" />


ini syakirah di bagian product miliknya
<img width="1873" height="866" alt="image" src="https://github.com/user-attachments/assets/46f1328e-56ab-4ae6-931d-2bd4f8f64f11" />


ini adalah tampilan untuk user zahra
<img width="1870" height="870" alt="image" src="https://github.com/user-attachments/assets/34b0b297-c94e-4a35-9fb4-f034dab22c14" />


ini zahra di bagian produk miliknya
<img width="1880" height="874" alt="image" src="https://github.com/user-attachments/assets/de74e01b-6ed1-4789-b7ce-8394b346966a" />

Terima kasih Kak.
