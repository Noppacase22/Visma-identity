class URI:
    def __init__(self, uri):
        self.uri = uri
        self.scheme = ""
        self.path = ""
        self.parameters = []

    def checkScheme(self):
        acceptedSchemes = ['visma-identity']
        if self.scheme in acceptedSchemes:
            return True
        else:
            return False

    def checkPath(self):
        acceptedPaths = ["login", "confirm", "sign"]
        if self.path in acceptedPaths:
            return True
        else:
            return False

    def checkParameters(self, parameterString):
        parameterSplit = parameterString.split("=")
        # gets 'source=netvisor&paymentnumber=102226'
        # gives 'source', 'netvisor&paymentnumber', '102226'

        parameter1Name = parameterSplit[0]
        
        # Paths 'confirm' and 'sign' have 2 parameters
        if self.path == "confirm" or self.path == "sign":
            # In case there isn't 2 parameters (or 2 '=' to be precise)
            if len(parameterSplit) != 3:
                return False
            
            ampersandSplit = parameterSplit[1].split("&")
            # gets 'netvisor&paymentnumber'
            # gives 'netvisor', 'paymentnumber'

            parameter1Value = ampersandSplit[0]
            parameter2Name = ampersandSplit[1]
            parameter2Value = parameterSplit[2]
            
        else:
            # If the path is 'login', there is only one parameter.
            # The remaining string of parameterSplit is the value.
            parameter1Value = parameterSplit[1]


        # First parameter must be 'source'
        if parameter1Name != "source":
            return False

        if self.path == "confirm":
            if parameter2Name != "paymentnumber":
                return False

            # 'paymentnumber' must be of type integer
            try:
                integerCheck = int(parameter2Value)
            except:
                return False

        elif self.path == "sign":
            if parameter2Name != "documentid":
                return False

        elif self.path == "login":
            # check no additional parameters have made it here
            if "&" in parameter1Value:
                return False
        
        self.parameters.append([parameter1Name, parameter1Value])
        if self.path != "login":
            self.parameters.append([parameter2Name, parameter2Value])
        return True

    def returnString(self):
        returnable = "Path: " + self.path + "\nParameters: "
        for parameter in self.parameters:
            returnable += str(parameter)
        return returnable

    # Not in use
    def getPath(self):
        return self.path
    
    # Not in use
    def getParameters(self):
        s = ""
        for parameter in self.parameters:
            s += parameter
        return s