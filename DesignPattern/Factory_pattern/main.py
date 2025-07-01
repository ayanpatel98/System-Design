from ShapeFactory import ShapeFactory

if __name__=="__main__":
    factory = ShapeFactory()
    shape = factory.getShape('rectangle')
    shape.draw()
