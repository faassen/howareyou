import morepath


class App(morepath.App):
    pass


@App.path('/welcome')
class Welcome(object):
    pass


@App.view(model=Welcome)
def root_default(self, request):
    return "Hello World!"

# from version 0.4 until 0.12. 0.13 breaks this
#config = morepath.setup()
#config.scan()
#config.commit()

# 0.13
# morepath.commit(App)

# from 0.14
App.commit()

main = App()
