def class_set(name, title, movements=None):
    '''Display the info of a set by a composer'''
    if movements:
        class_set = {'Name': name.title(),
            'Musical Set' : title.title(),
            'Movements' : movements}
    else:
        class_set = {'Name': name.title(),
            'Musical Set' : title.title()}
    return class_set