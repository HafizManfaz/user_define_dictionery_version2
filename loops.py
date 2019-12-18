d1 = {}
pre_skill = "python"
skills = pre_skill+input("Enter skills")
skills_list = skills.split()
for keys in range(5):
    key1 = input(f"Enter Key{keys}")
    val1 = input(f"Enter value{keys}")
    d1[key1] = val1
d1["skills_lists"] = skills_list
print(d1)   


