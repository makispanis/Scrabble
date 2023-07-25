import random
import json
import itertools as it


class SakClass:
    def __init__(self):
        """Αρχικοποιεί την κλάση SakClass, δημιουργεί ένα λεξικό από τα γράμματα της ΑΒ με τον αριθμό τους και τις αξίες τους.\n\
Επίσης δημιουργεί και δύο κενές λίστες για τις προτάσεις σε χρήστη και PC."""
        self.letters = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                        'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                        'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                        'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                        'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}
        self.player_proposal = []
        self.pc_proposal = []

    @staticmethod
    def reset_proposal(proposal):
        """Αδειάζει εξ'ολοκλήρου τη λίστα της πρόταση"""
        proposal.clear()

    @staticmethod
    def sort_proposal(proposal):
        """Ταξινομεί την πρόταση από τα αριστερά προς τα δεξιά από το Ω…Α"""
        proposal.sort(key=lambda row: (row[0], row[1]), reverse=True)

    def num_available_letters(self):
        """Μετράει και επιστρέφει πόσα γράμματα υπάρχουν στο σακουλάκι"""
        count = 0
        for i in list(self.letters.keys()):
            if self.letters.get(i)[0] != 0:
                count = count + self.letters.get(i)[0]
        return count

    def make_proposal(self, proposal, mode, prev_proposal_length):
        """Δημιουργεί μια νέα πρόταση εξολοκλήρου ή προσθέτει σε ήδη υπάρχουσα και την επιστρέφει.\n\
Ανάλογα με τις συνθήκες και τους περιορισμούς μπορεί να επιστρέψει και -1 αν δεν μπορεί να δημιουργηθεί η πρόταση.\n"""
        if mode == 'vrhke' or (mode == 'paso' and self.num_available_letters() != prev_proposal_length):

            self.sort_proposal(proposal)
            if self.num_available_letters() >= 7 - len(proposal):
                temp_letters = self.getletters(7 - len(proposal))
                b = [x[:] for x in proposal]
                for i in range(0, len(temp_letters)):
                    b.append(temp_letters[i])
                self.sort_proposal(b)
                return b
            elif self.num_available_letters() < 7 - len(proposal) and self.num_available_letters() >= 0:
                temp_letters = self.getletters(self.num_available_letters())
                b = [x[:] for x in proposal]
                for i in range(0, len(temp_letters)):
                    b.append(temp_letters[i])
                self.sort_proposal(b)
                return b
        elif mode == 'paso' and self.num_available_letters() == prev_proposal_length:
            return -1

    def delete_letter(self, letter):
        """Αφαιρεί ένα γράμμα από το σακουλάκι"""
        if letter in self.letters:
            if self.letters[letter][0] > 1:
                self.letters[letter][0] = self.letters[letter][0] - 1
            elif self.letters[letter][0] == 1:
                del self.letters[letter]

    def getletters(self, N):
        """Επιστρέφει μια 2D λίστα Ν γραμμάτων με τις αξίες τους"""
        if N <= self.num_available_letters():
            temp_letter = [[0 for j in range(2)] for i in range(N)]
            for i in range(0, N):
                x = random.choice(list(self.letters))
                temp_letter[i][0] = x
                temp_letter[i][1] = self.letters.get(x)[1]
                self.delete_letter(x)
            return temp_letter
        else:
            return -1

    def putbackletters(self, proposal):
        """Επιστρέφει τα γράμματα μιας πρότασης στο σακουλάκι"""
        for i in range(0, len(proposal)):
            if proposal[i][0] in self.letters:
                self.letters.get(proposal[i][0])[0] = self.letters.get(proposal[i][0])[0] + 1
            else:
                self.letters[proposal[i][0]] = [1, proposal[i][1]]
        self.reset_proposal(proposal)

    def randomize_sak(self):
        """Τυχαιοπεί των αριθμό και τις αξίες κάθε γράμματος μέσα στα αντίστοιχα όρια"""
        for i in list(self.letters.keys()):
            self.letters.get(i)[0] = random.randint(1, 3)
            self.letters.get(i)[1] = random.randint(1, 10)

    def print_letters(self):
        """Εκτυπώνει τα γράμματα που βρίσκονται στο σακουλάκι"""
        print(self.letters)


class Player:
    def __init__(self, name):
        """Αρχικοποιεί την κλάση Player"""
        self.name = name
        self.score = 0
        self.correct_answers = 0

    def __repr__(self):
        """Επιστρέφει ένα string σαν αναπαράσταση του αντικειμένου"""
        rep = 'Player(' + str(self.name) + ',' + str(self.score) + ',' + str(self.correct_answers) + ')'
        return rep


class Human(Player):
    def __init__(self, name):
        """Αρχικοποιεί την κλάση Human"""
        super().__init__(name)

    def __repr__(self):
        """Επιστρέφει ένα string σαν αναπαράσταση του αντικειμένου"""
        rep = 'Human(' + str(self.name) + ',' + str(self.score) + ',' + str(self.correct_answers) + ')'
        return rep

    def play(self, sak):
        """Υλοποιεί το παιχνίδι όσο παίζει ο χρήστης"""
        print('*****************************')
        print('Παίκτης: ' + str(self.name) + '\t\tΣκορ: ' + str(self.score))
        z = len(sak.player_proposal)
        sak.player_proposal = sak.make_proposal(sak.player_proposal, 'vrhke', z)
        if Game.checkIFgameAlive(sak.player_proposal):
            Game.gameIsalive[0] = False
            Game.end()
            return -10
        else:
            print('Γράμματα:  ' + str(sak.player_proposal))
            print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
            print('Μπορείς να γράψεις λέξη (μόνο κεφαλαία ελληνικά χωρίς τόνους), διαφορετικά γράψε (p) για πάσο ή (q) για έξοδο.')
            while True:
                word = input('ΛΕΞΗ: ')
                if word == 'q':
                    print('Εγκατέλειψες το παιχνίδι.')
                    Game.end()
                    Game.gameIsalive[0] = False
                    break
                elif word == 'p':
                    print('Έκανες Πάσο!')
                    z = len(sak.player_proposal)
                    sak.putbackletters(sak.player_proposal)
                    sak.player_proposal = sak.make_proposal(sak.player_proposal, 'paso', z)
                    if Game.checkIFgameAlive(sak.player_proposal):
                        Game.gameIsalive[0] = False
                        Game.end()
                        break
                    print('Νέα Γράμματα:  ' + str(sak.player_proposal))
                    print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
                    Game.humanTurn[0] = False
                    Game.pcTurn[0] = True
                    break
                elif word in Game.dictionary:
                    if Game.valid_via_proposal(word, sak.player_proposal):
                        self.score = self.score + Game.dictionary[word]
                        print('Πόντοι Λέξης= ' + str(Game.dictionary[word]) + '     Νέο Σκορ: ' + str(self.score))
                        self.correct_answers = self.correct_answers + 1
                        for i in list(word):
                            for j in range(0, len(sak.player_proposal)):
                                if i == sak.player_proposal[j][0]:
                                    sak.player_proposal.pop(j)
                                    break
                        z = len(sak.player_proposal)
                        sak.player_proposal = sak.make_proposal(sak.player_proposal, 'vrhke', z)
                        if Game.checkIFgameAlive(sak.player_proposal):
                            Game.gameIsalive[0] = False
                            Game.end()
                            break
                        print('Νέα Γράμματα:  ' + str(sak.player_proposal))
                        print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
                        Game.humanTurn[0] = False
                        Game.pcTurn[0] = True
                        break
                    else:
                        print(
                            'Η Λέξη που έδωσες δεν ταιριάζει με τα γράμματα που έχεις διαθέσιμα! Προσπάθησε ξανά.')
                else:
                    print('Η λέξη που έδωσες δεν υπάρχει! Διάλεξε ξανά. ')
            if not Game.gameIsalive[0]:
                return -10


class Computer(Player):
    def __init__(self, name):
        """Αρχικοποιεί την κλάση Computer"""
        super().__init__(name)

    def __repr__(self):
        """Επιστρέφει ένα string σαν αναπαράσταση του αντικειμένου"""
        rep = 'Computer(' + str(self.name) + ',' + str(self.score) + ',' + str(self.correct_answers) + ')'
        return rep

    def play(self, sak, difficulty_level):
        """Υλοποιεί το παιχνίδι όσο παίζει ο Η/Υ"""
        print('*****************************')
        print('Παίκτης: ' + str(self.name) + '\t\tΣκορ: ' + str(self.score))
        z = len(sak.pc_proposal)
        sak.pc_proposal = sak.make_proposal(sak.pc_proposal, 'vrhke', z)
        if Game.checkIFgameAlive(sak.pc_proposal):
            Game.gameIsalive[0] = False
            Game.end()
            return -10
        else:
            print('Γράμματα:  ' + str(sak.pc_proposal))
            print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
            word = Game.make_move(difficulty_level, sak.pc_proposal)
            if word != -1:
                print('Παίζει τη Λέξη: ' + word)
                self.score = self.score + Game.dictionary[word]
                print('Πόντοι Λέξης= ' + str(Game.dictionary[word]) + '     Νέο Σκορ: ' + str(self.score))
                self.correct_answers = self.correct_answers + 1
                for i in list(word):
                    for j in range(0, len(sak.pc_proposal)):
                        if i == sak.pc_proposal[j][0]:
                            sak.pc_proposal.pop(j)
                            break
                z = len(sak.pc_proposal)
                sak.pc_proposal = sak.make_proposal(sak.pc_proposal, 'vrhke', z)
                if Game.checkIFgameAlive(sak.pc_proposal):
                    Game.gameIsalive[0] = False
                    Game.end()
                    return -10
                print('Νέα Γράμματα:  ' + str(sak.pc_proposal))
                print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
                Game.humanTurn[0] = True
                Game.pcTurn[0] = False
            else:
                print('Ο PC πήγε Πάσο!')
                z = len(sak.pc_proposal)
                sak.putbackletters(sak.pc_proposal)
                sak.pc_proposal = sak.make_proposal(sak.pc_proposal, 'paso', z)
                if Game.checkIFgameAlive(sak.pc_proposal):
                    Game.gameIsalive[0] = False
                    Game.end()
                    return -10
                print('Νέα Γράμματα:  ' + str(sak.pc_proposal))
                print('Απομένουν ' + str(sak.num_available_letters()) + ' γράμματα στο σακουλάκι.')
                Game.humanTurn[0] = True
                Game.pcTurn[0] = False


class Game:
    human = None
    computer = None
    dictionary = {}
    sak = None
    gameIsalive = [False]
    humanTurn = [False]
    pcTurn = [False]

    def __init__(self, difficulty_level):
        """Αρχικοποιεί την κλάση Game"""
        Game.gameIsalive[0] = True
        Game.humanTurn[0] = True
        Game.pcTurn[0] = False
        Game.sak = SakClass()
        Game.name = input('Δώστε το όνομα σας:')
        Game.human = Human(Game.name)
        Game.computer = Computer('Pc')
        Game.setup(difficulty_level)

    @classmethod
    def __repr__(cls):
        """Επιστρέφει ένα string σαν αναπαράσταση του αντικειμένου"""
        rep = 'Game: ' + str(Game.human.__repr__()) + ' , ' + str(Game.computer.__repr__()) + ')'
        return rep

    @classmethod
    def word_value(cls, word):
        """Υπολογίζει και επιστρέφει την αξία μιας λέξης"""
        x = list(word)
        value = 0
        for i in x:
            value = value + Game.sak.letters.get(i)[1]
        return value

    @classmethod
    def setup(cls, difficulty_level):
        """Τυχαιοποιεί το σακουλάκι, διαβάζει το λεξικό και καλεί τη μέθοδο run()"""
        Game.sak.randomize_sak()
        Game.read_dictionary()
        Game.run(difficulty_level)

    @classmethod
    def read_dictionary(cls):
        """Διαβάζει το αρχείο greek7.txt και το αποθηκεύει σε ένα λεξικό"""
        try:
            with open("greek7.txt", "r", encoding="utf8") as file:
                for line in file:
                    Game.dictionary[line.strip('\n')] = Game.word_value(line.strip('\n'))
        except:
            print('--------------------')
            print('Σφάλμα κατά το άνοιγμα του αρχείου.')
            print('--------------------')
        else:
            print('--------------------')
            print('Το λεξικό φορτώθηκε επιτυχώς!')
            print('--------------------')
        file.close()

    @classmethod
    def valid_via_proposal(cls, word, proposal):
        """Εξετάζει αν μια λέξη που δίνει ο χρήστης είναι συμβατή με τα γράμματα που του προσφέρονται"""
        temp = [x[:] for x in proposal]
        letters_matched = 0
        for i in list(word):
            for j in range(0, len(proposal)):
                if i == temp[j][0]:
                    letters_matched = letters_matched + 1
                    temp[j][0] = '0'
                    break
        if letters_matched == len(word):
            return True
        else:
            return False

    @classmethod
    def end(cls):
        """Τελειώνει το παιχνίδι και κάνει της κατάλληλες εγγραφές στο αρχείο"""
        print('Το παιχνίδι τελείωσε!')
        if Game.human.score > Game.computer.score:
            print('Ο παίκτης ' + str(Game.human.name) + ' κέρδισε!')
            print('Το Σκορ ήρθε ' + str(Game.human.score) + ' έναντι ' + str(Game.computer.score) + '.')
            print('*****************************')
            winner = str(Game.human.name)
            loser = str(Game.computer.name)
            winner_answers = str(Game.human.correct_answers)
            loser_answers = str(Game.computer.correct_answers)
            winner_score = str(Game.human.score)
            loser_score = str(Game.computer.score)
        elif Game.human.score < Game.computer.score:
            print('Ο παίκτης ' + str(Game.computer.name) + ' κέρδισε!')
            print('Το Σκορ ήρθε ' + str(Game.computer.score) + ' έναντι ' + str(Game.human.score) + '.')
            print('*****************************')
            winner = str(Game.computer.name)
            loser = str(Game.human.name)
            winner_answers = str(Game.computer.correct_answers)
            loser_answers = str(Game.human.correct_answers)
            winner_score = str(Game.computer.score)
            loser_score = str(Game.human.score)
        else:
            print('Το παιχνίδι έληξε ισοπαλία!')
            print('Το Σκορ ήρθε ' + str(Game.computer.score) + ' - ' + str(Game.human.score) + '.')
            print('*****************************')
            winner = 'και οι δύο'
            loser = 'κανείς'
            winner_answers = str(Game.computer.correct_answers)
            loser_answers = ''
            winner_score = str(Game.computer.score)
            loser_score = ''

        dictionary = {
            "winner": winner,
            "loser": loser,
            "winner_score": winner_score,
            "loser_score": loser_score,
            "winner_answers": winner_answers,
            "loser_answers": loser_answers,
        }
        try:
            with open("sample.txt", "a") as outfile:
                json.dump(dictionary, outfile)
                outfile.write("\n")
        except:
            print('--------------------')
            print('Σφάλμα κατά το γράψιμο του αρχείου sample.txt.')
            print('--------------------')
        else:
            print('--------------------')
            print('Το sample.txt εγγράφη επιτυχώς!')
            print('--------------------')
        outfile.close()

    @classmethod
    def checkIFgameAlive(cls, proposal):
        """Εξετάζει αν το παιχνίδι πρέπει να συνεχιστεί ή να τελειώσει"""
        if proposal == -1:
            return True
        else:
            return False

    @classmethod
    def run(cls, difficulty_level):
        """Εκτελεί το παιχνίδι με σειρά χρήστης-PC-χρήστης έως ότου ικανοποιηθούν συνθήκες τερματισμού"""
        while Game.gameIsalive[0]:
            if Game.humanTurn[0]:
                t = Game.human.play(Game.sak)
                if t == -10:
                    break
            if Game.pcTurn[0]:
                t = Game.computer.play(Game.sak, difficulty_level)
                if t == -10:
                    break

    @classmethod
    def make_move(cls, choice, proposal):
        """Καλεί τον κατάλληλο αλγόριθμο ανάλογα με τη δυσκολία που έχει επιλεγεί"""
        if choice == 1:
            word = Game.minLetters(proposal)
            return word
        if choice == 2:
            word = Game.maxLetters(proposal)
            return word
        if choice == 3:
            word = Game.smartLetters(proposal)
            return word

    @classmethod
    def minLetters(cls, proposal):
        """Ο αλγόριθμος minLetters βρίσκει και επιστρέφει μια λέξη ή -1 αν δε βρει"""
        temp = ['' for x in range(len(proposal))]
        for i in range(0, len(proposal)):
            temp[i] = proposal[i][0]

        for x in range(2, len(proposal) + 1):
            for i in it.permutations(temp, x):
                word = "".join(i)
                if word in Game.dictionary:
                    return word
        return -1

    @classmethod
    def maxLetters(cls, proposal):
        """Ο αλγόριθμος maxLetters βρίσκει και επιστρέφει μια λέξη ή -1 αν δε βρει"""
        temp = ['' for x in range(len(proposal))]
        for i in range(0, len(proposal)):
            temp[i] = proposal[i][0]

        for x in range(len(proposal), 1, -1):
            for i in it.permutations(temp, x):
                word = "".join(i)
                if word in Game.dictionary:
                    return word
        return -1

    @classmethod
    def smartLetters(cls, proposal):
        """Ο αλγόριθμος smartLetters βρίσκει και επιστρέφει μια λέξη ή -1 αν δε βρει"""
        temp = ['' for x in range(len(proposal))]
        for i in range(0, len(proposal)):
            temp[i] = proposal[i][0]

        max_value = 0
        max_word = ''
        for x in range(2, len(proposal) + 1):
            for i in it.permutations(temp, x):
                word = "".join(i)
                if word in Game.dictionary:
                    if Game.dictionary[word] > max_value:
                        max_value = Game.dictionary[word]
                        max_word = word
        if max_word == '':
            return -1
        else:
            return max_word
