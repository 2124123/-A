import pygame
import math

pygame.init()

# Tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_width(), screen.get_height()
clock = pygame.time.Clock()

# Criando pontos da malha
points = [[x*20 + W//4, y*20 + H//4, x*20 + W//4, y*20 + H//4, 0]
          for y in range(30) for x in range(50)]

# Criando conexões entre pontos
lines = []
for i in range(len(points)):
    if (i + 1) % 50 != 0:
        lines.append((i, i + 1))
    if i + 50 < len(points):
        lines.append((i, i + 50))

# Loop principal
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    screen.fill((5, 5, 10))

    mx, my = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Movimento dos pontos
    for p in points:
        if not mouse_pressed[0]:
            dx = p[0] - mx
            dy = p[1] - my
            dist = math.hypot(dx, dy)

            if dist < 30:
                p[0], p[1] = mx, my

        # física simples (retorno ao original)
        vx = (p[2] - p[0]) * 0.1
        vy = (p[3] - p[1]) * 0.1
        p[0] += vx
        p[1] += vy

    # Ajuste das linhas (efeito tecido)
    for i1, i2 in lines:
        p1 = points[i1]
        p2 = points[i2]

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dist = math.hypot(dx, dy)

        if dist == 0:
            continue

        force = (dist - 20) / dist * 0.5

        p1[0] += dx * force
        p1[1] += dy * force
        p2[0] -= dx * force
        p2[1] -= dy * force

    # Desenhar linhas
    for i1, i2 in lines:
        pygame.draw.line(
            screen,
            (0, 255, 150),
            (points[i1][0], points[i1][1]),
            (points[i2][0], points[i2][1]),
            1
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


