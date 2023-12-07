def bits(hashed_value):
	return bin(hashed_value & 0xFFFFFFFF)[2:].zfill(32)

k1 = bits(hash("Monty"))
k2 = bits(hash("Money"))

diff = ("^ "[a==b] for a, b in zip(k1, k2))

print(f"{k1}\n{k2}\n{''.join(diff)}")