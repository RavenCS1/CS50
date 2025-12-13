from fpdf import FPDF

def main():
    name=input("Name: ")
    pdf=FPDF(orientation="portrait", format='A4')
    pdf.add_page()
    pdf.set_font('helvetica', "B", 55)
    pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT" ,align='C')
    pdf.image("shirtificate.png",x=0, y=70)
    pdf.set_font('helvetica', "B", 30)
    pdf.set_text_color(255,255,255)
    pdf.text(x=50,y=145,text=f"{name} took CS50")
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()