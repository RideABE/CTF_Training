with open('flag.jpg', 'rb') as f:
    f.seek(7060)
    data = f.read()
reversed_data = data[::-1]
 
with open('flag_final.png', 'wb') as f:
    f.write(reversed_data)