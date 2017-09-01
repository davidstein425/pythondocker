from werkzeug.security import generate_password_hash, check_password_hash

import main


class User(main.db.Model):
    """
    Create a User table
    """

    # Ensure this table will be named in plural not in singular
    __tablename__ = 'users'

    user_id = main.db.Column(main.db.Integer, primary_key=True)
    email = main.db.Column(main.db.String(100), index=True, unique=True)
    password_hash = main.db.Column(main.db.String(128))
    inserted_on = main.db.Column(main.db.DateTime)
    updated_on = main.db.Column(main.db.DateTime)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed property
        """
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User: {}>'.format(self.email)

