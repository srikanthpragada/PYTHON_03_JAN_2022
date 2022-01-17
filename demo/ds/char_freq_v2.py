# Char Frequency using dict

st = "This is to test a string"

freq = {}
for c in set(st):
    freq[c] = st.count(c)

print(freq)

freq2 = {c: st.count(c) for c in set(st)}

print(freq2)
