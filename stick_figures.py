import turtle
import random
import math

class AnimalFaceDrawer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Animal Face Generator with Realistic Fur")
        self.screen.bgcolor("white")
        self.t = turtle.Turtle()
        self.t.speed(0)  # Fastest speed
        self.t.pensize(1)
    
    def draw_layered_fur(self, x, y, radius, base_color, highlight_color, density=70):
        """Draw more realistic fur with layers and highlights"""
        self.t.pensize(0.5)  # Thinner lines for fur
        
        # Draw base layer
        for _ in range(density):
            angle = random.uniform(0, 360)
            distance = random.uniform(0, radius)
            fur_length = random.uniform(5, 15)
            
            # Slightly vary the fur color
            color_variation = random.uniform(-0.1, 0.1)
            fur_color = tuple(max(0, min(1, c + color_variation)) for c in base_color)
            
            self.t.penup()
            self.t.goto(
                x + distance * math.cos(math.radians(angle)),
                y + distance * math.sin(math.radians(angle))
            )
            self.t.setheading(angle)
            self.t.pencolor(fur_color)
            self.t.pendown()
            
            # Draw curved fur strands
            for _ in range(3):
                self.t.forward(fur_length/3)
                self.t.left(random.uniform(-5, 5))

        # Add highlight layer
        for _ in range(density//2):
            angle = random.uniform(0, 360)
            distance = random.uniform(radius/2, radius)
            
            self.t.penup()
            self.t.goto(
                x + distance * math.cos(math.radians(angle)),
                y + distance * math.sin(math.radians(angle))
            )
            self.t.setheading(angle)
            self.t.pencolor(highlight_color)
            self.t.pendown()
            self.t.forward(random.uniform(3, 8))

    def draw_circle(self, radius):
        """Draw a circle"""
        self.t.circle(radius)
    
    def draw_triangle(self, size):
        """Draw a triangle for ears"""
        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)
    
    def draw_cat(self, x, y, size=50):
        """Draw a cat face with realistic fur"""
        # Define colors
        base_color = (0.6, 0.6, 0.6)      # Gray
        highlight_color = (0.8, 0.8, 0.8)  # Light gray
        
        # Draw base shape
        self.t.penup()
        self.t.goto(x, y)
        self.t.fillcolor(base_color)
        self.t.begin_fill()
        self.t.circle(size)
        self.t.end_fill()
        
        # Add fur texture
        self.draw_layered_fur(x, y+size, size, base_color, highlight_color)
        
        # Draw ears with fur
        ear_positions = [(x-size/2, y+size*1.5), (x+size/2, y+size*1.5)]
        for ear_x, ear_y in ear_positions:
            # Draw ear base
            self.t.penup()
            self.t.goto(ear_x, ear_y)
            self.t.fillcolor(base_color)
            self.t.begin_fill()
            for _ in range(3):
                self.t.forward(size/2)
                self.t.left(120)
            self.t.end_fill()
            
            # Add fur to ears
            self.draw_layered_fur(ear_x+size/4, ear_y+size/4, size/4, base_color, highlight_color, density=30)
        
        # Eyes with gradient
        for eye_x in [x-size/3, x+size/3]:
            # Outer eye color
            self.t.penup()
            self.t.goto(eye_x, y+size/2)
            self.t.fillcolor("green")
            self.t.begin_fill()
            self.t.circle(size/6)
            self.t.end_fill()
            
            # Inner eye color
            self.t.goto(eye_x, y+size/2)
            self.t.fillcolor("black")
            self.t.begin_fill()
            self.t.circle(size/12)
            self.t.end_fill()
            
            # Eye highlight
            self.t.goto(eye_x-size/24, y+size/2+size/12)
            self.t.fillcolor("white")
            self.t.begin_fill()
            self.t.circle(size/24)
            self.t.end_fill()
        
        # Nose
        self.t.penup()
        self.t.goto(x, y+size/4)
        self.t.fillcolor("pink")
        self.t.begin_fill()
        self.t.circle(size/10)
        self.t.end_fill()
        
        # Whiskers with natural curve
        self.t.pensize(1)
        whisker_starts = [(x-size/4, y+size/4), (x+size/4, y+size/4)]
        for wx, wy in whisker_starts:
            for i in range(3):
                self.t.penup()
                self.t.goto(wx, wy + i*size/10)
                self.t.setheading(180 if wx < x else 0)
                self.t.pendown()
                # Create natural curved whiskers
                for _ in range(15):
                    self.t.forward(size/15)
                    self.t.left(3 if wx < x else -3)

    def draw_dog(self, x, y, size=50):
        """Draw a dog face with realistic fur"""
        # Define colors
        base_color = (0.6, 0.4, 0.2)      # Brown
        highlight_color = (0.7, 0.5, 0.3)  # Light brown
        
        # Draw base shape
        self.t.penup()
        self.t.goto(x, y)
        self.t.fillcolor(base_color)
        self.t.begin_fill()
        self.t.circle(size)
        self.t.end_fill()
        
        # Add fur texture
        self.draw_layered_fur(x, y+size, size, base_color, highlight_color, density=90)
        
        # Draw floppy ears with fur
        for ear_x in [x-size, x+size]:
            # Draw ear base
            self.t.penup()
            self.t.goto(ear_x, y+size)
            self.t.fillcolor(base_color)
            self.t.begin_fill()
            self.t.setheading(90)
            self.t.circle(size/2, 180)
            self.t.end_fill()
            
            # Add fur to ears
            self.draw_layered_fur(ear_x, y+size*1.25, size/2, base_color, highlight_color, density=40)
        
        # Eyes
        for eye_x in [x-size/3, x+size/3]:
            self.t.penup()
            self.t.goto(eye_x, y+size/2)
            self.t.fillcolor("brown")
            self.t.begin_fill()
            self.t.circle(size/8)
            self.t.end_fill()
            
            # Eye highlight
            self.t.goto(eye_x-size/16, y+size/2+size/10)
            self.t.fillcolor("white")
            self.t.begin_fill()
            self.t.circle(size/20)
            self.t.end_fill()
        
        # Nose
        self.t.penup()
        self.t.goto(x, y+size/4)
        self.t.fillcolor("black")
        self.t.begin_fill()
        self.t.circle(size/6)
        self.t.end_fill()
    
    def draw_rabbit(self, x, y, size=50):
        """Draw a rabbit face"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # Draw face
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.draw_circle(size)
        self.t.end_fill()
        
        # Draw long ears
        self.t.fillcolor("white")
        self.t.penup()
        self.t.goto(x-size/2, y+size)
        self.t.pendown()
        self.t.begin_fill()
        self.t.setheading(90)
        self.t.forward(size*2)
        self.t.circle(size/4, 180)
        self.t.forward(size*2)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x+size/2, y+size)
        self.t.pendown()
        self.t.begin_fill()
        self.t.setheading(90)
        self.t.forward(size*2)
        self.t.circle(size/4, 180)
        self.t.forward(size*2)
        self.t.end_fill()
        
        # Draw eyes
        self.t.penup()
        self.t.goto(x-size/3, y+size/2)
        self.t.pendown()
        self.t.fillcolor("red")
        self.t.begin_fill()
        self.draw_circle(size/8)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x+size/3, y+size/2)
        self.t.pendown()
        self.t.begin_fill()
        self.draw_circle(size/8)
        self.t.end_fill()
        
        # Draw nose
        self.t.penup()
        self.t.goto(x, y+size/4)
        self.t.pendown()
        self.t.fillcolor("pink")
        self.t.begin_fill()
        self.draw_circle(size/10)
        self.t.end_fill()
    
    def draw_random_animals(self, count=2):
        """Draw multiple random animal faces"""
        screen_width = self.screen.window_width()
        screen_height = self.screen.window_height()
        
        animals = [self.draw_cat, self.draw_dog]
        
        for _ in range(count):
            x = random.randint(-screen_width//4, screen_width//4)
            y = random.randint(-screen_height//4, screen_height//4)
            size = random.randint(50, 80)
            random.choice(animals)(x, y, size)
    
    def clear_screen(self):
        """Clear the screen"""
        self.t.clear()
    
    def exit_on_click(self):
        """Close the window on click"""
        self.screen.exitonclick()

# Create and run the program
if __name__ == "__main__":
    drawer = AnimalFaceDrawer()
    drawer.draw_random_animals(2)  # Draw 2 random animal faces
    drawer.exit_on_click()
