import ipaddress
import pygame
import sys
import random
import imageio
import math
from pygame.locals import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

pygame.init()
font = pygame.font.Font(None, 20)

# Set up credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("/Users/jiwonbae/Codable/pythongame/hulahula/eighth-breaker-406405-db255db36bf9.json", scope)
gc = gspread.authorize(credentials)

# Open the Google Spreadsheet using its title
spreadsheet = gc.open("Rangtal: Scoreboard")

# Select the worksheet
worksheet = spreadsheet.sheet1

worksheet.update_acell("A1", "JWB")

# Constants
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Set display
display = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")

pygame.mixer.music.load("Backgroundmusic.mp3")  
collision_sound = pygame.mixer.Sound("536105__eminyildirim__sword-hit-medium.wav")  
stack_sound = pygame.mixer.Sound("420882__inspectorj__impact-ice-moderate-a.wav") 


# Play background music
pygame.mixer.music.play(-1) 

class Background:
    def __init__(self, image_path1, image_path2):
        self.image1 = pygame.image.load(image_path1).convert()
        self.image2 = pygame.image.load(image_path2).convert()
        self.image1 = pygame.transform.scale(self.image1, (400, 600))
        self.image2 = pygame.transform.scale(self.image2, (400, 600))
        self.y_position = 0

    def update(self):
        self.y_position += 1
        if self.y_position >= self.image1.get_height():
            self.y_position = 0

    def draw(self, surface):
        surface.blit(self.image1, (0, self.y_position))
        surface.blit(self.image2, (0, self.y_position - self.image1.get_height()))

# Define Scoop sprite
class Scoop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("icecream.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(70, SCREEN_WIDTH - 70), 0)

    def move(self, flag):
        self.rect.move_ip(0, 5)
        if flag == 1:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        
class Dong(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Dong.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

    def move(self, flag):
        self.rect.move_ip(0, 5)
        if flag == 1:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    
class Stackice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("icecream.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > -50:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH+50:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
class Stackice2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("icecream.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 450)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
class Stackice3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("icecream.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 450)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        

# Define Cone
class Cone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Cone.png")
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 580)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        

Cone1 = Cone()
Scoop1 = Scoop()
dong1 = Dong()
Stackice1 = Stackice()
stackice2 = Stackice2()
stackice3 = Stackice3()

Running = True
game_state = "start"
frames = []
max_score = 0
clock = pygame.time.Clock()

flag = 0
end = False
flag_scoop = 0
flag_stackice2 = 0
flag_stackice = 0
flag_dong =0
flag_cone =0
tick = 0
stack = 0
end_flag = 0
Numb_hearts = 3
dongflag = 0
WHITE = (255, 255, 255)
dongflag_timer = 0
dongflag_delay = 8 * FPS
input_text = ""

background = Background("RANGJOE.png", "SKY.png")

# sky_background = pygame.image.load("RANGJOE.png").convert()
# sky_background_scale = pygame.transform.scale(background, (400, 600))
start_background = pygame.image.load("Start.png")
start_background_fin = pygame.transform.scale(start_background, (400, 600))

bg_y = 0  # Initial y-position of the background


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "end_score":
                if event.key == pygame.K_BACKSPACE:
                    # Handle backspace to delete characters from the input
                    input_text = input_text[:-1]

                else:
                    # Handle other key presses to build the input_text
                    input_text += event.unicode
                    
            if event.key == K_RETURN:  # Enter key
                if game_state == "start":
                    game_state = "playing"
                elif game_state == "end_score":
                    input_text = ""
                    # Change the game state
                    game_state = "end"
                    Numb_hearts = 3
                    print("ENTER WAS PRESSED")
                    break
                elif game_state == "end":
                    game_state = "playing"
                    Numb_hearts = 3
                    max_score = 0
            if event.key == K_ESCAPE:
                Running = False
            if event.key == K_t:
                Numb_hearts = 0
    
    print(game_state)
    
    if Numb_hearts == 0:
        game_state = "end_score"
        
    if game_state == "start":
        # Display the start screen
        display.blit(start_background_fin, (0, 0))
        frame = pygame.surfarray.array3d(display)  
        frames.append(frame)

    elif game_state == "end_score":
        pygame.mixer.music.pause()
        display.fill(WHITE)
        endscore_text = font.render(f"Your Score is: {max_score}", True, (0, 0, 0))
        display.blit(endscore_text, (140, 260))
        endscore = font.render(f"New Score! Type in your initials to save your score!", True, (0, 0, 0))
        display.blit(endscore, (40, 300))

        # Draw the input text on the screen
        inputtext1 = font.render(f"{input_text}", True, (0, 0, 0))
        display.blit(inputtext1, (140, 360))

        endscores = font.render(f"Press enter after you're done!", True, (0, 0, 0))
        display.blit(endscores, (120, 400))
        
        
    elif game_state == "end":
        # Display the end screen
        display.fill(WHITE)
        worksheet.update_acell("B1", f"{max_score}")
        worksheet.update_acell("A1", f"{input_text}")
        endscore_text = font.render(f"Your Score is: {max_score}", True, (0, 0, 0))
        display.blit(endscore_text, (140, 260))
        end1_text = font.render(f"BOO HOO GAME OVER", True, (0, 0, 0))
        display.blit(end1_text, (120, 200))
        end2_text = font.render(f"Press ENTER to Start a New Game", True, (0, 0, 0))
        display.blit(end2_text, (80, 320))
        end3_text = font.render(f"Press ESC to Quit game", True, (0, 0, 0))
        display.blit(end3_text, (120, 340))
        
        data_range1 = worksheet.get("A1:B1")
        data_range2 = worksheet.get("A2:B2")
        data_range3 = worksheet.get("A3:B3")
        
        if end_flag == 1:
            if data_range1:
                data_string1 = f"{data_range1[0][0]} : {data_range1[0][1]}"
                data_text1 = font.render(data_string1, True, (0, 0, 0))

                data_string2 = f"{data_range2[0][0]} : {data_range2[0][1]}"
                data_text2 = font.render(data_string2, True, (0, 0, 0))

                data_string3 = f"{data_range3[0][0]} : {data_range3[0][1]}"
                data_text3 = font.render(data_string3, True, (0, 0, 0))
                end_flag = 0
        
        display.blit(data_text1, (120, 380))       
        display.blit(data_text2, (120, 420))
        display.blit(data_text3, (120, 460))
        
        tick = tick +1
        if tick%3 == 0:
            frame = pygame.surfarray.array3d(display)  # Convert the Pygame surface to a NumPy array
            frames.append(frame)
        
    elif game_state == "playing":
        end_flag = 1
        Cone1.update()
        Stackice1.update()
        stackice2.update()
        stackice3.update()
        Scoop1.move(0)
        
        if tick > 50:
            dong1.move(0)
            
        # if stack > 10:
            
        
        if stack > max_score:
            max_score = stack
        
        flag_cone = 0
        flag_stackice = 0
        if pygame.sprite.collide_mask(dong1, Stackice1) or pygame.sprite.collide_mask(dong1, stackice2) or pygame.sprite.collide_mask(dong1, stackice3):
            if dongflag == 0:
                flag = 0
                dong1.move(1)
                Numb_hearts = Numb_hearts - 1
                stack = 0
            collision_sound.play()
            dongflag = 1            
            bg_y = 0
            Cone1.rect.center = (160, 580)
            
                
        if pygame.sprite.collide_mask(Cone1, Scoop1):
            if flag == 0:
                stack_sound.play()
                collision_x, collision_y = Scoop1.rect.center
                col_x, col_y = Cone1.rect.center
                # Set the position of Stackice1 to the collision point
                Stackice1.rect.center = (collision_x, col_y - 50)
                flag = 1
                stack = stack + 1
                flag_scoop = 1
                Scoop1.move(flag_scoop)
                print("collide at", collision_x, collision_y)
                    

        if pygame.sprite.collide_mask(Stackice1, Scoop1):
            if flag == 1:
                # Check for collision
                # Get the collision point
                stack_sound.play()
                collision_x, collision_y = Scoop1.rect.center
                cone_x, cone_y = Cone1.rect.center
                x_1, y_1 = Stackice1.rect.center
                # Set the position of Stackice2 to the collision point
                Cone1.rect.center = (cone_x, cone_y +30)
                Stackice1.rect.center = (x_1, cone_y-20)
                stackice2.rect.center = (collision_x, y_1 - 30)
                flag = 2
                stack = stack + 1
                flag_scoop = 1
                Scoop1.move(flag_scoop)
                print("collide at", collision_x, collision_y)

        if pygame.sprite.collide_mask(stackice2, Scoop1):
            if flag == 2:
                # Check for collision
                # Get the collision point
                stack_sound.play()
                collision_x, collision_y = Scoop1.rect.center
                cone_x, cone_y = Cone1.rect.center
                x_1, y_1 = Stackice1.rect.center
                x_2, y_2 = stackice2.rect.center

                # Set the position of Stackice1 to the collision point
                Stackice1.rect.center = (x_1, cone_y-40)
                Cone1.rect.center = (cone_x, cone_y +30)
                stackice2.rect.center = (x_2, y_1 -30)
                stackice3.rect.center = (collision_x, y_2 - 30)
                flag = 3
                stack = stack + 1
                flag_scoop = 1
                Scoop1.move(flag_scoop)
                print("collide at", collision_x, collision_y)
        
        if pygame.sprite.collide_mask(stackice3, Scoop1):
            if flag >= 3:
                # Check for collision
                    # Get the collision point
                stack_sound.play()
                collision_x, collision_y = Scoop1.rect.center
                x_1, y_1 = Stackice1.rect.center
                x_2, y_2 = stackice2.rect.center
                x_3, y_3 = stackice3.rect.center
                x_4, y_4 = Cone1.rect.center

                # Set the position of Stackice1 to the collision poin
                # CHANGE THIS PART OF THE CODE PLZ!!!!!!!!!!!!!!!!!!
                Stackice1.rect.center = (x_2, y_1)
                Cone1.rect.center = (cone_x, cone_y +3000000)                    
                stackice2.rect.center = (x_3, y_2)
                stackice3.rect.center = (collision_x, y_2 - 50)
                flag = flag + 1
                print(flag)
                stack = stack + 1
                flag_scoop = 1
                Scoop1.move(flag_scoop)
                print("collide at", collision_x, collision_y)
                    
        
        dongflag = 0

        # # display.blit(background, (0, 0))
        # display.blit(background_scale, (0, bg_y))
        # display.blit(background_scale, (0, bg_y - background_scale.get_height()))

        # # Increment the y-position of the background to move upwards
        # bg_y += 1
        # if bg_y >= background_scale.get_height():
        #     bg_y = 0
        background.update()
        background.draw(display)
        
        Cone1.draw(display)
        Scoop1.draw(display)

        if tick > 50:
            dong1.draw(display)

        # Draw Scoop1 separately if it's not stacked with the cone

        Scoop1.draw(display)
        
        if flag >= 1:
            Stackice1.draw(display)
        if flag >= 2:
            stackice2.draw(display)
        if flag >= 3:
            stackice3.draw(display)
                    

        for i in range(Numb_hearts):
            original_image = pygame.image.load("heart.png")
            im = pygame.transform.scale(original_image, (20, 20))
            rect = im.get_rect()
            display.blit(im, (150 + i * 20, 10))
            
        score_text = font.render(f"Score: {max_score}", True, (0, 0, 0))
        stack_text = font.render(f"Stack: {stack}", True, (0, 0, 0))
        display.blit(score_text, (10, 10))
        display.blit(stack_text, (10, 30))
        tick = tick +1
        if tick%3 == 0:
            frame = pygame.surfarray.array3d(display)  # Convert the Pygame surface to a NumPy array
            frames.append(frame)
            
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
    

    
    pygame.display.update()
    clock.tick(FPS)
    

# Save frames as a GIF
#imageio.mimsave("my_animation.gif", frames, duration=1 / FPS * 3)
pygame.quit()
sys.exit()
