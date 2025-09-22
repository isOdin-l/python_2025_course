
# p - point
def count_area(l_p_width: int, r_p_width: int, l_p_height: int, h_p_height: int)->int:
    return (r_p_width-l_p_width) * min(l_p_height, h_p_height)


a = [int(x) for x in input().split()]

l = 0
r = len(a)-1
mx_area = 0

while True:
    mx_area = max(mx_area, count_area(l,r,a[l],a[r]))
    if l+1 == r:
        break

    if a[l] < a[r]: # Правый больше -> двигаем левый
        l+=1
    elif a[l] > a[r]: # Левый больше -> двигаем правый
        r-=1
    elif a[l] == a[r]: # Они равны -> думаем, какой двигать надо
        if a[l+1] <= a[r-1]:
            r-=1
        elif a[l+1] > a[r-1]:
            l+=1
    
print(mx_area)