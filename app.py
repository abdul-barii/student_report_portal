from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Folder where reports are stored
REPORTS_FOLDER = "reports"
if not os.path.exists(REPORTS_FOLDER):
    os.makedirs(REPORTS_FOLDER)  # Ensure the folder exists

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        admission_number = request.form.get("admission_number")
        pdf_filename = f"Report_{admission_number}.pdf"
        pdf_path = os.path.join(REPORTS_FOLDER, pdf_filename)

        if os.path.exists(pdf_path):
            return send_from_directory(REPORTS_FOLDER, pdf_filename, as_attachment=True)
        else:
            error = "Invalid Admission Number. Report not found."
    
    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
