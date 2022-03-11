
def append(data):
    f = open("nofile.data", "a")
    f.write(data)
    f.close()

def getList() -> list:
    f = open("nofile.data", "r")
    return f.read().split(";")        