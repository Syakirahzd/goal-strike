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
b. buatlah navbar.html yang responsive
```html
<nav class="navbar fixed top-0 left-0 w-full z-50">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">

      <!-- Brand -->
      <div class="flex items-center">
        <h1 class="text-xl font-bold">
          <div class="flex items-center">
            <h1 class="text-xl font-semibold">
                <span class="text-blue-800">Goal</span><span class="text-gray-900">Strike</span>
            </h1>
            </div>
        </h1>
      </div>

      <!-- Desktop Navigation -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="/" class="nav-link">Home</a>
        <a href="{% url 'main:create_product' %}" class="nav-link">Create Product</a>
      </div>

      <!-- Desktop User Section -->
      <div class="hidden md:flex items-center space-x-6">
        {% if user.is_authenticated %}
          <div class="text-right">
            <div class="text-sm font-semibold">{{ name|default:user.username }}</div>
            <div class="text-xs text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="nav-link text-red">Logout</a>
        {% else %}
          <a href="{% url 'main:login' %}" class="nav-link">Login</a>
          <a href="{% url 'main:register' %}" class="btn-primary px-4 py-2">Register</a>
        {% endif %}
      </div>

      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button id="mobile-menu-toggle" class="nav-toggle">
          <span class="sr-only">Open menu</span>
          <!-- Hamburger Icon -->
          <svg id="icon-hamburger" class="h-6 w-6 block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
          <!-- X Icon -->
          <svg id="icon-close" class="h-6 w-6 hidden" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-gray-200">
    <div class="px-6 py-4 space-y-4">

      <!-- Mobile Navigation -->
      <div class="space-y-1">
        <a href="/" class="nav-link block py-2">Home</a>
        <a href="{% url 'main:create_product' %}" class="nav-link block py-2">Create Product</a>
      </div>

      <!-- Mobile User Section -->
      <div class="border-t border-gray-200 pt-4">
        {% if user.is_authenticated %}
          <div class="mb-4">
            <div class="font-medium">{{ name|default:user.username }}</div>
            <div class="text-sm text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="nav-link text-red block py-2">Logout</a>
        {% else %}
          <div class="space-y-3">
            <a href="{% url 'main:login' %}" class="nav-link block py-2">Login</a>
            <a href="{% url 'main:register' %}" class="btn-primary block py-2 text-center">Register</a>
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</nav>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("mobile-menu-toggle");
    const menu = document.getElementById("mobile-menu");
    const iconHamburger = document.getElementById("icon-hamburger");
    const iconClose = document.getElementById("icon-close");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
      iconHamburger.classList.toggle("hidden");
      iconClose.classList.toggle("hidden");
    });
  });
</script>

```

c. lalu kita perlu mengkonfigurasi static file ke aplikasi lewat settings.py. serta konfigurasi variabel STATIC_ROOT dan STATIC_URL
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
```
```python
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
```
d. untuk styling, kita bisa membuat file global.css di dalam direktory static, global.css ini akan menjadi template yang bisa kita gunakan saat mendesign aplikasi kita sehingga lebih konsisten
```html
.form-style form input,
form textarea,
form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}

/* Fokus biru tua elegan */
.form-style form input:focus,
form textarea:focus,
form select:focus {
    outline: none;
    border-color: #1E3A8A;
    box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.2);
}

/* Checkbox */
.form-style input[type="checkbox"] {
    width: 1.25rem;
    height: 1.25rem;
    padding: 0;
    border: 2px solid #d1d5db;
    border-radius: 0.375rem;
    background-color: white;
    cursor: pointer;
    position: relative;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}

/* Checkbox ketika dicentang */
.form-style input[type="checkbox"]:checked {
    background-color: #1E3A8A;
    border-color: #1E3A8A;
}

.form-style input[type="checkbox"]:checked::after {
    content: '✓';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-weight: bold;
    font-size: 0.875rem;
}

/* Checkbox focus */
.form-style input[type="checkbox"]:focus {
    outline: none;
    border-color: #1E3A8A;
    box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.2);
}


/* ===== CARD PRODUCT STYLE ===== */
.card-style {
    background: white;
    border: 1px solid #e5e7eb; /* border-gray-200 */
    border-radius: 0.75rem;    /* rounded-xl */
    transition: all 0.3s ease-in-out;
    font-family: 'Montserrat', sans-serif;
}

.card-style:hover {
    box-shadow: 0 10px 20px rgba(30, 58, 138, 0.15); /* efek hover elegan biru tua */
}

/* Title */
.card-style h3 a {
    font-family: 'Oswald', sans-serif;
    color: #111827; /* text-gray-900 */
    transition: color 0.3s ease;
}

.card-style h3 a:hover {
    color: #1E3A8A; /* biru tua elegan */
}

/* Harga */
.card-style .price {
    color: #1E3A8A;
    font-weight: bold;
}

/* Category badge */
.card-style .badge-blue {
    background-color: #DBEAFE; /* bg-blue-100 */
    color: #1E3A8A;           /* text-blue-800 */
    text-transform: uppercase;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.5rem;
    border-radius: 0.375rem;
}

/* Badge Variants */
.badge-yellow {
  background-color: #FEF3C7; /* bg-yellow-100 */
  color: #92400E;           /* text-yellow-800 */
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
}

.badge-red {
  background-color: #FEE2E2; /* bg-red-100 */
  color: #B91C1C;           /* text-red-800 */
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
}


body {
  font-family: 'Inter', sans-serif;
  color: #1F2937; /* default text-gray-900 */
}

/* Heading */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  color: #1F2937; /* sama dengan text-gray-900 */
}

/* Paragraph */
p {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  color: #4B5563; /* sama dengan text-gray-600 */
}

/* Highlight text (misalnya harga, link utama) */
.text-highlight {
  color: #1E3A8A; /* text-blue-800 */
  font-weight: 600;
}

.btn-primary {
  background-color:  #1E3A8A; /* biru solid */
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  font-weight: 600;
  text-align: center;
  transition: background 0.3s ease;
}
.btn-primary:hover {
  background-color: #1E40AF; /* biru tua hover */
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-weight: 500;
  color: #2e3a4d;
  text-align: center;
  transition: background 0.3s ease, color 0.3s ease;
}
.btn-cancel:hover {
  background-color: #2e3a4d; /* biru pudar saat hover */
  color: white;
}

/* Alert messages */
.alert-error {
  background-color: #FEE2E2; /* bg-red-100 */
  border: 1px solid #FCA5A5; /* border-red-200 */
  color: #B91C1C;            /* text-red-700 */
  padding: 0.75rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

/* Navbar */
.navbar {
  background: white;
  border-bottom: 1px solid #e5e7eb; /* gray-200 */
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}

/* Navigation links */
.nav-link {
  color: #4B5563; /* gray-600 */
  font-weight: 500;
  transition: color 0.3s ease;
  text-decoration: none;
}

.nav-link:hover {
  color: #1F2937; /* gray-900 */
}

.nav-link.text-red {
  color: #DC2626; /* red-600 */
}

.nav-link.text-red:hover {
  color: #B91C1C; /* red-700 */
}

/* Mobile toggle button */
.nav-toggle {
  padding: 0.5rem;
  color: #6a7d98;
  transition: color 0.3s ease;
}

.nav-toggle:hover {
  color: #6a7d98;
}
```

d. styling navbar
```html
<nav class="navbar fixed top-0 left-0 w-full z-50">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">

      <!-- Brand -->
      <div class="flex items-center">
        <h1 class="text-xl font-bold">
          <div class="flex items-center">
            <h1 class="text-xl font-semibold">
                <span class="text-blue-800">Goal</span><span class="text-gray-900">Strike</span>
            </h1>
            </div>
        </h1>
      </div>

      <!-- Desktop Navigation -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="/" class="nav-link">Home</a>
        <a href="{% url 'main:create_product' %}" class="nav-link">Create Product</a>
      </div>

      <!-- Desktop User Section -->
      <div class="hidden md:flex items-center space-x-6">
        {% if user.is_authenticated %}
          <div class="text-right">
            <div class="text-sm font-semibold">{{ name|default:user.username }}</div>
            <div class="text-xs text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="nav-link text-red">Logout</a>
        {% else %}
          <a href="{% url 'main:login' %}" class="nav-link">Login</a>
          <a href="{% url 'main:register' %}" class="btn-primary px-4 py-2">Register</a>
        {% endif %}
      </div>

      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button id="mobile-menu-toggle" class="nav-toggle">
          <span class="sr-only">Open menu</span>
          <!-- Hamburger Icon -->
          <svg id="icon-hamburger" class="h-6 w-6 block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
          <!-- X Icon -->
          <svg id="icon-close" class="h-6 w-6 hidden" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-gray-200">
    <div class="px-6 py-4 space-y-4">

      <!-- Mobile Navigation -->
      <div class="space-y-1">
        <a href="/" class="nav-link block py-2">Home</a>
        <a href="{% url 'main:create_product' %}" class="nav-link block py-2">Create Product</a>
      </div>

      <!-- Mobile User Section -->
      <div class="border-t border-gray-200 pt-4">
        {% if user.is_authenticated %}
          <div class="mb-4">
            <div class="font-medium">{{ name|default:user.username }}</div>
            <div class="text-sm text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="nav-link text-red block py-2">Logout</a>
        {% else %}
          <div class="space-y-3">
            <a href="{% url 'main:login' %}" class="nav-link block py-2">Login</a>
            <a href="{% url 'main:register' %}" class="btn-primary block py-2 text-center">Register</a>
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</nav>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("mobile-menu-toggle");
    const menu = document.getElementById("mobile-menu");
    const iconHamburger = document.getElementById("icon-hamburger");
    const iconClose = document.getElementById("icon-close");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
      iconHamburger.classList.toggle("hidden");
      iconClose.classList.toggle("hidden");
    });
  });
</script>

```

e. styling halaman login
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login - GoalStrike</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen flex items-center justify-center p-8">
  <div class="max-w-md w-full">
    <div class="card-style p-6 sm:p-8 form-style">
      <div class="text-center mb-8">
        <h1 class="text-2xl mb-2">Sign In</h1>
        <p>Welcome back to GoalStrike</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="alert-error">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="alert-error mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-6">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium mb-2">Username</label>
          <input id="username" name="username" type="text" required placeholder="Enter your username">
        </div>

        <div>
          <label for="password" class="block text-sm font-medium mb-2">Password</label>
          <input id="password" name="password" type="password" required placeholder="Enter your password">
        </div>

        <button type="submit" class="btn-primary w-full">
          Sign In
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded-md text-sm border mb-2
                {% if message.tags == 'success' %} bg-green-50 border-green-200 text-green-700
                {% elif message.tags == 'error' %} bg-red-50 border-red-200 text-red-700
                {% else %} bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center pt-6 border-t border-gray-200">
        <p class="text-sm">
          Don't have an account? 
          <a href="{% url 'main:register' %}" class="text-highlight hover:underline">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

f. styling halaman register
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register - GoalStrike</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 min-h-screen flex items-center justify-center p-8">
  <div class="max-w-md w-full">
    <div class="card-style p-8 form-style">
      <div class="text-center mb-8">
        <h2 class="text-2xl mb-2">Join Us</h2>
        <p>Create your GoalStrike account</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="alert-error">{{ error }}</div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="alert-error mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" class="space-y-5">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block mb-2">{{ form.username.label }}</label>
          {{ form.username }}
        </div>

        <div>
          <label for="password1" class="block mb-2">{{ form.password1.label }}</label>
          {{ form.password1 }}
        </div>

        <div>
          <label for="password2" class="block mb-2">{{ form.password2.label }}</label>
          {{ form.password2 }}
        </div>

        <button type="submit" class="btn-primary w-full">Create Account</button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div class="{% if message.tags == 'success' %}alert-success{% elif message.tags == 'error' %}alert-error{% else %}alert-info{% endif %} mb-2">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center">
        <p class="text-sm">
          Already have an account? 
          <a href="{% url 'main:login' %}" class="text-highlight hover:underline">Sign In</a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

g. Styling halaman home dengan card_product.html. Dengan  menyertakan image (buat folder baru di static)
```html
<article class="card-style overflow-hidden">
  <!-- Thumbnail -->
  <div class="aspect-[1/1] relative overflow-hidden bg-gray-50">
    {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="{{ product.name }}"
           class="w-full h-full object-contain transform hover:scale-105 transition-transform duration-500">
    {% else %}
      <div class="w-full h-full flex items-center justify-center text-gray-400 text-sm">No Image</div>
    {% endif %}
  </div>

  <!-- Content -->
  <div class="p-4">
    <!-- Product Name & Price -->
    <div class="flex justify-between items-start mb-2">
      <h3 class="text-lg font-bold tracking-wide leading-tight line-clamp-2">
        <a href="{% url 'main:show_product' product.id %}">
          {{ product.name }}
        </a>
      </h3>
      <span class="price text-sm">
        Rp {{ product.price|floatformat:0 }}
      </span>
    </div>

    <!-- Category + Status -->
    <div class="flex items-center flex-wrap gap-2 mb-3">
      <span class="badge-blue">
        {{ product.get_category_display }}
      </span>

      {% if product.is_featured %}
        <span class="badge-yellow">
          Featured
        </span>
      {% endif %}
      {% if product.is_product_hot %}
        <span class="badge-red">
          Hot
        </span>
      {% endif %}
    </div>

    <!-- Description -->
    <p class="text-sm leading-relaxed line-clamp-3 mb-4">
      {{ product.description|truncatewords:15 }}
    </p>

    <!-- Action -->
    <div class="pt-3 border-t border-gray-100 flex justify-between items-center">
      <a href="{% url 'main:show_product' product.id %}" class="text-highlight hover:underline text-sm">
        Read more →
      </a>

      {% if user.is_authenticated and product.user == user %}
        <div class="flex space-x-3">
          <a href="{% url 'main:edit_product' product.id %}" class="text-gray-600 hover:text-gray-800 text-sm font-medium transition-colors">
            Edit
          </a>
          <a href="{% url 'main:delete_product' product.id %}" class="text-red-600 hover:text-red-700 text-sm font-medium transition-colors">
            Delete
          </a>
        </div>
      {% endif %}
    </div>
  </div>
</article>
```

setelah itu, edit di bagian main.html
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>GoalStrike</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="bg-gray-50 w-full pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

    <!-- Header Section -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Latest Product</h1>
      <p class="text-gray-600">Stay updated with the latest product stories and analysis</p>
    </div>

    <!-- Filter Section -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 card-style p-4">
      <div class="flex space-x-3 mb-4 sm:mb-0">
        <!-- All product -->
        <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter %} btn-primary {% else %} btn-cancel {% endif %}">
          All product
        </a>
        <!-- My product -->
        <a href="?filter=my" class="{% if request.GET.filter == 'my' %} btn-primary {% else %} btn-cancel {% endif %}">
          My product
        </a>
      </div>
      {% if user.is_authenticated %}
        <div class="text-sm text-gray-500">
          Last login: {{ last_login }}
        </div>
      {% endif %}
    </div>

    <!-- Product Grid -->
    {% if not product_list %}
      <div class="card-style p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.png' %}" alt="No product available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
        <p class="text-gray-500 mb-6">Be the first to share product with the community.</p>
        <a href="{% url 'main:create_product' %}" class="btn-primary inline-flex items-center px-4 py-2 rounded-md">
          Create Product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in product_list %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}

  </div>
</div>
{% endblock content %}
```

h. styling halaman product_detail
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>{{ product.name }} - GoalStrike</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Back Navigation -->
        <div class="mb-6">
            <a href="{% url 'main:show_main' %}" class="text-highlight hover:underline font-medium">
                ← Back to product
            </a>
        </div>
        
        <!-- Article -->
        <article class="card-style overflow-hidden">
            
            <!-- Header -->
            <div class="p-6 sm:p-8">
                <div class="flex flex-wrap items-center gap-2 mb-4">
                    <span class="badge-blue">{{ product.get_category_display }}</span>
                    {% if product.is_featured %}
                        <span class="badge-yellow">Featured</span>
                    {% endif %}
                    {% if product.is_product_hot %}
                        <span class="badge-red">Hot</span>
                    {% endif %}
                </div>
                
                <h1 class="text-3xl sm:text-4xl mb-2">{{ product.name }}</h1>

                <!-- Harga Produk -->
                <p class="text-highlight font-semibold text-2xl mb-4">
                    Rp {{ product.price|floatformat:0 }}
                </p>
                
                <div class="flex flex-wrap items-center text-sm text-gray-500 gap-4">
                    <time datetime="{{ product.created_at|date:'c' }}">
                        {{ product.created_at|date:"M j, Y g:i A" }}
                    </time>
                    <span>{{ product.product_views }} views</span>
                </div>
            </div>

            <!-- Featured Image -->
            {% if product.thumbnail %}
                <div class="px-6 sm:px-8">
                    <img src="{{ product.thumbnail }}" 
                         alt="{{ product.title }}" 
                         class="w-full h-64 sm:h-80 lg:h-96 object-cover rounded-lg">
                </div>
            {% endif %}

            <!-- Content -->
            <div class="p-6 sm:p-8">
                <div class="text-gray-700 leading-relaxed whitespace-pre-line text-base sm:text-lg">
                    {{ product.description }}
                </div>
            </div>

            <!-- Author Info -->
            <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
                <div class="flex items-center justify-between">
                    <div>
                        <div class="font-medium text-gray-900">
                            {% if product.user %}
                                <p>Author: {{ product.user.username }}</p>
                            {% else %}
                                <p>Author: Anonymous</p>
                            {% endif %}
                        </div>
                        <p class="text-sm text-gray-500">Author</p>
                    </div>
                </div>
            </div>
        </article>
    </div>
</div>
{% endblock content %}

```

i. styling halaman create_product
```html
{% extends 'base.html' %}
{% block meta %}
<title>Create product - GoalStrike </title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-highlight hover:underline font-medium">
        ← Back to product
      </a>
    </div>
    
    <!-- Form -->
    <div class="card-style p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl mb-2">Create New Product</h1>
        <p>Share your product and stories with the community</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium mb-2">
              {{ field.label }}
            </label>
            <div>
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 btn-cancel">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 btn-primary flex-1">
            Publish Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}

```

j. terakhir, styling halaman edit_product
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Edit Product - GoalStrike</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-highlight hover:underline font-medium">
        ← Back to product
      </a>
    </div>
    
    <!-- Form -->
    <div class="card-style p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl mb-2">Edit Product</h1>
        <p>Update your product and stories</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium mb-2">
              {{ field.label }}
            </label>
            <div>
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 btn-cancel">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 btn-primary flex-1">
            Update Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}

```
