from flask import Flask, request, redirect, session
from transformers import pipeline

app = Flask(__name__)

app.secret_key = "cybersecurityproject"

# AI Model
classifier = pipeline("sentiment-analysis")

# Store Users
users = {}


# =========================
# LOGIN PAGE
# =========================

@app.route('/')
def login_page():

    return """

    <html>

    <head>

        <title>Login</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                text-align:center;
                margin-top:100px;
            }

            input{
                padding:12px;
                width:250px;
                margin:10px;
                border:none;
                border-radius:6px;
            }

            button{
                padding:12px 25px;
                background:red;
                color:white;
                border:none;
                border-radius:6px;
                cursor:pointer;
            }

            a{
                color:#38bdf8;
            }

        </style>

    </head>

    <body>

        <h1>AI Dark Web Monitoring Login</h1>

        <form method='POST' action='/login'>

            <input type='text' name='username' placeholder='Username' required>

            <br>

            <input type='password' name='password' placeholder='Password' required>

            <br>

            <button type='submit'>Login</button>

        </form>

        <br>

        <p>
            Don't have an account?
            <a href='/register'>Create Account</a>
        </p>

    </body>

    </html>

    """


# =========================
# REGISTER PAGE
# =========================

@app.route('/register')
def register_page():

    return """

    <html>

    <head>

        <title>Create Account</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                text-align:center;
                margin-top:100px;
            }

            input{
                padding:12px;
                width:250px;
                margin:10px;
                border:none;
                border-radius:6px;
            }

            button{
                padding:12px 25px;
                background:green;
                color:white;
                border:none;
                border-radius:6px;
                cursor:pointer;
            }

            a{
                color:#38bdf8;
            }

        </style>

    </head>

    <body>

        <h1>Create Account</h1>

        <form method='POST' action='/create_account'>

            <input type='text' name='username' placeholder='Create Username' required>

            <br>

            <input type='password' name='password' placeholder='Create Password' required>

            <br>

            <button type='submit'>Create Account</button>

        </form>

        <br>

        <a href='/'>Back to Login</a>

    </body>

    </html>

    """


# =========================
# CREATE ACCOUNT
# =========================

@app.route('/create_account', methods=['POST'])
def create_account():

    username = request.form['username']

    password = request.form['password']

    users[username] = password

    return """

    <h1 style='color:lightgreen;text-align:center;margin-top:100px;'>

    Account Created Successfully

    </h1>

    <div style='text-align:center;'>

        <a href='/'>
            <button style='padding:10px 20px;'>Go To Login</button>
        </a>

    </div>

    """


# =========================
# LOGIN VALIDATION
# =========================

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']

    password = request.form['password']

    if username in users and users[username] == password:

        session['user'] = username

        return redirect('/home')

    return """

    <h1 style='color:red;text-align:center;margin-top:100px;'>

    Invalid Username or Password

    </h1>

    """


# =========================
# HOME PAGE
# =========================

@app.route('/home')
def home():

    if 'user' not in session:

        return redirect('/')

    return f"""

    <html>

    <head>

        <title>Home</title>

        <style>

            body{{
                background:#0f172a;
                color:white;
                font-family:Arial;
                text-align:center;
                margin-top:120px;
            }}

            h1{{
                color:#38bdf8;
            }}

            button{{
                padding:15px 30px;
                background:red;
                border:none;
                color:white;
                font-size:18px;
                cursor:pointer;
                border-radius:8px;
                margin:10px;
            }}

        </style>

    </head>

    <body>

        <h1>Welcome {session['user']}</h1>

        <p>AI Cyber Threat Intelligence Dashboard</p>

        <a href='/scan'>
            <button>Start Scan</button>
        </a>

        <a href='/logout'>
            <button>Logout</button>
        </a>

    </body>

    </html>

    """


# =========================
# AI THREAT SCAN
# =========================

@app.route('/scan')
def scan():

    if 'user' not in session:

        return redirect('/')

    posts = [

        "Selling stolen credentials",

        "Ransomware toolkit found",

        "Normal programming discussion",

        "Phishing scam detected",

        "Fake banking website available",

        "Safe coding tutorial"

    ]

    threats = []

    id = 1

    for post in posts:

        result = classifier(post)[0]

        confidence = round(result['score'], 2)

        if "credentials" in post.lower():

            category = "Credential Theft"

        elif "ransomware" in post.lower():

            category = "Malware"

        elif "scam" in post.lower():

            category = "Scam"

        elif "bank" in post.lower():

            category = "Banking Fraud"

        else:

            category = "Safe"

        if category == "Safe":

            risk = "LOW"

        else:

            if confidence > 0.80:

                risk = "HIGH"

            elif confidence > 0.50:

                risk = "MEDIUM"

            else:

                risk = "LOW"

        threats.append({

            "id": id,

            "threat": post,

            "category": category,

            "risk": risk,

            "confidence": confidence

        })

        id += 1

    html = """

    <html>

    <head>

        <title>AI Threat Dashboard</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                text-align:center;
            }

            h1{
                color:#38bdf8;
                margin-top:30px;
            }

            table{
                width:90%;
                margin:auto;
                margin-top:40px;
                border-collapse:collapse;
            }

            th{
                background:#1e293b;
            }

            th,td{
                border:1px solid #334155;
                padding:15px;
            }

            tr:nth-child(even){
                background:#1e293b;
            }

            .high{
                color:red;
                font-weight:bold;
            }

            .medium{
                color:orange;
                font-weight:bold;
            }

            .low{
                color:lightgreen;
                font-weight:bold;
            }

            button{
                padding:10px 20px;
                margin:10px;
                background:#2563eb;
                border:none;
                color:white;
                border-radius:6px;
                cursor:pointer;
            }

        </style>

    </head>

    <body>

    <h1>AI Threat Dashboard</h1>

    <a href='/home'>
        <button>Home</button>
    </a>

    <a href='/scan'>
        <button>Rescan</button>
    </a>

    <a href='/logout'>
        <button>Logout</button>
    </a>

    <table>

    <tr>

        <th>ID</th>

        <th>Threat</th>

        <th>Category</th>

        <th>Risk</th>

        <th>AI Confidence</th>

    </tr>

    """

    for t in threats:

        risk_class = ""

        if t['risk'] == "HIGH":

            risk_class = "high"

        elif t['risk'] == "MEDIUM":

            risk_class = "medium"

        else:

            risk_class = "low"

        html += f"""

        <tr>

            <td>{t['id']}</td>

            <td>{t['threat']}</td>

            <td>{t['category']}</td>

            <td class='{risk_class}'>{t['risk']}</td>

            <td>{t['confidence']}</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """

    return html


# =========================
# LOGOUT
# =========================

@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/')


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=7860)