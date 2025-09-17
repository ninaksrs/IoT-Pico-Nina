import qrcode as qr
path_of_file = r'qr_text.txt'
with open(path_of_file, 'rt', encoding ='UTF8') as f:
    read_L = f.readlines()
    count = 0
    for i in read_L:
        count += 1
        i = i.strip()
        print(i)
        qr_link = i
        qr_pic = qr.make(qr_link)
        qr_path = "QR Link_"+str(count)+".png"
        qr_pic.save(qr_path)
