def generate_subsequences(s):
    n = len(s)
    subsequences = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            current = s[i:j]
            subsequences.append(current)

    return subsequences

input_string = "xyz"
result = generate_subsequences(input_string)
print(result)