from uri import URI

class Identifier:
    def identify(self, givenUri):
        uri = URI(givenUri)

        # Dummy check to see the URI can even be valid
        # 30 is slightly less than realistic minimum length
        # but should eliminate much of the noise
        if len(uri.uri) < 30:
            return self.wrongID(0)

        # Split to fetch URI.
        # If split fails (there is no '://') then the
        # whole string is taken and comparison fails.
        splitUri = uri.uri.split("://")
        uri.scheme = splitUri[0]
        if uri.checkScheme() == False:
            return self.wrongID(1)

        # Split path and parameters
            
        pathSplit = splitUri[1].split("?")
        # gets 'confirm?source=netvisor&paymentnumber=102226'
        # gives 'confirm' 'source=netvisor&paymentnumber=102226'

        # The comparison fails if path is incorrect,
        # or if there is no '?' in the uri.
        uri.path = pathSplit[0]
        if uri.checkPath() == False:
            return self.wrongID(2)
        
        # Using a method to check and set parameters.
        # Returns True if everything is OK, else false
        if uri.checkParameters(pathSplit[1]) == False:
            return self.wrongID(3)


        # Reaching this point means the URI is valid.
        # Returns the following
        # Path: path
        # Parameters: [Parameter1, Value1][Parameter2, Value2]
        return uri.returnString()


    # Method for printing errors
    def wrongID(self, errorCode):
        if errorCode == 0:
            errorMessage = "The URI is too short"
        elif errorCode == 1:
            errorMessage = "The URI Scheme is incorrect"
        elif errorCode == 2:
            errorMessage = "PATH is incorrect"
        elif errorCode == 3:
            errorMessage = "The URI contains incorrect parameter(s)"
        else:
            return "Unspecified error."
        return f"{errorMessage}. Please try again."

#eof