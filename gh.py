# مشروع: توليد تقرير PDF من بيانات Excel
# المطور: prof.dr.sh

from fpdf import FPDF
import pandas as pd

# تعريف كلاس PDF يدعم العربية
class ArabicPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arabic", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font("Arabic", "", 14)
        self.cell(0, 10, "تقرير المبيعات - prof.dr.sh", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arabic", "", 10)
        self.cell(0, 10, "صفحة %s" % self.page_no(), align="C")

    def render_table(self, dataframe):
        self.set_font("Arabic", "", 12)
        col_widths = [40, 30, 30, 30]
        columns = list(dataframe.columns)

        # عنوان الجدول
        for i, col in enumerate(columns):
            self.cell(col_widths[i], 10, str(col), border=1, align='C')
        self.ln()

        # بيانات الجدول
        for _, row in dataframe.iterrows():
            for i, val in enumerate(row):
                self.cell(col_widths[i], 10, str(val), border=1, align='C')
            self.ln()

# بيانات تجريبية
data = {
    'المنتج': ['قلم', 'دفتر', 'مسطرة'],
    'الكمية': [10, 5, 7],
    'السعر للوحدة': [1.5, 3.0, 2.0]
}
df = pd.DataFrame(data)
df['الإجمالي'] = df['الكمية'] * df['السعر للوحدة']

# توليد ملف PDF
pdf = ArabicPDF()
pdf.add_page()
pdf.render_table(df)
pdf.output("report_by_prof_dr_sh.pdf")

# حفظ ملف Excel (اختياري للعرض)
df.to_excel("sample_data_by_prof_dr_sh.xlsx", index=False)
