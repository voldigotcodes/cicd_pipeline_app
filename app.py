# from flask import Flask, jsonify, render_template_string, request
# import os

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template_string(
#         """
#         <!doctype html>
#         <html lang="en">
#         <head>
#           <meta charset="UTF-8" />
#           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#           <title>Hello World</title>
#           <script src="https://cdn.tailwindcss.com"></script>
#         </head>
#         <body class="bg-gray-100 flex items-center justify-center h-screen">
#         <h1>Welcome to the CI/CD Pipeline App!</h1>
#         </body>
#         </html>
        
#         """)

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 8001))
#     app.run(host='0.0.0.0', port=port)
