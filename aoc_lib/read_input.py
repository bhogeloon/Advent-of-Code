def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename,encoding='utf-8') as f:
        data = f.read()

    return data.splitlines()

if __name__ == '__main__':
    pass