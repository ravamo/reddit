
class Reddit:

    def __init__(self, subreddits='', post=0, points=0, id=0):
        self.subreddits = subreddits
        self.post = post
        self.points = points
        self.id = id

    def get_subreddits(self):
        return self.subreddits

    def set_subreddits(self, subreddits):
        self.subreddits = subreddits


    def get_post(self):
        return self.post


    def set_post(self, post):
        self.post = post


    def get_points(self):
        return self.points

    def set_points(self , points):
        self.points = points

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id