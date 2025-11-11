from flask import Flask, render_template_string, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# ----------- FUNCTION TO LOAD HTML -----------
def get_html_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# ----------- CHATBOT LOGIC -----------
@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    if not data:
        return jsonify({'reply': 'No data received'}), 400

    user_message = data.get('user_message', '').lower()

    if "admission" in user_message:
        reply = "Admissions are open till June 30. Please visit the Admission Office."
    elif "courses" in user_message:
        reply = "We offer B.Tech, BCA, MCA, MBA, and other professional programs."
    elif "fees" in user_message:
        reply = "Fee structure varies by course. You can check it on our official website."
    elif "hostel" in user_message:
        reply = "Yes, hostels are available for both boys and girls with Wi-Fi and mess facilities."
    elif "placement" in user_message:
        reply = "Our top recruiters include Infosys, Wipro, TCS, and Accenture."
    else:
        reply = "Sorry, I didn't understand. Please ask something else about the college."

    return jsonify({'reply': reply})


# ----------- PAGE ROUTES -----------
@app.route('/')
def home():
    return render_template_string(get_html_content('index.html'))

@app.route('/about.html')
def about():
    return render_template_string(get_html_content('about.html'))

@app.route('/chatbot.html')
def chatbot():
    return render_template_string(get_html_content('chatbot.html'))

@app.route('/faq.html')
def faq():
    return render_template_string(get_html_content('faq.html'))

@app.route('/contact.html')
def contact():
    return render_template_string(get_html_content('contact.html'))

# ----------- SERVE STATIC FILES -----------
@app.route('/<path:filename>')
def serve_static(filename):
    # Serve JS, CSS, and other static files
    if os.path.exists(filename):
        return send_from_directory(os.getcwd(), filename)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
