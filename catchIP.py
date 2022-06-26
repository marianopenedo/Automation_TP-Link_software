import subprocess as sub
import os, re
import pyperclip as pc


def catchIp(Wifi):
    lines = []
    finallines = []
    count = 0
    res = ''
    
    cwd = os.getcwd()
    # print(cwd)
    pc.copy(cwd)

    pc.copy(sub.check_output(['ipconfig']).decode('iso8859-1'))
    os.system("cd %s" %cwd)
    os.system('ipconfig > ipDefault.txt')

    if Wifi:
        with open ("ipDefault.txt", "w", encoding="iso-8859-1") as file:
            file.write(pc.paste())
            file.close()

        with open ("%s\ipDefault.txt" %cwd) as file:
            file_read = file.read()
            matches = re.findall(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', file_read)
            file.close()
        
        ip_tuple = matches[-1]
        ip = "%s.%s.%s.%s"%(ip_tuple[0],ip_tuple[1],ip_tuple[2],ip_tuple[3])
        res ='http://' + ip

    else:
        with open('%s\IpDefault.txt' %cwd) as f:
            for line in f:
                lines.append(line)
        
        for i in range(len(lines)):
            if re.search('(?i)Adaptador Ethernet Ethernet.*', lines[i]):
                while count != 2:
                    finallines.append(lines[i])
                    if lines[i] == "\n": 
                        count += 1
                    i+=1

        for i in range(len(finallines)):
            if re.search(r'(?i) gateway*.', finallines[i]):
                gateway = finallines[i]

        for i in range(len(gateway)-1):
            if gateway[i].isnumeric():
                count = i
                for j in range(count,len(gateway)-1):
                    if re.search(r'([0-9.])', gateway[j]):
                        res += gateway[j]
                break
        
        res = 'http://' + res

    # print(res)
    os.remove("%s\IpDefault.txt" %cwd)
    return [res, cwd]

catchIp(True)