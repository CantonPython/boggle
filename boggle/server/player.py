'''You can instantiate the Player object by supplying the username and password.  The hash is automatically generated.
>>> player = Player('user', 'pass') # Instantiating the class with a username of "user" and a password of "pass"
>>> player.username
'user'
>>> player.password # This will not return the password supplied, but a hash of it
'5b722b307fce6c944905d132691d5e4a2214b7fe92b738920eb3fce3a90420a19511c3010a0e7712b054daef5b57bad59ecbd93b3280f210578f547f4aed4d25'
>>> player.authenticate('pass') # Checking if the password is "pass"
True
>>> player.authenticate('password') # Checking if the password is "password"
False
>>> player.password = 'password' # This will set the password to "password"
>>> player.password # The password was not ovverwritten with the value "password", but a hash of it
'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
>>> player.authenticate('password') # A confirmation that the password was set to "password"
True
>>> del player.password # This will not delete the password, but set it to a hash of an empty string, as there must be a password property
>>> player.password
'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
>>> player.authenticate('')
True
>>> player2 = Player('user', 'pass')
>>> player.id == player2.id # Each player's ID will be randomly generated at time of instantiation
False
'''
from hashlib import sha512
from uuid import uuid4
class Password:
    def __init__(self, password):
        self.__set__(self, password)
    def __get__(self, instance, owner):
        return self.__password_hash
    def __set__(self, instance, value):
        self.__password_hash = sha512(value.encode()).hexdigest()
    def __delete__(self, instance):
        self.__set__(self, '')
class Player:
    password = Password('')
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = uuid4()
    def authenticate(self, password):
        return sha512(password.encode()).hexdigest() == self.password    
def main():
    from doctest import testmod
    testmod()
def test():
    return main()
if __name__ == '__main__': main()
