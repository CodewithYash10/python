# student = {
#     "name" : "Yash",
#     "scores" : {
#         "chem" : 97,
#         "phy" : 98,
#         "maths" : 99,
#     }
# }
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("scores"))
# print(student.update({"key" : "Yash"}))

student = {"name": "John"}
student.update({"key": "Yash"})
print(student)
# Output: {'name': 'John', 'key': 'Yash'}
