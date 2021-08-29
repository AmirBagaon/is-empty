def is_empty(expression):
    is_empty_boolean = True
    if not expression:
        print('This thing has been mathematically proven to be 100% empty')
    elif expression:
        print('ERROR ERROR ERROR!!! IS NOT EMPTY! DOES NOT COMPUTE!')
        is_empty_boolean = False
    else:
        print('If you got here, you\'re a hacker.')
        raise ValueError('impossible value, get a life.')
    return is_empty_boolean

if __name__ == '__main__':
    pass