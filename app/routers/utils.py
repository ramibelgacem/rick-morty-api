def build_filters(model, attributes):
    filters = []
    for attribute in attributes:
        if attributes[attribute]:
            if attribute in ['name']:
                filters.append(
                    getattr(model, attribute).ilike(
                        f"%{attributes[attribute]}%")
                )
            else:
                filters.append(
                    getattr(model, attribute) == attributes[attribute]
                )
    return filters
