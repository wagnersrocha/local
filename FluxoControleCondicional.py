def clinic():
    print ("Voce acabou de entrar na clinica!")
    print ("Voce entra pela porta a esquerda (left) ou a direita (right)?")
    answer = raw_input("Digite left (esquerda) ou right (direita) e pressione 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("Esta e a sala de Abuso Verbal, seu monte de caca de papagaio!")
    elif answer == "right" or answer == "r":
        print ("E claro que esta e a Sala das Discussoes. Eu ja disse isso!")
    else:
        print ("Voce nao escolheu esquerda ou direita. Tente de novo.")

    clinic()
clinic()


# Atribua True se 17 < 328 ou False se nao for.
bool_one = True   # Fizemos esta para voce!

# Atribua True se 100 == (2 * 50) ou False caso contrario.
bool_two = True

# Atribua True se 19 <= 19 ou False se nao for.
bool_three = True

# Atribua True se -22 >= -18 ou False se nao for.
bool_four = True

# Atribua True se 99 != (98 + 1) ou False caso contrário.
bool_five = False