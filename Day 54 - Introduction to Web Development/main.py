
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in == True:
                function(args[0])
        return wrapper

    @is_authenticated_decorator
    def create_blog_post(user):
        print(f"This is {user.name}'s new blog post.")


new_user = User("Felipe")
new_user.is_logged_in = True
new_user.create_blog_post()


class Player:
    def __init__(self, name):
        self.name = name
        self.is_created = False

    def is_created_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_created == True:
                function(args[0])
        return wrapper

    @is_created_decorator
    def create_player(player):
        print(f"{player.name} is now an active player.")


player = Player("Felipe")
player.is_created = True
player.create_player()
