from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Project</title>
        <style>
            body {
                font-family: "Segoe UI", Roboto, sans-serif;
                margin: 0;
                padding: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #fff;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                text-align: center;
                max-width: 600px;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 10px;
                backdrop-filter: blur(10px);
            }
            h1 {
                font-size: 48px;
                margin: 0 0 20px 0;
            }
            p {
                font-size: 18px;
                margin: 10px 0;
            }
            a {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background: white;
                color: #667eea;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                transition: 0.3s;
            }
            a:hover {
                background: #667eea;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Congratulations!</h1>
            <p>Your Django project is running successfully!</p>
            <p>Version: Django 5.2.11</p>
            <p>
                <a href="/blog/">Blog</a>
                <a href="/blog/about/">About</a>
                <a href="/admin/">Admin</a>
            </p>
        </div>
    </body>
    </html>
    """)

def home(request):
    return HttpResponse("Hello, World! This is the home page of the blog.")

def about(request):
    return HttpResponse("This is the about page of the blog. Here you can find more information about us.")\
    
def contact_us(request):
    return HttpResponse("This is the contact us page of the blog. You can reach us at contact@example.com")