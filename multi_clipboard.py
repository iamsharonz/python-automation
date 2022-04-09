import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'


def save_data(filepath, data):  # for writing into the json file
    with open(filepath, 'w') as f:
        json.dump(data, f)  # dump the data to the file f


def load_data(filepath):  # for reading the data
    try:  # an error will arise if the json file doesnt exist, so to handle that error we use try : except block
        with open(filepath, 'r') as f:
            data = json.load(f)  # to load the data from the file
            return data
    except:
        return {}

# def del_data(filepath, data):
#


# argv will give all the arguments that are passed in the command line along with the program name
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste() # to save the key along with the content in the clipboard
        save_data(SAVED_DATA, data)
        print('Data Saved!')
    elif command == 'load':
        key = input('Enter the key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to the clipboard!')
        else:
            print('Key does not exist!')
    elif command == 'list':
        print(data)
    # elif command == 'del':
    #

    else:
        print('Unknown Command')

else:
    print('Enter exactly one command.')

