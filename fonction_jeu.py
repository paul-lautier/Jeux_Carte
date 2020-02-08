def cree_main_joueur(deck1,deck2):
    main1 = []
    main2 = []



    for a in range (5):
        main1.append(deck1.pop(a))
        main2.append(deck2.pop(a))


    test_main(main1,main2)
    
    


def cree_pioche(deck1,deck2):
    pioche1 = []
    pioche2 = []

    for b in range(15) :
        pioche1.append(deck1.pop(b))
        pioche2.append(deck2.pop(b))

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

