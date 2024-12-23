# main.py
from flask import Flask
from View import index, blog, blog_page, chats, friend, popular, profile, register

class RunPlatform:
    def run_platform(self):
        app = Flask(__name__)

        # Route bindings
        app.add_url_rule('/', view_func=index)
        app.add_url_rule('/blog', view_func=blog)
        app.add_url_rule('/blog_page', view_func=blog_page)
        app.add_url_rule('/chats', view_func=chats)
        app.add_url_rule('/friend', view_func=friend)
        app.add_url_rule('/popular', view_func=popular)
        app.add_url_rule('/profile', view_func=profile)
        app.add_url_rule('/register', view_func=register)

        app.run(debug=True)

if __name__ == '__main__':
    platform = RunPlatform()
    platform.run_platform()
