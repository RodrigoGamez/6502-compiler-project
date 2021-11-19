import json

var_counter = 0x0000


def update_var(name, value, value_type='integer'):
    """update an existing variable or add new one if none is found"""
    global var_counter
    
    with open('variables.json', 'r') as f:
        content = json.load(f)
    f.close()

    if value_type == 'integer':
        number = value
    elif value_type == 'variable':
        number = content[value]["value"]
    else:
        number = 0

    if name in content:
        content[name][0] = number
    else:
        content[name] = {"value": int(number), "address": hex(var_counter)}
        var_counter += 2
        
    with open('variables.json', 'w') as f:
        json.dump(content, f, indent=4)
    f.close()


def get_value(variable):
    """gives the value of an variable"""
    with open('variables.json', 'r') as f:
        content = json.load(f)
    f.close()

    return content[variable]["value"]


def get_address(variable):
    """gives the adress of an variable"""
    with open('variables.json', 'r') as f:
        content = json.load(f)
    f.close()

    return content[variable]["address"]


def write_out(string, new_line=True):
    """writes an string onto the output.txt file"""
    with open('output.txt', 'r') as f:
        content = f.readlines()
    f.close()

    if new_line:
        content.append(str(string))
    else:
        content[-1] += str(string)

    with open('output.txt', 'w') as f:
        f.writelines(content)
    f.close()


def main():
    """main function of the programme"""
    with open(input_f, 'r') as f:
        code = f.readlines()
    f.close()

    out = ""

    for line in code:
        words = line.split()
        if 'var' in words[0]:
            update_var(words[1], words[2], wordmap[words[0]][1])
            for instruction in translation[words[0]]:
                if instruction == "integer":
                    write_out(hex(int(words[2])))
                elif instruction == "variable":
                    write_out(get_address(words[1]))
                else:
                    write_out(instruction)


if __name__ == "__main__":
    "open or create the var.json file and turn it empty"
    with open('variables.json', 'w') as f:
        json.dump({}, f, indent=4)
    f.close()

    with open('output.txt', 'w') as f:
        f.write("")
    f.close()

    "ask to the user for a file and check if it's valid, if none is given it"
    "will use a predefined one"
    f_flag = True

    while f_flag:
        input_f = input("File name:")
        if input_f == "":
            input_f = "test.ccode"
            f_flag = False
        elif input_f[-6:] == ".ccode" and len(input_f) >= 7 :
            f_flag = False
        else:
            print("File isn't valid")

    "take the wordmap.json and translation.json files and dump their contents"
    "into dictionaries so they're easily used"
    with open('wordmap.json', 'r') as f:
        wordmap = json.load(f)
    f.close()

    with open('translation.json', 'r') as f:
        translation = json.load(f)
    f.close()

    main()
