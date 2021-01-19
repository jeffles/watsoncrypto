import itertools
import random

_end = '_end_'


def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word.lower():
            if letter not in ("abcdefghijklmnopqrstuvwxyz"):
                continue
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root


def make_sorted_trie(words):
    root = dict()
    for word in words:
        word = "".join(sorted(word))
        current_dict = root
        for letter in word.lower():
            if letter not in ("abcdefghijklmnopqrstuvwxyz"):
                continue
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root


def in_trie(trie, word):
    current_dict = trie
    word = word.lower()
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict


def crack(eng_word_list, words):
    print(f'\n---------------\nTrying to crack the list {words}')
    sorted_trie = make_sorted_trie(eng_word_list)
    trie = make_trie(eng_word_list)
    # print(trie)
    my_letter = ''
    for x in "abcdefghijklmnopqrstuvwxyz":
        found = 0
        for word in words:
            test = word + x
            test = "".join(sorted(test))
            if in_trie(sorted_trie, test):
                my_letter = x
                found += 1
                # print(word, x)
        if found == len(words):
            print('The right letter is', my_letter)

            # print(trie)
            for word in words:
                perms = itertools.permutations(word + my_letter)
                for w in perms:
                    # print("".join(word))
                    if in_trie(trie, "".join(w)):
                        print("".join(w))
                        break

import collections
import string

def my_print(mapping, text):
    for w in text:
        if w in string.ascii_uppercase:
            print(mapping[w], end='')
        else:
            print(w, end='')
    print()

def solve_cryptogram(text):
    text = text.upper()
    letter_frequency = list('etaoinsrhdlucmfywgpbvkxqjz')
    print(text)
    mapping = {}
    char_counter = collections.Counter(text)
    for char, count in char_counter.most_common():
        if char in string.ascii_uppercase:
            # print(char, count)
            mapping[char] = letter_frequency.pop(0)

    my_print(mapping, text)
    while True:
        x = input("Enter command: (help)")
        if x == "help":
            print("print - display message")
            print("a/b - swap a and b")
            print("random - randomize the letters")
        elif x == "print":
            my_print(mapping, text)
        elif x == "q" or x == "quit":
            return
        elif x == "r" or x == "random":
            for one in mapping.keys():
                two = random.choice(list(mapping.keys()))
                if mapping[one] in string.ascii_lowercase and mapping[two] in string.ascii_lowercase:
                    (mapping[one], mapping[two]) = (mapping[two], mapping[one])
            my_print(mapping, text)
        elif len(x) > 1 and x[1] == "/":
            print("SWAP")
            k1 = -1
            k2 = -1
            for (k, i) in mapping.items():
                if x[0] == i:
                    k1 = k
                if x[2] == i:
                    k2 = k
            if k1 == -1:
                mapping[k2] = x[0]
            elif k2 == -1:
                mapping[k1] = x[2]
            else:
                (mapping[k1], mapping[k2]) = (mapping[k2], mapping[k1])
            my_print(mapping, text)
    print()







if __name__ == '__main__':
    data = []
    with open('words.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().lower())
    # crack(data, ['aroma', 'trance', 'foaming', 'amicus'])
    # crack(data, ['sine', 'primers', 'learn', 'micas'])
    # crack(data, ['mentor', 'pianos', 'repeal', 'cruelly'])
    # crack(data, ['parcel', 'reseated', 'pilfer', 'unit'])
    # solve_cryptogram("NAP ZPNPVNORP'L LOFAJNQKP VJBJGJLE DODP TJL DCDQBJKOYPZ GW TOBBOJM "
    #                  "FOBBPNNP, TEC DBJWPZ ECBMPL CA LNJFP OA NEP BJNP 1800L JAZ PJKBW 1900L.\n"
    #                  "LOZAPW DJFPN'L OBBQLNKJNOCAL LECTPZ NEP LBPQNE TONE J LNKJOFEN DODP, "
    #                  "GQN FOBBPNNP QLPZ J VQKRW VJBJGJLE DODP, J ZPNJOB NEJN BJLNPZ OA NEP ZPVJZPL NEJN HCBBCTPZ")
    # solve_cryptogram("NMZ JDYZK LNKZZN LNFG FE NMZ AFEVFE OEVZKHKFOEV MDL NRAZL NMDN LMFS NMZ "
    #                  "LRAMFOZNNZ FC NMZ BFLN CDBFOL (RC CRPNRFEDA) KZLRVZEN FC NMDN LNKZZN. "
    #                  "EZDKJW RL D BOLZOB VZQFNZV NF NMZ BDE DEV MRL SFKY.")
    # solve_cryptogram("C.C. CLHIBR VGRK'S G JDYSDLKGH NBSBYSDUB -- CB VGR G RBQDGH FDHHBQ, LJSBK "
    #                  "YLKRDNBQBN SCB JDQRS DK GIBQDYG. PLQK CBQIGK VBPRSBQ ITNABSS DK 1861, \n"
    #                  "CB YLKJBRRBN SL 27 ITQNBQR PTS IGX CGUB PBBK QBRMLKRDPHB "
    #                  "JLQ ILQB. CB VGR GHRL G PDAGIDRS, IGQQDBN SL SCQBB VLIBK GS SCB SDIB LJ CDR NBGSC.")

    # solve_cryptogram("KWDGDWCK RGJ CWKLZJVGOK VDPAOFZ KZPJZL, ZDVMCYLVP, ROJLVQZ, KTYFGSW, PJWHLVP, YDF PAYDFZKLVDZ.")
    # solve_cryptogram("pzljh zghfiljadkh vkk avpwkm ldk bpejni mklkzlfok fy ldk 1963 ejofk IDKHVJZR DJVEKI "
    #                  "PYM LDK MKPMVW YKZRVPZK.\n FY 1970, VKK AVPWKM P DJVEKI PCPFY - IDKHVJZR'I UHJLDKH EWZHJBL, "
    #                  "FY LDK EJOFK LDK AHFOPLK VFBK JB IDKHVJZR DJVEKI.\n DK DPN PVIJ AVPWKM IFH "
    #                  "DKYHW UPIRKHOFVVK FY PY KPHVFKH BFVE PMPALKM BHJE LDK DJNYM JB LDK UPIRKHOFVVKI.")
    # solve_cryptogram("PA KNV 1930J, BVAHFDP OIPKVI JNFIFQPAQL BFAQXCEFQNXFX PAKICQLTVQ F TNFIFTKVI "
    #                  "AFSVQ BXCSWVJN BFWJNP, ONC JCDMVQ SXJKVIPVJ BLK EIVZVIIVQ KNV KVIS \"KILKN - JVVWVI\""
    #                  " KC QVKVTKPMV.\n KNV TNFIFTKVI FEEVFIVQ PA 32 JKCIPVJ PA KNV QVTFQVJ KNFK ZCDDCOVQ, "
    #                  "FAQ PAJEPIVQ F KVDVMPJPCA JNCO FAQ JVMVIFD SCMPVJ.\n NV'J BVVA TFDDVQ \"KNV PAQPFA JNVIDCTW NCDSVJ.\"")
    # solve_cryptogram("XQOT QDJMHI EQPK BYQTKN EMYXKI, QON XQOT EQPK BYQTKN RQJIMO - ZLJ ZHGJGIE QDJMH "
    #                  "BQJHGDA XQDOKK RQI MOK MU JEK UKR JM BYQT ZMJE HMYKI NLHGOV Q YMOV DQHKKH!\n"
    #                  "EK BYQTKN JEK DEQHQDJKH MU RQJIMO MBBMIGJK HMVKH XMMHK QON DEHGIJMBEKH YKK.\n"
    #                  "qon jm dqb gj muu, go 1984, ek byqtkn q deqhqdjkh mo jek JKYKPGIGMO IEMR "
    #                  "XQVOLX B.G. REM EQN Q NKYLIGMO JEQJ EK RQI IEKHYMDA EMYXKI.")
    solve_cryptogram("VITIDN LTIRR AEMNIJ RXI SEIQRX WC M EBCY-TQCCWCY RIEIPWSWBC SITWIS ATBJQKIJ "
                     "LN YTMCMJM RIEIPWSWBC WC RXI IWYXRWIS MCJ CWCIRWIS.\n "
                     "ZBTRN-RGB BZ MTRXQT KBCMC JBNEI'S SRBTWIS GITI MJMARIJ"
                     " ZBT RXI SITWIS, MCJ RXI SITWIS XMJ M TIAQRMRWBC ZBT LIWCY ZMWRXZQE RB"
                     " RXI LBBFS.\n LTIRR XMJ MKRQMEEN AEMNIJ GMRSBC WC 1980, MKTBSS ZTBD KXMTERBC XISRBC'S XBEDIS.")
