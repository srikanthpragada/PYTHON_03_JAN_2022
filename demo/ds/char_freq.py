# Char Frequency

st = "This is to test a string"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")
