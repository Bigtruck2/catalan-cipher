def encrypt(x, key):
  new_str=''
  onHold=[]
  for character in range(0,len(key)):
    if len(x) > character:
      onHold.insert(0,x[character])
    if key[character] == '1':
      continue
    else:
      new_str+=onHold[0]
      onHold.pop(0)
  return new_str

def decrypt(x, key):
  onHold=[]
  filled=[]
  count=0
  for character in range(0,len(key)):
    if character >= len(x):
      filled=list(set(range(0,len(x)+1)) - set(filled))
      x = x[count:][::-1]
      for i in range(0,len(x)):
        onHold.insert(filled[i],x[i])
      break
    elif key[character] == '0':
      onHold.insert(character,x[count])
      count+=1
      filled.append(character)
  return ''.join(onHold)
x= "Hello world"
key = '1110011000100001111010'
print("cipher text:", encrypt(x, key))
print("deciphered text:", decrypt(encrypt(x,key),key))
