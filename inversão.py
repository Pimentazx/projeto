def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))
