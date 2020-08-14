# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import time

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False  # 只要有任一字母未被猜中，说明还未猜出整个单词

    return True  # 所有字母都被猜中，代表整个单词已被猜出


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    guessed_word = ''  # 初始化为空字符串
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += '_ '  # 尚未猜中的字母用'_ '表示
        else:
            guessed_word += letter  # 已被猜中的字母直接显示

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    # available_letters: list
    available_letters = list(string.ascii_lowercase)  # 初始化为全部小写字母构成的列表
    for letter in letters_guessed:
        if letter in available_letters:
            available_letters.remove(letter)  # 将那些已猜中过的字母删除

    return ''.join(available_letters)  # 返回string


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    def isvowel(letter):
        '''
        letter: one single ahphabetical letter.
        returns: bollean, True if the letter is a vowel; False otherwise.
        '''
        if len(letter) == 1 and letter in 'aeiou':
            return True
        else:
            return False

    guesses_remaining = 6  # 剩余猜测次数
    warnings_remaining = 3  # 剩余警告次数
    letters_guessed = []  # list，已猜过的字母

    # 打印欢迎信息
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings_remaining, 'warnings'
          if warnings_remaining > 1 else 'warning', 'left.')
    print('----------------')

    # 当剩余次数为0或已经猜出单词时退出循环
    while guesses_remaining > 0 and not is_word_guessed(
            secret_word, letters_guessed):
        print('You have', guesses_remaining, 'guesses'
              if guesses_remaining > 1 else 'guess', 'left.')
        print('Available letters:', get_available_letters(letters_guessed))
        current_guess = input('Pleaes guess a letter: ').lower()  # 将输入转换为小写字母

        # 若输入的字符个数不为1，要求用户重试
        if len(current_guess) != 1:
            print('You must input exactly one letter! Try again.')
            print('----------------')
            continue

        # 检测输入要求（input requirements）
        # 输入的不是字母
        if not current_guess.isalpha():
            print('Opps! That is not a valid letter.', end=' ')
            if warnings_remaining > 0:  # 剩余警告次数不为0
                warnings_remaining -= 1
                print(
                    'You have',
                    warnings_remaining,
                    'warnings' if warnings_remaining > 1 else 'warning',
                    'left:',
                    end=' ')
            else:  # 剩余警告次数为0
                guesses_remaining -= 1
                print(
                    'You have no warnings left so you lose one guess:',
                    end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
        # 输入了一个曾经猜过的字母
        elif current_guess in letters_guessed:
            print('Oops! You have already guessed that letter.', end=' ')
            if warnings_remaining > 0:  # 剩余警告次数不为0
                warnings_remaining -= 1
                letters_guessed.append(current_guess)
                print(
                    'You have',
                    warnings_remaining,
                    'warnings' if warnings_remaining > 1 else 'warning',
                    'left:',
                    end=' ')
            else:  # 剩余警告次数为0
                guesses_remaining -= 1
                print(
                    'You have no warnings left so you lose one guess:',
                    end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
        # 输入的是新猜的字母
        else:
            letters_guessed.append(current_guess)  # 添加到已经猜过的字母列表
            if current_guess in secret_word:
                print('Good guess:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word:',
                      get_guessed_word(secret_word, letters_guessed))
                if isvowel(current_guess):
                    guesses_remaining -= 2  # 元音字母，剩余猜测次数减2
                else:
                    guesses_remaining -= 1  # 辅音字母，剩余猜测次数减1

        print('----------------')
        time.sleep(0.5)  # 提高交互体验的延迟

    # 退出循环后显示游戏结果
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * len(set(secret_word))  # 使用set来统计不重复字母的个数
        print('Congratulations, you won!')
        print('Your total score for this game is:', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was',
              '`' + secret_word + '`.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    my_word = my_word.replace(' ', '')  # 去除空格
    if len(my_word) != len(other_word):
        return False  # 长度不同，不匹配
    else:
        for i in range(len(my_word)):
            if my_word[i].isalpha() and my_word[i] != other_word[i]:
                return False  # 是已猜出的字母但不相同，不匹配
            if my_word[i] == '_' and other_word[i] in my_word:
                return False  # 是未猜出的下划线，但待匹配单词中有已猜出的字母，不匹配
        return True  # 其他情况都是匹配


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    # 遍历wordlist，找出所有与当前猜测所匹配的单词
    possible_maches = [
        word for word in wordlist if match_with_gaps(my_word, word)
    ]
    if len(possible_maches):
        for match in possible_maches:
            print(match, end=' ')
    else:
        print('No matches found')
    print()  # 换行


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    def isvowel(letter):
        '''
        letter: one single ahphabetical letter.
        returns: bollean, True if the letter is a vowel; False otherwise.
        '''
        if len(letter) == 1 and letter in 'aeiou':
            return True
        else:
            return False

    guesses_remaining = 6  # 剩余猜测次数
    warnings_remaining = 3  # 剩余警告次数
    letters_guessed = []  # list，已猜过的字母

    # 打印欢迎信息
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings_remaining, 'warnings'
          if warnings_remaining > 1 else 'warning', 'left.')

    # 当剩余次数为0或已经猜出单词时退出循环
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print('----------------')

        print('You have', guesses_remaining,
              'guesses' if guesses_remaining > 1 else 'guess', 'left.')
        print('Available letters:', get_available_letters(letters_guessed))
        current_guess = input('Pleaes guess a letter: ').lower()  # 将输入转换为小写字母

        # 若输入的字符个数不为1，要求用户重试
        if len(current_guess) != 1:
            print('You must input exactly one letter! Try again.')
            continue

        # 用户输入*号，显示游戏提示
        if current_guess == '*':
            print('Possible word matches are:')
            show_possible_matches(
                get_guessed_word(secret_word, letters_guessed))
            continue

        # 检测输入要求（input requirements）
        # 输入的不是字母
        if not current_guess.isalpha():
            print('Opps! That is not a valid letter.', end=' ')
            if warnings_remaining > 0:  # 剩余警告次数不为0
                warnings_remaining -= 1
                print('You have', warnings_remaining,
                      'warnings' if warnings_remaining > 1 else 'warning', 'left:', end=' ')
            else:  # 剩余警告次数为0
                guesses_remaining -= 1
                print(
                    'You have no warnings left so you lose one guess:',
                    end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
        # 输入了一个曾经猜过的字母
        elif current_guess in letters_guessed:
            print('Oops! You have already guessed that letter.', end=' ')
            if warnings_remaining > 0:  # 剩余警告次数不为0
                warnings_remaining -= 1
                letters_guessed.append(current_guess)
                print(
                    'You have',
                    warnings_remaining,
                    'warnings' if warnings_remaining > 1 else 'warning',
                    'left:',
                    end=' ')
            else:  # 剩余警告次数为0
                guesses_remaining -= 1
                print(
                    'You have no warnings left so you lose one guess:',
                    end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
        # 输入的是新猜的字母
        else:
            letters_guessed.append(current_guess)  # 添加到已经猜过的字母列表
            if current_guess in secret_word:
                print('Good guess:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word:',
                      get_guessed_word(secret_word, letters_guessed))
                if isvowel(current_guess):
                    guesses_remaining -= 2  # 元音字母，剩余猜测次数减2
                else:
                    guesses_remaining -= 1  # 辅音字母，剩余猜测次数减1

        time.sleep(0.5)  # 提高交互体验的延迟

    print('----------------')
    # 退出循环后显示游戏结果
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * len(
            set(secret_word))  # 使用set来统计不重复字母的个数
        print('Congratulations, you won!')
        print('Your total score for this game is:', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was',
              '`' + secret_word + '`.')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
