def add_python(Z1,Z2):
    for i in Z1:
        if isinstance(i, list):
            add_python(i, Z2)
        else:
            print(i)