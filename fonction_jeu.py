def cree_main_joueur(deck1,deck2):
    main1 = []
    main2 = []
    pioche1 = []
    pioche2 = []


    for a in range (5):
        main1.append(deck1.pop(deck1.index(0)))
        main2.append(deck2.pop(deck2.index(0)))

    for b in range (15):
        pioche1.append(deck1.pop(deck1.index(0)))
        pioche2.append(deck2.pop(deck2.index(0)))

    test_main(main1,main2)
    test_pioche(pioche1,pioche2)
    





def test_main(main1,main2):
    print("main joueur 1 : ",main1)
    print(len(main1))

    print("main joueur 2 : ", main2)
    print(len(main2))


def test_pioche(pioche1,pioche2):
    print("pioche du joueur 1 : ", pioche1)
    print(len(pioche1))

    print("pioche du joueur 2 : ",pioche2)
    print(len(pioche2))

