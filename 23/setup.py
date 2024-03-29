# import serial
# import json

# # Define the serial port and baud rate
# ser = serial.Serial('COM4', 115200, timeout=1)

# # Create a sample JSON data
# data = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }

# # Convert the JSON data to a string
# json_data = json.dumps(data)

# # Send the JSON data over the serial port
# ser.write(json_data.encode())

# # Close the serial connection when done
# ser.close()

# print((4 - 2) / 10 * 180)

# def replace_values_recursive(dictionary, replacements):
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             replace_values_recursive(value, replacements)
#         elif value in replacements:
#             dictionary[key] = replacements[value]

# # Example usage
# sample_json = {"layer1": {"465": "X", "407": "Z", "523": "C", "348": "Ctrl", "931": "Cmd", "724": "O", "871": ">\n\n.", "794": "L", "700": ")\n \n0", "120": "Esc", "178": "!\n \n1", "294": "#\n \n3", "236": "@\n \n2", "410": "%\n \n5", "468": "^\n \n6", "352": "$\n \n4", "642": "(\n \n9", "584": "*\n \n8", "177": "Tab", "234": "Caps Lock", "291": "Shift", "260": "Q", "318": "W", "608": "U", "434": "R", "550": "Y", "492": "T", "666": "I", "376": "E", "504": "F", "446": "D", "678": "J", "562": "W", "620": "H", "736": "K", "388": "S", "330": "A", "581": "M", "755": "M", "639": "B", "697": "N", "813": "<\n \n,", "417": "Opt", "486": "Cmd", "555": " ", "816": "+\n \n=", "758": "-\n \n_", "874": "Backspace", "898": "} \n \n]", "840": "{\n \n[", "782": "P", "956": "| \n \n\\", "910": "\" \n\n'", "852": ":\n \n;", "968": "Enter", "929": "?\n \n/", "987": "Shift", "1106": "\u2191", "1047": "Ctrl", "989": "Fn", "1105": "\u2190", "1163": "\u2193", "1221": "\u2192", "526": "&&\n \n7", "1013": "", "1050": "Page\nUp", "1107": "Page\nDown", "1164": "Home", "317": "", "280": "", "81": "", "44": "", "97": "", "281": "", "244": ""}, "layer2": {"465": "", "407": "", "523": "", "348": "", "931": "", "724": "", "871": "", "794": "", "700": "F10", "120": "", "178": "F1", "294": "F3", "236": "F2", "410": "F5", "468": "F6", "352": "F4", "642": "F9", "584": "F8", "177": "", "234": "", "291": "", "260": "", "318": "", "608": "", "434": "", "550": "", "492": "", "666": "", "376": "", "504": "", "446": "", "678": "", "562": "", "620": "", "736": "", "388": "", "330": "", "581": "", "755": "", "639": "", "697": "", "813": "", "417": "", "486": "", "555": "", "816": "F12", "758": "F11", "874": "", "898": "", "840": "", "782": "", "956": "", "910": "", "852": "", "968": "", "929": "", "987": "", "1106": "", "1047": "", "989": "", "1105": "", "1163": "", "1221": "", "526": "F7", "1013": "", "1050": "", "1107": "", "1164": "", "317": "", "280": "", "81": "", "44": "", "97": "", "281": "", "244": ""}, "layer3": {"465": "", "407": "", "523": "", "348": "", "931": "", "724": "", "871": "", "794": "", "700": "", "120": "", "178": "", "294": "", "236": "", "410": "", "468": "", "352": "", "642": "", "584": "", "177": "", "234": "", "291": "", "260": "", "318": "", "608": "", "434": "", "550": "", "492": "", "666": "", "376": "", "504": "", "446": "", "678": "", "562": "", "620": "", "736": "", "388": "", "330": "", "581": "", "755": "", "639": "", "697": "", "813": "", "417": "", "486": "", "555": "", "816": "", "758": "", "874": "", "898": "", "840": "", "782": "", "956": "", "910": "", "852": "", "968": "", "929": "", "987": "", "1106": "", "1047": "", "989": "", "1105": "", "1163": "", "1221": "", "526": "", "1013": "", "1050": "", "1107": "", "1164": "", "317": "", "280": "", "81": "", "44": "", "97": "", "281": "", "244": ""}, "layer4": {"465": "", "407": "", "523": "", "348": "", "931": "", "724": "", "871": "", "794": "", "700": "", "120": "", "178": "", "294": "", "236": "", "410": "", "468": "", "352": "", "642": "", "584": "", "177": "", "234": "", "291": "", "260": "", "318": "", "608": "", "434": "", "550": "", "492": "", "666": "", "376": "", "504": "", "446": "", "678": "", "562": "", "620": "", "736": "", "388": "", "330": "", "581": "", "755": "", "639": "", "697": "", "813": "", "417": "", "486": "", "555": "", "816": "", "758": "", "874": "", "898": "", "840": "", "782": "", "956": "", "910": "", "852": "", "968": "", "929": "", "987": "", "1106": "", "1047": "", "989": "", "1105": "", "1163": "", "1221": "", "526": "", "1013": "", "1050": "", "1107": "", "1164": "", "317": "", "280": "", "81": "", "44": "", "97": "", "281": "", "244": ""}}

# replacements = {
#     "C": 6,
#     "W": 20,
#     "A": 4,
#     "S": 22,
#     "Z": 29,
#     "X": 27,
#     "E": 8,
#     "R": 21,
#     "D": 7
# }

# replace_values_recursive(sample_json, replacements)

# print(sample_json)

nu = [0,]
nu.extend([i for i in range(4,134)])
nu.extend([47, 48, 49, 52, 57, 70, 71, 74, 75, 78, 83, 116, 127, 128, 129, 130, 131, 132])
nu.extend([153, 156, 158, 224, 225, 226, 227, 228, 229, 230, 231])




ap = ['']
ap.extend([chr(i) for i in range(ord('A'), ord('Z')+1)])
ap.extend(['!\n \n1','@\n \n2','#\n \n3','$\n \n4','$\n \n5','%\n \n6','^\n \n7','*\n \n8','(\n \n9',')\n \n0', 'Enter', 'Esc', 'Backspace', 'Tab', 'Space', '-\n \n_', '+\n \n=', '(\n \n9', ')\n \n0', '| \n \n\\', '#', ':\n \n;', "\" \n \n'", '~\n \n`', '<\n \n,', '>\n \n.', '?\n \n/', 'Caps Lock'])
ap.extend(['F{}'.format(i) for i in range(1, 13)])
ap.extend(['Print\nscreen', 'Scroll\nlock', 'Pause', 'Insert', 'Home', 'Page\nUp', 'Del', 'End', 'Page\nDown', '\u2192', '\u2190', '\u2193', '\u2191', 'Num\nlock', '/', '*', '-', '+', 'Numpad Enter', ])
ap.extend(['Numpad {}'.format(i) for i in range(1, 10)])
ap.extend(['Numpad 0', '.', '~', 'Fn', 'Power', '=',])
ap.extend(['F{}'.format(i) for i in range(13, 25)])
ap.extend(['Exec', 'Help', 'Menu', 'Select', 'Stop', 'Again', 'Undo', 'Cut', 'Copy', 'Paste', 'Find', 'Mute', 'Vol+', 'Vol-', 'Locking\nCaps\nLock', 'Locking\nNum\nLock', 'Locking\nScroll\nLock', ',' ])
ap.extend(['(', ')', '\\', "'", 'Caps\nlock', 'Print Screen', 'Scroll Lock', 'Home Page', 'Page Up', 'Page Down', 'Num Lock', 'Execute', 'Volume Mute', 'Volume Up', 'Volume Down', 'Locking Caps Lock', 'Locking Num Lock', 'Locking Scroll Lock'])
ap.extend(['Alt\nErase', 'Clear', 'Return', 'Left\nCtrl', 'Left\nShift', 'Left\nAlt', 'Left\nWin', 'Right\nCtrl', 'Right\nShift', 'Right\nAlt', 'Right\nWin'])

# t = 7
# while(t != 777):
#     i = int(input('Index: '))
#     if t == 777:
#         break
#     else:
#         print(nu[i]) #Numbers
#         print(ap[i]) #Alphabets

k_val = zip(ap, nu)
k_val = dict(k_val)
print(k_val)