import smtplib
import tkinter as tk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

class EmailClient:
    def __init__(self, master):
        self.master = master
        master.title("Email Client")

        self.label_to = tk.Label(master, text="To:")
        self.label_to.pack()

        self.entry_to = tk.Entry(master)
        self.entry_to.pack()

        self.label_subject = tk.Label(master, text="Subject:")
        self.label_subject.pack()

        self.entry_subject = tk.Entry(master)
        self.entry_subject.pack()

        self.label_body = tk.Label(master, text="Body:")
        self.label_body.pack()

        self.text_body = tk.Text(master)
        self.text_body.pack()

        self.button_send = tk.Button(master, text="Send", command=self.send_email)
        self.button_send.pack()

    def send_email(self):
        to_address = self.entry_to.get()
        subject = self.entry_subject.get()
        body = self.text_body.get("1.0", tk.END)

        if not to_address or not subject or not body:
            messagebox.showerror("Error", "All fields must be filled")
            return

        message = MIMEMultipart()
        message["From"] = "resetnicov96@gmail.com"  # Your email address
        message["To"] = to_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login("resetnicov96@gmail.com", "ekma mbat endt ipep")  # Replace with your email and password
                server.sendmail("resetnicov96@gmail.com", to_address, message.as_string())
                messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    email_client = EmailClient(root)
    root.mainloop()