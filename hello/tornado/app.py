import tornado.web


class WelcomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello World!")


urls = [
    (r"/welcome", WelcomeHandler),
]

if __name__ == "__main__":
    import tornado.ioloop
    app = tornado.web.Application(urls, debug=False)
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
else:
    import tornado.wsgi
    main = tornado.wsgi.WSGIApplication(urls)
