Nama  : Rafata Zahi Cherie

NPM   : 2506621592

Kelas : PBP C

### Tugas 1

1. Ya, dalam merancang struktur KTML, saya memanfaatkan elemen semantik HTML5 hampir 
    di setiap bagian, terutama tag `<section>` untuk membagi setiap bagian utama 
    portofolio, seperti ``#home, #education, #experience, #skills, #skills, dan #contact``, 
    serta tag `<footer>` untuk bagian penutup paling bawah halaman.
    
    Alasan: `<section>` dipilih karena tiap bagian (Home, Education, Experience, Skills, 
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

    Contoh kasus: pada bagian experience, terdapat flip box yang sejajar secara horizontal 
    dan pada bagian skills juga, jenis skills dibagi menjadi 2 kolom. Sehingga saat layar 
    mengecil akan rawan terhimpit dan teks nya menjadi keluar batas jika dipaksakan dalam 
    bentuk aslinya. 

    Cara mengevaluasi dan menetukan prioritas ukuran/posisi elemen: 
    - Content flow: mengevaluasi halaman pada berbagai breakpoint (seperti 1285px, 991px, 
    dan 895px). Jika elemen horizontal mulai terhimpit, akan diprioritaskan tata letak 
    dengan satu kolom sehingga memanjang ke bawah (vertikal).
    - Visual: saat berpindah ke tampilan mobile, elemen visual yang besar (seperti foto profil) 
    diprioritaskan posisinya agar berada di atas teks perkenalan untuk menyesuaikan alur.
    - Skalabilitas font: menurunkan ukuran font dasar `(html { font-size: 55%; })` pada breakpoint 
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

Lampiran Prompting:
- Section Experience (flip box): Berdasarkan kode ini [kode dari tutorial], bisakah buat agar terdapat 
    button "see detail" lalu menampilkan deskripsi dari pengalaman yang dilakukan. Buat agar tulisannya 
    tidak keluar dari box, dan dapat di scroll jika teksnya panjang. Kembalikan lagi ke halaman depan 
    dari box dengan button "back".
- Section Skills (skills bar): Berdasarkan kode ini [kode dari tutorial], bisakah buat untuk 2 jenis skills 
    (technical and soft skills) dengan tampilan sejajar horizontal dan untuk tiap skills berikan 5 bar serta
    berikan garis pemisah antara 2 jenis skills tersebut.
- Section Contact (button "send me a message"): Berdasarkan kode ini [kode dari tutorial] sesuaikan agar 
    button dapat mendirect ke email untuk mengirimkan pesan.
- Section Footer (logo, navbar, dan copyright): Berdasarkan kode ini [kode dari tutorial] sesuaikan agar 
    layout footer berbaris berurutan dari atas ke bawah (vertikal) dan rata tengah.

AI Disclosure & Analisis:
- Tools yang Digunakan: Claude
- Analisis Keterbatasan AI: Ketika mencoba membangun komponen dari awal (build from scratch), AI memiliki 
    keterbatasan dalam memahami estetika visual dan presisi layout yang saya inginkan. Hasil kode pertama 
    dari AI sering kali tidak sesuai ekspektasi, sehingga memicu proses trial and error yang berulang-ulang 
    dan memakan banyak waktu jika hanya mengandalkan teks.
- Perbaikan Manual (oleh saya): Untuk mengatasi keterbatasan AI, saya beralih mencari referensi yang cocok 
    secara visual dari tutorial YouTube. Untuk beberapa section yang ingin saya rombak, saya perlu setidaknya 
    setengah gambaran kode yang sesuai secara visual, baru saya memberikan potongan kode tersebut ke AI dan 
    menyesuaikannya secara desain. Saya tidak menyuruh AI mendesain dari nol, melainkan memberikan instruksi 
    spesifik untuk memodifikasi, menambah fitur baru (seperti tombol back dan scroll pada flip box), serta 
    menyelaraskan layout agar sesuai dengan desain yang saya inginkan.