def outside():
    m="out"
    def inside():
        global m
        m="in"
        print(m)
    inside()
    print(m)

m="start"
outside()
print(m)
