# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from black import Report


example1 = 'Ruud Gullit'
example2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = example1 + f' {goal_0}'+ ', ' + example2+f' {goal_1}'

report = example1 + f' scored in the {goal_0}' + 'nd minute' + '\n' + example2 + f' scored in the {goal_1}' + 'th minute'


player = 'Marco van Basten'
first_name = player[0: player.find(' ')]
last_name_len = len(player[player.index(' ')+1:])
name_short = player[0:1] + '. '+ player[player.index(' ')+1:]
chant = (first_name + '! ') * (len(first_name)-1) + first_name + '!'
good_chant = chant[-1] != ' '
