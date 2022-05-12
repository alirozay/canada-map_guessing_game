import pandas
import turtle
from score_writer import Score_Writer

writer = Score_Writer()
score = 0
tries = 0
user_guess = []
data = pandas.read_csv("10_Provinces_and_3_Territories.csv")
answer_list = data["provinces"].to_list()
screen = turtle.Screen()
screen.title("Canada Provinces Game")
image = "blank_provinces_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
# data_dict = {"provinces": ["Yukon", "Northwest Territories", "Nunavut",
#                            "British Columbia", "Alberta",
#                            "Saskatchewan", "Manitoba", "Ontario", "Quebec",
#                            "New Brunswick", "Nova Scotia", "PEI",
#                            "Newfoundland and Labrador"],
#              "x": [-253.0, -170.0, -51.0, -248.0, -181.0, -121.0, -60.0, 16.0,
#                    136.0, 207.0, 239.0, 233.0, 196.0],
#              "y": [68.0, 32.0, 24.0, -73.0, -88.0, -114.0, -112.0, -146.0,
#                    -126.0, -154.0, -159.0, -143.0, -51.0]
#              }


# def get_mouse_click_coor(x, y):
#     data_dict["x"].append(x)
#     print(data_dict['x'])
#     data_dict["y"].append(y)
#     print(data_dict['y'])
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# provinces_data = pandas.DataFrame(data_dict)
# provinces_data.to_csv("10_Provinces_and_3_Territories.csv")
# turtle.mainloop()
while score < 13 and tries < 3:
    user_answer = screen.textinput(
        title=f"{score} out of {len(answer_list)} found",
        prompt="Make a guess").title()
    if user_answer == "Exit":
        break
    if user_answer in answer_list:
        user_guess.append(user_answer)
        score += 1
        x = int(data[data["provinces"] == user_answer]["x"])
        y = int(data[data["provinces"] == user_answer]["y"])
        writer.type(x=x, y=y, answer=user_answer)
        screen.update()
    elif user_answer not in answer_list and user_answer not in user_guess:
        tries += 1

not_found = list(set(answer_list) - set(user_guess))
not_found = pandas.Series(not_found)
not_found.to_csv("answers_not_found")
