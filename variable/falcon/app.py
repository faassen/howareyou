import falcon


class Welcome(object):

    def on_get(self, req, resp, name):
        resp.status = falcon.HTTP_200
        resp.body = ('User: %s' % name)


main = falcon.API(media_type='text/plain')
main.add_route('/users/{name}', Welcome())
