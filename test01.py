import os

# print(os.environ)

for k, v in os.environ.items():
    if os.path.isdir(v):
        print("name:", k)
        print(v)

