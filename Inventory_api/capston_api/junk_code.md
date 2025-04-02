 <!-- class LoginView(APIView):
#     def post(self, request):
#         """
#         extract the username and password from the request using the get method
#         we used the .get() because if the key is missing it wil return none instead of raisng an error
#         check if the user credentials are provided,
#         # if the correct credentials are goven, authenitcate the user
#         # check the provided credetial and user the log the user in
#         """
#         username = request.data.get('username') 
#         password = request.data.get('password')
       
#         if not username or not password:
#             return Response(
#                 {'error':'username and password required'},
#                 status= status.HTTP_400_BAD_REQUEST)
            
#         user = authenticate(username=username, password=password)  
        
#         if user is not None:
#             payload = {
#                 'id':user.id,
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#                 'iat': datetime.datetime.utcnow()
#             }
#             token =  jwt.encode(payload, 'secret', algorithm='HS256')
#             return Response(
#                 {'jwt': token},
#                 status=status.HTTP_200_OK )
#         else:
#             return Response(
#                 {'message':' invalide credentials'},
#                 status=status.HTTP_401_UNAUTHORIZED
#             ) -->