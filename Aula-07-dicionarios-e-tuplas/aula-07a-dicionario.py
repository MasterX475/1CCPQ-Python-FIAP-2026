eng2sp = dict()
eng2sp["one"] = "uno"

print(eng2sp)
print("one" in eng2sp)
print("uno" in eng2sp)

eng2sp = {"one": "uno",
          "two": "dois",
          "three": "tres"}

print(eng2sp)
print(eng2sp["two"])
print(eng2sp["three"])

valores = eng2sp.values()
print(valores)