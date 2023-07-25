import classes
import json
import os.path

def guidelines():
    """1.Έχω υλοποιήσει τις κλάσεις: SakClass, Player, Human, Computer και Game.
    2.Κληρονομικότητα υπάρχει μεταξύ των κλάσεων Player, Human και Computer όπου η κλάση Player είναι η βασική κλάση και
    οι Human και Computer οι παράγωγες. Αυτές κληρονομούν τις ιδιότητες name, score και correct_answers τις βασικής κλάσης.
    3.Επέκταση μεθόδου έγινε με τη μέθοδο super() στους κατασκευαστές των παράγωγων κλάσεων Human και Computer όπου και
    οι δύο καλούν τον κατασκευαστή της βασικής κλάσης Player. Επίσης, επέκταση έχει γίνει και στη μέθοδο __repr__ ώστε να
    επιστρέφει βασικές και χρήσιμες πληροφορίες για τις ιδιότητες των κλάσεων Player, Human, Computer και Game αντίστοιχα.
    4.Χρησιμοποιήθηκε ο decorator @classmethod σε όλες τις μεθόδους της κλάσης Game καθώς ήθελα να χειριστώ τις μεθόδους της
    κλάσης χωρίς να δημιουργήσω αντικείμενο τύπου Game. Επίσης, χρησιμοποιήθηκε ο decorator @staticmethod στις μεθόδους
    reset_proposal() και sort_proposal() της κλάσης SakClass καθώς δεν έχουν κάποια άμεση σχέση με την κλάση, τις ιδιότητες
    και τις μεθόδους της.
    5.Το πρόγραμμα μου αποθηκεύει τις λέξεις του αρχείου greek7.txt σε δομή λεξικό-dictionary με key την εκάστοτε λέξη και
    value την αξία της λέξης βάση πόντων. Με λεξικό αναπαραστάθηκε και το σακουλάκι με key το εκάστοτε γράμμα και value μια
    2D λίστα με το πόσα ίδια γράμματα υπάρχουν στο σακουλάκι και με την αξία του κάθε γράμματος. Η δομή λίστα χρησιμοποιήθηκε
    για να αναπαρασταθούν οι προτάσεις του χρήστη και του Pc (τα 7 γράμματα ή λιγότερα από τα οποία μπορεί να σχηματίσει
    λέξη). Οι δυο λίστες αυτές είναι 2D και περιέχουν τα γράμματα και τις αντίστοιχες αξίες τους. Λίστες με μέγεθος 1
    χρησιμοποιήθηκαν και για να αναπαραστήσουν διάφορες μεταβλητές που χρειαζόμουν να ήταν μεταλλάξιμες.
    6.Ο αλγόριθμος που υλοποίησα να παίζει ο Η/Υ είναι ο Min-Max-Smart με επιλογή για το χρήστη να παίζει ενάντια σε όποιον
    από τους τρεις θέλει.
    ->Bonus χρήσιμες πληροφορίες:
    i. Ο αριθμός των γραμμάτων στο σακουλάκι είναι by default τυχαίος απο το 1 μέχρι 3, και οι αξίες τους από το 1-10.
    Τα όρια αυτά αλλάζουν εύκολα με αλλαγή των ορίων στη μέθοδο randomize_sak() της κλάσης SakClass.
    ii. Πέρα από αυτά νομίζω το πρόγραμμα καθοδηγεί το χρήστη στο τι μπορεί να κάνει μέσω των επιλογών στο μενού."""


difficulty_level = 1

while True:
    print('--------------------')
    print('***** SCRABBLE *****')
    print('--------------------')
    option = str(input('1. Σκορ\n\
2. Ρυθμίσεις(Δυσκολία)\n\
3. Παιχνίδι\n\
4. Πληροφορίες\n\
5. help(guidelines)\n\
q. Έξοδος\n\
--------------------\n\
H επιλογή σας:'))

    if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != 'q' and option != 'help(guidelines)':
        print("Παρακαλώ πληκτρολογήστε μια από τις επιλογές.")
        continue

    if option == '1':
        print('--------------------')
        jsonList = []
        if os.path.exists('sample.txt'):
            try:
                with open('sample.txt', 'r') as openfile:
                    for json_object in openfile:
                        temp = json.loads(json_object)
                        jsonList.append(temp)

                    for student in jsonList:
                        print(student)
            except:
                print('--------------------')
                print('Σφάλμα κατά τo άνοιγμα του αρχείου sample.txt.')
                print('--------------------')
            else:
                print('--------------------')
                print('Το sample.txt άνοιξε επιτυχώς!')
                print('--------------------')
            openfile.close()
        else:
            print('Το αρχείο sample.txt δεν υπάρχει.')

    if option == '2':
        while True:
            print('--------------------')
            difficulty = str(input(
                'Επίπεδο Δυσκολίας\n--------------------\n1. MIN Letters\n2. MAX Letters\n3. SMART\nb. Πήγαινε πίσω\n--------------------\nH επιλογή σας:'))
            print('--------------------')
            if difficulty != '1' and difficulty != '2' and difficulty != '3' and difficulty != 'b':
                print("Παρακαλώ πληκτρολογήστε μια από τις επιλογές.")
                continue
            if difficulty == '1':
                difficulty_level = 1
                break
            if difficulty == '2':
                difficulty_level = 2
                break
            if difficulty == '3':
                difficulty_level = 3
                break
            if difficulty == 'b':
                break

    if option == '3':
        if os.path.exists('sample.txt'):
            game = classes.Game(difficulty_level)
        else:
            try:
                with open('sample.txt', 'w') as f:
                        f.write('')
            except:
                print('--------------------')
                print('Σφάλμα κατά τη δημιουργία του αρχείου sample.txt.')
                print('--------------------')
            else:
                print('--------------------')
                print('Το sample.txt δημιουργήθηκε επιτυχώς!')
                print('--------------------')
            f.close()
            game = classes.Game(difficulty_level)

    if option == '4':
        print('--------------------')
        print('Πληροφορίες')
        print('--------------------')
        print('->Στην επιλογή 1. ο χρήστης μπορεί να δει χρήσιμες πληροφορίες για τα παιχνίδια που υπάρχουν στο αρχείο\n\
->Στην επιλογή 2. ο χρήστης μπορεί να διαλέξει τη δυσκολία του παιχνιδιού (Προεπιλεγμένη είναι η 1η επιλογή)\n\
->Στην επιλογή 3. ο χρήστης μπορεί να παίξει το παιχνίδι\n\
->Στην επιλογή 4. είστε ήδη :)\n\
->Στην επιλογή 5. βρίσκεται το help(guidelines) που ζητήθηκε για την άσκηση\n\
->Στην επιλογή q. ο χρήστης τερματίζει το πρόγραμμα')
        print('--------------------')

    if option == '5' or option == 'help(guidelines)':
        print('--------------------')
        help(guidelines)
        print('--------------------')

    if option == 'q':
        print('Αντίο σας!')
        break
