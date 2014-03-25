def sesion_no_iniciada(user):
    return not user.is_authenticated()