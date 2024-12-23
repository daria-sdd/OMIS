# Base class for database context
class DBContext:
    pass

# Interfaces for repositories
class IReactionRepository:
    def addReaction(self, reaction):
        pass

    def deleteReaction(self, reaction):
        pass

    def getReaction(self, reaction):
        pass

class IPostRepository:
    def processPost(self, postBody):
        pass

    def deletePost(self, post):
        pass

    def getPost(self, post):
        pass

class ICommentRepository:
    def processComment(self, textComment):
        pass

    def deleteComment(self, comment):
        pass

    def getComment(self, comment):
        pass

class IBlogRepository:
    def getBlog(self, name):
        pass

    def setBlog(self, blog):
        pass

class IAuthRepository:
    def getUser(self, username):
        pass

    def createUser(self, user):
        pass

    def deleteUser(self, user):
        pass

class IMessageRepository:
    def sendMessage(self, message):
        pass

    def getMessages(self, sender, receiver):
        pass

# Interfaces for services
class IReactionService:
    def addReaction(self, reaction):
        pass

    def deleteReaction(self, reaction):
        pass

    def getReactions(self, post):
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

class ICommentService:
    def addComment(self, comment):
        pass

    def deleteComment(self, comment):
        pass

    def processComment(self, text):
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

class IAuthService:
    def login(self, email, password):
        pass

    def register(self, email, password):
        pass

    def getUserProfile(self, user):
        pass

    def updateUserProfile(self, user):
        pass

    def deleteUserProfile(self, user):
        pass

    def validateRegistration(self, email, password):
        pass

class IMessageService:
    def sendMessageToUser(self, sender, receiver, message):
        pass

    def getMessages(self, sender, receiver):
        pass

# Repository classes
class ReactionRepository(IReactionRepository):
    def __init__(self, databaseContext: DBContext):
        pass

class PostRepository(IPostRepository):
    def __init__(self, databaseContext: DBContext):
        pass

class CommentRepository(ICommentRepository):
    def __init__(self, databaseContext: DBContext):
        pass

class BlogRepository(IBlogRepository):
    def __init__(self, databaseContext: DBContext):
        pass

class AuthRepository(IAuthRepository):
    def __init__(self, databaseContext: DBContext):
        pass

class MessageRepository(IMessageRepository):
    def __init__(self, databaseContext: DBContext):
        pass

# Service classes
class ReactionService(IReactionService):
    def __init__(self, reactionRepository: IReactionRepository):
        pass

class PostService(IPostService):
    def __init__(self, postRepository: IPostRepository):
        pass

class CommentService(ICommentService):
    def __init__(self, commentRepository: ICommentRepository):
        pass

class BlogService(IBlogService):
    def __init__(self, blogRepository: IBlogRepository):
        pass

class AuthService(IAuthService):
    def __init__(self, authRepository: IAuthRepository):
        pass

class MessageService(IMessageService):
    def __init__(self, messageRepository: IMessageRepository):
        pass

# Models
class Reaction:
    def __init__(self, reactionType):
        self.reactionType = reactionType

class PostBody:
    def __init__(self, input):
        self.input = input

class Post:
    def __init__(self, uuid, body: PostBody, author, tags):
        self.uuid = uuid
        self.body = body
        self.author = author
        self.tags = tags

class Comment:
    def __init__(self, uuid, post, author, createdAt):
        self.uuid = uuid
        self.post = post
        self.author = author
        self.createdAt = createdAt

class Blog:
    def __init__(self, name, owner, editors):
        self.name = name
        self.owner = owner
        self.editors = editors

class User:
    def __init__(self, uuid, username, email, roles):
        self.uuid = uuid
        self.username = username
        self.email = email
        self.roles = roles

class Message:
    def __init__(self, uuid, content, sent_by, received_by, timestamp):
        self.uuid = uuid
        self.content = content
        self.sent_by = sent_by
        self.received_by = received_by
        self.timestamp = timestamp

# Supporting classes
class ReactionType:
    LIKE = "LIKE"
    DISLIKE = "DISLIKE"

class Role:
    ADMIN = "ADMIN"
    AUTHOR = "AUTHOR"
    READER = "READER"
