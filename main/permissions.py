from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    """
    Dipakai oleh Projects: semua orang boleh membaca (GET/HEAD/OPTIONS), tapi 
    hanya pemilik portofolio (is_superuser) yang boleh menambah/mengubah/menghapus.
    """
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD, OPTIONS (hanya membaca, aman untuk semua orang)
        # Pengunjung anonim punya is_superuser=False, jadi otomatis ditolak (403)
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """
    Dipakai oleh Experience: semua orang boleh membaca. Role Editor (Django Group "Editor") boleh 
    PUT/PATCH seperti sebelumnya, tapi hanya pemilik portofolio yang boleh POST (create) dan DELETE.
    """
    message = "Only the portfolio owner or an Editor can change this experience."

    def has_permission(self, request, view):
        # 1) Membaca: terbuka untuk semua orang
        if request.method in SAFE_METHODS:
            return True
        # 2) Menulis tanpa login: ditolak
        if not request.user.is_authenticated:
            return False
        # 3) Pemilik portofolio: boleh semua metode
        if request.user.is_superuser:
            return True
        # 4) Editor: hanya PUT/PATCH; POST (create) dan DELETE ditolak.
        #    Pengguna biasa tanpa group Editor juga ditolak di sini.
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )