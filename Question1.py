with open('twain.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Huck', 'HucK')

# Write the file out again
with open('twain.txt', 'w') as file:
  file.write(filedata)