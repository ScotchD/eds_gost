import gostcrypto.gosthash
from random import randint
from sympy import isprime

fname1 = "test2.docx"
with open(fname1, "r", encoding="utf-8") as f:
    print("Содержимое файла:", f.read())

# Создание хеша открытого текста
buffer_size = 128
hash_obj = gostcrypto.gosthash.new("streebog512")
with open(fname1, "rb") as file:
    #print("Содержимое файла:", file.read())
    buffer = file.read(buffer_size)
    while len(buffer) > 0:
        hash_obj.update(buffer)
        buffer = file.read(buffer_size)
hash_result = hash_obj.hexdigest()
hash_result = int(hash_result, 16)
print("Хэш:", hash_result)

# Генерация числа q
q = None
while not(isprime(q)):
    q = randint(2 ** 254, 2 ** 256)
print("q =", q)

# Генерация числа p
r = randint(2 ** 254, 2 ** 256)
p = q * r
while not(isprime(p + 1)):
    r += 1
    p = q * r
p += 1
print("p =", p)

# Генерация числа a
g = randint(2, p - 1)
a = pow(g, r, p)
print("a =", a)

# Запись ключей в файл
fname1 = "ключи2.txt"
with open(fname1, "w", encoding="utf-8") as file:
    file.write(f"p = {p}\n")
    file.write(f"q = {q}\n")
    file.write(f"a = {a}\n")

#Генерация числа x
x = randint(2, q - 1)
print("x =", x)

# Вычисление y
y = pow(a, x, p)
print("y =", y)
with open(fname1, "a", encoding="utf-8") as file:
    file.write(f"y = {y}\n")

# Создание подписи
k = randint(2, q - 1)
r = pow(a, k, p) % q
s = (x * r + k * hash_result) % q
print("Подпись:","\n", "r =", r, "\n", "s =", s)

# Запись подписи в файл
with open(fname1, "a", encoding="utf-8") as file:
    file.write(f"r = {r}\n")
    file.write(f"s = {s}\n")