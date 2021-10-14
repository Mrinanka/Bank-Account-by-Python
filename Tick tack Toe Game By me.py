#!/usr/bin/env python
# coding: utf-8

# In[40]:


from IPython.display import clear_output

def display_board(board):
    
    
    
    
    
    
    print("      "+'|' +"      "+'|'+"      ")
    
    print('  '+board[1]+'   |   '+board[2]+'  |   '+board[3])
    
    print("______"+'|'+"______"+'|'+"______")
    print("      "+'|' +"      "+'|'+"      ")
    
    print('  '+board[4]+'   |   '+board[5]+'  |   '+board[6])
    
    print("______"+'|'+"______"+'|'+"______")
    print("      "+'|' +"      "+'|'+"      ")
    
    print('  '+board[7]+'   |   '+board[8]+'  |   '+board[9])
    
    print("      "+'|' +"      "+'|'+"      ")


# In[41]:


def player_input():
    
    marker='A'
    while marker not in ['X','O']:
        marker=input("Choose What Do You Want To Be! ('X' or 'O')   :\n")
        marker=marker.upper()
        clear_output()
        if marker not in ['X','O']:
            print("'Ops!' You did not choose it right.\n Try again")
            
        
    if marker=='X':
        return ['X','O']
    else:
        return ['O','X']


# In[42]:


def place_marker(board, marker, position):
    
    board[position]=marker
    return board


# In[43]:


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[44]:


import random

def choose_first():
    
    x=random.randint(1,2)
    if x==1:
        
        return ['Player 1','Player 2']
    else:
        
        return ['Player 2','Player 1']


# In[45]:


def space_check(board, position):
    
    return board[position]==' '
    


# In[46]:


def full_board_check(board):
    space=False
    for i in range(1,10):
        if ' ' in board :
            return False
            
        
        
        else:
            return True
    
    


# In[47]:


def player_choice(board):
    
     
    pos=11
    while pos not in range(1,10) or not space_check(board, pos):
        pos=input("enter a position of your choice : 1-9 \n")
        pos=int(pos)
        clear_output()
        if pos not in range(1,10):
            print("'Ops!' Try a valid number.\n Try again")
            
    
        if not space_check(board, pos):
            print("Opz! That place is already filled \n Try another")
    
    return pos
   
            

    


# In[48]:


def replay():
    want='A'
    while want not in ['Y','N']:
        want=input("Do u want to play again?  Y or N")
        want=want.upper()
        clear_output()
        if want not in ['Y','N']:
            print("Hey thats not what i asked")
    if want=='Y':
        return True
    else:
        return False


# In[ ]:


print('Welcome to Tic Tac Toe!')


while True:
    theboard=[' ']*10
    display_board(theboard)
    
    mark=player_input()
    player=choose_first()
    print("You are randomly chosen to be " + player[0] + " And you have choosen "+ mark[0]+ " Good luck!")
    
    game_on=True

    while game_on:
        print(" Now put your "+mark[0])
        pos=player_choice(theboard)
        theboard=place_marker(theboard, mark[0], pos)
        
        clear_output()
        
        display_board(theboard)
        
        worn=win_check(theboard, mark[0])
        if worn:
            print("Congratulations "+player[0]+ "! \n You have defeated " +player[1])
            break
        else:
            pass
        space=full_board_check(theboard)
        if space:
            print('This is a Tie')
            break
        else:
            pass
    
        # Player2's turn.
        print(player[1]+"'s Turn, put your "+mark[1])
        pos=player_choice(theboard)
        theboard=place_marker(theboard, mark[1], pos)
        
        clear_output()
        
        display_board(theboard)
        
        worn=win_check(theboard, mark[1])
        if worn:
            print("Congratulations "+player[1]+ "! \n You have defeated " +player[0])
            break
        else:
            pass
        space=full_board_check(theboard)
        if space:
            print('This is a Tie')
            break
        else:
            pass    
            

            
            
            
    if not replay():
        break


# In[ ]:





# In[ ]:





# In[ ]:




