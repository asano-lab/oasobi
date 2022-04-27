import os

ENV_VAR = os.getenv("PATH").split(";")
# print(ENV_VAR)

for i in ENV_VAR:
    if os.path.isdir(i):
        print(i)
