with open("digits.bin", "r") as f:
    bits = f.read().strip()

data = bytearray()

for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    data.append(int(byte, 2))

with open("output.jpg", "wb") as f:
    f.write(data)

print("Selesai!")
