#Afficher les nombres de 1 à 100
#Si le nombre est un multiple de 3 : Affichez Fizz
#Si le nombre est un multiple de 5 : Affichez Buzz
#Si c'est les deux : Afficher FizzBuzz
#Sinon juste afficher le nombre

for i in range(1,101):
    divisible_3 = i % 3 == 0
    divisible_5 = i % 5 == 0

    if divisible_5 and divisible_3:
        print("FizzBuzz")
    elif divisible_3:
        print("Fizz")
    elif divisible_5:
        print("Buzz")
    else:
        print(i)