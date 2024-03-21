def remove_spaces(row: str):
    row = list(row)
    i = 0
    for j in range(len(row)):
        if (row[i] != row[j]) or (row[i] == row[j] and row[j] != "_" and i != j):
            i += 1
            row[i] = row[j]
    row[:] = row[:i + 1]
    if len(row) > 1 and row[0] == "_":
        row.pop(0)
    if len(row) > 1 and row[-1] == "_":
        row.pop(-1)
    return "".join(row)


if __name__ == "__main__":
    example = "_On__my___home_world"
    print(remove_spaces(example))
    print("blah1")
