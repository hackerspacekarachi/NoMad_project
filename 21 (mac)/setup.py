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
import json

data = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}

with open('try.json', 'w') as file:
             json.dump(data, file)