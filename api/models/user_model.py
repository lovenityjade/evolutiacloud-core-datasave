# user_model.py - User model (for future use)
class User:
    def __init__(self, userid, username, permissions, patreontier):
        self.userid = userid            # User ID
        self.username = username        # Username
        self.permissions = permissions  # Permissions: userperm_new/confirm/admin
        self.patreontier = patreontier  # Patreon tier: 0,1,2,3
