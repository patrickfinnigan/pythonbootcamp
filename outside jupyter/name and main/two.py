import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print("TWO.PY IS RUNNING DIRECTLY")
else:
    print("two.py has been imported")