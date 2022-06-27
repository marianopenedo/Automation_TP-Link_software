import menu
import catchIP
import web
import os


results = menu.menu()
ip = catchIP.catchIp(results[2])
web.web(login=results[0], passw=results[1], res=ip[0], ssid=results[3], senhaW=results[4], model=results[5], cwd=ip[1])
os.system("cls") or None
