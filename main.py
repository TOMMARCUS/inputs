import os

name = os.environ.get('NAME')
if not name:
    print("No name provided")
else:
    print(f"Hello, {name}!")
