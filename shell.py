#!/usr/bin/python3
import os
import aplusplus

while True:
    text = input("A++ > ")
    if text.strip() == "cwear":
        os.system('clear' if os.name == 'posix' else 'cls')
        continue
    if text.strip() == "":
        continue
    result, error = aplusplus.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
