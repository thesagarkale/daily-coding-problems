def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    if dividend == 0:
        return (0, 0)

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0

    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += multiple
            temp += temp
            multiple += multiple

    return quotient, dividend

result = divide(100, 2)
print(result)