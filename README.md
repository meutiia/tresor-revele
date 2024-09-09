# Trésor Révélé
link PWS: 

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Instalasi python, django, github, dan virtual environment.
    - Tambahkan requirements, dependencies, dan konfigurasi yang diperlukan untuk melakukan deployment.
    - Membuat project dan aplikasi (main) menggunakan startproject dan startapp.
    - Menambahkan atribut dan property yang diperlukan pada models.py lalu migrasi model untuk update data base menggunakan makemigrations dan migrate.
    - Menambahkan data yang diperlukan pada views.py.
    - Membuat main.html sebagai template tampilan yang akan diberikan.
    - Menghubungkan urls aplikasi dan project.
    - Deployment hasil ke Pacil Web Service (PWS) agar dapat diakses.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    client request -> urls.py -> views.py -> models.py -> views.py -> HTML -> client response

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    Git memudahkan pengembang dalam **berkolaborasi**, menyimpan **back-up data**, melakukan **branching**, dan melihat atau menggunakan ulang versi lama dari kode tertentu. Dengan menggunakan git, perangkat lunak yang dalam pengembangannya melibatkan banyak orang dapat dengan mudah disesuaikan karena sebuah repository dapat diakses dan dipakai oleh semua pihak bersangkutan. Bagi pengguna pribadi, git juga dapat digunakan sebagai tempat penyimpanan back-up data yang kita perlukan dalam proses pengembangan software. Hal ini akan mengurangi risiko kehilangan data penting yang dapat menghambat proses developing.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Django dipilih sebagai framework untuk pemula adalah karena:
        - Django sudah memiliki banyak fitur bawaan yang dapat mempermudah kita untuk membuat dan mengembangkan sebuah software.
        - Django dinilai sebagai salah satu framework yang memiliki dokumentasi paling lengkap, sehingga mudah untuk dipelajari lebih lanjut.
        - Django memiliki prinsip DRY atau Don't Repeat Yourself, prinsip ini membuat code pada Django lebih efisien dan tidak repetitif.
        - Django memiliki struktur yang jelas dan tidak membingungkan bagi pemula. Pada Django, aplikasi yang berbeda akan otomatis berada pada folder yang berbeda juga.
        - Django dapat digunakan untuk membuat project kecil maupun besar.

### 5. Mengapa model pada Django disebut sebagai ORM?
    Karena, Django menggunakan teknik ORM atau Object-Relational-Mapping yang mememungkinkan pengembang dapat mengakses database relasional seperti PostgreSQL, MySQL, dan SQLite dengan menggunakan kode python, tanpa perlu menulis query SQL (akses, kelola, manipulasi data) secara manual.