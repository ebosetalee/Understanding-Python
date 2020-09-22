def sum(value):
    total = 0
    if len(value) >= 2:
        for number in value:
            if number < 0:
                raise TypeError
            else:
                total += number
        return total
    else:
        return TypeError
