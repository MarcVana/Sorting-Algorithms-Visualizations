"""
DEVELOPED BY MARC VANA 04/20/2021

SIMPLE SORTING ALGORITHMS VISUALIZATION PROJECT
- made with Python 3.9 and pygame 2.0.1

It includes the following sorting algorithms:
    - bitonic sort
    - bubble sort
    - insertion sort
    - merge sort
    - radix sort
    - selection sort

The visualizations are made in a 1000x1000 pixels window with the
numbers from 1 to 256 randomly shuffled. All the instructions are
visible on the window.

You can:
    - reset the array (generate new one)
    - change the sorting algorithm
    - start the sorting algorithm
"""

# We import the libraries we need
import pygame
import random


def initialize_numbers(amount):
    """
    Initializes the array with 'amount' randomly shuffled numbers from 1 to 'amount'.
    :param amount: the size of the array
    """
    global numbers_stack, arr_clr, colors, values, normalized_values
    numbers_stack = []
    arr_clr = []
    for i in range(1, amount + 1):
        numbers_stack.append(i)
        arr_clr.append(colors[0])
    random.shuffle(numbers_stack)


def update_window():
    """
    Updates the window with the current numbers, colors and text.
    """
    txt = title_font.render("PRESS 'ENTER' TO START SORTING", True, (255, 255, 255))
    screen.blit(txt, (50, 20))

    txt1 = title_font.render("PRESS 'R' FOR NEW ARRAY.", True, (255, 255, 255))
    screen.blit(txt1, (50, 50))

    txt2 = title_font.render("ALGORITHM USED: " + sorting_algorithm, True, (255, 255, 0))
    screen.blit(txt2, (500, 50))

    txt3 = title_font.render("PRESS 'C' TO CHANGE ALGORITHM.", True, (255, 255, 255))
    screen.blit(txt3, (500, 20))

    pygame.draw.line(screen, (255, 255, 255), (0, 95), (screen_width, 95), 6)
    pygame.draw.line(screen, (255, 255, 255), (0, 900), (screen_width, 900), 6)

    txt4 = dev_font.render("DEVELOPED BY MARC VANA", True, (0, 255, 255))
    screen.blit(txt4, (300, 935))

    element_width = (screen_width - (n_numbers - 1)) // (n_numbers - 1)
    boundary_arr = screen_width / (n_numbers - 1)

    for i in range(n_numbers):
        pygame.draw.line(screen, arr_clr[i], (boundary_arr * i, 100),
                         (boundary_arr * i, numbers_stack[i] * 3 + 100),
                         element_width)


def refill():
    """
    Clears the window and updates it with the new numbers, colors and text.
    :return:
    """
    screen.fill((0, 0, 0))
    update_window()
    pygame.display.update()
    pygame.time.delay(20)


def merge_sort(numbers, left, right):
    """
    Standard recursive merge sort function.
    :param numbers: the array to be sorted
    :param left: the start position
    :param right: the end position
    """
    mid = (left + right) // 2
    if left < right:
        merge_sort(numbers, left, mid)
        merge_sort(numbers, mid + 1, right)
        merge(numbers, left, mid, mid + 1, right)


def merge(numbers, x1, y1, x2, y2):
    """
    Helper function for merge_sort function which merges
    the two halves.
    :param numbers: the array to be sorted
    :param x1: the start position of the first half
    :param y1: the end position of the first half
    :param x2: the start position of the second half
    :param y2: the end position of the second half
    :return:
    """
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = colors[1]
        arr_clr[j] = colors[1]
        refill()
        arr_clr[i] = colors[0]
        arr_clr[j] = colors[0]
        if numbers[i] < numbers[j]:
            temp.append(numbers[i])
            i = i + 1
        else:
            temp.append(numbers[j])
            j = j + 1

    while i <= y1:
        arr_clr[i] = colors[1]
        refill()
        arr_clr[i] = colors[0]
        temp.append(numbers[i])
        i = i + 1
    while j <= y2:
        arr_clr[j] = colors[1]
        refill()
        arr_clr[j] = colors[0]
        temp.append(numbers[j])
        j = j + 1

    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        numbers[i] = temp[j]
        j = j + 1
        arr_clr[i] = colors[2]
        refill()
        if y2 - x1 == len(numbers) - 1:
            arr_clr[i] = colors[3]
        else:
            arr_clr[i] = colors[0]


def bubble_sort(numbers):
    for i in range(n_numbers - 1):
        for j in range(n_numbers - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            arr_clr[j] = colors[1]
            arr_clr[j + 1] = colors[1]
            refill()
            arr_clr[j] = colors[0]
            arr_clr[j + 1] = colors[0]
    for i in range(n_numbers):
        arr_clr[i] = colors[3]
        refill()


def selection_sort(numbers):
    """
    Standard iterative selection sort function.
    :param numbers: the array to be sorted
    """
    for i in range(n_numbers):
        min_index = i
        for j in range(i + 1, n_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        arr_clr[min_index] = colors[1]
        arr_clr[i] = colors[2]
        refill()
        arr_clr[min_index] = colors[0]
        arr_clr[i] = colors[0]
    for i in range(n_numbers):
        arr_clr[i] = colors[3]
        refill()


def insertion_sort(numbers):
    """
    Standard iterative insertion sort function.
    :param numbers: the array to be sorted
    """
    for i in range(1, n_numbers):
        current = numbers[i]
        j = i - 1
        while j >= 0 and current < numbers[j]:
            numbers[j + 1] = numbers[j]
            j = j - 1
        arr_clr[i] = colors[2]
        arr_clr[j + 1] = colors[1]
        refill()
        arr_clr[i] = colors[0]
        arr_clr[j + 1] = colors[0]
        numbers[j + 1] = current
    for i in range(n_numbers):
        arr_clr[i] = colors[3]
        refill()


def bitonic_sort(numbers, low, count, direction):
    """
    Standard recursive bitonic sort function.
    :param numbers: the array to be sorted
    :param low: the start position
    :param count: the count of numbers to be sorted
    :param direction: 1 = ascending, 0 = descending
    """
    if count > 1:
        k = count // 2
        bitonic_sort(numbers, low, k, 1)
        bitonic_sort(numbers, low + k, k, 0)
        bitonic_merge(numbers, low, count, direction)
        if count == n_numbers:
            for i in range(n_numbers):
                arr_clr[i] = colors[3]
                refill()


def bitonic_merge(numbers, low, count, direction):
    """
    Helper function for bitonic_sort function which does
    the merging of the array sequences.
    :param numbers: the array to be sorted
    :param low: the start position
    :param count: the count of numbers to be sorted
    :param direction: 1 = ascending, 0 = descending
    """
    if count > 1:
        k = count // 2
        for i in range(low, low + k):
            if (direction == 1 and numbers[i] > numbers[i + k]) or (direction == 0 and numbers[i] < numbers[i + k]):
                numbers[i], numbers[i + k] = numbers[i + k], numbers[i]
                arr_clr[i + k] = colors[1]
                arr_clr[i] = colors[1]
                refill()
                arr_clr[i + k] = colors[0]
                arr_clr[i] = colors[0]
        bitonic_merge(numbers, low, k, direction)
        bitonic_merge(numbers, low + k, k, direction)


def radix_sort(numbers):
    """
    Standard iterative radix sort function.
    :param numbers: the array to be sorted.
    """
    _max = max(numbers)
    exp = 1
    while _max // exp > 0:
        count_sort(numbers, exp)
        exp = exp * 10

    for i in range(n_numbers):
        arr_clr[i] = colors[3]
        refill()


def count_sort(numbers, exp10):
    """
    Helper function for radix_sort function. Radix sort
    is based on the counting sort on digits.
    :param numbers: the array to be sorted
    :param exp10: the current exponent of 10
    """
    output = [0] * n_numbers
    count = [0] * 10
    for i in range(n_numbers):
        count[int((numbers[i] / exp10) % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n_numbers - 1, -1, -1):
        index = int((numbers[i] / exp10) % 10)
        output[count[index] - 1] = numbers[i]
        count[index] -= 1
        arr_clr[i] = colors[1]
        arr_clr[max(i - 1, 0)] = colors[1]
        arr_clr[min(i + 1, n_numbers - 1)] = colors[1]
        arr_clr[max(i - 2, 0)] = colors[1]
        arr_clr[min(i + 2, n_numbers - 1)] = colors[1]
        refill()
        arr_clr[i] = colors[0]
        arr_clr[max(i - 1, 0)] = colors[0]
        arr_clr[min(i + 1, n_numbers - 1)] = colors[0]
        arr_clr[max(i - 2, 0)] = colors[0]
        arr_clr[min(i + 2, n_numbers - 1)] = colors[0]

    k = n_numbers // 4
    for i in range(k):
        numbers[i] = output[i]
        numbers[i + k] = output[i + k]
        numbers[i + 2 * k] = output[i + 2 * k]
        numbers[i + 3 * k] = output[i + 3 * k]
        arr_clr[i] = colors[1]
        arr_clr[i + k] = colors[1]
        arr_clr[i + 2 * k] = colors[1]
        arr_clr[i + 3 * k] = colors[1]
        refill()
        arr_clr[i] = colors[0]
        arr_clr[i + k] = colors[0]
        arr_clr[i + 2 * k] = colors[0]
        arr_clr[i + 3 * k] = colors[0]


def sort_by_algorithm(algorithm, numbers):
    """
    Starts the sorting with the desired sorting algorithm.
    :param algorithm: the algorithm to use
    :param numbers: the array to be sorted
    """
    if algorithm == 'BUBBLE SORT':
        bubble_sort(numbers)
    if algorithm == 'SELECTION SORT':
        selection_sort(numbers)
    if algorithm == 'INSERTION SORT':
        insertion_sort(numbers)
    if algorithm == 'MERGE SORT':
        merge_sort(numbers, 0, n_numbers - 1)
    if algorithm == 'BITONIC SORT':
        bitonic_sort(numbers, 0, n_numbers, 1)
    if algorithm == 'RADIX SORT':
        radix_sort(numbers)


if __name__ == '__main__':
    # Initialize the window
    pygame.init()
    pygame.font.init()
    title_font = pygame.font.SysFont("consolas", 25)
    dev_font = pygame.font.SysFont("consolas", 35)

    screen_height = 1000
    screen_width = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Title and Icon
    pygame.display.set_caption("Sorting Algorithms")
    pygame.display.set_icon(pygame.image.load('icon.png'))

    # Numbers and Colors
    sorted_size = 0
    numbers_stack = []
    n_numbers = 256
    arr_clr = [(255, 255, 255)] * n_numbers
    colors = [(255, 255, 255), (255, 0, 0), (0, 0, 155), (0, 205, 105)]
    initialize_numbers(n_numbers)

    # Sorting algorithms
    algorithms = ['BITONIC SORT', 'BUBBLE SORT', 'INSERTION SORT', 'MERGE SORT', 'RADIX SORT', 'SELECTION SORT']
    alg_index = 0
    sorting_algorithm = algorithms[alg_index]

    # The loop
    run = True
    while run:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R (generate new array)
                    initialize_numbers(n_numbers)
                if event.key == pygame.K_c:  # C (change the sorting algorithm)
                    alg_index = (alg_index + 1) % len(algorithms)
                    sorting_algorithm = algorithms[alg_index]
                if event.key == pygame.K_RETURN:  # ENTER (start the sorting)
                    sort_by_algorithm(sorting_algorithm, numbers_stack)
        update_window()
        pygame.display.update()
    pygame.quit()
