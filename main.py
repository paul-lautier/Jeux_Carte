import pygame 
import json
from creation_deck import *
from interface import * 



def main():
    main1, pioche1, main2, pioche2 = cree_deck()
    cree_ecran(main1, pioche1, main2, pioche2)
    # load_card_images(main1,main2)

    

    
    

main()