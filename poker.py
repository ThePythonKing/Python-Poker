#!/usr/bin/env python3

import ramdom
from intertools import groupby
#note:
nine=1, ten=2, jack=3, queen=4, king=5, ace=6
note:#
names= (nine:"9",ten:"10",jack:"J",queen:"Q",king:"K", ace:"A")
#initiates the score at zero
player_score=0, computer_score=0

def score():
    global player_score, computer_score
    print "HIGH SCORES"
    print "Player:", player_score
    print "Computer:"computer_score
if __name__ =='__main__':
    start()
    
