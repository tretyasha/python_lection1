text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-1])
# print(text[-5])  # б
# # съешь ещё этих мягких французских булок
# print(text[:])
# # # съ  нулевой первый,второй не включая
# print(text[:2])
# # print(text[len(text)-2:])  # ок
# print(text[20:])  #
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
print(text)
