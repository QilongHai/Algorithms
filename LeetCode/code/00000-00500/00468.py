class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            ipv4 = IP.split('.')
            if len(ipv4) != 4:
                return 'Neither'
            for item in ipv4:
                if len(item) > 1 and item[0] == '0':
                    return 'Neither'
                elif not item.isdigit():
                    return 'Neither'
                elif int(item) < 0:
                    return 'Neither'
                elif int(item) > 255:
                    return 'Neither'
            return 'IPv4'
        else:
            ipv6 = IP.split(':')
            if len(ipv6) != 8:
                return 'Neither'
            for item in ipv6:
                if not item:
                    return 'Neither'
                if len(item) > 4:
                    return 'Neither'
                if not all(map(lambda x: x.lower() in '0123456789abcdef', item)):
                    return 'Neither'
            return 'IPv6'