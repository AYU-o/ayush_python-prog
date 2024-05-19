import matplotlib.pyplot as plt

cat = ["a","b","c"]
exp=[100,300,500]

plt.bar(cat,exp, color='blue')

plt.xlabel("x")
plt.ylabel("y")
plt.title("abc")

plt.show()