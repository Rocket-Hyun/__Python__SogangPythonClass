def outside():
    m="out"
    def inside():
        m="in"
        print(m)
    inside()
    print(m)

m="start"
outside()
print(m)
