import os
import json
import ast
import traceback

def get_specified_attributes(filepath, findstring):
    return_list = []

    if os.path.exists(filepath):  # Check the json file is existed
        try:  # if the file could not open, it will throw an exception and return null value
            with open(filepath, 'r') as f:  # read file from top to bottom line by line
                for line in f:
                    try:  # if some line is not valid, it will throw exception and continue to read the next line
                        line_list = ast.literal_eval(line)  # convert string representation of list to list
                        for line_json in line_list:  # if multiple json string is in a line
                            for key in line_json:  # get the key value in each json string
                                value = line_json[key]
                                key_lower = key.lower()  # convert the name of the property to lower string
                                # print(key_lower)
                                if key_lower.find(findstring) >= 0:  # find if the string 'april' is in
                                                                   # the name of the property
                                    return_list.extend(value)  # if find the property, extend the value list
                                                               # to return list
                    except Exception as e:
                        print(e)
                        traceback.print_exc()
        except Exception as e:
            print(e)
            traceback.print_exc()

    return return_list


if __name__ == '__main__':
    filepath = "test.json"  # json file path
    find_str = "april"  # in the json file, it will search the attributes which the name contains 'april'.
                        # such as april1 is a valid value because it contains 'april'
                        #         April2 is a valid value because if lower the case of April2, it will turn to april2 which contains 'april'

    return_list = get_specified_attributes(filepath, find_str)  # invoke the function and get the return list
    print(return_list)
