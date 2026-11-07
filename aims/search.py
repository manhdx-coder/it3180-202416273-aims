def search_by_title(cart, title):
    """Search DVDs by title without case sensitivity."""
    result = []

    for dvd in cart.items:
        if title.lower() in dvd.title.lower():
            result.append(dvd)

    return result