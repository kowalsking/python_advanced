class Auth:
    isAuthed: bool = False

    def login(self):
        self.isAuthed = True
        
    def logout(this):
        this.isAuthed = False
        
auth_service = Auth()
auth_service.login()
auth_service.logout()
# Auth.login(auth_service)
print(auth_service.isAuthed)
        