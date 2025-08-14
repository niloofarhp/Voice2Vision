from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Voice2Vision Summary", ln=True, align="C")
        self.ln(10)

    def add_summary(self, text):
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, text)
        self.ln()

    def add_image(self, image_path):
        if os.path.exists(image_path):
            self.image(image_path, x=30, y=self.get_y(), w=150)
            self.ln(10)

def generate_pdf(summary_text, image_path, output_path="outputs/summary.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf = PDF()
    pdf.add_page()
    pdf.add_summary(summary_text)
    pdf.add_image(image_path)
    pdf.output(output_path)
    return output_path
