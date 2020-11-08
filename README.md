# Bouncing_cube 1.6.1

## What does the program do ?
- A cube bounces against the edges of the window and against a central obstacle which contracts little by little
- The cube changes color depending on the location of its collision (upper/lower edges of the window, side edges of the window, over/under the central obstacle, etc.)
- Each time the cube comes in contact with an edge of the window, the width of the central obstacle contracts a notch. The obstacle continues to contract to a minimum before it returns to its original size
- The initial color of the obstacle changes color as it contracts
- The animation speed can be controlled by pressing up arrow (speed ++) or pressing down arrow (speed --), the initial speed can be retrieved by pressing space
- Real-time information can be displayed at the top left of the window (cube coordinates, obstacle width, vector etc. (Set `infoDisplay` to True)

## Screenshots
### Animation mosaic
![bouncing](https://user-images.githubusercontent.com/11463619/97807740-dcb2a500-1c62-11eb-8fbd-18d26d138d20.jpg)

### Infos display
![bouncing_info](https://user-images.githubusercontent.com/11463619/97807743-e20fef80-1c62-11eb-819d-89c5786ad166.jpg)

## Requirements :
- `pygame`
