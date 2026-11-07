def search_by_category(cart, category):
    result = []

    for dvd in cart.items:
        if category.lower() in dvd.category.lower():
            result.append(dvd)

    return result


def search_by_title(cart, title):
    result = []

    for dvd in cart.items:
        if title.lower() in dvd.title.lower():
            result.append(dvd)

    return result