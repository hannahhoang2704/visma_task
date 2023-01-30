# Visma task and requirements
The task is to design and implement a class which is responsible for identifying what kind of requests it receives. Other apps can call the identity app using the scheme visma-identity.

A uri consists of three parts:
Example: visma-identity://login?source=severa
Scheme: visma-identity
Path: login
Parameters: source=severa

The class needs to satisfy the following requirements:
1. It takes the following information as input
    URI (type: string)
    Example: visma-identity://login?source=severa
2. It has to parse and validate that:
    Used URI scheme is right: visma-identity
    Path is one of the allowed: login, confirm or sign
3. All parameters for a path are valid
4. Requirements for the parameters:
      - Path login:
      source(type:string)
      Example: visma-identity://login?source=severa
      - Path confirm:
      source(type:string)
      payment number(type:integer)
      Example: visma-identity://confirm?source=netvisor&paymentnumber=102226
      - Path sign:
     source(type: string)
     documentid(type:string)
     Example: visma-identity://sign?source=vismasign&documentid=105ab44
5. Class returns:
     Path
     Parameters as key value pairs
6. Is designed using the practises of object-oriented programming
7. Implementation needs to have a client, which uses the new class. You can for example implement the client as another class that uses the relevant methods.

#Description

The purpose of the task was to design and implement a class to help Visma solutions’ identity management application. The class designed is responsible for identifying the requests it receives and enabling other applications to call on it by using visma-identity scheme. 

The URI (Uniform Resource Identifier) includes three parts: scheme (protocol to access the resource), path (location of the resource within the scheme) and source parameter (in the example it’s Severa, a project management tool by Visma). 

The first thing to think about is to make a function that would take in the full URI string and parse it by using for example python’s urlib.parse module. However, since URI does not consist of “netloc” which consequently leads to the problems that the path is parsed in the key “netloc” and the “path” value is empty. Therefore, to solve this problem, split() method was implemented to extract different parts in the URI. The split() method does this by parsing the URI into three (scheme, path & parameters), and then checking that the scheme is equal to “visma-identity”, the path is one of the three allowed ones (“login”, “confirm” or “sign”), and finally checking that the parameters meet the requirements (this is done in a separate method).

After designing and implementing the class, we use associate class Client to process and check the given URI. It calls upon the corresponding methods of the first function and returns the path and parameter dictionary of the URI. 

The classes/functions designed have several shortcomings. One of the challenges it would face is if the URI scheme is outside of “visma-identity” , the path is not login/confirm/sign or the parameters are not in correct format. It would require testing and more validation before it could be used. Additionally, the client should get notified if any specific part in URI is not valid. This could be done by implementing an error handling system to the code, which would make the error handling more user-friendly. The class is also missing security features such as encryption, and it probably wouldn’t scale well if it received a large number of URI’s. However, it could be a starting point for further design and after more testing and design it could even be implemented into a production environment. 
