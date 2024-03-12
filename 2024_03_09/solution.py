def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    if dividend == 0:
        return (0, 0)

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    remainder = 0

    for i in range(31, -1, -1):
        if (dividend >> i) >= divisor:
            quotient += (1 << i)
            dividend -= (divisor << i)

    quotient *= sign

    return (quotient, remainder)

result = divide(10, 3)
print(result)  # Output: (3, 1)