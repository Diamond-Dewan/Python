class Resturent:
    name = ''
    woner = ''

    def details(self):
        print(self.name, self.woner)


# create new Resturent object
resturent = Resturent()

# set
resturent.name = "Hungry Chiken"
resturent.woner = "Jibel"

# call the function using object
resturent.details()
