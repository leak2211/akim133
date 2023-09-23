import random
import time

strtrng = 0
endrng = 500000000
lenth_array = 1000
array = []
array_bubble=[]
array_quick=[]
array_choice=[]

for z in range(strtrng, endrng):
    num = random.randint(1, lenth_array)
    array.append(num)
    array_bubble.append(num)
    array_quick.append(num)
    array_choice.append(num)

def bubblesort(x):
    for z in range(endrng-1):
        for j in range(endrng-z-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]            
    return x

def quicksort(x):
   if len(x) <= 1:
       return x
   else:
       q = random.choice(x)
   l_x = [n for n in x if n < q]
   e_x = [q] * x.count(q)
   b_x = [n for n in x if n > q]
   return quicksort(l_x) + e_x + quicksort(b_x)

def choicesort(x):
    n = len(x)
    for z in range(n-1):
        m = z
        for j in range(z+1, n):
            if x[j] < x[m]:
                m = j
        x[z], x[m] = x[m], x[z]
    return x

print("\033[42m")
print('начальный массив -', array)
print("\033[43m")

start_bubble = time.time()
print('результат пузырьковой сортировки -', bubblesort(array_bubble))
end_bubble = time.time() - start_bubble
print('время выполнения пузырьковой сортировки -', end_bubble, 'сек')
print("\033[45m")

start_quick = time.time()
print('результат ,быстрой сортировки -', quicksort(array_quick))
end_quick = time.time() - start_quick
print('время выполнения быстрой сортировки -', end_quick, 'сек')
print("\033[46m")

start_choice = time.time()
print('результат сортировки выбором -', choicesort(array_choice))
end_choice = time.time() - start_choice
print('время выполнения сортировки выбором -', end_choice, 'сек')