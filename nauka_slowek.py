# function which opening and reading file and cleaning file with whitespaces and return clear list of words
# using method strip, and change all letters for lower
# function return cleaning list of words from file
# function change the word for lowercase
def open_file(filename): 
    list_word = []
    list_word_lower=[] 
    with open (filename, "r", encoding="utf-8") as file:
        for readline in file:
            line_strip = readline.strip()
            if len(line_strip) > 0:  
                list_word.append(line_strip)
                list_word_lower = [x.lower() for x in list_word]
    return list_word_lower

# function which checking user answer by comparing with pattern and counts user result
# user answer are cleaning with whitespaces
# function return message about user answer
# PROBLEM jak uzyc w print wyrazu z listy pol, zeby wpisac, ze odpowiedz nie jest danym wyrazem z listy pol? 
# PROBLEM nie zlicza result
def check (ang, user_answer):
    result = 0
    if ang == user_answer.strip():
        message = print(f'Very good! {user_answer} is correct answer \n')
        result += 1
    else:
        message = print (f"Sorry, but {user_answer}, is the wrong answer. Correct answer is: {ang}.\n")
    return message, result

# function which match result to grade using match-case
def grade (result):
    match result:
        case 3:
            return '5'
        case 2:
            return '4'
        case 1:
            return '3'
        case other:
            return '1'
            
# function which create list of user answer (and change for lowercase), and using map to compare correct user answer with list ang 
# next count result and make grade  by function grade  
def main_game (pol, ang): 
    list_user_answer = [] 
    for i in pol:
        
        user_answer = input(f"Write a word - {i} - in english: ")
        list_user_answer.append(user_answer.lower())

    compare = list(map(check, ang, list_user_answer))
    max_result=len(ang)
    print(check (ang, user_answer))
    print ("Your result is: ",check(result),"pkt on possible: ",(max_result))
    print ("Your grade is: ", grade(result))

  
def menu(show_options):
    for key in show_options.keys():
        print(key, '--', show_options[key])

def main():
    ang = open_file("ang.txt")  
    pol = open_file("pol.txt")
    main_game(pol,ang)
    
    show_options = {
        1 : 'Repeat the game' ,
        2 : 'Exit'
    }
    while (True):
        menu (show_options)
        option = int (input ("Choice option: "))
        if option == 1:
            main_game(pol,ang)
        else:
            exit()
main()

 




    

     


