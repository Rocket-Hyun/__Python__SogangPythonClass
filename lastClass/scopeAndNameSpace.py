def outside():
    m="out"
    def inside():
        #한 단계 위만 건드린다.
        nonlocal m
        m="in"
        print(m)
    inside()
    print(m)

m="start"
outside()
print(m)
