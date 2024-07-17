from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>Identity Reconciliation API</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
            h1 { color: #333; }
            p { margin-bottom: 10px; }
            code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Identity Reconciliation API</h1>
        <p>This API provides identity reconciliation services.</p>
        <p>To use the API, send a POST request to the following endpoint:</p>
        <code>/api/identify/</code>
        <p>The request body should be in JSON format and include either an email or a phone number (or both):</p>
        <pre><code>
{
    "email": "example@email.com",
    "phoneNumber": 1234567890
}
        </code></pre>
        <p>The API will return consolidated contact information based on the provided data.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)