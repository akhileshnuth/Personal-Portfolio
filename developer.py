from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import subprocess

class DeveloperPortfolio:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1024x600")

        # Define color themes
        self.dark_mode = False  # Start with light theme
        self.dark_theme = {"bg": "navy", "fg": "white", "accent": "cyan", "button_bg": "darkblue"}
        self.light_theme = {"bg": "#f0f0f0", "fg": "black", "accent": "blue", "button_bg": "#d0d0d0"}
        self.theme = self.light_theme

        self.root.configure(bg=self.theme["bg"])

        # Header Frame (now instance variable)
        self.header_frame = Frame(self.root, bg=self.theme["bg"])
        self.header_frame.place(relx=0, rely=0, relwidth=1, height=40)

        # Toggle Button for Dark Mode
        self.toggle_btn = Button(self.header_frame, text="🌙", font=("Times New Roman", 14), bg=self.theme["button_bg"], fg=self.theme["fg"], bd=0, cursor="hand2", command=self.toggle_theme)
        self.toggle_btn.place(x=10, y=5, width=30, height=30)

        # Navigation Buttons
        nav_items = ["HOME", "ABOUT", "CONTACT", "PROJECTS"]
        total_width = 1024
        button_width = 110
        spacing = (total_width - len(nav_items) * button_width) // (len(nav_items) + 1)
        self.nav_buttons = []
        for i, item in enumerate(nav_items):
            x_pos = spacing + i * (20 + spacing)
            btn = Button(self.header_frame, text=item, font=("Times New Roman", 12, "bold"), bg=self.theme["bg"], fg=self.theme["fg"],
                         activebackground=self.theme["button_bg"], activeforeground=self.theme["fg"], bd=0, cursor="hand2",
                         command=lambda x=item: self.show_section(x))
            btn.place(x=x_pos, y=5, width=button_width, height=30)
            self.nav_buttons.append(btn)

        # Title
        self.title_lbl = Label(self.root, text="HEY! I'M AKHILESH", font=("Times New Roman", 26, "bold"), fg=self.theme["fg"], bg=self.theme["bg"])
        self.title_lbl.place(x=160, y=110)

        self.sub_title = Label(self.root, text="I'M A DEVELOPER |", font=("Times New Roman", 30, "bold"), fg=self.theme["accent"], bg=self.theme["bg"])
        self.sub_title.place(x=160, y=170)

        self.desc = Label(self.root, text="I build and design intuitive websites and software solutions.",
                          font=("Times New Roman", 14), fg=self.theme["fg"], bg=self.theme["bg"])
        self.desc.place(x=160, y=220)

        # Profile Image
        img = Image.open("projectphotos/IMG_0017.JPG")
        img = img.resize((330, 440), Image.LANCZOS)
        self.profile_img = ImageTk.PhotoImage(img)
        img_label = Label(self.root, image=self.profile_img, bg=self.theme["bg"])
        img_label.place(x=800, y=80)

        # Social Media Links
        socials = [
            ("🐙Github", "https://github.com/akhileshnuth"),  # GitHub
            ("🔗Linkedin", "https://linkedin.com/in/akhilesh-nuthalapati-9130b9227"),  # LinkedIn
            ("🐦Twitter", "https://twitter.com"),  # Twitter
            ("📸Instagram", "https://www.instagram.com/ak.hilesh4032?utm_source=qr&igsh=MTdqajNjeGV1bXlxcQ==")  # Instagram
        ]

        for i, (name, url) in enumerate(socials):
            link = Label(self.root, text=name, font=("Times New Roman", 14, "underline"), fg=self.theme["accent"], bg=self.theme["bg"], cursor="hand2")
            link.place(x=30 + i * 130, y=650)
            link.bind("<Button-1>", lambda e, link=url: webbrowser.open(link))

        # Content Frame
        self.content_frame = Frame(self.root, bg=self.theme["bg"])
        self.content_frame.place(x=160, y=360, width=440, height=220)

    def toggle_theme(self):
        """Toggle between Dark and Light mode."""
        self.dark_mode = not self.dark_mode
        self.theme = self.dark_theme if self.dark_mode else self.light_theme

        # Update background colors
        self.root.configure(bg=self.theme["bg"])
        self.header_frame.config(bg=self.theme["bg"])
        self.title_lbl.config(fg=self.theme["fg"], bg=self.theme["bg"])
        self.sub_title.config(fg=self.theme["accent"], bg=self.theme["bg"])
        self.desc.config(fg=self.theme["fg"], bg=self.theme["bg"])
        self.content_frame.config(bg=self.theme["bg"])
        self.toggle_btn.config(bg=self.theme["button_bg"], fg=self.theme["fg"])

        # Update nav buttons
        for btn in self.nav_buttons:
            btn.config(bg=self.theme["bg"], fg=self.theme["fg"], activebackground=self.theme["button_bg"], activeforeground=self.theme["fg"])

        # Update social links and content frame widgets
        for widget in self.root.winfo_children():
            if isinstance(widget, Label) and widget != self.title_lbl and widget != self.sub_title and widget != self.desc:
                widget.config(bg=self.theme["bg"], fg=self.theme["accent"])
        for widget in self.content_frame.winfo_children():
            if isinstance(widget, Label):
                fg = self.theme["accent"] if "underline" in widget.cget("font") or "📧" in widget.cget("text") else self.theme["fg"]
                widget.config(bg=self.theme["bg"], fg=fg)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_section(self, section):
        self.clear_content()

        if section == "HOME":
            subprocess.Popen(["python", "main.py"])
            self.root.destroy()

        elif section == "PROJECTS":
            # Use the current theme's foreground color for text
            project_color = self.theme["fg"]

            Label(
                self.content_frame,
                text=(
                    "Projects:\n"
                    "1. Portfolio Website\n"
                    "2. Student Management System\n"
                    "3. Face Recognition Attendance System\n"
                    "4. Multi Disease Detection\n"
                    "5. Parkinson's Disease Detection"
                ),
                font=("Times New Roman", 14),
                fg=project_color,
                bg=self.theme["bg"],
                justify=LEFT
            ).pack(anchor="w", padx=10, pady=10)

        elif section == "ABOUT":
            Label(self.content_frame, text="About Me:", font=("Times New Roman", 16, "bold"), fg=self.theme["accent"], bg=self.theme["bg"]).pack(anchor="w", padx=10)
            about_lines = [
                "I'm Akhilesh, a full-stack developer with a passion",
                "for creating seamless digital experiences. I love",
                "working with modern software technologies and AI",
                "to build products that are both useful and beautiful."
            ]
            for line in about_lines:
                Label(self.content_frame, text=line, font=("Times New Roman", 14), fg=self.theme["fg"], bg=self.theme["bg"]).pack(anchor="w", padx=20)


        elif section == "CONTACT":
            Label(self.content_frame, text="Contact Me:", font=("Times New Roman", 14, "bold"),
                fg="orange", bg=self.theme["bg"]).pack(anchor="w", padx=10, pady=(10, 0))

            email = Label(self.content_frame, text="📧 akhileshnuthalapati7@gmail.com", font=("Times New Roman", 14, "underline"),
                        fg=self.theme["accent"], bg=self.theme["bg"], cursor="hand2")
            email.pack(anchor="w", padx=20, pady=2)
            email.bind("<Button-1>", lambda e: webbrowser.open("mailto:akhileshnuthalapati7@gmail.com"))

            phone = Label(self.content_frame, text="📞 +91-9392330638", font=("Times New Roman", 14, "underline"),
                        fg=self.theme["accent"], bg=self.theme["bg"], cursor="hand2")
            phone.pack(anchor="w", padx=20, pady=2)
            phone.bind("<Button-1>", lambda e: webbrowser.open("tel:+919392330638"))

            youtube = Label(self.content_frame, text="▶ Visit YouTube Channel", font=("Times New Roman", 14, "underline"),
                            fg=self.theme["accent"], bg=self.theme["bg"], cursor="hand2")
            youtube.pack(anchor="w", padx=20, pady=2)
            youtube.bind("<Button-1>", lambda e: webbrowser.open("https://www.youtube.com/@akhilcreations401"))

            insta = Label(self.content_frame, text="📸 Follow on Instagram for Updates", font=("Times New Roman", 14, "underline"),
                        fg=self.theme["accent"], bg=self.theme["bg"], cursor="hand2")
            insta.pack(anchor="w", padx=20, pady=2)
            insta.bind("<Button-1>", lambda e: webbrowser.open("https://www.instagram.com/ak.hilesh4032?utm_source=qr&igsh=MTdqajNjeGV1bXlxcQ=="))

if __name__ == "__main__":
    root = Tk()
    app = DeveloperPortfolio(root)
    root.mainloop()
