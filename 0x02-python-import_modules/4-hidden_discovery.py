#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    files = dir(hidden_4)
    for names in files:
        if names[:2] != "__":
            print(names)
