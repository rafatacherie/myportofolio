from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    """
    Dipakai oleh Projects (contoh inti tutorial): semua orang boleh membaca
    (GET/HEAD/OPTIONS), tapi hanya pemilik portofolio (is_superuser) yang
    boleh menambah/mengubah/menghapus.
    """
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """
    Dipakai oleh Experience (bagian pilihan tugas): semua orang boleh membaca.
    Role Editor (Django Group "Editor", dari Tugas 4) boleh PUT/PATCH seperti
    sebelumnya, tapi hanya pemilik portofolio yang boleh POST (create) dan DELETE.
    """
    message = "Only the portfolio owner or an Editor can change this experience."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )