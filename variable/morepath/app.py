import morepath


class App(morepath.App):
    pass


class User(object):
    def __init__(self, name):
        self.name = name


@App.path('/users/{name}', model=User)
def get_user(name):
    return User(name)


@App.view(model=User)
def root_default(self, request):
    return "User: %s" % self.name


# from version 0.4 until 0.12. 0.13 breaks this
#config = morepath.setup()
#config.scan()
#config.commit()

# 0.13
# morepath.commit(App)

# from 0.14
App.commit()

main = App()
