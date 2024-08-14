def categorizeBox(length, width, height, mass):
    volume = length * width * height
    is_bulky = False
    is_heavy = False
    if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**4:
        is_bulky = True
    if mass >= 100:
        is_heavy = True

    if is_bulky and is_heavy:
        return "Both"
    elif not is_bulky and not is_heavy:
        return "Neither"
    elif is_bulky and not is_heavy:
        return "Bulky"
    else:
        return "Heavy"

        