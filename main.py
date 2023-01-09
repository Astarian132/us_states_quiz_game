import turtle
import pandas
from states import State

# set path to your project location
PATH = 'Day_25\\project\\'



screen = turtle.Screen()
screen.title("U.S. States Game")
image = PATH + "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# method to get the coordinates on the map
"""def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

"""

all_states = pandas.read_csv(PATH + "50_states.csv")
num_of_states = all_states['state'].count()
correct_answers = 0
game_on = True
guessed_states = []
not_guessed_states = []

while game_on:
    answer_state = screen.textinput(title=f"{correct_answers}/{num_of_states} Guess the state", prompt="What's another state's name?")
    # include cases of improper spelling
    temp_answer = answer_state.split(' ')
    temp_answer = [ans.capitalize() for ans in temp_answer]
    answer_state = ' '.join(temp_answer)
    checked_state = all_states[all_states.state == answer_state]
    # way to exit the game
    if answer_state.capitalize() == 'Exit' or answer_state.capitalize() == 'Quit':
        game_on = False
    if not checked_state.empty:
        checked_state_dict = checked_state.to_dict('records')[0]
        if len(checked_state_dict.get('state')) > 0 and checked_state_dict.get('state') not in guessed_states:
            correct_answers += 1
            guessed_states.append(checked_state_dict.get('state'))
            State(checked_state_dict.get('x'), checked_state_dict.get('y'), checked_state_dict.get('state'))
            screen.update()
    # Victory condition
    if correct_answers == 50:
        State.victory()
        game_on = False
        screen.update()


# Ganerate not guessed states
all_states[~all_states['state'].isin(guessed_states)].to_csv(PATH + 'not_guessed.csv')

screen.exitonclick()

