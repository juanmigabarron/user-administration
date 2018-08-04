def add_superpowers(backend, user, response, *args, **kwargs):
    ''' Converts user into superuser '''
    if user and not user.is_superuser:
        user.is_superuser = True
        user.save()
