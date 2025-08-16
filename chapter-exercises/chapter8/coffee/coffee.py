def make_coffee(size, type, *custom):
    if not custom:
        print(f'\nMaking a {size.upper()}-size {type}.')
    else:
        print(f'\nMaking a {size.upper()} {type} with the following:')
        for request in custom:
            print(f'- {request}')