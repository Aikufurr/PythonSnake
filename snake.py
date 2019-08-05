import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(1)
window.timeout(100)
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_x, snake_y],
    [snake_x, snake_y-1],
    [snake_x, snake_y-2]
]

food = [sh//2, sw//2]

window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if str(key) == "KEY_ESCAPE":
        curses.endwin();
        print("Score: " + str(score))
        quit()

    window.addstr(0, 0, "Score: " + str(score))

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        window.clear()
        window.addstr(0, 0, "Score: " + str(score))
        curses.endwin();
        print("Score: " + str(score))
        quit()
        break

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = None
        while not food:
            new_food = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        snake_tail = snake.pop()
        window.addch(snake_tail[0], snake_tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
