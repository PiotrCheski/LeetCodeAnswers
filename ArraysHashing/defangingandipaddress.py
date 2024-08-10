def defangIPaddr(address):
    return address.replace(".", "[.]")
    new_address = ""
    for idx, char in enumerate(address):
        if char == ".":
            new_address += "["
            new_address += "."
            new_address += "]" 
        else:
            new_address += address[idx]
    return new_address


address_t = "1.1.1.1"
print(defangIPaddr(address_t))