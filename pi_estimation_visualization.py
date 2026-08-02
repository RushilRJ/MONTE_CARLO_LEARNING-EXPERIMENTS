import random as rand
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ====================== SETTINGS ======================
num_points = 10000          

# Square boundaries
x_min, x_max = 5, 15
y_min, y_max = 15, 25

# Circle parameters
h, k, r = 25, 20, 10

# Playing field (where points are generated)
field_x_min, field_x_max = 5, 35
field_y_min, field_y_max = 10, 30
# ======================================================

# Lists to store points of different categories
square_x, square_y = [], []
circle_x, circle_y = [], []
both_x, both_y = [], []
outside_x, outside_y = [], []

square_count = 0
circle_count = 0

for _ in range(num_points):
    x = rand.uniform(field_x_min, field_x_max)
    y = rand.uniform(field_y_min, field_y_max)

    in_square = (x_min <= x <= x_max) and (y_min <= y <= y_max)
    in_circle = (x - h)**2 + (y - k)**2 <= r**2

    if in_square:
        square_count += 1
    if in_circle:
        circle_count += 1

    # Store points for visualization
    if in_square and in_circle:
        both_x.append(x)
        both_y.append(y)
    elif in_square:
        square_x.append(x)
        square_y.append(y)
    elif in_circle:
        circle_x.append(x)
        circle_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

# Estimate π
pi_estimate = circle_count / square_count if square_count > 0 else 0

# ====================== PLOTTING ======================
fig, ax = plt.subplots(figsize=(10, 8))

# Plot points
ax.scatter(outside_x, outside_y, color='lightgray', s=8, label='Outside', alpha=0.6)
ax.scatter(square_x, square_y, color='blue', s=10, label='Only Square')
ax.scatter(circle_x, circle_y, color='red', s=10, label='Only Circle')
ax.scatter(both_x, both_y, color='purple', s=12, label='Both (Overlap)')

# Draw the Square
square = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                           linewidth=2, edgecolor='blue', facecolor='none', label='Square')
ax.add_patch(square)

# Draw the Circle
circle = patches.Circle((h, k), r, linewidth=2, edgecolor='red', facecolor='none', label='Circle')
ax.add_patch(circle)

# Settings
ax.set_aspect('equal')
ax.set_xlim(field_x_min, field_x_max)
ax.set_ylim(field_y_min, field_y_max)
ax.set_title(f"Monte Carlo Visualization\nEstimated π = {pi_estimate:.5f}", fontsize=14)
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.tight_layout()
plt.show()

print(f"Points in Square : {square_count}")
print(f"Points in Circle : {circle_count}")
print(f"Estimated π      : {pi_estimate:.5f}")