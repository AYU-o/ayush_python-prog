import matplotlib.pyplot as plt

cat = ["Aryan","Askini","Ayush","Divakar"]
exp=[10,95,78,81]

plt.bar(cat,exp, color='blue')

plt.xlabel("Name of students-->")
plt.ylabel("Marks (in %age) -->")
plt.title("9th Class Final term marks :-")

plt.show()