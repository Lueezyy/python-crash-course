def print_models(incomplete, complete):
    while incomplete:
        current = incomplete.pop()
        print(f'Printing {current} model...')
        complete.append(current)

def show_completed(complete):
    print('The following models have been printed:')
    for each in complete:
        print(each.title())