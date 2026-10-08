class Light:
    def turn_on(self):
        print('Light is turned on!')

class Music:
    def turn_on(self):
        print('Music in on!')

class SmartHome(Light, Music):
    def play(self):
        print('Alternative play!')
    
    def start(self):
        print('Smart house in on!')
        self.turn_on()
        # self.play()

sm = SmartHome()

sm.start()
print(SmartHome.mro())