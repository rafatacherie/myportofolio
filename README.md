Nama  : Rafata Zahi Cherie

NPM   : 2506621592

Kelas : PBP C

### Tugas 1

1. Ya, dalam merancang struktur KTML, saya memanfaatkan elemen semantik HTML5 hampir 
    di setiap bagian, terutama tag `<section>` untuk membagi setiap bagian utama 
    portofolio, seperti ``#home, #education, #experience, #skills, #skills, dan #contact``, 
    serta tag `<footer>` untuk bagian penutup paling bawah halaman.
    
    **Alasan**: `<section>` dipilih karena tiap bagian (Home, Education, Experience, Skills, 
    dan Contact) memang mempresentasikan blok konten tematik yang berdiri sendiri dalam 
    satu bagian/halaman. Elemen semantik ini membantu dalam pembuatan static web karena 
    mudah dibaca, dipahami, dan dirawat (maintainable) selama proses pengembangan, serta 
    membantu mesin pencari memahami informasi penting pada website portofolio dengan lebih baik.
    `<article>` tidak dipakai karena konten di dalam portofolio (misalnya kartu Experience) 
    bukan konten yang berdiri sendiri dan bisa didistribusikan lepas dari konteks halaman 
    (seperti artikel blog atau berita), kartu-kartu tersebut tetap bergantung pada konteks 
    section induknya.
    `<aside>` juga tidak relevan karena tidak ada konten sekunder/sampingan di desain ini. 
    Semua informasi ditampilkan sebagai konten utama yang sejajar.

2. Saat mengatur CSS agar tetap responsive, tantangan tata letak terbesar yang saya temukan 
    adalah mengubah elemen multi-kolom horizontal menjadi tata letak vertikal tanpa merusak 
    proporsi visual.

    **Contoh kasus**: pada bagian experience, terdapat flip box yang sejajar secara horizontal 
    dan pada bagian skills juga, jenis skills dibagi menjadi 2 kolom. Sehingga saat layar 
    mengecil akan rawan terhimpit dan teks nya menjadi keluar batas jika dipaksakan dalam 
    bentuk aslinya. 

    Cara mengevaluasi dan menetukan prioritas ukuran/posisi elemen: 
    - **Content flow**: mengevaluasi halaman pada berbagai breakpoint (seperti 1285px, 991px, 
    dan 895px). Jika elemen horizontal mulai terhimpit, akan diprioritaskan tata letak 
    dengan satu kolom sehingga memanjang ke bawah (vertikal).
    - **Visual**: saat berpindah ke tampilan mobile, elemen visual yang besar (seperti foto profil) 
    diprioritaskan posisinya agar berada di atas teks perkenalan untuk menyesuaikan alur.
    - **Skalabilitas font**: menurunkan ukuran font dasar `(html { font-size: 55%; })` pada breakpoint 
    tertentu agar semua teks yang menggunakan satuan rem otomatis menyusut secara proporsional.
    
3. Sebagai website statis murni, batasan terbesar yang saya rasakan dalam menyajikan informasi 
    secara optimal meliputi:
    - Pengunjung tidak dapat mengirimkan pesan langsung dari kotak input portofolio ke email 
    saya tanpa bantuan pihak ketiga atau pembukaan aplikasi email eksternal.
    - Setiap kali ada pembaruan data pendidikan, pengalaman baru, atau persentase keahlian, 
    saya harus membongkar dan mengubah baris kode HTML/CSS secara manual.

    Fungsionalitas dinamis yang ingin ditambahkan pada iterasi selanjutnya:
    form kontak fungsional yang menggantikan tombol ``"Send me a message"`` saat ini. Form ini 
    akan berisi tiga input utama, meniru struktur email pada umumnya, seperti email pengirim dan 
    penerima, subjek email, dan isi pesan. karena saat ini, tombol ``"Send me a message"`` hanya 
    membuka aplikasi email default pengguna ``(mailto:)``. Dengan form input langsung di halaman, 
    pesan bisa dikirim tanpa perlu berpindah aplikasi.

---

### Penggunaan AI Tugas 1

Dalam tugas ini, saya menggunakan tutorial yang tersedia melalui youtube dan google gemini untuk
beberapa section. Untuk section home, education, dan experience saya menggunakan source code dari
tutorial youtube lalu disesuaikan dengan gaya yang saya inginkan, seperti warna font, ukuran, dan 
animasi. Pada section experience, saya memberikan ide untuk animasi boxnya (button "see detail" dan 
scroll text) kepada google gemini dan melakukan peninjauan ulang terhadap beberapa hasil yang diberikan.
Lalu, untuk section skills, saya menggunakan tutorial youtube dan disempurnakan menggunakan google 
gemini agar skills bar dapat sesuai layout yang saya inginkan (sejajar horizontal). Selanjutnya, untuk 
section contact, idenya dari saya sendiri (button "send me a message") yang terinspirasi dari fitur di 
section yang sudah dibuat sebelumnya, tetapi untuk code diambil dari tutorial youtube dan disempurnakan 
dengan google gemini. Terakhir, untuk footer juga mengikuti tutorial youtube dan disempurnakan serta 
disesuaikan agar sesuai dengan keinginan menggunakan google gemini.

**Lampiran Prompting:**
- **Section Experience (flip box)**: Berdasarkan kode ini [kode dari tutorial], bisakah buat agar terdapat 
    button "see detail" lalu menampilkan deskripsi dari pengalaman yang dilakukan. Buat agar tulisannya 
    tidak keluar dari box, dan dapat di scroll jika teksnya panjang. Kembalikan lagi ke halaman depan 
    dari box dengan button "back".
- **Section Skills (skills bar)**: Berdasarkan kode ini [kode dari tutorial], bisakah buat untuk 2 jenis skills 
    (technical and soft skills) dengan tampilan sejajar horizontal dan untuk tiap skills berikan 5 bar serta
    berikan garis pemisah antara 2 jenis skills tersebut.
- **Section Contact (button "send me a message")**: Berdasarkan kode ini [kode dari tutorial] sesuaikan agar 
    button dapat mendirect ke email untuk mengirimkan pesan.
- **Section Footer (logo, navbar, dan copyright)**: Berdasarkan kode ini [kode dari tutorial] sesuaikan agar 
    layout footer berbaris berurutan dari atas ke bawah (vertikal) dan rata tengah.

**AI Disclosure & Analisis:**
- **Tools yang Digunakan**: Claude
- **Analisis Keterbatasan AI**: Ketika mencoba membangun komponen dari awal (*build from scratch*), AI memiliki 
    keterbatasan dalam memahami estetika visual dan presisi layout yang saya inginkan. Hasil kode pertama 
    dari AI sering kali tidak sesuai ekspektasi, sehingga memicu proses trial and error yang berulang-ulang 
    dan memakan banyak waktu jika hanya mengandalkan teks.
- **Perbaikan Manual (oleh saya)**: Untuk mengatasi keterbatasan AI, saya beralih mencari referensi yang cocok 
    secara visual dari tutorial YouTube. Untuk beberapa section yang ingin saya rombak, saya perlu setidaknya 
    setengah gambaran kode yang sesuai secara visual, baru saya memberikan potongan kode tersebut ke AI dan 
    menyesuaikannya secara desain. Saya tidak menyuruh AI mendesain dari nol, melainkan memberikan instruksi 
    spesifik untuk memodifikasi, menambah fitur baru (seperti tombol back dan scroll pada flip box), serta 
    menyelaraskan layout agar sesuai dengan desain yang saya inginkan.

---

### Tugas 2

1. Alur ketika pengguna membuka halaman portofolio
    
    Ketika pengguna membuka halaman portofolio, misalnya `/experience/`, alurnya adalah:
    **Browser → `urls.py` proyek → `urls.py` aplikasi → View → Model → Template → Browser**

    - **`urls.py` proyek** menerima request dari browser dan menentukan aplikasi mana 
        yang menangani URL tersebut. Misalnya, pada `portofolio/urls.py` terdapat:

        ```python
        path("", include("main.urls"))
        ```
        sehingga request diteruskan ke `main/urls.py`.

    - **`urls.py` aplikasi** menentukan view yang sesuai dengan URL. Contohnya:

        ```python
        path("experience/", show_experience, name="show_experience")
        ```
        sehingga URL `/experience/` akan menjalankan `show_experience`.

    - **View** memproses request dan mengambil data yang diperlukan dari model. Contohnya:
        
        ```python
        def show_experience(request):
            context = {
                "name": "Rafata Zahi Cherie",
                "experience_list": Experience.objects.all(),
            }
            return render(request, "experience.html", context)
        ```

    - **Model** berfungsi sebagai penghubung dengan database. `Experience.objects.all()` 
        mengambil data pengalaman yang tersimpan di database.

    - **Template** (`experience.html`) menerima data dari view dan 
        menampilkannya menggunakan Django Template Language, misalnya:

        ```html
        {% for experience in experience_list %}
            <h4>{{ experience.title }}</h4>
            <p>{{ experience.description }}</p>
        {% endfor %}
        ```
        Setelah template diproses oleh Django, hasil HTML dikirim kembali ke 
        browser dan ditampilkan sebagai halaman portofolio.

2. Mengapa data sebaiknya disimpan pada model?

    Data portofolio sebaiknya disimpan pada model dan database, bukan ditulis 
    langsung di template, karena lebih mudah untuk dipelihara dan dikembangkan.

    Jika data ditulis langsung:
    ```html
    <h4>Compfest 18</h4>
    <p>Direct Marketing Staff</p>
    ```
    setiap perubahan data mengharuskan kita mengubah kode HTML secara manual.

    Sedangkan jika data disimpan pada model, template cukup menggunakan:
    ```html
    <h4>{{ experience.title }}</h4>
    <p>{{ experience.description }}</p>
    ```

    Dengan cara tersebut, kita dapat menambah, mengubah, atau menghapus data pengalaman melalui 
    database tanpa perlu mengubah struktur template. Hal ini membuat aplikasi lebih fleksibel, 
    mudah dipelihara, dan mudah dikembangkan, terutama ketika jumlah data semakin banyak.

3. Perbedaan `makemigrations` dan `migrate`

- **`makemigrations`** digunakan untuk **membuat file migration** berdasarkan perubahan 
    pada model. Migration tersebut **berisi instruksi perubahan struktur database**.
- **`migrate`** digunakan untuk **menerapkan migration tersebut ke database**, sehingga 
    struktur database benar-benar berubah.

    Contohnya, awalnya model `Experience` hanya memiliki:
    ```python
    title = models.CharField(max_length=255)
    description = models.TextField()
    ```

    Kemudian kita ingin menambahkan field baru:
    ```python
    role = models.CharField(max_length=255, blank=True, default="")
    ```

    Maka jalankan:
    ```bash
    python manage.py makemigrations
    ```
    untuk membuat migration baru.

    Setelah itu:
    ```bash
    python manage.py migrate
    ```
    untuk menerapkan perubahan tersebut ke database.

---

### Penggunaan AI Tugas 2

Dalam tugas ini, saya menggunakan Claude untuk membantu memperbaiki kode yang masih memiliki 
kesalahan agar sesuai dengan instruksi pada tutorial, seperti pada bagian experience yang 
sebelumnya belum mengimplementasikan DTL (Django Template Language). AI juga membantu menyesuaikan 
kode agar tampilan pada setiap section tetap konsisten dan tidak berantakan, terutama pada bagian 
education, skills, dan contact. Selain itu, AI digunakan untuk membantu menganalisis error yang 
terjadi serta memberikan solusi untuk memperbaikinya.

**Lampiran Prompting:**
- **Section Education**: Bisakah buat agar struktur kode ini [kode lama statis] sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Experience**: Bisakah buat agar struktur kode ini [kode lama statis] sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Skills**: Bisakah buat agar struktur kode ini [kode lama statis] sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Contact**: Bisakah buat agar struktur kode ini [kode lama statis] sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].

**AI Disclosure & Analisis**
- **Tools yang Digunakan**: Claude
- **Analisis Keterbatasan AI**: Ketika mencoba membangun section baru dari awal 
    (*build from scratch*), AI memiliki keterbatasan dalam memahami estetika visual 
    dan presisi layout yang saya inginkan. Hasil kode yang diberikan terkadang tidak 
    sesuai dengan tampilan yang diharapkan, sehingga perlu dilakukan *trial and error* 
    secara berulang. Selain itu, ketika kode diubah menjadi lebih dinamis dengan 
    menerapkan DTL dan MVT, terdapat beberapa perubahan pada gaya tulisan di bagian 
    tertentu yang sebelumnya sudah sesuai.
- **Perbaikan Manual (oleh saya)**: Untuk mengatasi keterbatasan tersebut, saya menganalisis 
    kembali kode yang sudah ada, terutama bagian HTML dan CSS yang mengatur tampilan setiap 
    section. Saya kemudian mengidentifikasi kode yang menyebabkan perubahan pada gaya tulisan, 
    ukuran, atau layout, lalu memperbaikinya secara manual agar tetap sesuai dengan desain 
    sebelumnya.

---

### Tugas 3

1. Mengapa menggunakan `ModelForm` dan `{% csrf_token %}`?

    `ModelForm` digunakan karena dapat membuat form berdasarkan model Django secara otomatis. 
    Field pada form akan menyesuaikan dengan field yang terdapat pada model, sehingga tidak 
    perlu membuat setiap input HTML dan validasinya secara manual. `ModelForm` juga memudahkan 
    proses pengolahan dan penyimpanan data form ke database.

    Sementara itu, `{% csrf_token %}` digunakan untuk melindungi form dari serangan 
    **Cross-Site Request Forgery (CSRF)**. Token tersebut memastikan bahwa request POST berasal 
    dari form yang dibuat oleh aplikasi, sehingga dapat mencegah pengiriman request palsu oleh pihak lain.

2. Mengapa JSON lebih disukai dibandingkan XML?

    **JSON (JavaScript Object Notation)** lebih sering digunakan dalam pengembangan aplikasi web 
    modern karena memiliki struktur yang lebih sederhana dan ringan dibandingkan XML. JSON menggunakan 
    format key-value yang mudah dibaca oleh manusia maupun diproses oleh program.

    Contoh JSON:
    ```json
    {
        "title": "Portfolio Website",
        "tech_stack": "Django, Python"
    }
    ```

    Sedangkan XML menggunakan tag pembuka dan penutup:
    ```xml
    <project>
        <title>Portfolio Website</title>
        <tech_stack>Django, Python</tech_stack>
    </project>
    ```

    JSON juga lebih mudah digunakan dalam komunikasi antara frontend dan backend, terutama pada API. 
    Selain itu, JSON didukung oleh berbagai bahasa pemrograman dan umumnya memiliki ukuran data yang 
    lebih kecil dibandingkan XML.

3. Alur view mengembalikan data portofolio dalam bentuk JSON

    Alurnya adalah:
    **Request → View → Mengambil data dari Model → Serialization → JSON Response → Client**

    Contohnya:
    ```python
    def show_json(request):
        data = Project.objects.all()
        return HttpResponse(
            serializers.serialize("json", data),
            content_type="application/json"
        )
    ```

    Ketika URL diakses, Django menjalankan fungsi `show_json()`. View kemudian mengambil data project 
    dari database menggunakan `Project.objects.all()`.

    Data tersebut masih berupa **QuerySet/object Django**, sehingga perlu diubah terlebih dahulu ke 
    format yang dapat dikirim dan dibaca oleh client. Proses tersebut disebut **serialization**:

    ```python
    serializers.serialize("json", data)
    ```

    Serialization mengubah object atau data dari model Django menjadi format JSON. Setelah itu, JSON 
    dikembalikan melalui `HttpResponse` dengan `content_type="application/json"`, sehingga client 
    menerima data portofolio dalam format JSON.

---

### Penggunaan AI Tugas 3

Dalam tugas ini, saya menggunakan Claude untuk membantu menyesuaikan kode pada section Experience 
agar dapat menerima input secara langsung melalui website, dengan struktur yang serupa dengan section 
Projects dari tutorial. AI juga digunakan untuk membantu merapikan layout dan gaya tulisan pada fitur 
tambahan tersebut agar tetap sesuai dengan desain website yang sudah dibuat.

**Lampiran Prompting:**
- **Section Experience**: Berdasarkan kode pada section Projects, bisakah sesuaikan kode yang ada di 
    section Experience agar memiliki struktur yang sama dan dapat menerima input melalui website.   

**AI Disclosure & Analisis**
- **Tools yang Digunakan**: Claude
- **Analisis Keterbatasan AI**: Ketika kode diubah agar section Experience dapat menerima input langsung 
    melalui website, terdapat beberapa perubahan pada layout dan gaya tulisan di bagian tertentu yang 
    membuat tampilannya tidak lagi sepenuhnya sesuai dengan desain awal.
- **Perbaikan Manual (oleh saya)**: Untuk mengatasi perubahan tersebut, saya menganalisis kembali kode yang 
    telah dibuat, terutama bagian CSS yang mengatur tampilan setiap section. Saya mengidentifikasi bagian 
    kode yang memengaruhi ukuran, jarak, dan layout, kemudian melakukan penyesuaian secara manual agar tampilan 
    pada fitur tetap konsisten dengan desain keseluruhan website.

---

### Penggunaan AI Tugas 4

Dalam tugas ini, saya menggunakan Claude untuk membantu menganalisis dan memperbaiki kode yang mengalami 
kesalahan, khususnya pada section Projects setelah penambahan fitur login, register, dan logout. AI juga 
digunakan untuk membantu memastikan section Projects dapat disesuaikan dengan contoh pada Tutorial 4 dan 
berjalan dengan baik tanpa error.

**Lampiran Prompting:**
- **Section Projects**: Analisislah kesalahan yang terdapat pada kode berikut [kode terbaru setelah Tutorial 4] 
    dan perbaiki kesalahan tersebut agar dapat berjalan sebagaimana mestinya sesuai dengan tutorial.

**AI Disclosure & Analisis**
- **Tools yang Digunakan**: Claude
- **Analisis Keterbatasan AI**: Setelah penambahan fitur login, register, dan logout, terdapat beberapa bug 
    pada kode. Salah satunya adalah halaman **Add Experience** dan **Add Project** yang mengarah ke halaman 
    edit, bukan halaman untuk menambahkan data. Selain itu, akun superuser yang telah didaftarkan belum dapat 
    melakukan beberapa aksi seperti mengedit, menghapus, dan menambahkan data serta menggunakan fitur star.
- **Perbaikan Manual (oleh Saya)**: Untuk mengatasi masalah tersebut, saya menganalisis kembali penyebab akun 
    superuser tidak dapat melakukan beberapa aksi, seperti menambah, mengedit, dan menggunakan fitur star pada 
    section Projects. Kemudian, saya mencari dan menerapkan solusi yang sesuai agar kode dapat berjalan sebagaimana 
    mestinya sesuai dengan tutorial serta hak akses yang telah ditentukan untuk setiap role pengguna.

---

### Tugas 5

1. Jelaskan apa itu *debouncing* dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

    *Debouncing* adalah teknik yang digunakan untuk memberi jeda sebelum sebuah fungsi dijalankan. Pada fitur 
    pencarian, fungsi tidak langsung dijalankan setiap kali pengguna mengetik, tetapi menunggu sampai pengguna 
    berhenti mengetik selama waktu tertentu. Contoh penerapannya pada `experience.html`:

    ````javascript
    const EXP_SEARCH_DEBOUNCE_DELAY = 300;
    let experienceSearchDebounceTimer;

    experienceSearchInput.addEventListener("input", function() {
        clearTimeout(experienceSearchDebounceTimer);
        experienceSearchDebounceTimer = setTimeout(function() {
            searchExperiences();
        }, EXP_SEARCH_DEBOUNCE_DELAY);
    });
    ````

    Misalnya, pengguna ingin mencari data dengan kata `experience`. Tanpa *debouncing*, setiap karakter yang 
    diketik dapat menyebabkan request baru ke server:

    ```text
    e → request
    ex → request
    exp → request
    expe → request
    exper → request
    ...
    experience → request
    ```

    Artinya, satu proses pencarian bisa menghasilkan banyak request. Jika fitur ini digunakan oleh banyak 
    pengguna, jumlah request yang masuk ke server juga akan semakin banyak.

    Dengan *debouncing*, sistem akan menunggu pengguna berhenti mengetik selama 300 ms. Jika selama 300 ms 
    tidak ada input baru, barulah request AJAX dikirim.

    Contohnya menjadi seperti berikut:

    ```text
    e
    ex
    exp
    expe
    exper
    experience → berhenti mengetik → request
    ```

    Penerapan *debouncing* pada pencarian AJAX penting karena dapat:
    * Mengurangi jumlah request ke server.
    * Mengurangi beban server dan database.
    * Menghindari request yang sebenarnya tidak diperlukan.
    * Membuat proses pencarian menjadi lebih efisien dan responsif.

    Jadi, *debouncing* digunakan agar request pencarian tidak dikirim terus-menerus setiap kali terjadi 
    perubahan input, tetapi hanya setelah pengguna selesai atau berhenti mengetik dalam waktu tertentu.

2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika 
    kita tidak menggunakan `await`?

    `fetch()` digunakan untuk melakukan request ke server, misalnya untuk mengambil data experience dari 
    endpoint JSON. Karena request tersebut membutuhkan waktu untuk mendapatkan response dari server, 
    prosesnya berjalan secara asynchronous.

    Hasil dari `fetch()` adalah sebuah **Promise**, yaitu objek yang mewakili proses yang masih berlangsung 
    atau akan selesai nantinya.

    `await` digunakan untuk menunggu Promise tersebut selesai sebelum kode dilanjutkan ke proses berikutnya.

    Contohnya:

    ```javascript
    const response = await fetch('/api/experience/');
    const data = await response.json();
    ```

    Pada baris pertama, `await` membuat program menunggu sampai request `fetch()` mendapatkan response dari server.

    Kemudian pada baris kedua, `await` digunakan lagi karena `response.json()` juga merupakan proses asynchronous. 
    Program akan menunggu sampai response selesai diubah menjadi data JSON sebelum data tersebut digunakan.

    Alurnya:

    ```text
    fetch()
    ↓
    menunggu response dari server
    ↓
    response.json()
    ↓
    menunggu proses JSON selesai
    ↓
    data siap digunakan
    ```

    Jika tidak menggunakan `await`, hasil dari `fetch()` masih berupa Promise. Misalnya:

    ```javascript
    const response = fetch('/api/experience/');
    console.log(response);
    ```

    Variabel `response` pada kondisi tersebut bukan langsung berisi response dari server, tetapi masih 
    berupa Promise. Jika Promise tidak ditunggu atau ditangani dengan benar, data belum dapat digunakan 
    sebagai hasil JSON yang sebenarnya. Akibatnya, jika kode langsung mencoba menggunakan data tersebut, 
    proses dapat menghasilkan error atau data belum tersedia karena request masih berlangsung.

    `await` biasanya digunakan di dalam fungsi yang diberi `async`, contohnya:

    ```javascript
    async function loadExperience() {
        const response = await fetch('/api/experience/');
        const data = await response.json();

        console.log(data);
    }
    ```

    Jadi, penggunaan `await` pada `fetch()` bertujuan untuk memastikan response dari server sudah diterima 
    dan datanya sudah siap sebelum digunakan oleh kode berikutnya. Tanpa `await`, Promise perlu ditangani 
    dengan cara lain, misalnya menggunakan `.then()`.

3. Jelaskan apa itu serangan XSS (*Cross-Site Scripting*) dan mengapa data yang ditampilkan melalui AJAX/JavaScript 
    lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui *template* Django!

    XSS (*Cross-Site Scripting*) adalah serangan yang terjadi ketika seseorang berhasil memasukkan kode 
    atau script berbahaya ke dalam sebuah aplikasi web, kemudian kode tersebut ikut dijalankan di browser 
    ketika data ditampilkan.

    Contohnya:

    ```html
    <script>alert('XSS')</script>
    ```

    Jika aplikasi tidak menangani data tersebut dengan benar dan langsung memasukkannya ke halaman sebagai 
    HTML, browser dapat menganggapnya sebagai script dan menjalankannya.

    Pada penggunaan AJAX, data dari server biasanya diterima dalam bentuk JSON. Setelah itu, JavaScript 
    bertugas mengambil data tersebut dan memasukkannya ke halaman. 
    
    Contohnya:

    ```javascript
    element.innerHTML = data.description;
    ```

    Masalahnya, `innerHTML` akan membaca isi yang diberikan sebagai HTML. Jadi, apabila `data.description` 
    mengandung tag HTML atau script yang berbahaya dan tidak melalui proses escaping atau sanitasi, kode 
    tersebut dapat diproses oleh browser.

    Untuk data yang hanya berupa teks, salah satu cara yang lebih aman adalah menggunakan `textContent`:

    ```javascript
    element.textContent = data.description;
    ```

    Dengan `textContent`, isi data dianggap sebagai teks biasa sehingga tag HTML di dalamnya tidak langsung 
    diproses sebagai elemen HTML. Sementara itu, ketika data ditampilkan menggunakan template Django, Django 
    secara default sudah melakukan **automatic HTML escaping**.

    Contohnya:

    ```django
    <p>{{ experience.description }}</p>
    ```

    Jika isi `experience.description` mengandung:

    ```html
    <script>alert('XSS')</script>
    ```

    Django akan melakukan escaping sehingga isi tersebut ditampilkan sebagai teks dan tidak langsung 
    dijalankan sebagai script oleh browser. Perbedaannya dapat digambarkan seperti berikut:

    ```text
    Template Django:
    Data → Template Django → Automatic escaping → Ditampilkan sebagai teks

    AJAX:
    Data → JSON → JavaScript → Masuk ke DOM → Harus dipastikan aman
    ```

    Jadi, **AJAX sendiri tidak otomatis lebih rentan terhadap XSS**. Risikonya bergantung pada cara data 
    dimasukkan ke halaman. Karena itu, selain escaping di sisi tampilan, input juga dapat dibersihkan di 
    server, misalnya menggunakan strip_tags() pada ModelForm.

---

### Penggunaan AI Tugas 5

Dalam tugas ini, saya menggunakan Claude untuk membantu menyesuaikan kode pada section **Experience** 
agar memiliki alur kode yang sama seperti section **Projects** setelah perubahan pada Tutorial 5.

**Lampiran Prompting:**
- **Section Experience**: Bisakah membuat section Experience agar mengimplementasikan kode yang sama 
    seperti section Projects setelah perubahan pada Tutorial 5?

**AI Disclosure & Analisis**
- **Tools yang Digunakan**: Claude
 **Analisis Keterbatasan AI**: Saat mengimplementasikan perubahan pada beberapa section, terdapat perubahan 
    pada tampilan dan hak akses pengguna. Salah satunya adalah akun superuser tidak dapat melihat tombol 
    untuk mengedit dan menghapus data pada section Experience.
- **Perbaikan Manual (oleh Saya)**: Untuk mengatasi masalah tersebut, saya menganalisis penyebab tombol 
    edit dan delete tidak muncul meskipun akun yang digunakan adalah superuser. Setelah menemukan penyebabnya, 
    saya menyesuaikan kembali kode agar tombol edit dan delete dapat ditampilkan untuk akun superuser pada 
    section Experience.

---

### Tugas 6

1. REST, JSON, PUT, dan PATCH

    **REST (Representational State Transfer)** adalah gaya arsitektur perangkat lunak yang mengatur bagaimana 
    client dan server berkomunikasi serta bertukar data melalui jaringan menggunakan antarmuka yang seragam 
    (*uniform interface*).

    REST memiliki beberapa prinsip, yaitu:
    - **Client-Server:** Memisahkan client dan server.
    - **Stateless:** Setiap request harus membawa informasi yang dibutuhkan untuk diproses.
    - **Cacheable:** Respons dapat disimpan dalam cache jika diizinkan.
    - **Uniform Interface:** Komunikasi menggunakan aturan yang konsisten.
    - **Layered System:** Komunikasi dapat melewati perantara seperti proxy.

    Mengembalikan JSON saja belum cukup untuk menyebut suatu API sebagai RESTful karena JSON hanyalah 
    format pertukaran data, bukan aturan arsitektur REST. Sebuah API juga harus menerapkan prinsip-prinsip 
    REST, seperti penggunaan HTTP method yang sesuai, pemisahan client-server, dan komunikasi yang stateless.

    Contohnya, endpoint `/get_projects_json/` mengembalikan JSON, tetapi URL-nya berupa aksi, bukan resource, 
    dan tidak memakai status HTTP yang bermakna. Versi RESTful-nya adalah `GET /api/v1/experience/` untuk daftar, 
    `POST` dengan status `201` untuk membuat, `DELETE /api/v1/experience/<id>/` dengan status `204` untuk menghapus, 
    serta `400`, `403`, dan `404` untuk kondisi gagal.

    **Perbedaan PUT dan PATCH**

    | PUT | PATCH |
    | ------------------------------- | ------------------------------- |
    | Mengganti seluruh representasi data resource. | Mengubah sebagian data resource. |
    | Client mengirimkan data lengkap. | Client cukup mengirimkan field yang ingin diubah. |
    | Digunakan jika ingin mengganti seluruh data. | Digunakan jika hanya ingin memperbarui atribut tertentu. |

    **Contoh pada proyek ini:**

    Misalnya terdapat data Experience:

    ```json
    {
    "title": "Web Developer",
    "role": "Frontend Developer",
    "description": "Mengembangkan tampilan website",
    "category": "internship",
    "ended_at": null
    }
    ```

    **PUT:** Jika Editor ingin mengganti keseluruhan data Experience, client mengirimkan seluruh data:

    ```json
    {
    "title": "Fullstack Developer",
    "role": "Web Developer",
    "description": "Mengembangkan aplikasi web",
    "category": "internship",
    "ended_at": "2026-05"
    }
    ```

    **PATCH:** Jika Editor hanya ingin mengubah tanggal berakhir Experience, client cukup mengirimkan:

    ```json
    {
    "ended_at": "2026-05"
    }
    ```

2. Peran Serializer pada Django REST Framework

    **Serializer** adalah komponen pada Django REST Framework yang berfungsi untuk mengubah objek Django, 
    seperti Model Instance dan QuerySet, menjadi tipe data Python standar yang kemudian dapat diubah menjadi 
    JSON (*serialization*).

    Serializer juga melakukan proses sebaliknya, yaitu menerima data JSON, memvalidasi data, dan mengubahnya 
    menjadi data Python atau Django Model Instance (*deserialization*).

    Pada proyek ini, `ExperienceSerializer` menentukan field mana yang ditampilkan, memvalidasi input melalui 
    `validate_title` dengan `strip_tags`, dan menghitung field tambahan seperti `star_count`, `is_starred`, dan 
    `starred_by_names`.

    **Keuntungan Serializer dibandingkan JsonResponse manual**

    1. **Konversi data otomatis:** Tidak perlu mengambil dan menyusun setiap field model secara manual menjadi dictionary.
    2. **Validasi data:** Serializer menyediakan `.is_valid()` untuk memeriksa apakah data yang dikirim client sesuai 
        dengan aturan yang ditentukan. Jika tidak valid, Serializer dapat menghasilkan pesan error untuk setiap field.
    3. **Integrasi dengan model:** `ModelSerializer` dapat mengambil field dan aturan validasi langsung dari Django Model.
    4. **Mendukung operasi CRUD:** `ModelSerializer` menyediakan implementasi `create()` dan `update()` sehingga mengurangi 
        kode yang harus ditulis.
    5. **Mengurangi kesalahan:** Validasi dan proses konversi data dilakukan secara terstruktur dan konsisten.
    6. **Field read-only:** `SerializerMethodField` digunakan untuk menghitung field tambahan seperti `star_count` dan 
        `is_starred`, sehingga nilainya tidak dapat diisi secara langsung oleh client.

    **Contoh penggunaan pada proyek ini:**

    ```python
    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)  # tidak valid -> otomatis 400
    serializer.save()
    ```

    Dengan demikian, Serializer lebih efisien dan terstruktur dibandingkan harus membuat dictionary secara 
    manual dan mengelola validasi sendiri menggunakan `JsonResponse`.

3. Perbedaan Authentication dan Authorization pada Django REST Framework

    **Authentication (autentikasi)** adalah proses memverifikasi identitas pengguna yang mengirimkan request. 
    Tujuannya untuk mengetahui siapa pengguna tersebut. Pada proyek ini, autentikasi menggunakan `SessionAuthentication`, 
    yang membaca cookie sesi dan mengidentifikasi pengguna melalui `request.user`.

    **Authorization (otorisasi)** adalah proses menentukan apakah pengguna yang sudah teridentifikasi memiliki 
    hak untuk mengakses atau melakukan tindakan tertentu terhadap suatu resource. Pada proyek ini, otorisasi 
    dilakukan menggunakan permission class `IsPortfolioOwnerOrEditorOrReadOnly`, yang mengatur hak akses 
    berdasarkan peran dan kepemilikan data.

    Contohnya:
    - Pengunjung hanya dapat membaca data.
    - Pengguna biasa dapat memberikan star.
    - Pemilik portofolio (superuser) boleh melakukan semua tindakan: `POST`, `PUT`, `PATCH`, dan `DELETE`.
    - Editor hanya boleh `PUT` dan `PATCH`; `POST` dan `DELETE` ditolak dengan `403`.

    **Perbedaan Authentication dan Authorization**

    | Authentication | Authorization |
    | ------------------------------- | ------------------------------- |
    | Memeriksa identitas pengguna. | Memeriksa hak akses pengguna. |
    | Menjawab: Siapa kamu? | Menjawab: Apa yang boleh kamu lakukan? |
    | Contoh: SessionAuthentication. | Contoh: IsPortfolioOwnerOrEditorOrReadOnly. |

    **Mengapa Permission Harus Diperiksa di Server?**

    Hak akses harus diperiksa menggunakan *permission class* di server karena menyembunyikan tombol pada 
    template hanya membatasi tampilan antarmuka, bukan akses sebenarnya terhadap API. Pengguna masih dapat 
    mengirim request secara langsung menggunakan browser developer tools, `curl`, atau Postman tanpa melalui 
    tombol yang disediakan. Oleh karena itu, server harus tetap memeriksa permission setiap kali menerima 
    request agar pengguna yang tidak memiliki hak akses tidak dapat melakukan tindakan yang dilarang.

4. CSRF pada SessionAuthentication dan force_authenticate

    **CSRF (Cross-Site Request Forgery)** adalah serangan yang memanfaatkan browser pengguna yang sudah login 
    untuk mengirimkan request ke suatu website tanpa sepengetahuan atau persetujuan pengguna.

    Ketika API menggunakan `SessionAuthentication`, browser secara otomatis mengirimkan session cookie pada 
    request. Hal ini menimbulkan risiko CSRF karena website lain dapat mencoba memanfaatkan session pengguna 
    yang masih aktif. Oleh karena itu, request yang mengubah data seperti POST, PUT, PATCH, dan DELETE tetap 
    harus menyertakan CSRF Token agar server dapat memverifikasi bahwa request berasal dari sumber yang sah.

    Pada Django REST Framework, client biasanya mengambil cookie `csrftoken`, kemudian mengirimkan nilainya 
    melalui HTTP header:

    ```http
    X-CSRFToken: <csrf_token>
    ```

    **Mengapa force_authenticate Tidak Cukup?**

    `force_authenticate` merupakan fitur pada pengujian DRF yang secara langsung memaksa request dianggap 
    sudah terautentikasi sebagai pengguna tertentu. Dengan demikian, pengujian tersebut melewati proses 
    autentikasi normal melalui `SessionAuthentication`, termasuk mekanisme pemeriksaan CSRF yang berkaitan 
    dengan proses tersebut. Akibatnya, test yang menggunakan `force_authenticate` hanya membuktikan bahwa 
    pengguna dapat mengakses endpoint setelah dianggap terautentikasi, tetapi tidak membuktikan bahwa 
    perlindungan CSRF berjalan dengan benar.

    Untuk menguji perlindungan CSRF, gunakan pengujian dengan `APIClient` yang mengaktifkan pemeriksaan CSRF 
    (`enforce_csrf_checks=True`), kemudian lakukan login menggunakan `.login()` agar pengujian menggunakan 
    session yang sebenarnya.

    **Pengujian pada proyek ini:**

    Test client DRF secara default tidak melakukan pemeriksaan CSRF (`enforce_csrf_checks=False`). Selain itu, 
    `force_authenticate` melewati proses autentikasi menggunakan `SessionAuthentication`. Oleh karena itu, 
    pengujian berikut menggunakan `APIClient(enforce_csrf_checks=True)` untuk mengaktifkan pemeriksaan CSRF 
    dan `.login()` untuk melakukan login menggunakan session seperti pada kondisi sebenarnya:

    - `test_session_write_without_csrf_is_rejected`: request tanpa CSRF Token ditolak dengan respons `403`, 
        dan database tidak berubah.
    - `test_session_write_with_csrf_succeeds`: request dengan CSRF Token yang valid diterima, dengan catatan 
        autentikasi dan permission juga terpenuhi.

---

### Penggunaan AI Tugas 6

Dalam tugas ini, saya menggunakan Claude untuk membantu mengimplementasikan Django REST Framework pada 
Tugas 6 (section **Experience**), di antaranya serializer, permission class, API view, integrasi halaman 
dengan `fetch()`, fitur star, edit lewat `PATCH`, serta test `APITestCase`.

**Lampiran Prompting:**
- **Section Experience**: Bisakah section Experience disesuaikan agar menerapkan perubahan yang sama seperti 
    section Projects setelah pembaruan pada Tutorial 7?

**AI Disclosure & Analisis**
- **Tools yang Digunakan**: Claude
- **Analisis Keterbatasan AI**: Saat mengimplementasikan perubahan pada section Experience, terdapat perubahan
    pada gaya halaman, contohnya tombol star. Kode yang diberikan terkadang tidak sesuai dengan gaya pada tombol
    lain sehingga diperlukan penyesuaian agar gaya halaman tetap konsisten.
- **Perbaikan Manual (oleh Saya)**: Untuk mengatasi masalah tersebut, saya mencari aturan CSS yang mengatur gaya
    tombol tersebut dan menyesuaikannya agar konsisten dengan elemen lain yang terdapat pada halaman tersebut.

---