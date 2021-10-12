def isPalindrome(number):
    '''
    Determina daca un numar este palindrom.
    :param number: numarul dat , int
    :return: True, daca numarul este palindrom, False, in caz contrar
    '''
    clone_number = number
    inverted_number = 0
    if number // 10 == 0:
        return True
    while clone_number != 0:
        inverted_number = inverted_number * 10 + clone_number % 10
        clone_number = clone_number // 10
    if inverted_number == number:
        return True
    else:
        return False


def test_isPalindrome():
    assert isPalindrome(12321) is True
    assert isPalindrome(21212) is True
    assert isPalindrome(1234124) is False
    assert isPalindrome(2) is True


def citirelista():
    list = []
    givenString = input("Dati elemtele listei, separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        list.append(int(x))
    return list


def is_all_elements_palindromes(list):
    if len(list) == 0:
        return False
    for x in list:
        if isPalindrome(x) == False:
            return False
    return True


def test_is_all_elements_palindromes():
    assert is_all_elements_palindromes([121, 232, 1221, 4452]) is False
    assert is_all_elements_palindromes([]) is False
    assert is_all_elements_palindromes([123, 75, 985]) is False
    assert is_all_elements_palindromes([7557, 555]) is True


def get_longest_all_palindromes(list):
    '''
    Determina cea mai lunga subsecventa de numere palindroame.
    :param list: lista data, int.
    :return: cea mai lunga subsecventa de numere palindroame, int.
    '''
    subsecventaMax = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if is_all_elements_palindromes(list[i:j+1]) and len(subsecventaMax) < len(list[i:j+1]):
                subsecventaMax = list[i:j+1]
    return subsecventaMax


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([1, 2, 3]) == [1, 2, 3]
    assert get_longest_all_palindromes([121, 24, 232, 434, 535, 21, 747, 1221]) == [232, 434, 535]


def isPower(nr ,k):
    '''
    Verifica daca un numar se poate scrie ca x**k.
    :param nr: numarul pe care il verificam, int
    :param k: puterea lui x, int.
    :return: True, daca un numar se poate scrie ca x**k sau False, in caz contrar.
    '''
    x = 1
    while x**k <= nr:
        if x**k == nr:
            return True
        x = x + 1
    return False


def test_isPower():
    assert isPower(8, 3) is True
    assert isPower(9, 2) is True
    assert isPower(1,10) is True
    assert isPower(2, 3) is False


def is_all_elemnts_at_k_power(list, k):
    '''
    Determina daca toate elementele unei liste se pot scrie ca x^k.
    :param list: lista de numere intregi.
    :param k: puterea , int.
    :return: True, daca toate elementele unei liste se pot scrie ca x^k sau False, in caz contrar.
    '''
    if len(list) == 0:
        return False
    for x in list:
        if isPower(x, k) == False:
            return False
    return True


def test_is_all_elemnts_at_k_power():
    assert is_all_elemnts_at_k_power([], 10) is False
    assert is_all_elemnts_at_k_power([4, 9, 16], 2) is True
    assert is_all_elemnts_at_k_power([1, 8, 27, 64], 3) is True
    assert is_all_elemnts_at_k_power([1, 2, 3, 4], 5) is False


def get_longest_powers_of_k(list, k):
    '''
    Determina cea mai lunga subsecventa de numere care se pot scrie ca x^k.
    :param list:lista data, int.
    :param k: puterea data, int.
    :return: cea mai lunga subsecventa de numere care se pot scrie ca x^k.
    '''
    subsecventaMax = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if is_all_elemnts_at_k_power(list[i:j+1], k) and len(subsecventaMax) < len(list[i:j+1]):
                subsecventaMax = list[i:j+1]
    return subsecventaMax


def test_get_longest_powers_of_k():
   assert get_longest_powers_of_k([4, 9, 16, 3, 5], 2) == [4, 9, 16]
   assert get_longest_powers_of_k([1, 8, 27, 64, 5, 7, 1, 8, 27], 3) == [1, 8, 27, 64]
   assert get_longest_powers_of_k([1, 2, 3, 4], 1) == [1, 2, 3, 4]
   assert get_longest_powers_of_k([], 5) == []


def all_tests_functions():
    test_isPalindrome()
    test_is_all_elements_palindromes()
    test_get_longest_all_palindromes()
    test_isPower()
    test_is_all_elemnts_at_k_power()
    test_get_longest_powers_of_k()


def printMenu():
    print("1.Citire lista.")
    print("2.Determina cea mai lunga subsecventa de numere palindroame.")
    print("3.Determina cea mai lunga subsecventa de numere care se pot scrie ca x**k, k citit, x întreg pozitiv.")
    print("X.Iesire.")


if __name__ == "__main__":
    all_tests_functions()
    list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            list = citirelista()
        elif optiune == "2":
           print(f'Cea mai lunga subsecventa de palindroame este: {get_longest_all_palindromes(list)}')
        elif optiune == "3":
            k = int(input("Dati k: "))
            print(f'Cea mai lunga subsecventa de numere care se pot scrie ca x^{k} este: {get_longest_powers_of_k(list, k)}')
        elif optiune == "X":
            break
        else:
            print("Optiune gresita! ")
