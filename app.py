from flask import Flask, render_template, request
from user_agents import parse

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    # Get the User-Agent string from the request headers
    user_agent = request.headers.get('User-Agent')
    
    # Parse the user agent string to determine the device type
    user_agent_parsed = parse(user_agent)
    
    # Check if the user is on a mobile device
    if user_agent_parsed.is_mobile:
        # Render a mobile-specific template
        return render_template('mobile.html')
    else:
        # Render the regular desktop template
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
