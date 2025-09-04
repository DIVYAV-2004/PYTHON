#tuple
days=("sun","mon",["tue,fri"],"True",(1,2,3))
print(type(days))
print(len(days))
print(days[0][0])
print(days[2][0])
print(days[2][0][1])
print(f"{len(days[4])}")
print(f"size of the tuple is {len(days[4])}")
print(days)

