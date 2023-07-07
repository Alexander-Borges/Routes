from flask import Flask # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"
@app.route('/') # The '@' decorator associates this route with the function immediately following.
def hello_world():
    return 'Hello World' # Return the string 'Hello World' as a response

# import statements, maybe some other routes
@app.route('/success')
def success():
    return 'success'

# What if we wanted to be able to say "Hello, Michael" or "Hello, Amy" or "Hello, Wes"? We could make three routes, but that feels pretty repetitive. Also, every time we want to include someone else, we would need to create a new route. This is a great opportunity to add variable rules to our routes. For the example above, we could make the name a variable, like so:
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

# We can add as many of these we need, giving each variable a different name:
@app.route('/users/<username>/<id>') # for a route '/users/___/___'. two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username) 
    print(id)
    return "username: " + username + ". id: " + id

# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>')
def hello_num(name, num):
    return f"Hello, {name * num}"


    # app.run(debug=True) should be the very last statement
if __name__ =="__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True) # Run the app in debug mode