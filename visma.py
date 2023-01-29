from urllib.parse import urlsplit, parse_qs



class RequestIdentity:
    def __init__(self, uri:str, path=None):
        self.uri = uri
        self.scheme = "visma-identity"
        self.path = path
        self.accepted_path_list = ['login', 'confirm', 'sign']
        self.parameters = {}

    
    def uri_parse(self):
       uri_split_result = urlsplit(self.uri)
       if uri_split_result.scheme != self.scheme:   #check if scheme is valid
           print("Invalid scheme or path")

       if uri_split_result.path not in self.accepted_path_list:     #check if path is valid
           print("Invalid path")

       self.path = uri_split_result.path


       if self.path == self.accepted_path_list[0]: #if path is 'login'
           return self.login_parameter()
       elif self.path == self.accepted_path_list[1]: #if path is 'confirm'
           return self.confirm_parameter()
       elif self.path == self.accepted_path_list[2]: #if path is 'sign'
           return self.sign_parameter()







       
        



