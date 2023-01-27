import turtle 
import pandas 

screen = turtle.Screen()
screen.title("U.S. States Game")

#Creating a new shape using an image

image = ("blank_states_img.gif")
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")
#Turning column of data into a list 
all_states = data["state"].to_list()
guessed_states = []

counter = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{counter}/50", prompt = "Guess another state's name").title()


    print(answer_state)

    # If answer state is a state in csv 
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break 
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
    
    #pull out row of answer state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
        counter +=1






