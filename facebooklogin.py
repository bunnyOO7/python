import mechanize
ch=mechanize.Browser()
ch.set_handle_robots(False)
ch.addheaders=[('User-agent','Google Chrome')]
ch.open('https://www.facebook.com/login.php')
ch.select_form(nr=0)
ch.form['email']='adityabhardwaj792@gmail.com'
ch.form['pass']='iamosm'
sub=ch.submit()
print(sub.geturl())
