input = open('flag', 'rb')
input_all = input.read()
ss = input_all[::-1]
output = open('flag.zip', 'wb')
output.write(ss)
input.close()
output.close()

