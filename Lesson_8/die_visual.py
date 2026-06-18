import plotly.express as px
from die import Die

# ROLLING ONE DICE
# ==================================================
# Create a 6 sided dice.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)

# # Customize the plot
# title = "Results of Rolling One D6 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Render the resulting chart as an HTML file 
# and open that file in a new browser tab
fig.show()


# ROLLING TWO DICE
# ==================================================
# # Create two D6 dice.
# die_1 = Die()
# die_2 = Die()

# # Make some rolls, and store results in a list.
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_result+1)

# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results.
# title = "Results of Rolling Two D6 Dice 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# # Further customize chart.
# fig.update_layout(xaxis_dtick=1)

# fig.show()

# TODO: Refactor rolling two dice to make one dice a 10-sided dice
#       And change the roll amount to 50,000 instead of 1,000
#       Change the title to reflect the change

# TODO: Replace fig.show() with fig.write_html('dice_visual_d6d10.html')