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

### Penggunaan AI

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


    - **View** memproses request dan mengambil data yang diperlukan dari model. 
        Contohnya:
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

### Penggunaan AI
Dalam tugas ini, saya menggunakan Claude untuk membantu memperbaiki kode yang masih memiliki 
kesalahan agar sesuai dengan instruksi pada tutorial, seperti pada bagian experience yang 
sebelumnya belum mengimplementasikan DTL (Django Template Language). AI juga membantu menyesuaikan 
kode agar tampilan pada setiap section tetap konsisten dan tidak berantakan, terutama pada bagian 
education, skills, dan contact. Selain itu, AI digunakan untuk membantu menganalisis error yang 
terjadi serta memberikan solusi untuk memperbaikinya.

**Lampiran Prompting:**
- **Section Education**: Bisakah buat agar struktur kode ini [kode lama statis] agar sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Experience**: Bisakah buat agar struktur kode ini [kode lama statis] agar sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Skills**: Bisakah buat agar struktur kode ini [kode lama statis] agar sesuai 
    seperti yang ada pada kode di tutorial ini [kode baru dinamis].
- **Section Contact**: Bisakah buat agar struktur kode ini [kode lama statis] agar sesuai 
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