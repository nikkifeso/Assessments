a = [3,8,9,7,6]
k = 4
n = len(a)
new_list =[]

def rotation(a, k):
    for i in a:
        a[i]= a[i+1]
    new_list.append(i)
    