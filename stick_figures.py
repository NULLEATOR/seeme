import turtle
import random

class AnimalFaceDrawer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Animal Face Generator")
        self.screen.bgcolor("white")
        self.t = turtle.Turtle()
        self.t.speed(8)
        self.t.pensize(2)
    
    def draw_circle(self, radius):
        """Draw a circle"""
        self.t.circle(radius)
    
    def draw_triangle(self, size):
        """Draw a triangle for ears"""
        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)
    
    def draw_cat(self, x, y, size=50):
        """Draw a cat face"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # Draw face
        self.t.fillcolor("gray")
        self.t.begin_fill()
        self.draw_circle(size)
        self.t.end_fill()
        
        # Draw ears
        self.t.penup()
        self.t.goto(x-size/2, y+size*1.5)
        self.t.pendown()
        self.t.fillcolor("gray")
        self.t.begin_fill()
        self.draw_triangle(size)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x+size/2, y+size*1.5)
        self.t.pendown()
        self.t.begin_fill()
        self.draw_triangle(size)
        self.t.end_fill()
        
        # Draw eyes
        self.t.penup()
        self.t.goto(x-size/3, y+size/2)
        self.t.pendown()
        self.t.fillcolor("green")
        self.t.begin_fill()
        self.draw_circle(size/6)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x+size/3, y+size/2)
        self.t.pendown()
        self.t.begin_fill()
        self.draw_circle(size/6)
        self.t.end_fill()
        
        # Draw nose
        self.t.penup()
        self.t.goto(x, y+size/4)
        self.t.pendown()
        self.t.fillcolor("pink")
        self.t.begin_fill()
        self.draw_circle(size/8)
        self.t.end_fill()
        
        # Draw whiskers
        self.t.penup()
        self.t.goto(x-size/4, y+size/4)
        for i in range(3):
            self.t.pendown()
            self.t.goto(x-size, y+size/4 + i*size/8)
            self.t.penup()
            self.t.goto(x-size/4, y+size/4)
        
        self.t.goto(x+size/4, y+size/4)
        for i in range(3):
            self.t.pendown()
            self.t.goto(x+size, y+size/4 + i*size/8)
            self.t.penup()
            self.t.goto(x+size/4, y+size/4)
    
    def draw_dog(self, x, y, size=50):
        """Draw a dog face"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # Draw face
        self.t.fillcolor("brown")
        self.t.begin_fill()
        self.draw_circle(size)
        self.t.end_fill()
        
        # Draw floppy ears
        self.t.fillcolor("brown")
        self.t.penup()
        self.t.goto(x-size, y+size)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(size/2, 180)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x+size, y+size)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(-size/2, 180)
        self.t.end_fill()
        
        # Draw eyes
        self.t.penup()
        self.t.goto(x-size/3, y+size/2)
        self.t.pendown()
        self.t.fillcolor("black")
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
        self.t.fillcolor("black")
        self.t.begin_fill()
        self.draw_circle(size/6)
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
    
    def draw_random_animals(self, count=3):
        """Draw multiple random animal faces"""
        screen_width = self.screen.window_width()
        screen_height = self.screen.window_height()
        
        animals = [self.draw_cat, self.draw_dog, self.draw_rabbit]
        
        for _ in range(count):
            x = random.randint(-screen_width//4, screen_width//4)
            y = random.randint(-screen_height//4, screen_height//4)
            size = random.randint(30, 60)
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
    drawer.draw_random_animals(3)  # Draw 3 random animal faces
    drawer.exit_on_click()
