import pygame
grid_data = []

def read_grid_fom_file(grid):                   
    
    with open('grid.txt', 'r') as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            grid_data.append(row)
    return grid_data


def grid(window, size, rows, grid_data):
    distanceBtwRows = size // rows
    for i in range(rows):
        for j in range(rows):
            if grid_data[i][j] == 1:
                pygame.draw.rect(window, (255, 255, 255), (j*distanceBtwRows, i*distanceBtwRows, distanceBtwRows, distanceBtwRows ))
            elif grid_data[i][j] == 2:
                pygame.draw.rect(window, (0, 0, 0), (j*distanceBtwRows, i*distanceBtwRows, distanceBtwRows, distanceBtwRows ))
            elif grid_data[i][j] == 3: 
                pygame.draw.rect(window, (55, 55, 255), (j*distanceBtwRows, i*distanceBtwRows, distanceBtwRows, distanceBtwRows ))

def redraw(window, grid_data):
    window.fill((210, 210, 210))
    grid(window, size, rows, grid_data)
    pygame.display.update()



global size, rows
size = 500
rows = 20

window = pygame.display.set_mode((size,size))

grid_data = []
read_grid_fom_file(grid_data)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    redraw(window, grid_data)

pygame.quit()