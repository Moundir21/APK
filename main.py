from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty
from kivy.vector import Vector
from random import randint, choice
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse

# ألوان عشوائية
colors = [
    (1, 0, 0),  # أحمر
    (0, 1, 0),  # أخضر
    (0, 0, 1),  # أزرق
    (1, 1, 0),  # أصفر
    (1, 0, 1),  # بنفسجي
    (0, 1, 1),  # سماوي
]

class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    color = ListProperty([1, 0, 0])  # لون افتراضي أحمر

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.c = Color(*self.color)
            self.shape = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics, size=self.update_graphics, color=self.update_color)

    def update_graphics(self, *args):
        self.shape.pos = self.pos
        self.shape.size = self.size

    def update_color(self, *args):
        self.c.rgb = self.color

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # إنشاء الكرة
        self.ball = Ball(pos=(randint(100, 400), randint(100, 400)), size=(50, 50))
        self.ball.velocity = Vector(4, 4)
        self.add_widget(self.ball)

        # عرض النقاط
        self.score_label = Label(text=f"Score: {self.score}", font_size=24, pos=(10, self.height - 40))
        self.add_widget(self.score_label)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.ball.move()

        # الاصطدام بالحواف
        bounced = False
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            bounced = True
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
            bounced = True

        # عند الاصطدام
        if bounced:
            # تغيير اللون عشوائياً
            self.ball.color = choice(colors)
            # زيادة السرعة تدريجياً
            self.ball.velocity_x *= 1.05
            self.ball.velocity_y *= 1.05
            # تحديث النقاط
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

class PongApp(App):
    def build(self):
        game = PongGame()
        return game

if __name__ == '__main__':
    PongApp().run()
