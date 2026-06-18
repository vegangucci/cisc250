import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk()
    # Option: Increase the number of points to 50,000
    # rw = RandomWalk(50_000)
    rw.fill_walk()
    
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    # Option for 50,000: change figure size to 15 inches x 9 inches
    # fig, ax = plt.subplots(figsize=(15, 9))
    # Option for 50,000: adjusting dpi from default 100 to 128
    # fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # ax.scatter(rw.x_values, rw.y_values, s=15)
    # style each point with a color map
    # Set edgecolors='none' to get rid of the black outline around each point
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, 
               rw.y_values, 
               c=point_numbers, 
               cmap="Blues", 
               edgecolors='none', 
               s=15)
    # Option for 50,000: change point size to 1
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap="Blues", edgecolors='none', s=1)
    
    # specify that both axes should have equal spacing between tick marks
    ax.set_aspect('equal')
    
    # Emphasize the first and last points. 
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Remove the axes. TODO: Uncomment two following lines
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Press any key to make another walk? (Type 'n' to exit): ")
    if keep_running == 'n':
        break

plt.close('all') # Explicitly tears down remaining GUI hooks
