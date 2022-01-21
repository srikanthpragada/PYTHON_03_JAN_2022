# Map demo
def extract_upper(s: str) -> str:
    st = ""
    for c in s:
        if c.isupper():
            st += c

    return st


nums = ["10", "345", "23"]
for n in map(int, nums):
    print(n)

print(sum(map(int, nums)))

values = ["Abc", "BBC", "UxyDef"]
for s in map(extract_upper, values):
    print(s)
