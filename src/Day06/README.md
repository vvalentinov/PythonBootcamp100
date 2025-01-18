# 🎯 Day Six: Python Functions and Karel

This day focuses on Python functions and their role in structuring and optimizing code.  
It features exercises and examples using Karel the Robot to solve problems.  
Topics include function creation and reuse for efficient programming.  
A perfect resource for learning to write clean, functional Python code while having fun with Karel.

[Reeborg's World](https://reeborg.ca/index_en.html)

## 📚 Knowledge Gained

1. **Functions**  
*Covers Python functions, focusing on creating reusable code blocks.*
2. **While Loops**  
*Explores while loops, highlighting their use in controlling repetitive program flow based on conditions.*
3. **Indentation**  
*Emphasizes the importance of proper indentation in Python to ensure code readability and correct execution.*

### ✅ Hurdles Challenge (Hurdle 1) Using the For Loop:

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for number in range(1, 7):
    jump()

```

### ✅ Hurdles Challenge (Hurdle 1) Using the While Loop:

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_hurdles = 1

while number_of_hurdles <= 6:
    jump()
    number_of_hurdles += 1

```

### ✅ Hurdles Challenge (Hurdle 2) Using the While Loop:

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    jump()

```

### ✅ Hurdles Challenge (Hurdle 3) Using the While Loop and wall_in_front():

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()
        
```

### ✅ Hurdles Challenge (Hurdle 4) Using the While Loop and wall_on_right():

```
Option 1:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_wall():
    steps = 0
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        steps += 1
    move()
    turn_right()
    for n in range(steps):
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()
        
Option 2:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()
        
```

### ✅ Escaping the Maze:

```
def turn_right():    
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()

turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

```