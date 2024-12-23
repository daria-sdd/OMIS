from Model import User, Post, Blog, Comment, Reaction, Message

# Interface for services
class ICommentService:
    def processComment(self, text):
        pass

    def addComment(self, comment):
        pass

    def deleteComment(self, comment):
        pass

class IAuthService:
    def handleLogin(self, email, password):
        pass

    def handleRegistration(self, email, password):
        pass

    def showProfile(self, user):
        pass

    def updateProfile(self, user):
        pass

    def deleteProfile(self, user):
        pass

    def validateRegistration(self, email, password):
        pass

class IReactionService:
    def addReaction(self, reaction):
        pass

    def deleteReaction(self, reaction):
        pass

    def getReactions(self, post):
        pass

class IMessageService:
    def sendMessageToUser(self, sender, receiver, message):
        pass

    def getMessages(self, sender, receiver):
        pass

class IBlogService:
    def createBlog(self, blog):
        pass

    def deleteBlog(self, blog):
        pass

    def editBlog(self, blog):
        pass

    def addEditor(self, blog, editor):
        pass

    def removeEditor(self, blog, editor):
        pass

class IPostService:
    def createPost(self, post):
        pass

    def deletePost(self, post):
        pass

    def editPost(self, post):
        pass

    def getPost(self, postId):
        pass

# Interface for controllers
class ICommentController:
    def processComment(self, text):
        pass

    def addComment(self, comment):
        pass

    def deleteComment(self, comment):
        pass

class IAuthController:
    def handleLogin(self, email, password):
        pass

    def handleRegistration(self, email, password):
        pass

    def showProfile(self, user):
        pass

    def updateProfile(self, user):
        pass

    def deleteProfile(self, user):
        pass

    def validateRegistration(self, email, password):
        pass

class IReactionController:
    def addReaction(self, reaction):
        pass

    def deleteReaction(self, reaction):
        pass

    def getReactions(self, post):
        pass

class IMessageController:
    def sendMessageToUser(self, sender, receiver, message):
        pass

    def getMessages(self, sender, receiver):
        pass

class IBlogController:
    def createBlog(self, blog):
        pass

    def deleteBlog(self, blog):
        pass

    def editBlog(self, blog):
        pass

    def addEditor(self, blog, editor):
        pass

    def removeEditor(self, blog, editor):
        pass

class IPostController:
    def createPost(self, post):
        pass

    def deletePost(self, post):
        pass

    def editPost(self, post):
        pass

    def getPost(self, postId):
        pass

# Controllers
class CommentController(ICommentController):
    def __init__(self, commentService):
        self.commentService = commentService

    def processComment(self, text):
        pass

    def addComment(self, comment):
        pass

    def deleteComment(self, comment):
        pass

class AuthenticationController(IAuthController):
    def __init__(self, authService):
        self.authService = authService

    def handleLogin(self, email, password):
        pass

    def handleRegistration(self, email, password):
        pass

    def showProfile(self, user):
        pass

    def updateProfile(self, user):
        pass

    def deleteProfile(self, user):
        pass

    def validateRegistration(self, email, password):
        pass

class ReactionController(IReactionController):
    def __init__(self, reactionService):
        self.reactionService = reactionService

    def addReaction(self, reaction):
        pass

    def deleteReaction(self, reaction):
        pass

    def getReactions(self, post):
        pass

class MessageController(IMessageController):
    def __init__(self, messageService):
        self.messageService = messageService

    def sendMessageToUser(self, sender, receiver, message):
        pass

    def getMessages(self, sender, receiver):
        pass

class BlogController(IBlogController):
    def __init__(self, blogService):
        self.blogService = blogService

    def createBlog(self, blog):
        pass

    def deleteBlog(self, blog):
        pass

    def editBlog(self, blog):
        pass

    def addEditor(self, blog, editor):
        pass

    def removeEditor(self, blog, editor):
        pass

class PostController(IPostController):
    def __init__(self, postService):
        self.postService = postService

    def createPost(self, post):
        pass

    def deletePost(self, post):
        pass

    def editPost(self, post):
        pass

    def getPost(self, postId):
        pass

class MainController:
    def __init__(self):
        self.controllers = []

    def initControllers(self):
        pass
