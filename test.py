from base64 import b64encode

f = open("jplanh.png", 'rb')
#test = b"Thisisathesis"
mapping = {}
compression = []

iterator = iter(f.read())
#iterator = iter(test)
currentByte = next(iterator, None)
count = 300
byteSize = 0

while currentByte != None:
  byteSize += 1
  if currentByte in mapping:
    nextByte = next(iterator, None)
    concat = str(currentByte) + str(nextByte)
    if concat in mapping:
      nextByte = next(iterator, None)
      concat = str(currentByte) + str(nextByte)
      if concat in mapping:
        nextByte = next(iterator, None)
        concat = str(currentByte) + str(nextByte)
      else:
        nextByte = next(iterator, None)
        concat = str(currentByte) + str(nextByte)
        mapping[concat] = count
        compression.append(count)
        count+=1
        currentByte = nextByte    
    else:
      nextByte = next(iterator, None)
      concat = str(currentByte) + str(nextByte)
      mapping[concat] = count
      compression.append(count)
      count+=1
      currentByte = nextByte      
  else:
    mapping[currentByte] = currentByte
    nextByte = next(iterator, None)
    compression.append(currentByte)
    concat = str(currentByte) + str(nextByte)
    mapping[concat] = count
    count+=1
    currentByte = nextByte

print(byteSize)
print(len(compression))
f.close()

f = open("compression.uni", 'wb')
for i in compression:
  f.write(bytes(i))


