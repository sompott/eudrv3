from flask import Flask, render_template, request, send_file,jsonify,send_from_directory
from fpdf import FPDF
import os
from html import escape
import uuid
import tempfile
import base64
from datetime import datetime
import os
from PyPDF2 import PdfFileMerger

app = Flask(__name__)
from flask import session
# Path to the font file
FONT_PATH = "fonts/THSarabun Bold.ttf"
FONT_PATH1 = "fonts/THSarabun.ttf"
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = '9b62&dqhu@^q(_h0s0g#j(!w6bu0x8%jqd#6=d@7vfrx6x&y5v'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def draw_checkbox(pdf, x, y, size=5, checked=False):
    pdf.rect(x, y, size, size)
    if checked:
        pdf.set_fill_color(0, 0, 0)  # Set fill color to black
        pdf.rect(x + 1, y + 1, size - 2, size - 2, 'F')
 
@app.route('/')
def main():
    return render_template('main.html')
@app.route('/plotlevel')
def index():
    return render_template('index.html')
@app.route('/pdpa')
def pdpa():
    return render_template('pdpa.html')
@app.route('/pdpa1')
def pdpa1():
    return render_template('pdpa1.html')
@app.route('/farmer')
def farmer():
    return render_template('farmer.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')
@app.route('/save_signature', methods=['POST'])
def save_signature():
    data = request.json
    signature_data = data.get('signature')
    signature_bytes = base64.b64decode(signature_data.split(',')[1])
    # Save signature image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
        tmp_file.write(signature_bytes)
        signature_path = tmp_file.name
    
    session['signature_path'] = signature_path
    return jsonify({'success': True})



@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        current_date = datetime.now().strftime("%d-%m-%Y")
        signature_path = session.get('signature_path', None)
        # signature_data = request.form['signature']
        full_name = escape(request.form['full-name'])
        full_name2 = escape(request.form['full-name2'])
        full_name3 = escape(request.form['full-name3'])
        full_name4 = escape(request.form['full-name4'])
        full_name21 = escape(request.form['full-name21'])
        full_name31 = escape(request.form['full-name31'])
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        option41 = request.form.get('full-name41')
        option5 = request.form.get('option5')
        option51 = request.form.get('full-name51')
        option6 = request.form.get('option6')
        option61 = request.form.get('full-name61')
        option7 = request.form.get('option7')
        option71 = request.form.get('full-name71')
        option8 = request.form.get('option8')
        option81 = request.form.get('full-name81')
        name111 = request.form.get('full-name111')
        option9 = request.form.get('option9')
        option10 = request.form.get('option10')
        option11 = request.form.get('option11')
        option12 = request.form.get('option12')
        option13 = request.form.get('option13')
        option14 = request.form.get('option14')
        option15 = request.form.get('option15')
        option16 = request.form.get('option16')
        option17 = request.form.get('option17')
        option18 = request.form.get('option18')
        option19 = request.form.get('option19')
        option20 = request.form.get('option20')
        option21 = request.form.get('option21')
        option22 = request.form.get('option22')
        name199 = request.form.get('full-name199')
        comment = request.form.get('comment')
        num1 = request.form.get('num1')
        num = request.form.get('num')
        num2 = request.form.get('num2')
        num3 = request.form.get('num3')
        commesnt = request.form.get('signature')
        photo = request.files['photo']
        photo1 = request.files['photo1']
        print(commesnt)
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        if photo and allowed_file(photo.filename) and photo1 and allowed_file(photo1.filename):
    # บันทึกไฟล์ภาพแรก
            filename = str(uuid.uuid4()) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            photo_path = os.path.join(UPLOAD_FOLDER, filename)
            photo.save(photo_path)
            
            # บันทึกไฟล์ภาพที่สอง
            filename1 = str(uuid.uuid4()) + '.' + photo1.filename.rsplit('.', 1)[1].lower()
            photo_path1 = os.path.join(UPLOAD_FOLDER, filename1)
            photo1.save(photo_path1)

        
        pdf_file_name = f"VD{num}-{num1}-(1)-(1)({num3}).pdf"

        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("THSarabun-Bold", "B", FONT_PATH, uni=True)
        pdf.set_font("THSarabun-Bold", style="B" , size=16)
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD{num}-{num1}-(1)({num3})", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.set_font_size(25)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="           แบบสำรวจความถูกต้องตามกฎหมายของ EUDR – ระดับแปลง", ln=True, align='L')
        pdf.cell(200, 10, txt="EUDR Legality Survey - Plot Level", ln=True, align='C')
        pdf.set_font_size(16)
        pdf.cell(200, 12, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.1     ชื่อและนามสกุลหรือบริษัท Name of Farmer / Company: ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _________{full_name}_________", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Q.2     เลขรหัสแปลง Plot No__{full_name2}___    ที่อยู่ Address__{full_name21}___", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3     การใช้ที่ดินในการผลิตยางพารา (ต้นโต) คิดเป็นเปอร์เซ็นต์__{full_name3}__%   อายุต้นยาง__{full_name31}__ปี", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          what percentage of this land used for rubber production (mature trees)?/Age of trees ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4     ปริมาณการผลิตน้ำยางเฉลี่ยต่อเดือนจากแปลงที่ดินนี้ (กก.) คือเท่าใด?", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          What is the monthly average wet production volume from this plot of land (kg)?  ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _______{full_name4}____กก./เดือน (kg/month) ", ln=True, align='L')
        # Checkboxes Q5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.5     เอกสารสิทธิ์ในการใช้ที่ดิน (ประเภทการอนุญาตให้ใช้ที่ดิน)Land rights (Type of permission to use the land)", ln=True)
        if option1:
            pdf.cell(200, 5, txt="          [X] เอกสารสิทธิ์ที่ดิน (ไปที่ข้อ 6) Land documents (Go to Q.6)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เอกสารสิทธิ์ที่ดิน (ไปที่ข้อ 6) Land documents (Go to Q.6)", ln=True)
        if option2:
            pdf.cell(200, 5, txt="          [X] การใช้ที่ดินได้รับการยอมรับโดยไม่มีเอกสาร (ไปที่ข้อ 7)  Use is recognized without document (Go to Q.7)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การใช้ที่ดินได้รับการยอมรับโดยไม่มีเอกสาร (ไปที่ข้อ 7)  Use is recognized without document (Go to Q.7)", ln=True)
        if option3:
            pdf.cell(200, 5, txt="          [X] การใช้ที่ดินโดยไม่ได้รับอนุญาต (ไปที่ข้อ 8) Unauthorized use of the land (Go to Q.8)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การใช้ที่ดินโดยไม่ได้รับอนุญาต (ไปที่ข้อ 8) Unauthorized use of the land (Go to Q.8)", ln=True)
        # Checkboxes Q6
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.6     ประเภทของเอกสารสิทธิ์ type of documentation", ln=True)
        if option4:
            pdf.cell(200, 5, txt=f"          [X] น.ส.4 โฉนด (Nor Sor 4 – Land Deed) เลขที่เอกสาร Doc No__{option41}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] น.ส.4 โฉนด (Nor Sor 4 – Land Deed) เลขที่เอกสาร Doc No", ln=True)
        if option5:
            pdf.cell(200, 5, txt=f"          [X] น.ส.3/น.ส.3 ก. (Nor Sor 3/Nor Sor 3 Gor) เลขที่เอกสาร Doc No___{option51}___", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] น.ส.3/น.ส.3 ก. (Nor Sor 3/Nor Sor 3 Gor) เลขที่เอกสาร Doc No", ln=True)
        if option6:
            pdf.cell(200, 5, txt=f"          [X] ส.ป.ก. (Sor Por Kor) เลขที่เอกสาร Doc No__{option61}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ส.ป.ก. (Sor Por Kor) เลขที่เอกสาร Doc No", ln=True)
        if option7:
            pdf.cell(200, 5, txt=f"          [X] ท.บ.5 (Tor Bor 5) เลขที่เอกสาร Doc No__{option71}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ท.บ.5 (Tor Bor 5) เลขที่เอกสาร Doc No", ln=True)
        if option8:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ Other__{option81}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ Other", ln=True)
        # Checkboxes Q7
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.7     ขอบนิติกรรมการครอบครองที่ดินได้อย่างไร  How is land ownership legally recognized?", ln=True)
        if option9:
            pdf.cell(200, 5, txt="          [X] มีการตีระเบียบหรือทำเค้าโครงสร้างกำหนดเขตแบบดั้งเดิม (เช่น หิน/เสา/ต้นไม้)", ln=True)
            pdf.cell(200, 5, txt="             Physical customary demarcation (e.g. stone/pillar/tree)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] มีการตีระเบียบหรือทำเค้าโครงสร้างกำหนดเขตแบบดั้งเดิม (เช่น หิน/เสา/ต้นไม้)", ln=True)
            pdf.cell(200, 5, txt="          Physical customary demarcation (e.g. stone/pillar/tree)", ln=True)
        if option10:
            pdf.cell(200, 5, txt="          [X] ครอบครองท่านอยู่บนที่ดินมานานนับเป็นเวลากี่ปี(Number of years of long-term occupation)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ครอบครองท่านอยู่บนที่ดินมานานนับเป็นเวลากี่ปี(Number of years of long-term occupation)", ln=True)
        if option11:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ Others:__{name111}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ Others:", ln=True)
        # Checkboxes Q8
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.8     มีพืชชนิดใดบ้างที่ปลูกบนพื้นที่ Are any crops planted on peat?", ln=True)
        if option12:
            pdf.cell(200, 5, txt="          [X] ใช่ Yes", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ใช่ Yes", ln=True)
        if option13:
            pdf.cell(200, 5, txt="          [X] ไม่มี No", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มี No", ln=True)
        pdf.set_font_size(14)
        pdf.cell(200, 15, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="   ติดต่อสอบถาม บริษัทในเครือ บจก.ทองไทยรับเบอร์ ได้ที่อีเมล์ หรือ eudr@tongthai.co.th หรือ (02) 390-2051", ln=True)
        # Checkboxes Q9
        pdf.add_page()
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD{num}-{num1}-(1)-(1)({num3})", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.set_font_size(16)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.9     สารเคมีใดต่อไปนี้ถูกนำมาใช้บนที่ดิน? (สามารถเลือกได้มากกว่าหนึ่งตัวเลือก)", ln=True)
        pdf.cell(200, 5, txt="          Which of the following chemicals are used on the land? (multiple options allowed)", ln=True)
        pdf.cell(200, 5, txt=f"", ln=True, align='L')
        if option14:
            pdf.cell(200, 5, txt="          [X] พาราควอต (Paraquat)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] พาราควอต (Paraquat)", ln=True)
        if option15:
            pdf.cell(200, 5, txt="          [X] ไกลโฟเสต/ราวด์อัพ (Glyphosate/Roundup)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไกลโฟเสต/ราวด์อัพ (Glyphosate/Roundup)", ln=True)
        if option16:
            pdf.cell(200, 5, txt="          [X] 2-4D", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] 2-4D", ln=True)           
        if option17:
            pdf.cell(200, 5, txt="          [X] TMTD/ZnO (TZ)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] TMTD/ZnO (TZ)", ln=True)
        if option18:
            pdf.cell(200, 5, txt="          [X] คลอร์พรีฟอส (Chlorpyrifos)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] คลอร์พรีฟอส (Chlorpyrifos)", ln=True)
        if option19:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ)__{name199}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ (โปรดระบุ)", ln=True)
        if option20:
            pdf.cell(200, 5, txt="          [X] ไม่มีการใช้สารเคมีใดๆ ข้างต้น (Do not use any of the above chemicals)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มีการใช้สารเคมีใดๆ ข้างต้น (Do not use any of the above chemicals)", ln=True)
# Checkboxes Q10
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.10    ขณะนี้มีข้อพิพาทเรื่องที่ดินกับชนพื้นเมืองหรือกลุ่มพื้นเมืองที่ยังไม่ได้รับการแก้ไขหรือไม่?", ln=True)
        pdf.cell(200, 5, txt="          Are there currently any unresolved land disputes with indigenous or native groups?", ln=True)
        pdf.cell(200, 5, txt=f"", ln=True, align='L')
        if option21:
            pdf.cell(200, 5, txt="          [X] ใช่ (ไปที่ข้อ 10.1) Yes (Go to Q.10.1)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ใช่ (ไปที่ข้อ 10.1) Yes (Go to Q.10.1)", ln=True)
        if option22:
            pdf.cell(200, 5, txt="          [X] ไม่มี No (สิ้นสุดการสำรวจ) No (End of Survey)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มี No (สิ้นสุดการสำรวจ) No (End of Survey)", ln=True)

        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="10.1     โปรดอธิบายรายละเอียดเกี่ยวกับข้อพิพาทเรื่องที่ดิน Please elaborate on the land dispute", ln=True)
        pdf.cell(200, 10, txt=f"{comment}", ln=True, align='L')

        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      วัตถุประสงค์ของการสำรวจนี้คือเพื่อเข้าใจโซลูชันการผลิตยางธรรมชาติและความยั่งยืนของการเกษตรยางพารา ", ln=True)
        pdf.cell(200, 5, txt="การเข้าร่วมในการสำรวจนี้เป็นอิสระ คุณสามารถถอนตัวออกจากการสำรวจได้ตลอดเวลาโดยการติดต่อที่ eudr@tongthai.co.th", ln=True)
        pdf.cell(200, 5, txt="หรือ (02) 390-2051 โดยเราไม่มีความจำเป็นที่จะขายข้อมูลส่วนบุคคลเกี่ยวกับคุณที่เก็บรวบรวมในการสำรวจนี้หรือในทางอื่น", ln=True)
        pdf.cell(200, 5, txt="      The purpose of this survey is to understand the natural rubber supply chain and its ", ln=True)
        pdf.cell(200, 5, txt="sustainability.Your participation in this survey is voluntary.You may withdraw from this survey at", ln=True)
        pdf.cell(200, 5, txt="any time by contacting eudr@tongthai.co.th or (02) 390-2051. We do not sell the Personal Information ", ln=True)
        pdf.cell(200, 5, txt="about you which is collected in connection with this survey or otherwise.", ln=True)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      ข้าพเจ้าได้ให้ข้อมูลทั้งหมดแล้ว และยินยอมให้ใช้และเปิดเผยข้อมูลในการสำรวจนี้ เป็นไปตามกฎหมาย", ln=True)
        pdf.cell(200, 5, txt="คุ้มครองข้อมูลส่วนบุคคล (PDPA)", ln=True)
        pdf.cell(200, 5, txt="      This is to certify that the information I have provided above is to the best of my knowledge ", ln=True)
        pdf.cell(200, 5, txt="and belief.  I have consent to the collection, use and disclosure of this survey based on the Personal", ln=True) 
        pdf.cell(200, 5, txt="Data Protection Act (PDPA). ", ln=True)
        if signature_path:
            # Use signature image in PDF
            pdf.image(signature_path, x=10, y=225, w=50)
        pdf.cell(200, 35, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"____________________", ln=True, align='L')
        pdf.cell(200, 5, txt=f"ลายเซ็น Signature", ln=True, align='L')
        pdf.cell(200, 5, txt=f"วันที่ Date  {current_date}", ln=True, align='L')
        pdf.set_font_size(14)
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="   ติดต่อสอบถาม บริษัทในเครือ บจก.ทองไทยรับเบอร์ ได้ที่อีเมล์ หรือ eudr@tongthai.co.th หรือ (02) 390-2051", ln=True)


        folder_path = os.path.join("pdfs", num)
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        file_index = 1
        while os.path.exists(os.path.join(folder_path, pdf_file_name)):
            pdf_file_name = f"VD{num}-{num1}-(1)-(1)({num3}).pdf"
            file_index += 1
        pdf_file_path = os.path.join(folder_path, pdf_file_name)
        pdf.output(pdf_file_path)
        
        pdf_file_name1 = f"VD{num}-{num1}-(2)-(1)({num3}).pdf"
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        file_index = 1
        pdf = FPDF()
        if photo and allowed_file(photo.filename):
            pdf.add_page()
            pdf.image(photo_path, x=10, y=10, w=190)
        while os.path.exists(os.path.join(folder_path, pdf_file_name1)):
            pdf_file_name1 = f"VD{num}-{num1}-(2)-(1)({num3}).pdf"
            file_index += 1
        pdf_file_path1 = os.path.join(folder_path, pdf_file_name1)
        pdf.output(pdf_file_path1)

        pdf_file_name1 = f"VD{num}-{num1}-(3)-(1)({num3}).pdf"
        os.makedirs(folder_path, exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี
        pdf1 = FPDF()
        if photo1 and allowed_file(photo1.filename):
            pdf1.add_page()
            pdf1.image(photo_path1, x=10, y=10, w=190)
        while os.path.exists(os.path.join(folder_path, pdf_file_name1)):
            pdf_file_name1 = f"VD{num}-{num1}-(3)-(1)({num3}).pdf"
            file_index += 1
        pdf_file_path1 = os.path.join(folder_path, pdf_file_name1)
        pdf1.output(os.path.join(folder_path, pdf_file_name1))

        # folder_path = os.path.join("pdfs", full_name, num)
        # os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        # file_index = 1
        # while os.path.exists(os.path.join(folder_path, pdf_file_name)):
        #     pdf_file_name = f"VD{num}-{num1}-(1)-(1)({num3}).pdf"
        #     file_index += 1

        # pdf_file_path = os.path.join(folder_path, pdf_file_name)
        # pdf.output(pdf_file_path)
        
        # merge_pdfs_in_folder(folder_path, f"VD{num}-{num1}-(1)({num3}).pdf")


        # pdf_file_name1 = f"VD{num}-{num1}-(2)-(1)({num3}).pdf"
        # folder_path1 = os.path.join("img", full_name, num)
        # os.makedirs(folder_path1, exist_ok=True)  # Create folder if it doesn't exis
        # file_index = 1
        # pdf = FPDF()
        # if photo and allowed_file(photo.filename):
        #     pdf.add_page()
        #     pdf.image(photo_path, x=10, y=10, w=190)
        # while os.path.exists(os.path.join(folder_path1, pdf_file_name1)):
        #     pdf_file_name1 = f"VD{num}-{num1}-(2)-(1)({num3}).pdf"
        #     file_index += 1
        # pdf_file_path1 = os.path.join(folder_path1, pdf_file_name1)
        # pdf.output(pdf_file_path1)
        # merge_pdfs_in_folder_img(folder_path1, f"VD{num}-{num1}-(2)-(1)({num3}).pdf")

        # สร้าง PDF จากไฟล์ภาพที่สอง
        # pdf_file_name1 = f"VD{num}-{num1}-(3)-()({num3}).pdf"
        # folder_path1 = os.path.join("img1", full_name, num)
        # os.makedirs(folder_path1, exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี
        # pdf1 = FPDF()
        # if photo1 and allowed_file(photo1.filename):
        #     pdf1.add_page()
        #     pdf1.image(photo_path1, x=10, y=10, w=190)
        # while os.path.exists(os.path.join(folder_path1, pdf_file_name1)):
        #     pdf_file_name1 = f"VD{num}-{num1}-(3)-(1)({num3}).pdf"
        #     file_index += 1
        # pdf_file_path1 = os.path.join(folder_path1, pdf_file_name1)
        # pdf1.output(os.path.join(folder_path1, pdf_file_name1))


        return send_file(pdf_file_path, as_attachment=True, mimetype='application/pdf')
    
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

        # pdf_file_path = os.path.join("pdfs", full_name, pdf_file_name)
        # os.makedirs(os.path.dirname(pdf_file_path), exist_ok=True)  # Create folder if it doesn't exist
        # pdf.output(pdf_file_path)
        
        # merge_pdfs_in_folder(os.path.join("pdfs", full_name), f"{full_name}_merged.pdf")
        
        # folder_path = os.path.join("pdfs", full_name, full_name2)
        # os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

        # pdf_file_path = os.path.join(folder_path, pdf_file_name)
        # pdf.output(pdf_file_path)
        
        # Check if the folder already exists, if yes, append a number
from PyPDF2 import PdfFileMerger

def merge_pdfs_in_folder_img(folder_path1, output_filename):
    # merger = PdfMerger()
    merger = PdfFileMerger()
    for filename in os.listdir(folder_path1):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path1, filename)
            merger.append(pdf_path)

    merger.write(output_filename)
    merger.close()


def merge_pdfs_in_folder(folder_path, output_filename):
    # merger = PdfMerger()
    merger = PdfFileMerger()
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            merger.append(pdf_path)

    merger.write(output_filename)
    merger.close()


@app.route('/submit-form-pdpa', methods=['POST'])
def submit_form_pdpa():
    try:
        full_name = escape(request.form['full-name'])
        full_name2 = escape(request.form['num'])
        signature_path = session.get('signature_path', None)
        pdpa1 = request.form.get('pdpa1')
        pdpa2 = request.form.get('pdpa2')
        pdpa3 = request.form.get('pdpa3')
        current_date = datetime.now().strftime("%Y-%m-%d") 
        photo = request.files['photo']
        
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        if photo and allowed_file(photo.filename):
            filename = str(uuid.uuid4()) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            photo_path = os.path.join(UPLOAD_FOLDER, filename)
            photo.save(photo_path)

        pdf_file_name = f"VD-{full_name2}.pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("THSarabun-Bold", "B", FONT_PATH1, uni=True)
        pdf.set_font("THSarabun-Bold", style="B" , size=16)
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(170, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD - {full_name2}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.image('static/img4.jpg', x = 10, y = 20, w = 180)
        pdf.cell(200, 20 , txt=" ", ln=True, align='L')
        pdf.cell(200, 25, txt="", ln=True, align='C')
        pdf.set_font_size(16)
        pdf.cell(200, 12, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            เนื่องจาก บริษัท ทองไทยรับเบอร์ จำกัด และ บริษัทในเครือ ได้แก่ บริษัท แกรนด์รับเบอร์ ", ln=True, align='L')
        pdf.cell(200, 5, txt="จำกัด บริษัท ทองไทย เทคนิคอล รับเบอร์ จำกัด บริษัท สินทองไทย รับเบอร์ จำกัด และบริษัท ทีทีเอ็น รับเบอร์ จำกัด ", ln=True, align='L')
        pdf.cell(200, 5, txt="สำนักงานตั้งอยู่ที่เลขที่ 984/51-52 ถนนสุขุมวิท 71 แขวงคลองตันเหนือ เขตวัฒนา กรุงเทพมหานคร เป็นผู้ประกอบ", ln=True, align='L')
        pdf.cell(200, 5, txt="ธุรกิจผลิตและส่งออกยางแผ่นรมควัน ยางแท่ง น้ำยางข้น ผลิตภัณฑ์ยางพาราไปยังต่างประเทศ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            เนื่องจากสหภาพยุโรป ได้ประกาศใช้กฎหมายว่าด้วยสินค้าที่ปลอดจากการตัดไม้ทำลายป่า  ซึ่งกำหนดให้บริษัทต้อง", ln=True, align='L')
        pdf.cell(200, 5, txt="แจ้งพิกัดตำแหน่ง (จีพีเอส) ของสวนยางพาราทั้งหมดที่ขายยางพาราให้แก่บริษัทเพื่อให้แน่ใจว่าสวนยางพาราเหล่านั้นไม่ได้", ln=True, align='L')
        pdf.cell(200, 5, txt="ประเทศไทย (กยท.)หรือหน่วยงานราชการที่เกี่ยวข้อง ที่รับรองว่าสวนยางพาราที่ขายยางพาราให้แก่บริษัท มีการครอบครอง", ln=True, align='L')
        pdf.cell(200, 5, txt="ธุรกิจผลิตและส่งออกยางแผ่นรมควัน ยางแท่ง น้ำยางข้น ผลิตภัณฑ์ยางพาราไปยังต่างประเทศ", ln=True, align='L')
        pdf.cell(200, 5, txt="ที่ดินสวนยางพาราถูกต้องตามกฏหมาย ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            การที่บริษัทสามารถส่งออกยางพาราไปยัง สหภาพยุโรป บริษัทจึงจำเป็นต้องเก็บรวบรวม ใช้ เปิดเผยและโอนข้อมูล", ln=True, align='L')
        pdf.cell(200, 5, txt="ของท่านซึ่งเป็นเกษตรกรที่ขายยางพาราให้แก่บริษัทโดยบริษัทจะเก็บรวบรวมข้อมูลดังกล่าวผ่านทางเว็บพอร์ทัลของบริษัท", ln=True, align='L')
        pdf.cell(200, 5, txt="คือ georubber.net เพื่อระบุพิกัดตำแหน่งของสวนยางพาราของท่านและเก็บรวบรวมข้อมูลของท่านซึ่งประกอบด้วยข้อมูล", ln=True, align='L')
        pdf.cell(200, 5, txt="บัตรประชาชน เอกสารสิทธิ์ และสมุดทะเบียนเกษตรกรของท่าน  รวมถึงข้อมูลสวนยางของท่าน แล้วส่งพิกัดตำแหน่งสวน", ln=True, align='L')
        pdf.cell(200, 5, txt="ยางพาราและข้อมูลของท่านพร้อมกับปริมาณยางพาราที่บริษัทซื้อจากท่านส่งให้ลูกค้า ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            ดังนั้น เพื่อให้ท่านสามารถแจ้งพิกัดตำแหน่งสวนยางพาราและข้อมูลของท่านผ่านเว็บพอร์ทัล georubber.net ของ", ln=True, align='L')
        pdf.cell(200, 5, txt="บริษัทและเพื่อให้บริษัทสามารถบริหารและจัดการข้อมูลพิกัดตำแหน่งสวนยางพาราและข้อมูลของท่านได้โดยถูกต้องตาม", ln=True, align='L')
        pdf.cell(200, 5, txt="กฎหมายไทย บริษัทจึงขอความร่วมมือมายังท่านดังต่อไปนี้", ln=True, align='L')
        # Checkboxes Q5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="กรุณาทำเครื่องหมายหน้าข้อเพื่อยืนยันการเข้าใจ และยินยอมให้ข้อมูลแก่บริบริษัท", ln=True)
        if pdpa1:
            pdf.cell(200, 5, txt="[X]    ท่านรับทราบและยินยอมให้บริษัทเก็บรวบรวม เปิดเผยข้อมูลส่วนบุคคลของท่าน ", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]    ท่านรับทราบและยินยอมให้บริษัทเก็บรวบรวม เปิดเผยข้อมูลส่วนบุคคลของท่าน ", ln=True)
        if pdpa2:
            pdf.cell(200, 5, txt="[X]    ท่านรับทราบและให้ความยินยอมว่าให้บริษัทเก็บรวบรวม เปิดเผย ข้อมูลของท่านและข้อมูลอื่นที่เกี่ยวกับท่านดังต่อไปนี้", ln=True)
            pdf.cell(200, 5, txt="เท่าที่จำเป็นต่อการประกอบธุรกิจของบริษัทและตามนโยบายความเป็นส่วนตัวของบริษัทและเพื่อวัตถุประสงค์ที่กำหนด", ln=True)
            pdf.cell(200, 5, txt="ไว้เท่านั้น กล่าวคือ", ln=True)
            pdf.cell(200, 5, txt="            (ก)พิกัดตำแหน่งจีพีเอสของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ข)ปีที่ปลูกต้นยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ค)สำเนาบัตรประชาชนเจ้าของสวนยางพารา", ln=True) 
            pdf.cell(200, 5, txt="            (ง)ปริมาณยางพาราจากแต่ละสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (จ)ขนาดพื้นที่ของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ฉ)สำเนาหลักฐานการใช้ประโยชน์ที่ดิน เช่น โฉนด สมุดกองทุนสงเคราะห์การทำสวนยาง สมุดประจำตัวเกษตกร", ln=True)
            pdf.cell(200, 5, txt="                ชาวสวนยาง สมุดทะเบียนเกษตรกร", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]    ท่านรับทราบและให้ความยินยอมว่าให้บริษัทเก็บรวบรวม เปิดเผย ข้อมูลของท่านและข้อมูลอื่นที่เกี่ยวกับท่านดังต่อไปนี้", ln=True)
            pdf.cell(200, 5, txt="เท่าที่จำเป็นต่อการประกอบธุรกิจของบริษัทและตามนโยบายความเป็นส่วนตัวของบริษัทและเพื่อวัตถุประสงค์ที่กำหนด", ln=True)
            pdf.cell(200, 5, txt="ไว้เท่านั้น กล่าวคือ", ln=True)
            pdf.cell(200, 5, txt="            (ก)พิกัดตำแหน่งจีพีเอสของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ข)ปีที่ปลูกต้นยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ค)สำเนาบัตรประชาชนเจ้าของสวนยางพารา", ln=True) 
            pdf.cell(200, 5, txt="            (ง)ปริมาณยางพาราจากแต่ละสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (จ)ขนาดพื้นที่ของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ฉ)สำเนาหลักฐานการใช้ประโยชน์ที่ดิน เช่น โฉนด สมุดกองทุนสงเคราะห์การทำสวนยาง สมุดประจำตัวเกษตกร", ln=True)
            pdf.cell(200, 5, txt="                ชาวสวนยาง สมุดทะเบียนเกษตรกร", ln=True)
        pdf.image('static/img2.jpg', x = 50, y = 245, w = 100)
        pdf.add_page()
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(170, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD - {full_name2}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.cell(200, 20 , txt=" ", ln=True, align='L')


        pdf.image('static/img4.jpg', x = 10, y = 20, w = 180)
        pdf.cell(200, 20, txt="", ln=True, align='L')
        pdf.cell(200, 25, txt="", ln=True, align='C')
        pdf.set_font_size(16)
        if pdpa3:
            pdf.cell(200, 22, txt=f"", ln=True, align='L')
            pdf.cell(200, 5, txt="[X]         ท่านรับทราบและให้ความยินยอมให้บริษัทสามารถเปิดเผยข้อมูลของท่านไปยังประเทศอื่นเพื่อวัตถุประสงค์ที่", ln=True)
            pdf.cell(200, 5, txt="กำหนดไว้ โดยก่อนการโอนข้อมูลส่วนบุคคลของท่านไปยังประเทศอื่นบริษัทจะดำเนินการเพื่อให้แน่ใจว่าบริษัทมี", ln=True)
            pdf.cell(200, 5, txt="มาตรการป้องกันความปลอดภัยของข้อมูลที่เพียงพอหรือในระดับที่สูงกว่ามาตรการที่กำหนดไว้ตามกฎหมายคุ้มครอง", ln=True)
            pdf.cell(200, 5, txt="ข้อมูลส่วนบุคคลของประเทศไทย ", ln=True)
            pdf.cell(200, 5, txt="            หากท่านมีข้อสงสัยหรือข้อเสนอแนะเกี่ยวกับข้อมูลส่วนบุคคลของท่านหรือหนังสือยินยอมฉบับนี้หรือต้องการยื่นคำ", ln=True)
            pdf.cell(200, 5, txt="ร้องเรียนต่อบริษัท ท่านสามารถติดต่อเจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคลหรือเจ้าหน้าที่อื่นที่เกี่ยวข้องของบริษัทดังต่อไปนี้", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]         ท่านรับทราบและให้ความยินยอมให้บริษัทสามารถเปิดเผยข้อมูลของท่านไปยังประเทศอื่นเพื่อวัตถุประสงค์ที่", ln=True)
            pdf.cell(200, 5, txt="กำหนดไว้ โดยก่อนการโอนข้อมูลส่วนบุคคลของท่านไปยังประเทศอื่นบริษัทจะดำเนินการเพื่อให้แน่ใจว่าบริษัทมี", ln=True)
            pdf.cell(200, 5, txt="มาตรการป้องกันความปลอดภัยของข้อมูลที่เพียงพอหรือในระดับที่สูงกว่ามาตรการที่กำหนดไว้ตามกฎหมายคุ้มครอง", ln=True)
            pdf.cell(200, 5, txt="ข้อมูลส่วนบุคคลของประเทศไทย ", ln=True)
            pdf.cell(200, 5, txt="            หากท่านมีข้อสงสัยหรือข้อเสนอแนะเกี่ยวกับข้อมูลส่วนบุคคลของท่านหรือหนังสือยินยอมฉบับนี้หรือต้องการยื่นคำ", ln=True)
            pdf.cell(200, 5, txt="ร้องเรียนต่อบริษัท ท่านสามารถติดต่อเจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคลหรือเจ้าหน้าที่อื่นที่เกี่ยวข้องของบริษัทดังต่อไปนี้", ln=True)
        

        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            ชื่อ คุณซือชิง เชียน   (ผู้จัดการด้านความรับผิดชอบต่อสังคมและสิ่งแวดล้อม)", ln=True)
        pdf.cell(200, 5, txt="            เบอร์โทรศัพท์        (02) 390-2051", ln=True)
        pdf.cell(200, 5, txt="            อีเมล์               eudr@tongthai.co.th", ln=True)

        pdf.cell(200, 5, txt="            บริษัทขอขอบคุณท่านเป็นอย่างยิ่งที่กรุณาให้ความร่วมมือและให้ความยินยอมตามที่บริษัทขอมาข้างต้น", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทองไทยรับเบอร์ จำกัด     บริษัท แกรนด์รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทองไทย เทคนิคอล รับเบอร์ จำกัด    บริษัท สินทองไทย รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทีทีเอ็น รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="การเข้าร่วมในการสำรวจนี้เป็นอิสระ คุณสามารถถอนตัวออกจากการสำรวจได้ตลอดเวลาโดยการติดต่อที่ eudr@tongthai.co.th", ln=True)

        if signature_path:
            # Use signature image in PDF
            pdf.image(signature_path, x=50, y=180, w=30)
        pdf.rect(10, 180, 140, 20, 'D')
        pdf.set_xy(10, 175)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(170, 20, "ลงลายชื่อ :", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.rect(150, 180, 50, 20, 'D')
        pdf.set_xy(150, 175)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 20, f"วันที่ : {current_date}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        
        pdf.rect(10, 200, 190, 10, 'D')
        pdf.set_xy(10, 200)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(190, 10, f"ชื่อและนามสกุล :       {full_name}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้

        # if photo and allowed_file(photo.filename):
        #     pdf.add_page()
        #     pdf.image(photo_path, x=10, y=10, w=190)
        
        # pdf_file_path = os.path.join("pdfs_pdpa", pdf_file_name)
        # pdf.output(pdf_file_path)
        folder_path = os.path.join("pdfs_pdpa", full_name2)
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        pdf_file_path = os.path.join(folder_path, pdf_file_name)
        pdf.output(pdf_file_path)

        pdf_file_name1 = f"VD-{full_name2}-ID.pdf"
        folder_path1 = os.path.join("pdfs_pdpa", full_name2)
        os.makedirs(folder_path1, exist_ok=True)  # Create folder if it doesn't exis
        pdf = FPDF()
        if photo and allowed_file(photo.filename):
            pdf.add_page()
            pdf.image(photo_path, x=10, y=10, w=190)
        pdf_file_path1 = os.path.join(folder_path1, pdf_file_name1)
        pdf.output(pdf_file_path1)
        return send_file(pdf_file_path, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/submit-form-pdpa1', methods=['POST'])
def submit_form_pdpa1():
    try:
        full_name = escape(request.form['full-name'])
        full_name2 = escape(request.form['num'])
        signature_path = session.get('signature_path', None)
        pdpa1 = request.form.get('pdpa1')
        pdpa2 = request.form.get('pdpa2')
        pdpa3 = request.form.get('pdpa3')
        current_date = datetime.now().strftime("%Y-%m-%d") 
        photo = request.files['photo']
        num1 = escape(request.form['num1'])
        
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        if photo and allowed_file(photo.filename):
            filename = str(uuid.uuid4()) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            photo_path = os.path.join(UPLOAD_FOLDER, filename)
            photo.save(photo_path)

        pdf_file_name = f"VD-{full_name2}-PDPA-{num1}.pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("THSarabun-Bold", "B", FONT_PATH1, uni=True)
        pdf.set_font("THSarabun-Bold", style="B" , size=16)
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD-{full_name2}-PDPA-{num1}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.image('static/img4.jpg', x = 10, y = 20, w = 180)
        pdf.cell(200, 20 , txt=" ", ln=True, align='L')
        pdf.cell(200, 25, txt="", ln=True, align='C')
        pdf.set_font_size(16)
        pdf.cell(200, 12, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            เนื่องจาก บริษัท ทองไทยรับเบอร์ จำกัด และ บริษัทในเครือ ได้แก่ บริษัท แกรนด์รับเบอร์ ", ln=True, align='L')
        pdf.cell(200, 5, txt="จำกัด บริษัท ทองไทย เทคนิคอล รับเบอร์ จำกัด บริษัท สินทองไทย รับเบอร์ จำกัด และบริษัท ทีทีเอ็น รับเบอร์ จำกัด ", ln=True, align='L')
        pdf.cell(200, 5, txt="สำนักงานตั้งอยู่ที่เลขที่ 984/51-52 ถนนสุขุมวิท 71 แขวงคลองตันเหนือ เขตวัฒนา กรุงเทพมหานคร เป็นผู้ประกอบ", ln=True, align='L')
        pdf.cell(200, 5, txt="ธุรกิจผลิตและส่งออกยางแผ่นรมควัน ยางแท่ง น้ำยางข้น ผลิตภัณฑ์ยางพาราไปยังต่างประเทศ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            เนื่องจากสหภาพยุโรป ได้ประกาศใช้กฎหมายว่าด้วยสินค้าที่ปลอดจากการตัดไม้ทำลายป่า  ซึ่งกำหนดให้บริษัทต้อง", ln=True, align='L')
        pdf.cell(200, 5, txt="แจ้งพิกัดตำแหน่ง (จีพีเอส) ของสวนยางพาราทั้งหมดที่ขายยางพาราให้แก่บริษัทเพื่อให้แน่ใจว่าสวนยางพาราเหล่านั้นไม่ได้", ln=True, align='L')
        pdf.cell(200, 5, txt="ประเทศไทย (กยท.)หรือหน่วยงานราชการที่เกี่ยวข้อง ที่รับรองว่าสวนยางพาราที่ขายยางพาราให้แก่บริษัท มีการครอบครอง", ln=True, align='L')
        pdf.cell(200, 5, txt="ธุรกิจผลิตและส่งออกยางแผ่นรมควัน ยางแท่ง น้ำยางข้น ผลิตภัณฑ์ยางพาราไปยังต่างประเทศ", ln=True, align='L')
        pdf.cell(200, 5, txt="ที่ดินสวนยางพาราถูกต้องตามกฏหมาย ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            การที่บริษัทสามารถส่งออกยางพาราไปยัง สหภาพยุโรป บริษัทจึงจำเป็นต้องเก็บรวบรวม ใช้ เปิดเผยและโอนข้อมูล", ln=True, align='L')
        pdf.cell(200, 5, txt="ของท่านซึ่งเป็นเกษตรกรที่ขายยางพาราให้แก่บริษัทโดยบริษัทจะเก็บรวบรวมข้อมูลดังกล่าวผ่านทางเว็บพอร์ทัลของบริษัท", ln=True, align='L')
        pdf.cell(200, 5, txt="คือ georubber.net เพื่อระบุพิกัดตำแหน่งของสวนยางพาราของท่านและเก็บรวบรวมข้อมูลของท่านซึ่งประกอบด้วยข้อมูล", ln=True, align='L')
        pdf.cell(200, 5, txt="บัตรประชาชน เอกสารสิทธิ์ และสมุดทะเบียนเกษตรกรของท่าน  รวมถึงข้อมูลสวนยางของท่าน แล้วส่งพิกัดตำแหน่งสวน", ln=True, align='L')
        pdf.cell(200, 5, txt="ยางพาราและข้อมูลของท่านพร้อมกับปริมาณยางพาราที่บริษัทซื้อจากท่านส่งให้ลูกค้า ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            ดังนั้น เพื่อให้ท่านสามารถแจ้งพิกัดตำแหน่งสวนยางพาราและข้อมูลของท่านผ่านเว็บพอร์ทัล georubber.net ของ", ln=True, align='L')
        pdf.cell(200, 5, txt="บริษัทและเพื่อให้บริษัทสามารถบริหารและจัดการข้อมูลพิกัดตำแหน่งสวนยางพาราและข้อมูลของท่านได้โดยถูกต้องตาม", ln=True, align='L')
        pdf.cell(200, 5, txt="กฎหมายไทย บริษัทจึงขอความร่วมมือมายังท่านดังต่อไปนี้", ln=True, align='L')
        # Checkboxes Q5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="กรุณาทำเครื่องหมายหน้าข้อเพื่อยืนยันการเข้าใจ และยินยอมให้ข้อมูลแก่บริบริษัท", ln=True)
        if pdpa1:
            pdf.cell(200, 5, txt="[X]    ท่านรับทราบและยินยอมให้บริษัทเก็บรวบรวม เปิดเผยข้อมูลส่วนบุคคลของท่าน ", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]    ท่านรับทราบและยินยอมให้บริษัทเก็บรวบรวม เปิดเผยข้อมูลส่วนบุคคลของท่าน ", ln=True)
        if pdpa2:
            pdf.cell(200, 5, txt="[X]    ท่านรับทราบและให้ความยินยอมว่าให้บริษัทเก็บรวบรวม เปิดเผย ข้อมูลของท่านและข้อมูลอื่นที่เกี่ยวกับท่านดังต่อไปนี้", ln=True)
            pdf.cell(200, 5, txt="เท่าที่จำเป็นต่อการประกอบธุรกิจของบริษัทและตามนโยบายความเป็นส่วนตัวของบริษัทและเพื่อวัตถุประสงค์ที่กำหนด", ln=True)
            pdf.cell(200, 5, txt="ไว้เท่านั้น กล่าวคือ", ln=True)
            pdf.cell(200, 5, txt="            (ก)พิกัดตำแหน่งจีพีเอสของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ข)ปีที่ปลูกต้นยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ค)สำเนาบัตรประชาชนเจ้าของสวนยางพารา", ln=True) 
            pdf.cell(200, 5, txt="            (ง)ปริมาณยางพาราจากแต่ละสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (จ)ขนาดพื้นที่ของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ฉ)สำเนาหลักฐานการใช้ประโยชน์ที่ดิน เช่น โฉนด สมุดกองทุนสงเคราะห์การทำสวนยาง สมุดประจำตัวเกษตกร", ln=True)
            pdf.cell(200, 5, txt="                ชาวสวนยาง สมุดทะเบียนเกษตรกร", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]    ท่านรับทราบและให้ความยินยอมว่าให้บริษัทเก็บรวบรวม เปิดเผย ข้อมูลของท่านและข้อมูลอื่นที่เกี่ยวกับท่านดังต่อไปนี้", ln=True)
            pdf.cell(200, 5, txt="เท่าที่จำเป็นต่อการประกอบธุรกิจของบริษัทและตามนโยบายความเป็นส่วนตัวของบริษัทและเพื่อวัตถุประสงค์ที่กำหนด", ln=True)
            pdf.cell(200, 5, txt="ไว้เท่านั้น กล่าวคือ", ln=True)
            pdf.cell(200, 5, txt="            (ก)พิกัดตำแหน่งจีพีเอสของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ข)ปีที่ปลูกต้นยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ค)สำเนาบัตรประชาชนเจ้าของสวนยางพารา", ln=True) 
            pdf.cell(200, 5, txt="            (ง)ปริมาณยางพาราจากแต่ละสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (จ)ขนาดพื้นที่ของสวนยางพารา", ln=True)
            pdf.cell(200, 5, txt="            (ฉ)สำเนาหลักฐานการใช้ประโยชน์ที่ดิน เช่น โฉนด สมุดกองทุนสงเคราะห์การทำสวนยาง สมุดประจำตัวเกษตกร", ln=True)
            pdf.cell(200, 5, txt="                ชาวสวนยาง สมุดทะเบียนเกษตรกร", ln=True)
        pdf.image('static/img2.jpg', x = 50, y = 245, w = 100)
        pdf.add_page()
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD-{full_name2}-PDPA-{num1}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.cell(200, 20 , txt=" ", ln=True, align='L')


        pdf.image('static/img4.jpg', x = 10, y = 20, w = 180)
        pdf.cell(200, 20, txt="", ln=True, align='L')
        pdf.cell(200, 25, txt="", ln=True, align='C')
        pdf.set_font_size(16)
        if pdpa3:
            pdf.cell(200, 22, txt=f"", ln=True, align='L')
            pdf.cell(200, 5, txt="[X]         ท่านรับทราบและให้ความยินยอมให้บริษัทสามารถเปิดเผยข้อมูลของท่านไปยังประเทศอื่นเพื่อวัตถุประสงค์ที่", ln=True)
            pdf.cell(200, 5, txt="กำหนดไว้ โดยก่อนการโอนข้อมูลส่วนบุคคลของท่านไปยังประเทศอื่นบริษัทจะดำเนินการเพื่อให้แน่ใจว่าบริษัทมี", ln=True)
            pdf.cell(200, 5, txt="มาตรการป้องกันความปลอดภัยของข้อมูลที่เพียงพอหรือในระดับที่สูงกว่ามาตรการที่กำหนดไว้ตามกฎหมายคุ้มครอง", ln=True)
            pdf.cell(200, 5, txt="ข้อมูลส่วนบุคคลของประเทศไทย ", ln=True)
            pdf.cell(200, 5, txt="            หากท่านมีข้อสงสัยหรือข้อเสนอแนะเกี่ยวกับข้อมูลส่วนบุคคลของท่านหรือหนังสือยินยอมฉบับนี้หรือต้องการยื่นคำ", ln=True)
            pdf.cell(200, 5, txt="ร้องเรียนต่อบริษัท ท่านสามารถติดต่อเจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคลหรือเจ้าหน้าที่อื่นที่เกี่ยวข้องของบริษัทดังต่อไปนี้", ln=True)
        else:
            pdf.cell(200, 5, txt="[ ]         ท่านรับทราบและให้ความยินยอมให้บริษัทสามารถเปิดเผยข้อมูลของท่านไปยังประเทศอื่นเพื่อวัตถุประสงค์ที่", ln=True)
            pdf.cell(200, 5, txt="กำหนดไว้ โดยก่อนการโอนข้อมูลส่วนบุคคลของท่านไปยังประเทศอื่นบริษัทจะดำเนินการเพื่อให้แน่ใจว่าบริษัทมี", ln=True)
            pdf.cell(200, 5, txt="มาตรการป้องกันความปลอดภัยของข้อมูลที่เพียงพอหรือในระดับที่สูงกว่ามาตรการที่กำหนดไว้ตามกฎหมายคุ้มครอง", ln=True)
            pdf.cell(200, 5, txt="ข้อมูลส่วนบุคคลของประเทศไทย ", ln=True)
            pdf.cell(200, 5, txt="            หากท่านมีข้อสงสัยหรือข้อเสนอแนะเกี่ยวกับข้อมูลส่วนบุคคลของท่านหรือหนังสือยินยอมฉบับนี้หรือต้องการยื่นคำ", ln=True)
            pdf.cell(200, 5, txt="ร้องเรียนต่อบริษัท ท่านสามารถติดต่อเจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคลหรือเจ้าหน้าที่อื่นที่เกี่ยวข้องของบริษัทดังต่อไปนี้", ln=True)
        

        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="            ชื่อ คุณซือชิง เชียน   (ผู้จัดการด้านความรับผิดชอบต่อสังคมและสิ่งแวดล้อม)", ln=True)
        pdf.cell(200, 5, txt="            เบอร์โทรศัพท์        (02) 390-2051", ln=True)
        pdf.cell(200, 5, txt="            อีเมล์               eudr@tongthai.co.th", ln=True)

        pdf.cell(200, 5, txt="            บริษัทขอขอบคุณท่านเป็นอย่างยิ่งที่กรุณาให้ความร่วมมือและให้ความยินยอมตามที่บริษัทขอมาข้างต้น", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทองไทยรับเบอร์ จำกัด     บริษัท แกรนด์รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทองไทย เทคนิคอล รับเบอร์ จำกัด    บริษัท สินทองไทย รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 5, txt="                บริษัท ทีทีเอ็น รับเบอร์ จำกัด", ln=True)
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="การเข้าร่วมในการสำรวจนี้เป็นอิสระ คุณสามารถถอนตัวออกจากการสำรวจได้ตลอดเวลาโดยการติดต่อที่ eudr@tongthai.co.th", ln=True)

        if signature_path:
            # Use signature image in PDF
            pdf.image(signature_path, x=50, y=180, w=30)
        pdf.rect(10, 180, 140, 20, 'D')
        pdf.set_xy(10, 175)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(170, 20, "ลงลายชื่อ :", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.rect(150, 180, 50, 20, 'D')
        pdf.set_xy(150, 175)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 20, f"วันที่ : {current_date}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        
        pdf.rect(10, 200, 190, 10, 'D')
        pdf.set_xy(10, 200)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(190, 10, f"ชื่อและนามสกุล :       {full_name}", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้

        # if photo and allowed_file(photo.filename):
        #     pdf.add_page()
        #     pdf.image(photo_path, x=10, y=10, w=190)
        folder_path = os.path.join("pdpa", full_name2)
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        pdf_file_path = os.path.join(folder_path, pdf_file_name)
        pdf.output(pdf_file_path)


        # pdf_file_path = os.path.join("pdpa", pdf_file_name)
        # pdf.output(pdf_file_path)

        pdf_file_name1 = f"VD-{full_name2}-PDPA-{num1}-ID.pdf"
        folder_path1 = os.path.join("pdpa", full_name2)
        os.makedirs(folder_path1, exist_ok=True)  # Create folder if it doesn't exis
        pdf = FPDF()
        if photo and allowed_file(photo.filename):
            pdf.add_page()
            pdf.image(photo_path, x=10, y=10, w=190)
        pdf_file_path1 = os.path.join(folder_path1, pdf_file_name1)
        pdf.output(pdf_file_path1)
        return send_file(pdf_file_path, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


@app.route('/submit-form-farmer', methods=['POST'])
def submit_form_farmer():
    try:
        Farm1 = escape(request.form['Farm1'])
        Farm = escape(request.form['Farm'])
        signature_path = session.get('signature_path', None)
        q3 = request.form.get('q3')
        q31 = request.form.get('q31')
        q311 = request.form.get('q311')
        q3111 = request.form.get('q3111')
        option3 = request.form.get('option3')
        option31 = request.form.get('option31')
        option311 = request.form.get('option311')
        option3111 = request.form.get('option3111')
        option31 = request.form.get('option31')
        option311 = request.form.get('option311')
        option3111 = request.form.get('option3111')
        option32 = request.form.get('option32')
        option322 = request.form.get('option322')
        option33 = request.form.get('option33')
        option333 = request.form.get('option333')
        option3333 = request.form.get('option3333')

        o1= request.form.get('o1')
        o2= request.form.get('o2')
        o3= request.form.get('o3')
        o4= request.form.get('o4')
        o5= request.form.get('o5')
        o6= request.form.get('o6')
        o7= request.form.get('o7')
        o8= request.form.get('o8')
        o9= request.form.get('o9')
        o10= request.form.get('o10')
        o11= request.form.get('o11')
        o12= request.form.get('o12')
        o13= request.form.get('o13')
        o14= request.form.get('o14')
        o15= request.form.get('o15')
        o16= request.form.get('o16')
        o17= request.form.get('o17')
        o18= request.form.get('o18')
        o19= request.form.get('o19')
        o20= request.form.get('o20')
        o21= request.form.get('o21')
        o22= request.form.get('o22')
        o23= request.form.get('o23')
        o24= request.form.get('o24')
        o25= request.form.get('o25')
        o26= request.form.get('o26')
        o27= request.form.get('o27')
        o28= request.form.get('o28')
        o29= request.form.get('o29')
        o299= request.form.get('o299')
        o30= request.form.get('o30')
        o31= request.form.get('o31')
        o32= request.form.get('o32')
        o33= request.form.get('o33')
        o34= request.form.get('o34')
        o35= request.form.get('o35')
        o36= request.form.get('o36')
        o37= request.form.get('o37')
        o38= request.form.get('o38')
        o39= request.form.get('o39')
        o40= request.form.get('o40')
        o41= request.form.get('o41')
        o42= request.form.get('o42')
        o43= request.form.get('o43')
        o44= request.form.get('o44')
        o45= request.form.get('o45')
        o46= request.form.get('o46')
        o47= request.form.get('o47')
        o48= request.form.get('o48')
        o49= request.form.get('o49')
        o50= request.form.get('o50')
        o51= request.form.get('o51')
        num= request.form.get('num')
        num1= request.form.get('num1')
        current_date = datetime.now().strftime("%Y-%m-%d")
        photo = request.files['photo']
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        if photo and allowed_file(photo.filename):
            filename = str(uuid.uuid4()) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            photo_path = os.path.join(UPLOAD_FOLDER, filename)
            photo.save(photo_path)

        
        pdf_file_name = f"VD-{num}-PDPA{num1}-FL.pdf"

        pdf = FPDF()
        pdf.add_page()                                                                                                                                                              
        pdf.add_font("THSarabun-Bold", "B", FONT_PATH, uni=True)
        pdf.set_font("THSarabun-Bold", style="B" , size=16)

        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD-{num}-PDPA{num1}-FL", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.cell(200, 12, txt=f"", ln=True, align='L')

        pdf.set_font_size(25)
        pdf.cell(200, 10, txt="           แบบสำรวจความถูกต้องตามกฎหมายของ EUDR - ระดับเกษตรกร", ln=True, align='L')
        pdf.cell(200, 10, txt="EUDR Legality Survey - Farmer Level", ln=True, align='C')
        pdf.set_font_size(16)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.1     ชื่อและนามสกุลหรือบริษัท Name of Farmer / Company: ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _________{Farm}_________", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.2     มีสวนยางทั้งหมดกี่แปลง (ขั้นต่ำ: 0, สูงสุด: 1,000)", ln=True, align='L')    
        pdf.cell(200, 5, txt=f"Number of natural rubber plots (Min: 0, Max: 1000)", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _______{Farm1}____", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3     นอกจากตัวท่านแล้ว มีสมาชิกในครอบครัวอยู่ในพื้นที่นี้หรือไม่ Other than the farmer", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          are there any additional household members staying on or around the land?", ln=True, align='L')
        if q3 == "yes":
            pdf.cell(200, 5, txt="          [X] ใช่ (ไปที่ข้อ 3.1) Yes (Go to Q3.1)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ใช่ (ไปที่ข้อ 3.1) Yes (Go to Q3.1)", ln=True)
        if q3 == "no":
            pdf.cell(200, 5, txt="          [X] ไม่ (ไปที่ข้อ 4) No (Go to Q4)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่ (ไปที่ข้อ 4) No (Go to Q4)", ln=True)
        # Q.3.1
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3.1    โปรดเลือกช่วงอายุของสมาชิกในครัวเรือน (อนุญาตให้มีหลายตัวเลือก):", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         Please select the age categories of the household members (multiple options allowed):", ln=True, align='L')       
        if option31:
            pdf.cell(200, 5, txt=f"          [X] อายุ 18 ปีขึ้นไป Above 18 years old จำนวน__{q31}____คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อายุ 18 ปีขึ้นไป Above 18 years old จำนวน___________คน No. of people", ln=True)
        if option311:
            pdf.cell(200, 5, txt=f"          [X] อายุระหว่าง 15-18 ปี (ไปที่ข้อ 3.2) Between 15-18 years old (Go to Q3.2)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน___{q311}___คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อายุระหว่าง 15-18 ปี (ไปที่ข้อ 3.2) Between 15-18 years old (Go to Q3.2)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน_____________คน No. of people", ln=True)
        if option3111:
            pdf.cell(200, 5, txt=f"          [X] อายุต่ำกว่า 15 ปี(ไปที่ข้อ 3.2) Under 15 years old  (Go to Q3.2)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน___{q3111}___คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อายุต่ำกว่า 15 ปี(ไปที่ข้อ 3.2) Under 15 years old  (Go to Q3.2)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน_________คน No. of people", ln=True)
            # Q.3.2
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3.2    สำหรับผู้ที่อายุต่ำกว่า 18 ปี มีงานหรือช่วยงานบนที่ดินหรือไม่?", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         For those below 18 years old, do any of them work or help on the land?", ln=True, align='L')       
        if option32== "yes":
            pdf.cell(200, 5, txt=f"          [X] ใช่ (ไปที่ข้อ 3.3 และ 3.4 ) Yes (Go to Q3.3 & Q3.4)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ใช่ (ไปที่ข้อ 3.3 และ 3.4 ) Yes (Go to Q3.3 & Q3.4)", ln=True)
        if option32== "no":
            pdf.cell(200, 5, txt=f"          [X] ไม่ (ไปที่ข้อ 4) No (Go to Q4)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่ (ไปที่ข้อ 4) No (Go to Q4)", ln=True)
            # Q.3.3
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3.3    สำหรับผู้ที่อายุต่ำกว่า 18 ปี ช่วยงานประเภทใดบ้าง? (อนุญาตให้มีหลายตัวเลือก)", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         For those below 18 years old, what type of tasks do they help with? ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         (multiple options allowed) ", ln=True, align='L')      
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุระหว่าง 15-18 ปี for those age between 15-18 years old", ln=True, align='L')                 
        if option33:
            pdf.cell(200, 5, txt=f"          [X] กรีดยาง Tapping rubber tress", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] กรีดยาง Tapping rubber tress", ln=True)
        if option333:
            pdf.cell(200, 5, txt=f"          [X] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools)", ln=True)
        if option3333:
            pdf.cell(200, 5, txt=f"          [X] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)    
        if o1:
            pdf.cell(200, 5, txt=f"          [X] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        if o2:
            pdf.cell(200, 5, txt=f"          [X] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        if o3:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ) Others (Please specify)_____{o4}_____", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อื่นๆ (โปรดระบุ) Others (Please specify)_____", ln=True)
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุต่ำกว่า 15 ปี for those age under 15 years old", ln=True, align='L')                 
        if o5:
            pdf.cell(200, 5, txt=f"          [X] กรีดยาง Tapping rubber tress", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] กรีดยาง Tapping rubber tress", ln=True)
        if o6:
            pdf.cell(200, 5, txt=f"          [X] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools)", ln=True)
        if o7:
            pdf.cell(200, 5, txt=f"          [X] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True) 
        if o8:
            pdf.cell(200, 5, txt=f"          [X] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        if o9:
            pdf.cell(200, 5, txt=f"          [X] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        if o10:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ) Others (Please specify)_____{o11}_____", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อื่นๆ (โปรดระบุ) Others (Please specify)_____", ln=True)

        pdf.add_page()
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD-{num}-PDPA{num1}-FL", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.cell(200, 12, txt=f"", ln=True, align='L')
        pdf.set_font_size(16)      
        # Question 3.4
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3.4    สำหรับผู้ที่อายุต่ำกว่า 18 ปี ชั่วโมงทำงานเฉลี่ยต่อวันคือเท่าใด", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         For those under 18 years old, what is their average work hours per day", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         (multiple options allowed) ", ln=True, align='L')      
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุระหว่าง 15-18 ปี for those age between 15-18 years old", ln=True, align='L')                 
        if o12== "yes":
            pdf.cell(200, 5, txt=f"          [X] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        if o12== "no":
            pdf.cell(200, 5, txt=f"          [X] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)    
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุต่ำกว่า 15 ปี for those age under 15 years old", ln=True, align='L')                 
        if o14== "yes":
            pdf.cell(200, 5, txt=f"          [X] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        if o14== "no":
            pdf.cell(200, 5, txt=f"          [X] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        # Question 4
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4    มีคนงานในสวนหรือไม่ Are there any workers on the farm?", ln=True, align='L')      
        if o16 == "yes":
            pdf.cell(200, 5, txt=f"          [X] ใช่ (พนักงานประจำ/ไม่เป็นทางการ/แบ่งผลกำไร/พนักงานเต็มเวลาหรือนอกเวลา)(ไปที่ข้อ 4.1 ถึง 4.6)", ln=True)
            pdf.cell(200, 5, txt=f"                Yes (regular/casual/profit sharing/full or part time workers)(Go to Q4.1 to Q4.6)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ใช่ (พนักงานประจำ/ไม่เป็นทางการ/แบ่งผลกำไร/พนักงานเต็มเวลาหรือนอกเวลา)(ไปที่ข้อ 4.1 ถึง 4.6)", ln=True)
            pdf.cell(200, 5, txt=f"                Yes (regular/casual/profit sharing/full or part time workers)(Go to Q4.1 to Q4.6)", ln=True)
        if o16 == "no":
            pdf.cell(200, 5, txt=f"          [X] ไม่มีคนงาน (ไปที่ข้อ 5) No workers (Go to Q5)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ไม่มีคนงาน (ไปที่ข้อ 5) No workers (Go to Q5)", ln=True)          
        # Question 4.1
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.1    ประเภทของการทำสัญญาจ้างงาน Type of consent given by workers to work on the land?", ln=True, align='L')      
        if o18 == "yes":
            pdf.cell(200, 5, txt=f"          [X] ข้อตกลงเป็นลายลักษณ์อักษร Written consent", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ข้อตกลงเป็นลายลักษณ์อักษร Written consent", ln=True)
        if o18 == "no":
            pdf.cell(200, 5, txt=f"          [X] ตกลงกันด้วยวาจา Verbal consent", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ตกลงกันด้วยวาจา Verbal consent", ln=True)  
        if o18 == "none":
            pdf.cell(200, 5, txt=f"          [X] ไม่มีข้อตกลงหรือสัญญา No Consent", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ไม่มีข้อตกลงหรือสัญญา No Consent", ln=True)          
        # Question 4.2
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.2    รายได้เฉลี่ยต่อชั่วโมงของคนงาน (บาท) Average hourly income of workers (THB)", ln=True, align='L')      
        pdf.cell(200, 5, txt=f"______{o21}________บาท (THB)", ln=True, align='L')      
        # Question 4.3
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.3    ชั่วโมงทำงานเฉลี่ยต่อสัปดาห์ของคนงาน Average weekly work hours of workers?", ln=True, align='L')      
        if o22 == "yes":
            pdf.cell(200, 5, txt=f"          [X] น้อยกว่า 48 ชม. Less than 48  hours", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] น้อยกว่า 48 ชม. Less than 48  hours", ln=True)
        if o22 == "no":
            pdf.cell(200, 5, txt=f"          [X] ระหว่าง 48 ชม.ถึง 84 ชม. Between 48  hours to 84 hours", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ระหว่าง 48 ชม.ถึง 84 ชม. Between 48  hours to 84 hours", ln=True)  
        if o22 == "yes3":
            pdf.cell(200, 5, txt=f"          [X] มากกว่า 84 ชม. More than 84 hours", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] มากกว่า 84 ชม. More than 84 hours", ln=True)        
        # Q.4.4
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.4    อายุของคนงาน (อนุญาตหลายตัวเลือก) Age of the workers (multiple options allowed):", ln=True, align='L')
        if o25:
            pdf.cell(200, 5, txt=f"          [X] อายุ 18 ปีขึ้นไป (ไปที่ข้อ 5) Above 18 years old (Go to Q5)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน__{o26}____คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อายุ 18 ปีขึ้นไป (ไปที่ข้อ 5) Above 18 years old (Go to Q5)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน__________คน No. of people", ln=True)
        if o27:
            pdf.cell(200, 5, txt=f"          [X] อายุระหว่าง 15-18 ปี (ไปที่ข้อ 4.5และ 4.6) Between 15-18 years old (Go to Q4.5&4.6)  ", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน___{o28}___คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อายุระหว่าง 15-18 ปี (ไปที่ข้อ 4.5และ 4.6) Between 15-18 years old (Go to Q4.5&4.6)  ", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน_____________คน No. of people", ln=True)
        if o29:
            pdf.cell(200, 5, txt=f"          [X] อายุต่ำกว่า 15 ปี(ไปที่ข้อ 3.2) Under 15 years old  (Go to Q3.2)", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน___{o299}___คน No. of people", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อายุต่ำกว่า 15 ปี (ไปที่ข้อ 4.5และ 4.6) Under 15 years old (Go to Q4.5&4.6) ", ln=True)
            pdf.cell(200, 5, txt=f"                    จำนวน_________คน No. of people", ln=True) 
# Q.4.5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.5    สำหรับผู้ที่อายุต่ำกว่า 18 ปี ช่วยงานประเภทใดบ้าง? (อนุญาตให้มีหลายตัวเลือก)", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         For those below 18 years old, what type of tasks do they help with? ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         (multiple options allowed) ", ln=True, align='L')      
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุระหว่าง 15-18 ปี for those age between 15-18 years old", ln=True, align='L')                 
        if o30:
            pdf.cell(200, 5, txt=f"          [X] กรีดยาง Tapping rubber tress", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] กรีดยาง Tapping rubber tress", ln=True)
        if o31:
            pdf.cell(200, 5, txt=f"          [X] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools)", ln=True)
        if o32:
            pdf.cell(200, 5, txt=f"          [X] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)    
        if o33:
            pdf.cell(200, 5, txt=f"          [X] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        if o34:
            pdf.cell(200, 5, txt=f"          [X] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        if o35:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ) Others (Please specify)_____{o36}_____", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อื่นๆ (โปรดระบุ) Others (Please specify)_____", ln=True)


        pdf.add_page()
        pdf.set_font_size(14)
        pdf.rect(160, 10, 40, 7, 'D')
        pdf.set_xy(160, 8)  # กำหนดตำแหน่งเริ่มต้นของข้อความ
        pdf.cell(40, 10, f"VD-{num}-PDPA{num1}-FL", align='L')  # ใส่ข้อความลงในสี่เหลี่ยมผืนผ้
        pdf.set_font_size(16)   
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุต่ำกว่า 15 ปี for those age under 15 years old", ln=True, align='L')                 
        if o37:
            pdf.cell(200, 5, txt=f"          [X] กรีดยาง Tapping rubber tress", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] กรีดยาง Tapping rubber tress", ln=True)
        if o38:
            pdf.cell(200, 5, txt=f"          [X] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การกำจัดวัชพืชด้วยตนเองด้วยเครื่องมือ Weed clearing manually with tools)", ln=True)
        if o39:
            pdf.cell(200, 5, txt=f"          [X] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การฉีดพ่นสารเคมี (สารกำจัดวัชพืช ฯลฯ ) Spraying chemicals (herbicide etc.)", ln=True) 
        if o40:
            pdf.cell(200, 5, txt=f"          [X] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] การแปรรูปยาง (ทำยางแผ่น) Rubber Processing (rubber sheets)", ln=True)
        if o41:
            pdf.cell(200, 5, txt=f"          [X] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เก็บรวบรวมน้ำยางจากถ้วย Collecting latex from cups", ln=True)
        if o42:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ) Others (Please specify)_____{o43}_____", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] อื่นๆ (โปรดระบุ) Others (Please specify)_____", ln=True)
        # Question 4.6
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4.6    สำหรับผู้ที่อายุต่ำกว่า 18 ปี ชั่วโมงทำงานเฉลี่ยต่อวันคือเท่าใด", ln=True, align='L')
        pdf.cell(200, 5, txt=f"         For those under 18 years old, what is their average work hours per day", ln=True, align='L') 
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุระหว่าง 15-18 ปี for those age between 15-18 years old", ln=True, align='L')                 
        if o44 == "yes":
            pdf.cell(200, 5, txt=f"          [X] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        if o44 == "no":
            pdf.cell(200, 5, txt=f"          [X] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)    
        pdf.cell(200, 5, txt=f"         สำหรับผู้ที่อายุต่ำกว่า 15 ปี for those age under 15 years old", ln=True, align='L')                 
        if o46 == "yes":
            pdf.cell(200, 5, txt=f"          [X] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] น้อยกว่า 3 ชั่วโมง (Less than 3 hours)", ln=True)
        if o46 == "no":
            pdf.cell(200, 5, txt=f"          [X] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] มากกว่า 3 ชั่วโมง (More than 3 hours)", ln=True)
        # Question 5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.5    พวกเขาเป็นแรงงานต่างด้าวหรือเปล่า Are they any foreign workers?", ln=True, align='L')               
        if o48 == "yes":
            pdf.cell(200, 5, txt=f"          [X] ต่างด้าวอย่างน้อย 1 คน Yes, at least 1 foreign worker", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ต่างด้าวอย่างน้อย 1 คน Yes, at least 1 foreign worker", ln=True)
        if o48 == "no":
            pdf.cell(200, 5, txt=f"          [X] ไม่ใช่ มีแต่คนทำงานในพื้นที่เท่านั้น No, only local workers", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ไม่ใช่ มีแต่คนทำงานในพื้นที่เท่านั้น No, only local workers", ln=True)
        # Question 6
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.6    แรงงานต่างด้าวจำเป็นต้องจ่ายค่าหลักประกันใดเพื่อทำงานบนที่ดินหรือไม่", ln=True, align='L')   
        pdf.cell(200, 5, txt=f"         Are foreign workers required to pay any fees to secure work on the land?", ln=True, align='L') 
            
        if o50 == "yes":
            pdf.cell(200, 5, txt=f"          [X] เงินประกัน (การเงิน ทรัพย์สินส่วนบุคคล หรือทรัพย์สิน) ", ln=True)
            pdf.cell(200, 5, txt=f"              Security Deposit (Financial, personal property or belongings) ", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] เงินประกัน (การเงิน ทรัพย์สินส่วนบุคคล หรือทรัพย์สิน) ", ln=True)
            pdf.cell(200, 5, txt=f"              Security Deposit (Financial, personal property or belongings) ", ln=True)
        if o50 == "yes1":
            pdf.cell(200, 5, txt=f"          [X] ค่าสมัคร (รวมค่านายหน้าด้วย) Recruitment fee (including to agent)", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ค่าสมัคร (รวมค่านายหน้าด้วย) Recruitment fee (including to agent)", ln=True)
        if o50 == "yes2":
            pdf.cell(200, 5, txt=f"          [X] ไม่เก็บหลักประกันใดๆ Do not collect any", ln=True)
        else:
            pdf.cell(200, 5, txt=f"          [ ] ไม่เก็บหลักประกันใดๆ Do not collect any", ln=True)

        # pdf.add_page()   
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      วัตถุประสงค์ของการสำรวจนี้คือเพื่อเข้าใจโซลูชันการผลิตยางธรรมชาติและความยั่งยืนของการเกษตรยางพารา ", ln=True)
        pdf.cell(200, 5, txt="การเข้าร่วมในการสำรวจนี้เป็นอิสระ คุณสามารถถอนตัวออกจากการสำรวจได้ตลอดเวลาโดยการติดต่อที่ eudr@tongthai.co.th", ln=True)
        pdf.cell(200, 5, txt="หรือ (02) 390-2051 โดยเราไม่มีความจำเป็นที่จะขายข้อมูลส่วนบุคคลเกี่ยวกับคุณที่เก็บรวบรวมในการสำรวจนี้หรือในทางอื่น", ln=True)
        pdf.cell(200, 5, txt="      The purpose of this survey is to understand the natural rubber supply chain and its ", ln=True)
        pdf.cell(200, 5, txt="sustainability.Your participation in this survey is voluntary.You may withdraw from this survey at", ln=True)
        pdf.cell(200, 5, txt="any time by contacting eudr@tongthai.co.th or (02) 390-2051. We do not sell the Personal Information ", ln=True)
        pdf.cell(200, 5, txt="about you which is collected in connection with this survey or otherwise.", ln=True)
        pdf.cell(200, 5, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      ข้าพเจ้าได้ให้ข้อมูลทั้งหมดแล้ว และยินยอมให้ใช้และเปิดเผยข้อมูลในการสำรวจนี้ เป็นไปตามกฎหมาย", ln=True)
        pdf.cell(200, 5, txt="คุ้มครองข้อมูลส่วนบุคคล (PDPA)", ln=True)
        pdf.cell(200, 5, txt="      This is to certify that the information I have provided above is to the best of my knowledge ", ln=True)
        pdf.cell(200, 5, txt="and belief.  I have consent to the collection, use and disclosure of this survey based on the Personal", ln=True) 
        pdf.cell(200, 5, txt="Data Protection Act (PDPA). ", ln=True)
        if signature_path:
            # Use signature image in PDF
            pdf.image(signature_path, x=10, y=235, w=30)
        pdf.cell(200, 25, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"____________________", ln=True, align='L')
        pdf.cell(200, 5, txt=f"ลายเซ็น Signature", ln=True, align='L')
        pdf.cell(200, 5, txt=f"วันที่ Date  {current_date}", ln=True, align='L')
 


        folder_path = os.path.join("pdfs_farmer", num)
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exis
        pdf_file_path = os.path.join(folder_path, pdf_file_name)
        pdf.output(pdf_file_path)
        
        pdf_file_name1 =  f"VD-{num}-PDPA-{num1}-ID.pdf"
        pdf = FPDF()
        if photo and allowed_file(photo.filename):
            pdf.add_page()
            pdf.image(photo_path, x=10, y=10, w=190)
        pdf_file_path1 = os.path.join(folder_path, pdf_file_name1)
        pdf.output(pdf_file_path1)

        return send_file(pdf_file_path, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500



pdf_folder1 = 'pdfs_pdpa'
pdf_folder2 = '../New folder'
pdf_folder3 = 'pdfs_farmer'

@app.route('/pdf/<folder>/<filename>')
def get_pdf(folder, filename):
    # เลือกโฟลเดอร์ที่จะส่งไฟล์ PDF จากพารามิเตอร์ folder
    if folder == 'folder1':
        return send_from_directory(pdf_folder1, filename)
    elif folder == 'folder2':
        return send_from_directory(pdf_folder2, filename)
    elif folder == 'folder3':
        return send_from_directory(pdf_folder3, filename)
    else:
        return 'Invalid folder'

@app.route('/pdf')
def pdf():
    # เรียกดูไฟล์ PDF จากทั้งสองโฟลเดอร์
    pdf_files1 = [file for file in os.listdir(pdf_folder1) if file.endswith('.pdf')]
    pdf_files2 = [file for file in os.listdir(pdf_folder2) if file.endswith('.pdf')]
    pdf_files3 = [file for file in os.listdir(pdf_folder3) if file.endswith('.pdf')]
    return render_template('pdf.html', pdf_files1=pdf_files1, pdf_files2=pdf_files2, pdf_files3=pdf_files3)


@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        folder_name = request.form['folder_name']
        folder_name1 = request.form['sec1']
        print(folder_name1)
        pdf_files = find_pdf_files(folder_name, folder_name1)
        # เรียกใช้งาน render_template เพื่อแสดงผลหน้าเว็บ
        return render_template('list.html', files=pdf_files, folder=folder_name, subfolder=folder_name1)
    return render_template('list.html', files=None, folder=None, subfolder=None)


def find_pdf_files(folder_name, folder_name1):
    try:
        folder_path = os.path.join(folder_name, folder_name1)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]
            return pdf_files
        else:
            return []
    except Exception as e:
        print(f"Error finding PDF files: {e}")
        return []



from urllib.parse import unquote

@app.route('/download_file/<path:subfolder>/<path:filename>')
def download_file(subfolder, filename):
    try:
        # Decode subfolder and filename from URL
        subfolder = unquote(subfolder)
        filename = unquote(filename)
        
        # Construct the full path to the file
        folder_path = os.path.join(app.root_path, subfolder)
        file_path = os.path.join(folder_path, filename)
        
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "File not found", 404
    except Exception as e:
        print(f"Error downloading file: {e}")
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(port=9999)
