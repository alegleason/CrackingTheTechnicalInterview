# Method to check the value of a bit on pos i of x number
import math


def get_bit(num, i):
    return num & (1 << i) != 0


# Sets a bit at 1 on pos i of x number
def set_bit(num, i):
    mask = 1 << i
    return mask | num


# Clears a bit on pos i of x number, setting it to zero
def clear_bit(num, i):
    mask = ~(1 << i)
    return mask & num


# Clear bits from the most significant bit through i, inclusive
def clear_bit_msb_i(num, i):
    mask = (1 << i) - 1
    return mask & num


# Clear bits from i through 0, inclusive
def clear_bit_i_0(num, i):
    # + 1 bc zero based index
    mask = (-1 << (i + 1))
    return mask & num


# Set bit at i to 1 or zero, depending on bool parameter
def update_bit(num, i, bit_is1):
    value = 0 if not bit_is1 else 1
    mask = ~(1 << i)
    return num & mask | value << i


# Given two 32-bit numbers, N and M, and two bit positions i and j,
# insert M into N, such that M starts at bit j and ends at bit i.
def insert_MN(n, m, i, j):
    # Clear the bits j through i in N
    allOnes = ~0
    # 1s before position j, then 0s. left = 11100000
    left_part = allOnes << (j + 1)
    # 1s after position i. right = 00000011, the -1 adds 1 to the end
    right_part = ((1 << i) - 1)
    mask = left_part | right_part
    # Clear bits j through i then put m in there
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted


insert_MN(1024, 19, 2, 6)


# Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation
def binary_to_string(num):
    if num <= 0 or num >= 1:
        return "ERROR"

    res = "."
    st = ""
    count = 0
    hundred = pow(10, len(str(num)) - 2)
    num = num * hundred
    while num > 0:
        aux = num % 2
        st += str(int(aux))
        num = math.floor(num / 2)
        count += 1
        if count > 32:
            return "ERROR"

    st = st[::-1]
    res += st
    return res


binary_to_string(.333)


def flip_bit_to_win(num):
    current_length = 0
    previous_length = 0
    max_length = 1
    while num > 0:
        # If current bit is 1, checking from the lsb to the msb
        if num & 1 == 1:
            current_length += 1
        # If current bit is 0
        else:
            # Update to 0 (if next bit is 0) or current_length (if next bit is 1).
            previous_length = 0 if 2 & num == 0 else current_length
            current_length = 0
        # Get either the max of the new joint or the past max
        max_length = max(current_length + previous_length + 1, max_length)
        # This simulates the logical shift
        num >>= 1
    return max_length


flip_bit_to_win(1775)
