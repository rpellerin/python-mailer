import tempfile, time, sys
import pymailer

f = tempfile.NamedTemporaryFile('r+t', suffix='.html', delete=True)

f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\
<html lang="fr">\
<head>\
<meta http-equiv="content-type" content="text/html;charset=utf-8" />\
</head>\
<body>\
<p>The computer has been turned on, on ')

#print(f.name + ' created')

arg = ['-s', f.name, '~/python-mailer/recipients.csv', 'Computer Turned On']

f.write((time.strftime("%A %d %B %Y, %H:%M:%S")))
f.write('.</p>\
</body>\
</html>')

f.seek(0) # return to beginning of file

pymailer.main(arg)

f.close() # temporary file is automatically deleted here
