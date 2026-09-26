def role_flags(request):
    user = request.user
    is_editor = user.is_authenticated and user.groups.filter(name='Editor').exists()
    return {'is_editor': is_editor}