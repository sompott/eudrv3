
// Initialize Signature Pad
var canvas = document.getElementById('signature');
var signaturePad = new SignaturePad(canvas, {
    backgroundColor: 'rgba(255, 255, 255, 0)',
    penColor: 'black',
    minWidth: 1,
    maxWidth: 3
});

// ปรับขนาด canvas เมื่อเกิดการเปลี่ยนขนาดหน้าต่าง
window.addEventListener('resize', resizeCanvas);

function resizeCanvas() {
    var ratio = Math.max(window.devicePixelRatio || 1, 1);
    canvas.width = canvas.offsetWidth * ratio;
    canvas.height = canvas.offsetHeight * ratio;
    canvas.getContext("2d").scale(ratio, ratio);
    signaturePad.clear(); // เคลียร์ลายเซ็นเมื่อขนาด canvas เปลี่ยน
}

// เรียกฟังก์ชัน resizeCanvas เพื่อปรับขนาด canvas เมื่อโหลดหน้าเว็บ
resizeCanvas();

document.getElementById('clear-button').addEventListener('click', function () {
    signaturePad.clear();
});
document.getElementById('submit-bu').addEventListener('click', function () {
// Get the signature data URL
var dataURL = signaturePad.toDataURL();

// Send the signature data to Flask
fetch('/save_signature', {
method: 'POST',
headers: {
    'Content-Type': 'application/json',
},
body: JSON.stringify({ signature: dataURL }),
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        isSignatureSaved = true; // เมื่อบันทึกลายเซ็นเรียบร้อยแล้วให้ตั้งค่าตัวแปร isSignatureSaved เป็น true
        alert('บันทึกลายเซ็นสำเร็จ');
    } else {
        isSignatureSaved = false; // เมื่อไม่สามารถบันทึกลายเซ็นได้ให้ตั้งค่าเป็น false
        alert('Failed to save signature!');
    }
})
.catch(error => {
    console.error('Error:', error);
    isSignatureSaved = false; // เกิดข้อผิดพลาดในการส่งข้อมูลลายเซ็น
    alert('Error saving signature!');
});
});


var isSignatureSaved = false; // เพิ่มตัวแปรสำหรับเก็บสถานะการบันทึกลายเซ็น

document.getElementById('data-form').addEventListener('submit', function (event) {
event.preventDefault(); // Prevent form submission

if (!isSignatureSaved) { // Check if the signature is saved
    alert('กรุณาบันทึกลายเซ็นก่อนที่จะส่งข้อมูล');
    return;
}

var formData = new FormData(this); // Get form data
// Send form data to Flask endpoint
fetch('/submit-form', {
    method: 'POST',
    body: formData
})
.then(function (response) {
    if (response.ok) {
        window.location.href = '/page2';
        return response.blob(); // Convert response to blob
    } else {
        throw new Error('Failed to submit form');
    }
})
.then(function (blob) {
var fullName = document.getElementById('full-name').value.trim().replace(/\s+/g, '_'); // Get the value of input with id "full-name"
var fullName1 = document.getElementById('full-name2').value.trim().replace(/\s+/g, '_'); // Get the value of input with id "full-name2"

if (window.navigator && window.navigator.msSaveOrOpenBlob) { // Check if the browser is Internet Explorer
    window.navigator.msSaveOrOpenBlob(blob, fullName + '_submitted_form.pdf'); // Use IE-specific method to download file
} else { // For other browsers
    var url = window.URL.createObjectURL(blob); // Create URL for blob

    var a = document.createElement('a');
    a.href = url;
    
    // Set the file name with full names, replacing special characters with underscores
    a.download = fullName + '-' + fullName1 + '.pdf'; 
    
    a.style.display = 'none';
    document.body.appendChild(a);

    a.click();

    // For Chrome on Android, additional handling may be needed
    if (navigator.userAgent.match(/Android/i) && navigator.userAgent.match(/Chrome/i)) {
        // Delay removing the link to ensure download is complete
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 100);
    } else {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }
}
})


.catch(function (error) {
    console.error('Error:', error);
});
});