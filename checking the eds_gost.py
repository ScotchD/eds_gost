import gostcrypto.gosthash

# Получение файла и создание хэша
fname1 = "test2.docx"
with open(fname1, "r", encoding="utf-8") as f:
    print("Содержимое файла:", f.read())

buffer_size = 128
hash_obj = gostcrypto.gosthash.new("streebog512")
with open(fname1, "rb") as file:
    buffer = file.read(buffer_size)
    while len(buffer) > 0:
        hash_obj.update(buffer)
        buffer = file.read(buffer_size)
hash_result = hash_obj.hexdigest()
hash_result = int(hash_result, 16)
print("Хэш:", hash_result)

# Получение открытых ключей и подписи
fname2 = "ключи2.txt"
with open(fname2, "r", encoding="utf-8") as f:
    p = int(f.readline()[4:])
    q = int(f.readline()[4:])
    a = int(f.readline()[4:])
    y = int(f.readline()[4:])
    r = int(f.readline()[4:])
    s = int(f.readline()[4:])
print(f"p = {p}\nq = {q}\na = {a}\ny = {y}\nr = {r}\ns = {s}")

# Проверка
v = pow(hash_result, q - 2, q)
z1 = s * v % q
z2 = (q - r) * v % q
u = ((pow(a, z1, p) * pow(y, z2, p)) % p) % q
print("u =", u)
if u == r:
    print("Подпись верна")
else:
    print("Подпись неверна")