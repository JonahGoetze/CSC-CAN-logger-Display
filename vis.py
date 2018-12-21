from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock

from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'fullsreen', 1)
Config.set('graphics', 'show_cursor', 0)
Config.set('graphics', 'borderless', 1)
Config.set('graphics', 'max_fps', 30)
Config.set('graphics', 'allow_screensaver', 0)
Config.write()

import random
import math


class Gague(Widget):
    max_value = NumericProperty(1)
    value = NumericProperty(0)
    current_gague_width = NumericProperty(100)

    threshold_1 = NumericProperty(65)
    threshold_2 = NumericProperty(80)
    threshold_3 = NumericProperty(95)

    threshold_1_color = ListProperty([1,   1, 0, 1])
    threshold_2_color = ListProperty([1, 0.5, 0, 1])
    threshold_3_color = ListProperty([1,   0, 0, 1])

    default_bar_color = ListProperty([0, 1, 0, 1])
    bar_color = ListProperty([0, 1, 0, 1])

    title = StringProperty("Temperature")

    def set_value(self, value):
        self.value = value
        percent = self.value / self.max_value
        self.current_gague_width = math.floor(self.width * percent)

        percent

        if (self.threshold_3 != 0 and
            percent >= (self.threshold_3/self.max_value)):
            self.bar_color = self.threshold_3_color
        elif(self.threshold_2 != 0 and
            percent >= (self.threshold_2/self.max_value)):
            self.bar_color = self.threshold_2_color
        elif(self.threshold_1 != 0 and
            percent >= (self.threshold_1/self.max_value)):
            self.bar_color = self.threshold_1_color
        else:
            self.bar_color = self.default_bar_color



class Root(Widget):
    speed_gague = ObjectProperty(None)
    throttle_gague = ObjectProperty(None)
    rpm_gague = ObjectProperty(None)
    temp_gague = ObjectProperty(None)
    count = 0

    def update(self, delta):
        if self.count < 100:
            self.count = min(self.count+1, 100)
        else:
            self.count = max(self.count-random.randint(0, 50), 0)

        self.speed_gague.set_value(int(self.count/100 * self.speed_gague.max_value))
        self.rpm_gague.set_value(int(self.count/100 * self.rpm_gague.max_value))
        self.throttle_gague.set_value(int(self.count/100 * self.throttle_gague.max_value))
        self.temp_gague.set_value(self.count/100 * self.temp_gague.max_value)



class VisApp(App):
    def build(self):
        root = Root()
        Clock.schedule_interval(root.update, 1.0/20.0)

        return root


if __name__ == '__main__':
    VisApp().run()
