# def my_decorator(func):
#   def wrapper():
#     print("Before")
#     func()
#     print("After")
#   return wrapper

# #it wraps hello inside another function and used to pass it to the another function can also modify the function behaviour
# @my_decorator
# def hello():
#   print("hello")
# hello()


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
 


 