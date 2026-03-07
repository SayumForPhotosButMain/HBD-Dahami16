import matplotlib.pyplot as plt

def plot_sayum():
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Define coordinate sets for each letter
    # Each entry is a list of tuples: (x_coordinates, y_coordinates)
    letters = {
        'S': [([1, 0, 0, 1, 1, 0], [2, 2, 1, 1, 0, 0])],
        'A': [([0, 0.5, 1], [0, 2, 0]), ([0.25, 0.75], [1, 1])],
        'Y': [([0, 0.5], [2, 1]), ([1, 0.5], [2, 1]), ([0.5, 0.5], [1, 0])],
        'U': [([0, 0, 1, 1], [2, 0, 0, 2])],
        'M': [([0, 0, 0.5, 1, 1], [0, 2, 1, 2, 0])]
    }
    
    word = "SAYUM"
    spacing = 1.5  # Horizontal distance between letters
    
    for i, char in enumerate(word):
        offset = i * spacing
        if char in letters:
            for x_coords, y_coords in letters[char]:
                # Apply the offset to the x-coordinates for each letter
                ax.plot([x + offset for x in x_coords], y_coords, color='blue', linewidth=3)
    
    # Formatting the graph
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes for a cleaner look
    ax.set_title("SAYUM Graph", fontsize=20)
    
    plt.savefig('sayum_graph.png')
    plt.show()

# Call the function
plot_sayum()