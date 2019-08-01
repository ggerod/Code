#!/usr/bin/python3

def st_gcd(u,v):
    # GCD(0,v) == v; GCD(u,0) == u, GCD(0,0) == 0 */
    if (u == 0):
        return v
    if (v == 0):
        return u
 
    # Let shift := lg K, where K is the greatest power of 2 dividing both u and v. */
    shift=0
    while (((u | v) & 1) == 0):
        shift +=1
        u >>= 1
        v >>= 1

    # while u is even
    while ((u & 1) == 0):
        u >>= 1

    # From here on, u is always odd. */
    while (True):
        # remove all factors of 2 in v -- they are not common note: v is not zero, so while will terminate */
        while ((v & 1) == 0):  #/* Loop X */
            v >>= 1

        #* Now u and v are both odd. Swap if necessary so u <= v,
        #then set v = v - u (which is even). For bignums, the
        #swapping is just pointer movement, and the subtraction
        #can be done in-place. */
        if (u > v):
            t = v
            v = u
            u = t #/ Swap u and v.

        v = v - u; # Here v >= u.

        if (v == 0):
            break

    # restore common factors of 2 */
    return(u << shift)


print("Enter numbers to get gcd:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("gcd of ",a,"and",b,"is: ",end="")
print(st_gcd(a,b))
