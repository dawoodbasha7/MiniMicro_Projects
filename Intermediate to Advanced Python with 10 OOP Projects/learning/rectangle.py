from random import randint

class Point:

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowerleft.x < self.x < rectangle.upright.y and \
            rectangle.lowerleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lowerleft, upright):
        self.lowerleft=lowerleft
        self.upright=upright

    def area_of_rectangle(self):
        return (self.upright.x-self.lowerleft.x)*(self.upright.y-self.lowerleft.y)



rectanglex=Rectangle(Point(randint(0,9), randint(0,9)),
                     Point(randint(10,19), randint(10,19)))
print("Rectangle coordinates are: (",
      rectanglex.lowerleft.x," ,",
      rectanglex.lowerleft.y,") and (",
      rectanglex.upright.x," ,",
      rectanglex.upright.y,")"
      )

user_point=Point(float(input("Guess x: ")),
                 float(input("Guess y: ")))



print("your point is inside the above rectangle: ",
      user_point.falls_in_rectangle(rectanglex))


print("area of the rectangle: ",
      rectanglex.area_of_rectangle()
      )