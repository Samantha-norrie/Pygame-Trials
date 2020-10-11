#import
import pygame
import random
import time

#global vars
display_width = 900
display_height = 600
moving_asset_width = 40
black = (0,0,0)
day_status = False
time_since_last_spawn = 0.0
time_since_last_transition = 0.0
time_since_last_firework = 0.0
time_since_last_phase = 0.0


#assets


#sky background png assets
night_sky = pygame.image.load('assets\\night_sky.png')
day_sky = pygame.image.load('assets\\day_sky.png')

#city vehicle png assets
city_bus_png = pygame.image.load('assets\\city_bus.png')
city_bus_purple_png = pygame.image.load('assets\\city_bus_purple.png')
bar_cart_of_sorts_png = pygame.image.load('assets\\bar_cart_of_sorts.png')
odd_unicycle_png = pygame.image.load('assets\\odd_unicycle.png')
car_one_png = pygame.image.load('assets\\car_one.png')
car_two_png = pygame.image.load('assets\\car_two.png')
car_three_png = pygame.image.load('assets\\car_three.png')
car_four_png = pygame.image.load('assets\\car_four.png')

#country vehicle png assets
country_car_one_png = pygame.image.load('assets\\country_car_one.png')
country_car_two_png = pygame.image.load('assets\\country_car_two.png')
country_car_three_png = pygame.image.load('assets\\country_car_three.png')

#tuples of vehicle png assets
city_moving_asset_png_tuple = (city_bus_png, city_bus_purple_png, bar_cart_of_sorts_png, odd_unicycle_png, car_one_png, car_two_png, car_three_png, car_four_png);
country_moving_asset_png_tuple = (country_car_one_png, country_car_two_png, country_car_three_png);

#firework png images
firework_one_png = pygame.image.load('assets\\firework_one.png')
firework_two_png = pygame.image.load('assets\\firework_two.png')
firework_three_png = pygame.image.load('assets\\firework_three.png')
firework_four_png = pygame.image.load('assets\\firework_four.png')

#minimum num of fireworks that can spawn
firework_spawn_num = 3

#tuple of firework png assets
firework_png_tuple = (firework_one_png, firework_two_png, firework_three_png, firework_four_png);

#star png images
star_phase_one_png = pygame.image.load('assets\\star_phase_one.png')
star_phase_two_png = pygame.image.load('assets\\star_phase_two.png')
star_phase_three_png = pygame.image.load('assets\\star_phase_three.png')
star_phase_four_png = pygame.image.load('assets\\star_phase_four.png')
star_phase_five_png = pygame.image.load('assets\\star_phase_five.png')
star_phase_six_png = pygame.image.load('assets\\star_phase_six.png')
star_phase_seven_png = pygame.image.load('assets\\star_phase_seven.png')
star_phase_eight_png = pygame.image.load('assets\\star_phase_eight.png')
star_phase_nine_png = pygame.image.load('assets\\star_phase_nine.png')
star_png_tuple = (star_phase_one_png, star_phase_two_png, star_phase_three_png, star_phase_four_png, star_phase_five_png, star_phase_six_png, star_phase_seven_png, star_phase_eight_png, star_phase_nine_png);
sky_assets_tuple = (night_sky, day_sky);

#city (night) png building assets
city_building_one_png = pygame.image.load('assets\\city_building_one.png')
city_building_two_png = pygame.image.load('assets\\city_building_two.png')
city_building_three_png = pygame.image.load('assets\\city_building_three.png')
city_building_four_png = pygame.image.load('assets\\city_building_four.png')
city_park_one_png = pygame.image.load('assets\\city_park_one.png')
city_restaurant_one_png = pygame.image.load('assets\\city_restaurant_one.png')

#country (morning) png building assets
country_house_one_png = pygame.image.load('assets\\country_house_one.png')
country_house_two_png = pygame.image.load('assets\\country_house_two.png')
country_barn_one_png = pygame.image.load('assets\\country_barn_one.png')
country_forest_one_png = pygame.image.load('assets\\country_forest_one.png')
country_forest_two_png = pygame.image.load('assets\\country_forest_two.png')

#initialize game
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('As I Wake')
clock = pygame.time.Clock()

#class for stationary assets
class stationary_asset:
    def __init__(self, image_name, width, height, x_location):
        self.image_name = image_name
        self.width = width
        self.height = height
        self.x_location = x_location
        self.y_location = 0

#class for star asset
class star_asset:
    def __init__(self):
        self.star_phase_tuple = star_png_tuple
        self.x_location = random.randint(20, 880)
        self.y_location = random.randint(20, 430)
        self.phase_start = random.randint(0, len(star_png_tuple)-1)
        self.time_since_last_phase = 0.0

#create stationary asset objects for cityscape
city_building_one = stationary_asset(city_building_one_png, 20, 150, 100)
city_building_two = stationary_asset(city_building_two_png, 300, 150, 180)
city_building_three = stationary_asset(city_building_three_png, 100, 150, 450)
city_building_four = stationary_asset(city_building_four_png, 100, 150, 520)
city_restaurant_one = stationary_asset(city_restaurant_one_png, 75, 150, 583)
city_park_one = stationary_asset(city_park_one_png, 125, 150, 130)

#create stationary asset objects for countryscape
country_house_one = stationary_asset(country_house_one_png, 300, 150, 450)
country_house_two = stationary_asset(country_house_two_png, 300, 150, 550)
country_barn_one = stationary_asset(country_barn_one_png, 100, 150, 232)
country_forest_one = stationary_asset(country_forest_one_png, 125, 150, 0)
country_forest_two = stationary_asset(country_forest_two_png, 125, 150, 650)

#tuples for city/town assets that change w/ day
stationary_assets_tuple_night = (city_building_one, city_building_two, city_park_one, city_building_three, city_restaurant_one, city_building_four);
stationary_assets_tuple_day = (country_house_one, country_house_two, country_barn_one, country_forest_one, country_forest_two);

#linked list node class
class linked_list_node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

#linked list class (single linked)
class linked_list:
    def __init__(self):
        self.head = None
        self.count = 0

    #function that adds new node to end of linked list
    def add_node(self, node_to_add):
        if self.head == None:
            self.head = node_to_add
           
        else:
            current_node = self.head
            for i in range(0, self.count):
                if current_node.next_node == None:
                    current_node.next_node = node_to_add
                    break
                current_node = current_node.next_node
        self.count = self.count+1

    #function that removes head from linked list, and makes next node the new had (if exists)
    def remove_head(self):
        if(self.head == None):
            return
        elif(self.count == 1):
            self.head = None
        else:
            self.head = self.head.next_node
        self.count = self.count-1
    
#class for moving asset options 
class moving_asset:

    #constructor
    def __init__(self):
        asset_png_tuple = city_moving_asset_png_tuple
        if day_status:
            asset_png_tuple = country_moving_asset_png_tuple
        image_chosen = random.randint(0, len(asset_png_tuple)-1)
        direction_chosen = random.randint(0, 1)
        self.image_name = asset_png_tuple[image_chosen]
        self.moving_left = True
        if(direction_chosen == 0):
            self.moving_left = False
        #self.moving_left = True
        self.x_location = 940
        if(self.moving_left):
            self.x_location = -40

    #function that moves asset
    def move_asset(self):
        if self.moving_left:
            return self.x_location +1
        return self.x_location -1

#class for firework assets
class firework_asset:

    #constructor
    def __init__(self):
        image_chosen = random.randint(0, len(firework_png_tuple)-1)
        self.image_name = firework_png_tuple[image_chosen]
        self.x_location = random.randint(20, 880)
        self.y_location = random.randint(20, 550)

#linked lists for assets
currently_moving = linked_list()
current_fireworks = linked_list()
current_stars = linked_list()

#function that displays current moving assets at their updated location
def update_moving_assets():
    current_node = currently_moving.head
    while current_node != None:
        current_node.data.x_location = current_node.data.move_asset()
        gameDisplay.blit(current_node.data.image_name, (current_node.data.x_location, 580))
        current_node = current_node.next_node

#function that updates phases of stars
def update_star_assets():
    current_node = current_stars.head
    current_time = time.time()
    while current_node != None:
        gameDisplay.blit(current_node.data.star_phase_tuple[current_node.data.phase_start], (current_node.data.x_location, current_node.data.y_location))
        if current_time - current_node.data.time_since_last_phase > 1:
            #time_since_last_phase = time.time()
            if current_node.data.phase_start < len(star_png_tuple)-1:
                current_node.data.phase_start = current_node.data.phase_start + 1
            else:
                current_node.data.phase_start = 0
            current_node.data.time_since_last_phase = time.time()
        current_node = current_node.next_node

#function that updates firework positions (if they currently exist)
def update_firework_assets():
    current_time = time.time()
    if(current_fireworks.head == None):
        return
    elif current_time - time_since_last_firework > 3:
        for i in range(0, firework_spawn_num):
            current_fireworks.remove_head()
    else:
        current_node = current_fireworks.head
        while current_node != None:
            current_node.data.y_location = current_node.data.y_location -5
            gameDisplay.blit(current_node.data.image_name, (current_node.data.x_location, current_node.data.y_location))
            current_node = current_node.next_node

#function that spawns sationary assets if not in a state of day transition and calls on update_stationary_assets()
#if in day transition 
def stationary_assets():
    if day_status:
        for i in range (0, len(stationary_assets_tuple_day)):
            stationary_assets_tuple_day[i].y_location = 450
            gameDisplay.blit(stationary_assets_tuple_day[i].image_name, (stationary_assets_tuple_day[i].x_location, stationary_assets_tuple_day[i].y_location))
    else:
        for i in range (0, len(stationary_assets_tuple_night)):
            stationary_assets_tuple_night[i].y_location = 450
            gameDisplay.blit(stationary_assets_tuple_night[i].image_name, (stationary_assets_tuple_night[i].x_location, stationary_assets_tuple_night[i].y_location))       
        
#function that clears any moving assets from currently_moving list 
def clear_offscreen_assets():
    #if currently_moving.count == 0 or currently_moving.head == None:
        #day_time()
    if(is_offscreen(currently_moving.head.data.x_location)):
        currently_moving.remove_head()

#function that returns True if moving asset is no longer on-screen
def is_offscreen(current_x_coord):
    if current_x_coord+80 < 0 or current_x_coord-80 > 900:
        return True
    return False

#function that spawns moving assets
def spawn_asset():
    global time_since_last_spawn
    current_time = time.time()
    if(time_since_last_spawn == 0.0 or current_time-time_since_last_spawn > 1):
        time_since_last_spawn = current_time
        node_to_add = linked_list_node(moving_asset())
        currently_moving.add_node(node_to_add)

#function that spawns fireworks
def spawn_fireworks():
    global time_since_last_firework
    global firework_spawn_num
    firework_spawn_num = random.randint(3, 6)
    time_since_last_firework = time.time()
    for i in range(0, firework_spawn_num):
        new_node = linked_list_node(firework_asset())
        current_fireworks.add_node(new_node)

def spawn_stars():
    star_count = random.randint(100, 250) 
    for i in range(0, star_count):
        new_star = star_asset()
        new_node = linked_list_node(new_star)
        current_stars.add_node(new_node)   

def despawn_stars():
    global current_stars
    current_stars = linked_list()
    #while current_stars.head != None:
    #    current_stars.remove_head

#function that reads user key input
def click_spawn(event):
    global day_status
    global time_since_last_transition
    global time_since_last_firework

    current_time = time.time()
    if event.type == pygame.KEYDOWN:

        #if up key pressed, change day time and transition old stationary assets upwards
        if event.key == pygame.K_UP and (time_since_last_transition == 0 or current_time - time_since_last_transition > 10):
            day_status = (not day_status)
            if not day_status:
                spawn_stars()
            else:
                despawn_stars()
            in_transition = True
            transition_upwards = True
            time_since_last_transition = current_time
            #time_of_day_transition(True)

        #if down key pressed, change day time and transition old stationary assets downwards    
        elif event.key == pygame.K_DOWN and (time_since_last_transition == 0 or current_time - time_since_last_transition > 10):
            day_status = (not day_status)
            if not day_status:
                spawn_stars()
            else:
                despawn_stars()

        #if s key pressed, spawn a new moving asset    
        elif event.key == pygame.K_s:
            spawn_asset()

        #if 'SPACE' key is pressed and correct fireworks conditions exist, spawn fireworks
        elif event.key == pygame.K_SPACE and (time_since_last_firework == 0.0 or current_time-time_since_last_firework > 5):
            if not day_status:
                spawn_fireworks()

#function that auto-spawns moving assets if less than 5 are currently on screen
def auto_spawn_assets():
    current_time = time.time()
    if(currently_moving.count < 2):
        spawn_asset()
    if(current_time-time_since_last_firework > 40 and not day_status):
        spawn_fireworks()

#function that displays night time assets
def night_time():
    gameDisplay.blit(night_sky, (0, 0))

#function that displays day time assets
def day_time():
    gameDisplay.blit(day_sky, (0, 0))

#function that runs 'As I Wake' game procedures
def as_I_wake_gameplay():
    crashed = False
    spawn_stars()
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        #background       
        gameDisplay.fill(black)
        click_spawn(event)
      
        if day_status:
            day_time()
        else:
            night_time()

        #bus = moving_asset(city_bus, True, 200)
        #currently_moving.append(bus)
        stationary_assets()
        update_moving_assets()
        update_firework_assets()
        update_star_assets()
        auto_spawn_assets()
        clear_offscreen_assets()
        pygame.display.update()
        clock.tick(60)
as_I_wake_gameplay()