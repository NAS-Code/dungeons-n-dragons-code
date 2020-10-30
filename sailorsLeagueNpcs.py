import random


class ImportantNpc:
    def __init__(self, name, prof_bonus, dex, int, cha, distance, bombs):
        self.name = name
        self.prof_bonus = prof_bonus
        self.dex = dex
        self.int = int
        self.cha = cha
        self.distance = distance
        self.bombs = bombs

    def d20_roll(self):
        return random.randint(1,20)

    def start_position(self):
        position = self.d20_roll() + self.dex + self.prof_bonus
        return self.name, 'start position:', position

    def chicken(self):
        score = self.d20_roll() + self.cha
        return self.name, 'chicken score:', score

    def read_wind(self):
        nature = self.d20_roll() + self.int + self.prof_bonus
        if nature == 20 + self.int + self.prof_bonus:
            self.distance += 60
            print('Crit success')
        elif nature >= 13:
            self.distance += 50
            print('Success')
        elif 13 > nature >= 2 + self.int + self.prof_bonus:
            s_or_t = random.randint(1, 2)
            if s_or_t == 1:
                self.distance += 50
            else:
                self.distance += 25
            print('Fail')
        else:
            self.distance += 25
            print('Crit fail')
        return self.name, 'distance:', self.distance

    def round_buoy(self):
        acrobatics = self.d20_roll() + self.dex + self.prof_bonus
        if acrobatics == 20 + self.dex + self.prof_bonus:
            self.distance += 10
            print('Crit success')
        elif acrobatics >= 15:
            print('Success')
        elif 15 > acrobatics >= 2 + self.dex + self.prof_bonus:
            self.distance -= 25
            print('Fail')
        else:
            self.distance -= 25
            print('Crit fail, no spinnaker first round downwind')
        return self.name, 'distance:', self.distance

    def downwind_sailing(self):
        check = input('Is your spinnaker up? (yes or no): ')
        if check[0].lower() == 'y':
            dc = 16
            movement = 75
        else:
            dc = 14
            movement = 50
        acrobatics = self.d20_roll() + self.dex + self.prof_bonus
        if acrobatics == 20 + self.dex + self.prof_bonus:
            self.distance += movement + 20
            print('Crit success!')
        elif acrobatics >= dc:
            self.distance += movement
            print('Success')
        elif dc > acrobatics >= 2 + self.dex + self.prof_bonus:
            self.bombs += 1
            if self.bombs == 1:
                if movement == 75:
                    self.distance += 35
                else:
                    self.distance += 50
                print('Fail')
                print('Bomb count:', self.bombs)
            elif self.bombs == 3:
                print('Fail')
                print('Ship blows up!')
            else:
                print('Fail')
                print('Bomb count:', self.bombs)

        else:
            self.bombs += 2
            if self.bombs >= 3:
                print('Crit fail')
                print('The boat blows up!')
            else:
                print('Crit fail')
                print('Bomb count:', self.bombs)
        return self.name, 'distance:', self.distance


# -------- L O G I C --------

keel_spraylog = ImportantNpc('Keel Spraylog',2,5,2,4,0,0)

print(keel_spraylog.start_position())

print(keel_spraylog.chicken())

while keel_spraylog.distance < 250:
    print(keel_spraylog.read_wind())

print(keel_spraylog.round_buoy())

while keel_spraylog.distance < 500:
    print(keel_spraylog.downwind_sailing())
    if keel_spraylog.bombs >=3:
        break
