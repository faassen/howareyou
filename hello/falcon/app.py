import falcon


class Welcome(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Hello World!')


main = falcon.API(media_type='text/plain')
main.add_route('/welcome', Welcome())
