1. Apa perbedaan antara synchronous request dan asynchronous request?
Perbedaan utama antara synchronous dan asynchronous request terletak pada alur eksekusi (flow of execution). Pada sinkron, klien (misalnya, browser) akan mengirim permintaan dan menghentikan (memblokir) semua tugas lain hingga respons dari server tiba, sehingga aplikasi terkesan "membeku" jika permintaan lama. Sebaliknya, pada asinkron (seperti yang digunakan AJAX), klien mengirim permintaan dan langsung melanjutkan eksekusi tugas lain tanpa menunggu, membuat aplikasi tetap responsif; respons dari server akan ditangani belakangan melalui fungsi callback.


2. Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX bekerja di Django melalui alur yang non-blokir: Pengguna memicu aksi di browser, yang kemudian dieksekusi oleh JavaScript untuk membuat permintaan HTTP asinkron (biasanya membawa data JSON) ke sebuah URL Django. Permintaan ini diproses oleh View Django yang terkait, yang berinteraksi dengan Model dan Database. View kemudian membuat respons, seringkali berupa JSON, yang dikirim kembali ke klien. JavaScript menerima JSON tersebut dan, alih-alih me-render ulang seluruh halaman, ia hanya memanipulasi DOM untuk memperbarui bagian spesifik dari halaman web.


3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungan menggunakan AJAX dibandingkan render biasa di Django sangat signifikan bagi User Experience (UX). Dengan AJAX, hanya data yang diperlukan yang dikirim dan diterima (bukan seluruh HTML halaman), menghasilkan pemuatan yang lebih cepat dan penggunaan bandwidth yang lebih efisien. Aplikasi terasa lebih mulus dan responsif karena antarmuka pengguna tidak pernah berhenti atau flickering (blinking) seperti saat page refresh sinkron. Selain itu, state aplikasi (seperti posisi scroll) juga tetap terjaga.


4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Untuk memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django, beberapa lapisan pertahanan harus diterapkan. Yang paling penting adalah menyertakan CSRF Token pada setiap permintaan POST/PUT/DELETE untuk mencegah Cross-Site Request Forgery. Semua komunikasi harus dilakukan melalui HTTPS untuk mengenkripsi data sensitif seperti kredensial. Selain itu, validasi data yang ketat harus dilakukan di sisi server (View Django), dan password harus selalu di-hash menggunakan fungsi keamanan bawaan Django.


5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX memengaruhi pengalaman pengguna (UX) secara dramatis dengan menciptakan website yang terasa seperti aplikasi desktop yang cepat dan modern. Karena pembaruan konten dilakukan secara in-place tanpa full page reload, interaksi terasa instan dan mulus (seamless). Peningkatan kecepatan dan responsivitas ini mengurangi frustrasi dan meningkatkan kepuasan pengguna, karena mereka mendapatkan feedback visual yang cepat dan dapat melanjutkan interaksi tanpa gangguan menunggu seluruh halaman dimuat ulang.