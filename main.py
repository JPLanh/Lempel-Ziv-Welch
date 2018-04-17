import node
import mapReduce
from base64 import b64encode

nodesSet = []

node.Node(0)
for i in range(1, 6):
  focusNode = node.Node(i)
  nodesSet.append(focusNode)
  focusNode.joinRing(nodesSet)

for i in nodesSet:
  i.printInfo()
  
finger = nodesSet[0]
  
MR = mapReduce.map(nodesSet)

f=open("Text.txt", 'rb')
data = f.read()

i = 0
while i < len(data):
  MR.mapping(data[i:i+4096], finger)
  i+=4096

MR.emit(finger)
