import matplotlib.pyplot as plt
f = open('dt.txt')
a = f.readlines()
t = []
A = []
for i in range (len(a)):
    t.append(float((a[i].split())[0]))
    A.append(float((a[i].split())[1]))
print(t)
print(A)
fig, ax = plt.subplots(figsize = (10, 5), dpi = 500)
ax.set_xlim(0, 16)
ax.set_ylim(-120, 120)
xerr = [0]
yerr = [0]
plt.plot(t, A, '-o', markersize = 2, c = 'green')
plt.legend(['A(t)'])
plt.xlabel('Время, с')
plt.ylabel('Амплитуда, мм')
plt.title('Зависимость амплитуды колебаний при резонансе от времени')
plt.grid(which = 'major', linewidth = 1.0)
plt.grid(which = 'minor', linewidth = 0.2)
plt.minorticks_on()
plt.savefig('График.jpg')
plt.show()
