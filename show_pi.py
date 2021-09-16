#!/usr/bin/env python3

def approximate_pi():
    return 355 / 113

def show_pi():
<<<<<<< HEAD
    print("π is {:.5f}".format(approximate_pi()))
=======
    print("pi is approximately {:.8f}".format(approximate_pi()))
>>>>>>> d6498480cddcf53c0750a1e4eca7ee492f35d6ff

if __name__ == "__main__":
    show_pi()
