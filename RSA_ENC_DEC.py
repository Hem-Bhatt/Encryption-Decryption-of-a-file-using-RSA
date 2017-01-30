


#PROGRAM MEASURING TIME FOR RSA ENCRYPTION FOR A FILE

from Crypto.PublicKey import RSA
from timeit import default_timer as timer
readsize = 127
writesize = 128

private_key = RSA.generate(writesize * 8)  #1024 bit key
public_key = private_key.publickey()
filename=raw_input("Enter filename:")
filename2=filename+"RSA_ENCRYPT"
filename3=filename+"RSA_DECRYPT"
f = open(filename,'rb')

p = open(filename2,'wb')
i = 0
se=timer()
while True:
	data = f.read(readsize)
	if not data:
		break
	i += 1
	enc_data = public_key.encrypt(data, 32)[0] #Encryption
	
	p.write(chr(len(enc_data)))
	p.write(enc_data)
p.close()
f.close()
ee=timer()
print("The time taken for RSA encryption is---------------------------------------------\n\n")
print(ee-se)
f = open(filename2,'rb')
p = open(filename3,'wb')
j = 0
sd=timer()
while True:
	length = f.read(1)
	if not length:
		break
	data = f.read(ord(length))
	
	j += 1
	dec_data = private_key.decrypt(data) #decryption
	p.write(dec_data[:readsize]) #writes the decrypted file 
p.close()
f.close()
ed=timer()
print("The time taken for RSA decryption is ----------------------------------------------\n\n")
print(ed-sd)

#print(i, j)
