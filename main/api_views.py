"""
API views (Django REST Framework) untuk Projects dan Experience.

Dipisah dari main/views.py supaya fungsi untuk halaman HTML (show_projects,
show_experience, dst.) dan fungsi untuk API (yang dipakai AJAX) mudah
dibedakan. Fungsi di main/views.py yang masih merender HTML TIDAK dihapus
atau diganti oleh berkas ini.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Project
from main.permissions import (
    IsPortfolioOwnerOrEditorOrReadOnly,
    IsPortfolioOwnerOrReadOnly,
)
from main.serializers import ExperienceSerializer, ProjectSerializer


# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_list(request):
    """GET: daftar project (opsional ?title=). POST: buat project (hanya pemilik)."""
    if request.method in ("GET", "HEAD"):
        # prefetch_related mencegah query tambahan per project saat serializer
        # menghitung star_count / starred_by_names
        projects = Project.objects.prefetch_related("starred_by").order_by("title", "id")
        # Pencarian kini berupa parameter query, mis. /projects/?title=web
        title = request.query_params.get("title", "").strip()
        if title:
            projects = projects.filter(title__icontains=title)
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request},
        )
        return Response(serializer.data)

    # POST: input tidak valid -> DRF otomatis membalas 400 lewat raise_exception
    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request, project_id):
    """GET: satu project. PUT/PATCH: ubah. DELETE: hapus (204). ID tak ada -> 404."""
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    # DELETE: berhasil -> 204 tanpa isi
    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # PUT mengganti seluruh data (semua field wajib), PATCH hanya field yang dikirim
    serializer = ProjectSerializer(
        project, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    # Akun pemberi star selalu request.user, bukan dari input klien
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)


# ---------------------------------------------------------------------------
# Experience
# ---------------------------------------------------------------------------

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request):
    """GET: daftar experience (opsional ?title=). POST: buat experience (hanya pemilik)."""
    if request.method in ("GET", "HEAD"):
        # prefetch_related menghindari query berulang untuk info star
        experiences = Experience.objects.prefetch_related("starred_by").order_by("-started_at", "title")
        # Pencarian kini berupa parameter query, mis. /experience/?title=compfest
        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)
        serializer = ExperienceSerializer(
            experiences, many=True, context={"request": request},
        )
        return Response(serializer.data)

    # Hanya pemilik portofolio yang lolos permission untuk POST (Editor
    # hanya diizinkan PUT/PATCH, lihat IsPortfolioOwnerOrEditorOrReadOnly).
    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id):
    """GET: satu experience. PUT/PATCH: ubah (pemilik/Editor). DELETE: hapus (pemilik)."""
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"), pk=experience_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = ExperienceSerializer(experience, context={"request": request})
        return Response(serializer.data)

    # DELETE: berhasil -> 204 tanpa isi (Editor ditolak 403 oleh permission)
    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # PUT mengganti seluruh data (semua field wajib), PATCH hanya field yang dikirim
    serializer = ExperienceSerializer(
        experience, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id):
    # Akun pemberi star selalu request.user, bukan dari input klien
    experience = get_object_or_404(Experience, pk=experience_id)
    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)
    serializer = ExperienceSerializer(experience, context={"request": request})
    return Response(serializer.data)