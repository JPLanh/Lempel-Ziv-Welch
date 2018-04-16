import node
import mapReduce
from base64 import b64encode

nodesSet = []

for i in range(0, 5):
  nodesSet.append(node.Node())
  
MR = mapReduce.map(nodesSet)

f=open("Text.txt", 'rb')
data = f.read()

i = 0
while i < len(data):
  MR.mapping(data[i:i+4096])
  i+=4096
