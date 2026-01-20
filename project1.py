class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to ChatBook! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            print("Thank you for visiting ChatBook. Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email
        self.password = password
        print("Signup successful! You can now signin.\n")
        self.menu()

    def signin(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self.username and password == self.password:
            self.loggedin = True
            print("Signin successful! Welcome back.\n")
        else:
            print("Signin failed! Incorrect email or password.\n")
        self.menu()

    def write_post(self):
        if self.loggedin:
            post_content = input("Write your post: ")
            print(f"Your post has been published!\n-> {post_content}")
        else:
            print("You need to signin first to write a post.\n")
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend_name = input("Enter your friend's name:")
            message = input("Enter your message:")
            print(f"Message sent to {friend_name}!\n-> {message}")
        else:
            print("You need to signin first to message a friend.\n")
        self.menu()


obj = chatbook()