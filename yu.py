print('-'*30)
print('-'*30)
print('welcome to my home')
print('-'*30)
print('-'*30)
import time
while True:
    shuzi = int(input('please a number:'))
    if shuzi > 1 and shuzi < 20:
        time.sleep(3)
        print('you is baby')
    elif shuzi > 21 and shuzi < 40:
        time.sleep(3)
        print('you is hu man')
    elif shuzi > 41 and shuzi < 80:
        time.sleep(3)
        print('you is big man')
    else :
        time.sleep(3)
        print('you is old man')
