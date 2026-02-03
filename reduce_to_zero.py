def min_operations_to_zero(n):
    """
    Find minimum number of operations required to add or subtract 2 raised to power k where k is a positive integer from the number to make it zero. 
    """
    operations = 0
    while n > 0:
        if n & 1:  # n is odd i.e. last bit is 1 then we have to check if previous bit is 1 or 0
            if n & 2:  # this returns true if second last bit is also 1
                n += 1  # if both last bits are 1 then we do +1 to make it even and then we can right shift
            else:
                n -= 1  # if last bit is 1 and second last bit is 0 then we do -1 to make it even as substracting 1 from binary
                        # representation of a number or subtracting 1 from a decimal number is same 
            operations += 1   # whenever we encounter 1, we need to do at least one operation so we increment operations
        n >>= 1  # if n is even i.e. zero at the end so left shift it as we want to reach next 1 bit
    return operations
    


print(min_operations_to_zero(7))   # 2
print(min_operations_to_zero(21))  # 3
print(min_operations_to_zero(8))
print(min_operations_to_zero(11))
print(min_operations_to_zero(203))
 # 3? Let's check: 11 = 8 + 2 + 1 (3 ops) but NAF: 11 mod 4=3 → +1→12/2=6, 6 even→3/2=3 odd mod4=3→+1→4/2=2 even→1 odd→-1→0
# coeffs: -1 (2^0), 0, -1 (2^2), 1 (2^3)? Let me compute manually: better trust algorithm.
# Actually 11 = 16 - 4 - 1 (3 ops) yes.
