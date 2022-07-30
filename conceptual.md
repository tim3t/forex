### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

> TDT: Syntax is different between the two languages.  In Python, indentation defines the code blocks (whereas Javascript is curly brace {} reliant, not indentation reliant).  
> Variables are defined differently, with Python using just a variable name to define the variable (such as "x = 1") and JavaScript using a keyword let or const (such as "let x = 1").   
>  Naming conventions vary, such as snake_case in Python vs. lowerCamelCase in JavaScript.  
> Operators are different (such as "and, or, not" in Python and "&&, ||, !" in JavaScript.  
> In functions, Python will cause an exception if the number of arguments passed to the function call does not match the number of parameters defined in the function itself.  JavaScript will not do this, but instead ignore unrecognized arguments.  
> Finally, the syntax of loops is different and requires care to not confuse the two.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?

> A unit test is small, bite-sized test that assesses the functionality of a single _unit_ of code.  Typically, this is a test written for a single function.

- What is an integration test?

> An integration test is larger than a unit test, assessing the functionality _and_ compatibility of multiple functions working together.

- What is the role of web application framework, like Flask?

> A web application framework is a set of libraries and tools that help build a web app. With Flask (a web application framework written in Python), it allows developers to write applications without worrying about low-level details (protocols, thread management, etc.)

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
> While they can both achieve the same desired result, I find that path parameters make more sense when retrieving a specific resource or resources, whereas query params are better used for filtering/sorting results.  

- How do you collect data from a URL placeholder parameter using Flask?

> URL parameters are handled using @app.route, but with < > around the variable.  Ex: subreddit names in Reddit are not all hardcoded in, but instead rely on @app.route('/r/<subreddit>')

- How do you collect data from the query string using Flask?

> With query string arguments, they are handled within the @app.route function using request.args

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

> A cookie is a small bit of data or info stored on the client (browser).  Cookies are commonly used for log-in information (keeping a user logged into their account as they navigate around a web app), shopping cart information (even when not logged in, the client can "remember" what has been put in the cart), etc.

- What is the session object in Flask?

> The session object in Flask is like a 'magic dictionary' that creates the cookie for you. Session objects are typically preferred as the cookie is still created but with encryption and is easier to use.

- What does Flask's `jsonify()` do?

>jsonify() in Flask is a functionality that converts a JSON output into a response object.
