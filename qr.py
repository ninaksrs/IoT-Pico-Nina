import qrcode as qr
import image
qr_link = 'www.sanook.com'

qr_pic = qr.make(qr_link)
qr_path = "qr_link_"+qr_link+".png"

qr_pic.save(qr_path)