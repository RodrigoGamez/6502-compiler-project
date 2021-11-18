import json

var_counter = 0x0000


def update_var(name, value):
    """update an existing variable or add new one if none is found"""
    global var_counter
    
    with open('variables.json', 'r') as f:
        content = json.load(f)
    f.close()
    
    if name in content:
        content[name].key[0] = value
    else:
        content[name] = [value, var_counter]
        var_counter += 2
        
    with open('variables.json', 'w') as f:
        json.dump(content, f, indent=4)
    f.close()


def main():
    """main function of the programme"""
    update_var('var_1', 1)
    update_var('var_2', 2)


if __name__ == "__main__":
    "open or create the var.json file and turn it empty"
    with open('variables.json', 'w') as f:
        json.dump({}, f, indent=4)
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
