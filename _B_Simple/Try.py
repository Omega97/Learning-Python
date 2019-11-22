"""
                                Try ... except ... else ... finally

try: try to run the following block
except: if something goes wrong in the try block, run the following block
else: if nothing goes wrong in the try block, run the following block
finally: will be executed no matter if the try block raises an error or not
"""


def check(x):
    try:
        1/x
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except TypeError:
        print("TypeError 1 /", str(x))
    else:
        print(1/x)
        print("Nothing went wrong :)")
    finally:
        print("---\n")


if __name__ == '__main__':

    check(1)
    check(0)
    check('a')
