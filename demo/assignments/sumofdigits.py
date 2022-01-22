def getnumber(s: str) -> int:
    st = ""
    for c in s:
        if c.isdigit():
            st += c

    return int(st)


data = ["a124y4", "456", "abc34", "32ab44"]

print(sum(map(getnumber, data)))
