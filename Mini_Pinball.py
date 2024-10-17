import pygame
import sys
import random



pygame.init()



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



DARK_COLORS = [
    (25, 25, 112),   (47, 79, 79),    (70, 130, 180),
        (0, 0, 128),     (139, 0, 0),     (0, 100, 0),
        (178, 34, 34),   (255, 140, 0),   (255, 20, 147),
        (255, 99, 71),   (85, 107, 47),   (60, 179, 113),
        (32, 178, 170),  (0, 139, 139),   (0, 128, 128),
        (128, 128, 0),   (119, 136, 153), (128, 0, 0),
        (139, 69, 19),   (70, 130, 180),  (0, 206, 209),
        (160, 32, 240),  (128, 0, 0),     (0, 255, 255),
        (240, 128, 128), (102, 51, 153),  (0, 255, 127),
        (128, 128, 224), (255, 228, 225), (119, 136, 153),
        (85, 107, 47),   (95, 158, 160),  (32, 178, 170),
        (70, 130, 180),  (102, 205, 170), (255, 20, 147),
        (0, 100, 0),     (205, 92, 92),   (112, 128, 144),
        (139, 137, 137), (30, 144, 255),  (123, 104, 238),
        (165, 42, 42),   (119, 136, 153),  (70, 130, 180),
        (255, 215, 0),   (255, 192, 203), (255, 160, 122),
        (255, 215, 0),   (255, 192, 203),(255, 160, 122)
]



BALL_RADIUS = 18
BALL_COLOR = (250, 250, 250)
BALL_SPEED_X = 4
BALL_SPEED_Y = 4



BUMPER_WIDTH = 80
BUMPER_HEIGHT = 20
YELLOW_BUMPER_COLOR = (255, 223, 0)
PURPLE_BUMPER_COLOR = (148, 0, 211)



MIN_DISTANCE_TO_BALL = 200
MIN_DISTANCE_TO_YELLOW_BUMPER = 150



def generate_random_bumpers(num_bumpers, yellow_bumper, ball_pos):
    bumpers = []
    for _ in range(num_bumpers):
        while True:
            x = random.randint(0, SCREEN_WIDTH - BUMPER_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - BUMPER_HEIGHT)
            new_bumper = pygame.Rect(x, y, BUMPER_WIDTH, BUMPER_HEIGHT)
            if (not are_rects_too_close(new_bumper, yellow_bumper, MIN_DISTANCE_TO_YELLOW_BUMPER) and
                not is_bumper_too_close_to_ball(new_bumper, ball_pos, MIN_DISTANCE_TO_BALL)):
                bumpers.append(new_bumper)
                break
    return bumpers



def are_rects_too_close(rect1, rect2, min_distance):
    center1 = rect1.center
    center2 = rect2.center
    distance = ((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2) ** 0.5
    return distance < min_distance



def is_bumper_too_close_to_ball(bumper, ball_pos, min_distance):
    bumper_center = bumper.center
    ball_center = (ball_pos[0], ball_pos[1])
    distance = ((bumper_center[0] - ball_center[0]) ** 2 + (bumper_center[1] - ball_center[1]) ** 2) ** 0.5
    return distance < min_distance



def generate_yellow_bumper():
    x = random.randint(0, SCREEN_WIDTH - BUMPER_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT - BUMPER_HEIGHT)
    return pygame.Rect(x, y, BUMPER_WIDTH, BUMPER_HEIGHT)



def main_menu():
    global score, level
    menu_font = pygame.font.Font(None, 50)
    title_text = menu_font.render('Mini Pinball', True, (75, 0, 130))
    start_text = menu_font.render('Press Enter to Start', True, (144, 238, 144))
    exit_text = menu_font.render('Press Esc to Exit', True, (255, 0, 0))



    while True:
        screen.fill((0, 0, 0))
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 180))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 240))
        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



def reset_game():
    global level, score, ball_pos, ball_vel, bumpers, yellow_bumper, start_time, BACKGROUND_COLOR
    level = 1
    score = 0
    ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]
    yellow_bumper = generate_yellow_bumper()
    BACKGROUND_COLOR = random.choice(DARK_COLORS)
    bumpers = generate_random_bumpers(4, yellow_bumper, ball_pos)
    start_time = pygame.time.get_ticks()



def increase_level():
    global level, ball_vel, bumpers, yellow_bumper, score, BACKGROUND_COLOR
    level += 1
    score += 10
    ball_vel[0] += random.choice([1, 2])
    ball_vel[1] += random.choice([1, 2])
    yellow_bumper = generate_yellow_bumper()
    BACKGROUND_COLOR = random.choice(DARK_COLORS)
    bumpers = generate_random_bumpers(4 + level, yellow_bumper, ball_pos)



def game_over():
    screen.fill((0, 0, 0))
    game_over_text = font.render('Game Over! -_- ', True, (255, 0, 0))
    restart_text = font.render('[Press R to Restart]', True, (255, 250, 250))
    exit_text = font.render('[ Press Esc to Exit ]', True, (255, 250, 250))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 68, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 88, 680))
    screen.blit(exit_text, (SCREEN_WIDTH // 2 - 88, 620))
    pygame.display.flip()



    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



def check_victory():
    if score >= 1500:
        victory_screen()



def interpolate_color(color1, color2, factor):
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
            int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor)
    )



def victory_screen():
    color_index = 0
    next_color_time = 2
    color_duration = 3000



    waiting = True
    while waiting:
        current_time = pygame.time.get_ticks()



        if current_time > next_color_time:
            color_index = (color_index + 1) % len(DARK_COLORS)
            next_color_time = current_time + color_duration



        start_color = DARK_COLORS[color_index]
        end_color = DARK_COLORS[(color_index + 1) % len(DARK_COLORS)]
        factor = (current_time % color_duration) / color_duration
        BACKGROUND_COLOR = interpolate_color(start_color, end_color, factor)



        screen.fill(BACKGROUND_COLOR)
        victory_text = font.render('Congratulations_You Win!', True, (0, 0, 0))
        restart_text = font.render('[Press R to Restart]', True, (0, 0, 0))
        exit_text = font.render('[ Press Esc to Exit ]', True, (0, 0, 0))



        screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 88, SCREEN_HEIGHT // 2 + 250))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - 88, SCREEN_HEIGHT // 2 + 280))
        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                        reset_game()
                        game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



def game_loop():
    global ball_pos, ball_vel, bumpers, yellow_bumper
    bumpers = generate_random_bumpers(4, generate_yellow_bumper(), ball_pos)
    yellow_bumper = generate_yellow_bumper()



    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        keys = pygame.key.get_pressed()
        ball_vel[0] = -BALL_SPEED_X if keys[pygame.K_a] else BALL_SPEED_X if keys[pygame.K_d] else 0
        ball_vel[1] = -BALL_SPEED_Y if keys[pygame.K_w] else BALL_SPEED_Y if keys[pygame.K_s] else 0



        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]



        if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= SCREEN_WIDTH - BALL_RADIUS:
                        ball_vel[0] = -ball_vel[0]
        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= SCREEN_HEIGHT - BALL_RADIUS:
                        ball_vel[1] = -ball_vel[1]



        ball_pos[0] = max(BALL_RADIUS, min(ball_pos[0], SCREEN_WIDTH - BALL_RADIUS))
        ball_pos[1] = max(BALL_RADIUS, min(ball_pos[1], SCREEN_HEIGHT - BALL_RADIUS))



        ball_rect = pygame.Rect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)



        if ball_rect.colliderect(yellow_bumper):
            increase_level()



        for bumper in bumpers:
            if ball_rect.colliderect(bumper):
                game_over()



        check_victory()



        screen.fill(BACKGROUND_COLOR)



        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)



        for bumper in bumpers:
            pygame.draw.rect(screen, PURPLE_BUMPER_COLOR, bumper)



        pygame.draw.rect(screen, YELLOW_BUMPER_COLOR, yellow_bumper)



        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        time_text = font.render(f'Time: {elapsed_time}s', True, (0, 0, 0))



        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))



        pygame.display.flip()
        clock.tick(165)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 30)



ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]



BACKGROUND_COLOR = random.choice(DARK_COLORS)



main_menu()