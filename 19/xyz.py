# s = "<PyQt5.QtWidgets.QPushButton object at 0x00000220FBF9C040>"
# print(s[-12:-1])
# a = {"465": "X", "407": "Z", "523": "C", "348": "Ctrl", "931": "Cmd", "724": "O", "871": ">\n \n.", "794": "L", "700": ") \n \n0", "120": "Esc", "178": "!\n \n1", "294": "#\n \n3", "236": "@\n \n2", "410": "%\n \n5", "468": "^\n \n6", "352": "$ \n \n4", "642": "( \n \n9", "584": "*\n \n8", "177": "Tab", "234": "Caps Lock", "291": "Shift", "260": "Q", "318": "W", "608": "U", "434": "R", "550": "Y", "492": "T", "666": "I", "376": "E", "504": "F", "446": "D", "678": "J", "562": "G", "620": "H", "736": "K", "388": "S", "330": "A", "581": "V", "755": "M", "639": "B", "697": "N", "813": "< \n \n,", "417": "Opt", "486": "Cmd", "555": "", "816": "+\n \n=", "758": "-\n \n_", "874": "Backspace", "898": "} \n \n]", "840": "{\n \n[", "782": "P", "956": "| \n \n\\", "910": "\" \n\n'", "852": ":\n \n;", "968": "Enter", "929": "?\n \n/", "987": "Shift", "1106": "\u2191", "1047": "Ctrl", "989": "Fn", "1105": "\u2190", "1163": "\u2193", "1221": "\u2192", "526": "&&\n \n7", "1013": "", "1050": "Page\nUp", "1107": "Page\nDown", "1164": "Home", "317": "", "280": "", "81": "", "44": "", "97": "", "281": "", "244": ""}
# # a = list(a.keys())
# a["465"] = "666"
# print(list(a.keys()))
# my_dict = {'64':'sg'}

# # Append an empty string as the value with the key '64'
# my_dict['64'] = ''

# # Print the dictionary to verify the result
# print(my_dict)

dict = {'layer1':{'a': 1, 'b': 2}}

# will create a new dictionary
# dict = {**dict, **{'c': 3}}

print(dict['layer1']['a'])
