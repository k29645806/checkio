game = [
    "X.O",
    "XX.",
    "XOO"]

game_1 = [
    "O.X",
    "XX.",
    "XOO"]


def checkio(game):
    for col in game:
        if len(set(col))==1 and col[0]!='.':
            return col[0]
            break

    transpose_game = zip(*game)
    for col in transpose_game:
        if len(set(col))==1 and col[0]!='.':
            return col[0]
            break

    line_LR = [game[0][0],game[1][1],game[2][2]]
    line_RL = [game[0][2],game[1][1],game[2][0]]
    if len(set(line_LR))==1 and game[0][0]!='.':
        return game[0][0]

    elif len(set(line_RL))==1 and game[0][2]!='.':
        return game[0][2]
    else:
        return 'D'



print checkio(game)

'''
def checkio(toe):

    chn = "".join(toe)
​
    sol = {"XXX", "OOO"}
    #Toutes les possibilités de victoires dans un tuple
    verif = (toe[0], toe[1], toe[2],
             chn[0::3], chn[1::3], chn[2::3],
             chn[0::4], chn[2::2][:-1])

    #Si l'intersection n'est pas nulle, alors il y a une victoire
    res = sol.intersection(verif)
    if res:
        #Renvoie "X" ou "O"
        return tuple(res)[0][0]
    else:
        return "D"
'''

'''
def checkio(g):
    if g[0][0]== g[1][1] == g[2][2] and g[1][1] in ['X','O']: return g[1][1]
    if g[0][2]== g[1][1] == g[2][0] and g[1][1] in ['X','O']: return g[1][1]
    for i in range(len(g)):
        if all(g[i][j] == g[i][0] for j in range(len(g))) and g[i][0]in ['X','O']: return g[i][0]
        elif all(g[j][i] == g[0][i] for j in range(len(g))) and g[0][i]in ['X','O']: return g[0][i]
        else: continue
    return 'D'
'''
