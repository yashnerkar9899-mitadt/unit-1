student={ "name":"Rahul","age":"21","course":"B.Tech"}
student2=dict(name="Amit",age=21,course="B.Sc")
empty_dict={}
mixed_dict={1:"one","two":2,(3,4):"Tuple as key"}
print("Name:",student["name"])
print("Age:",student.get("age"))
print("Marks:",student.get("marks",0))
print("Keys:",student.keys())
print("Values;",student.keys())
print("Items:",student.items())
print("students details:")
for key, value in statement.items():
    print(key,":",value)
