students=[
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherine","patronus":None}
]
n=1
for student in students:
    print(n, student["name"], student['house'], student["patronus"], sep=", ")
    n=n+1