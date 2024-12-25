# Security Policy for Smart Resume Analyzer

## Reporting a Vulnerability

If you discover a vulnerability or have concerns about the security of this project, please report it responsibly. Follow the steps below to ensure proper handling of the issue:

1. **Email**: Send your report to [your-email@example.com].
2. **Details**: Include a detailed description of the vulnerability or security concern, including steps to reproduce it (if possible), potential impact, and any relevant evidence.
3. **Confidentiality**: Please avoid disclosing the issue publicly until it has been addressed and fixed.

We will review your report and work to fix the issue as quickly as possible. You will be notified when a fix or mitigation has been implemented.

## Secure Coding Practices

The following practices have been followed to improve the security of this project:

1. **Input Validation**: Input from users, especially from file uploads, is validated to ensure that only supported file formats (PDF, DOCX, TXT) are accepted.
2. **File Handling**: Uploaded files are processed safely by extracting only text data. Avoiding execution of uploaded files helps mitigate potential threats such as code injection.
3. **Cross-Site Scripting (XSS) Protection**: The frontend sanitizes user input to prevent malicious scripts from being executed on the browser.
4. **Cross-Site Request Forgery (CSRF)**: For the sake of simplicity, CSRF protection has been assumed to be handled elsewhere (in Flask middleware or custom security layers). It's advised to implement CSRF tokens in the future if needed.
5. **Sensitive Information**: No sensitive information such as passwords or API keys is stored within the code. Always use environment variables or secure methods to store such data.

## Dependencies and Third-Party Libraries

This project relies on the following dependencies:

- **Flask**: Web framework for Python.
- **Flask-Cors**: Cross-origin resource sharing (CORS) support for Flask.
- **PyPDF2**: Library to extract text from PDF files.
- **python-docx**: Library to extract text from DOCX files.
- **scikit-learn**: For machine learning and text classification tasks.

All dependencies are regularly updated to patch any known vulnerabilities. You are encouraged to use a virtual environment and keep your dependencies up to date by running:

```bash
pip install --upgrade -r requirements.txt

