
d = {
    ".py": "py_files",
    ".c": "c_files",
}

a = "test.c"

for i in d:
    if a.endswith(i):
        print(d[i])
