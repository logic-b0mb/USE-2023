from itertools import product  

words=product('СВЕТА',repeat=5) #  с продуктом повтореятся, c пермутацией без репита 
k=0 # присвоили каунт 
for w in words: # честно говоря не ебу как объяснить
    word=''.join(w) # делаем из картежей строки
    if word.count('С')>=1: #тут просто меняем условие 
        k+=1 # т.к счёт с нуля всегда
print(k) # выводим