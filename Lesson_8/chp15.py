import matplotlib.pyplot as plt

# # Slide 6
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks


# # Slide 7: Improve the example
# squares = [num ** 2 for num in range(1,6)]
# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks

# # Slide 8
# input_values = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in range(1,6)]
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks

# Slide 9: Use builtin style
# input_values = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in range(1,6)]
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# # display all available styles
# for style in plt.style.available:
#     print(style)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks

# # Slide 11: Scatter Example
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks

# # Slide 12: Series of points with Scatter()
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()
# plt.close('all') # Explicitly tears down remaining GUI hooks


# Slide 13: Calculate Data automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)
# ax.scatter(x_values, y_values, color='red', s=10) # Slide 14
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10) # Slide 14
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # Slide 16
# ax.scatter(x_values, y_values, c=y_values, cmap='Blues', s=10) # Slide 16

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

ax.ticklabel_format(style='plain') # Slide 14: Tick label customization
plt.savefig('squares_plot.png', bbox_inches='tight') # Slide 17
plt.show()
plt.close('all') # Explicitly tears down remaining GUI hooks
