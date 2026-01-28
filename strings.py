ab = "ab0123456789abcdefghijklmnopqrstuvwxyz"
#slicing
# print(ab[1:10])
# print(ab[:5])
# print(ab[1:])
# print(ab[-10:-2])

##skip value
print(ab[1:10:2]) #selects in range of 1-10 with the skip value of 2

#strig finctions
#a = len(ab)
#a = ab.startswith("012")
#a = ab.endswith("789")
#a = ab.title()
#a = ab.capitalize()

print(a)

# text.strip()                            # remove leading/trailing whitespace
# text.split()                            # split on any whitespace → list
# " ".join(words)                         # list → string
# text.lower().replace("  ", " ")         # normalize spaces
# ",".join(map(str, numbers))             # numbers → csv string
# text.split(",", maxsplit=1)             # split only once (very useful!)
# text.startswith(("http://", "https://"))
# text.endswith((".jpg", ".png", ".webp"))
# "error" in text.lower()
# text.find("python") != -1               # old-school "contains"
# re.sub(r'\s+', ' ', text)               # normalize all whitespace
# text.strip().splitlines()               # get clean lines
# text.partition(sep)                     # split into (before, sep, after)
# name.removeprefix("Mr. ").removesuffix(" PhD")   # clean 3.9+
# f"{value:,.2f}"  

#                        # pretty numbers: 1,234,567.89

