import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAYA  =(115, 194, 251)
FPS = 60

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 15

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ice Hockey")

# Fonts
font = pygame.font.SysFont(None, 55)

# Fuzzy logic functions for opponent paddle
def fuzzy_distance(ball_y, paddle_y):
    """Return a fuzzy value representing how far the ball is from the paddle."""
    distance = abs(ball_y - paddle_y)
    if distance < 50:
        return "close"
    elif distance < 150:
        return "medium"
    else:
        return "far"

def fuzzy_move_speed(distance):
    """Return the paddle movement speed based on fuzzy distance."""
    if distance == "close":
        return PADDLE_SPEED + 2  # Faster speed
    elif distance == "medium":
        return PADDLE_SPEED  # Normal speed
    else:
        return PADDLE_SPEED - 2  # Slower speed

# Paddle and ball classes
class Paddle:
    def __init__(self, x, y):  # Corrected constructor name
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if not up and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, speed_x, speed_y):  # Corrected constructor name
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reset(self, speed_x, speed_y):
        self.rect.x = WIDTH // 2 - BALL_SIZE // 2
        self.rect.y = HEIGHT // 2 - BALL_SIZE // 2
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Functions
def draw_score(player_score, opponent_score):
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 30, 20))
    screen.blit(opponent_text, (WIDTH // 2 - 50, 20))

def check_collision(ball, player, opponent):
    # Bounce off top and bottom
    if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
        ball.speed_y *= -1

    # Bounce off paddles
    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponent.rect):
        ball.speed_x *= -1

def get_username():

    username = input("Enter your username: ")
    return username

def choose_difficulty():
    print("Welcome to Ice Hockeyy")
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 6, 7  # Easy
    elif choice == "2":
        return 7, 7  # Medium
    elif choice == "3":
        return 5, 7  # Hard
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 6, 7

def get_max_points():
    while True:
        try:
            max_points = int(input("Enter the maximum points required to win: "))
            if max_points > 0:
                return max_points
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def wait_for_start():
    user_input = ""
    start_text = font.render("Type 'START' to begin", True, WHITE)
    while user_input.strip().upper() != "START":
        screen.fill(MAYA )
        screen.blit(start_text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))

        input_text = font.render(user_input, True, WHITE)
        screen.blit(input_text, (WIDTH // 2 - 100, HEIGHT // 2 + 30))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    user_input = ""
                else:
                    user_input += event.unicode

def display_winner(winner):
    winner_text = font.render(f"{winner} Wins!", True, WHITE)
    screen.fill(MAYA)
    screen.blit(winner_text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    clock = pygame.time.Clock()

    # Get username, difficulty level, and maximum points
    username = get_username()
    ball_speed_x, ball_speed_y = choose_difficulty()
    max_points = get_max_points()

    # Wait for the user to type "START"
    wait_for_start()

    # Initialize paddles and ball
    player = Paddle(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    opponent = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(ball_speed_x, ball_speed_y)

    player_score = 0
    opponent_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(up=True)
        if keys[pygame.K_DOWN]:
            player.move(up=False)

        # Opponent AI with fuzzy logic
        distance = fuzzy_distance(ball.rect.centery, opponent.rect.centery)
        move_speed = fuzzy_move_speed(distance)

        if ball.rect.centery < opponent.rect.centery and opponent.rect.top > 0:
            opponent.rect.y -= move_speed
        elif ball.rect.centery > opponent.rect.centery and opponent.rect.bottom < HEIGHT:
            opponent.rect.y += move_speed

        # Move the ball
        ball.move()

        # Check for collisions
        check_collision(ball, player, opponent)

        # Check for scoring
        if ball.rect.left <= 0:
            player_score += 1
            ball.reset(ball_speed_x, ball_speed_y)
        if ball.rect.right >= WIDTH:
            opponent_score += 1
            ball.reset(ball_speed_x, ball_speed_y)

        # Check if a player has won
        if player_score >= max_points:
            display_winner(username)
            running = False
        if opponent_score >= max_points:
            display_winner("Opponent")
            running = False

        # Draw everything
        screen.fill(MAYA)
        player.draw()
        opponent.draw()
        ball.draw()
        draw_score(player_score, opponent_score)

        # Display username
        username_text = font.render(f"User: {username}", True, WHITE)
        screen.blit(username_text, (20, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()