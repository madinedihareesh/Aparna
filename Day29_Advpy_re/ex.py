import re
'''
\d(digits)
\D(non digits)
\w(a-zA-z)(word charts)
\W( !@#$%^&*0-9)(non-word chars)
\s(white space tab \f)
\S non white spaces
\A indicating strating of the string
\z ending of the string
'''
# pat='\A[\w\W\.\d]+@[\w]+\.(com|in)\Z' ##email
# string='welcome.1234@gmail.com'
# print(re.fullmatch(pat,string))

# pas='\A[A-Z]{1,}[\w\W\.]{8,16}\Z'
# string='Sunny@1234'
# print(re.fullmatch(pas,string))

# pas='\A[6-9]{1}[\d]{9}\Z'
# sat='5125700757'
# print(re.fullmatch(pas,sat))

