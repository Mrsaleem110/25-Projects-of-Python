#terminal main pip install qrcode run krne k bad import kia.
import qrcode
#jis chez ka code banana h us ka link data k variable main copy  paste krdo.
data = 'https://www.linkedin.com/in/muhammad-saleem-342269293/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BEsFs5oXGSl%2BBp57s4UfGjg%3D%3D'
# qrcode ki image generate hogi img k variable main .make(main data dedia k kis ki generate krne h)
img = qrcode.make(data)
#img save krwae h "my linkedin qrcode k name sa or yeah user k folder main save ho jaegi dafault"
img.save("My linkedin Qr Code")
