from subprocess import Popen, PIPE


def get_address():
    out, err = Popen(['netstat', '-antlp'], stdout=PIPE).communicate()

    for line in out.splitlines():
        line = line.decode('utf8')
        if 'ESTABLISHED' not in line:
            continue

        line = line.split()
        if '/' not in line[-1]:
            continue
        p = line[-1].split('/')[0]
        line[-1] = str(p) + ' -> ' + open('/proc/' + p + '/cmdline', 'rb').read().replace(b'\x00', b' ').decode('utf8')
        if 'jetty' not in line[-1]:
            continue

        res = line[3].split(':')
        return res[0], int(res[1])
