#import hmac
#import hashlib
#import base64
#dig = hmac.new(b'1234567890', msg=your_bytes_string, digestmod=hashlib.sha256).digest()
#base64.b64encode(dig).decode()      # py3k-mode
#'Nace+U3Az4OhN7tISqgs1vdLBHBEijWcBeCqL5xN9xg='
#######################

import hashlib
secretKey = "1234567890"
givenString = "foobar"
m = hashlib.sha256()

# Get string and put into givenString.

m.update(givenString + secretKey)
m.digest()