class RequestIdentity:
    def __init__(self, uri:str, path=None):
        self.uri = uri
        self.scheme = "visma-identity"
        self.valid_paths = ["login", "confirm", "sign"]
        self.path = path
        self.params = {}
        self.uri_parsed()

    def uri_parsed(self):
        uri_scheme, uri_query = self.uri.split("://")       #split the uri into 2 parts: scheme and query
        uri_path, uri_params = uri_query.split("?")         # split query in 2 parts: path and parameters

        if uri_scheme != self.scheme or uri_path not in self.valid_paths:
            print("Invalid scheme or path")
            return False
        self.path = uri_path                                #assign path

        separated_params = uri_params.split("&")            #split between different parameters
        for i in separated_params:
            key, value = i.split("=")                        #split between parameters keys and value
            self.params[key] = value

        return True

    def check_params(self):                                 #check if parameters are valid
        if self.uri_parsed():
            if self.path == self.valid_paths[0]:            #login path
                if "source" not in self.params:
                    return False
            elif self.path == self.valid_paths[1]:          #confirm path
                if "source" not in self.params or "paymentnumber" not in self.params:
                    return False
                if not self.params["paymentnumber"].isdigit():
                    return False
                self.params['paymentnumber'] = int(self.params['paymentnumber'])            #convert string payment number to integer
            elif self.params == self.valid_paths[2]:        #sign path
                if "source" not in self.params or "documentid" not in self.params:
                    return False
            return True

    def __str__(self):
        return f"{self.path}{self.params}"

class Client:
    def __init__(self, uri:str):
        self.request = RequestIdentity(uri)

    def return_path_params(self):
        answer = self.request.check_params()
        if not answer:
            return "Invalid parameters"
        return f"Path: {self.request.path}\nParameters: {self.request.params}"



client = Client("visma-identity://confirm?source=netvisor&paymentnumber=102226")
print(client.return_path_params())

