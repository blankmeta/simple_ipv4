def to_decimal(bnr):
    dec_mask = ''
    for i in enumerate(range(4)):
        dec_mask += str(int(bnr.split('.')[i[0]], 2))
        dec_mask += '.'
    dec_mask = dec_mask[0:-1]
    return dec_mask


class Ip4:
    def __init__(self, ipv):
        self.ipv = ipv
        self.ip = ipv.split('/')[0]
        self.mask = ipv.split('/')[1]
        self.bnr_mask = ''
        self.bnr_ip = ''

    def mask_binary(self):
        self.bnr_mask = ''
        mask = int(self.mask)
        for i in enumerate(range(32)):
            if i[0] % 8 == 0 and i[0] != 0:
                self.bnr_mask += '.'
            if mask > 0:
                self.bnr_mask += '1'
                mask -= 1
            else:
                self.bnr_mask += '0'
        return self.bnr_mask

    def mask_decimal(self):
        return to_decimal(self.mask_binary())

    def ip_binary(self):
        self.bnr_ip = ''
        for value in self.ip.split('.'):
            value = "{0:b}".format(int(value)).rjust(8, '0')
            self.bnr_ip += f'{value}.'
        self.bnr_ip = self.bnr_ip[0:-1]
        return self.bnr_ip

    def ip_decimal(self):
        return to_decimal(self.ip_binary())

    def node(self):
        mask = self.mask_binary()
        return mask.count('0')

    def bitwise_net_binary(self):
        res = ''
        one_b = self.ip_binary().replace('.', '')
        two_b = self.mask_binary().replace('.', '')
        result = ''
        for i in enumerate(range(len(one_b))):
            if i[0] > (len(one_b) - self.node() - 1) and one_b[i[0]] != '.':
                result += '0'
            else:
                if one_b[i[0]] == '.':
                    result += '.'
                else:
                    if one_b[i[0]] == '1' and two_b[i[0]] == '1':
                        result += '1'
                    else:
                        result += '0'

        for i in enumerate(result):
            if i[0] % 8 == 0 and i[0] != 0:
                res += '.'
            res += i[1]

        result = res
        return result

    def bitwise_net_decimal(self):
        return to_decimal(self.bitwise_net_binary())

    def bitwise_node_binary(self):
        res = ''
        one_b = self.ip_binary().replace('.', '')
        result = ''
        for i in enumerate(range(len(one_b))):
            if i[0] < (len(one_b) - self.node()) and one_b[i[0]] != '.':
                result += '0'
            else:
                if one_b[i[0]] == '.':
                    result += '.'
                else:
                    result += one_b[i[0]]
        for i in enumerate(result):
            if i[0] % 8 == 0 and i[0] != 0:
                res += '.'
            res += i[1]

        result = res
        return result

    def bitwise_node_decimal(self):
        return to_decimal(self.bitwise_net_binary())

    def broadcast_binary(self):
        res = ''
        one_b = self.ip_binary().replace('.', '')
        two_b = self.mask_binary().replace('.', '')
        result = ''
        for i in enumerate(range(len(one_b))):
            if i[0] > (len(one_b) - self.node() - 1) and one_b[i[0]] != '.':
                result += '1'
            else:
                if one_b[i[0]] == '.':
                    result += '.'
                else:
                    if one_b[i[0]] == '1' and two_b[i[0]] == '1':
                        result += '1'
                    else:
                        result += '0'

        for i in enumerate(result):
            if i[0] % 8 == 0 and i[0] != 0:
                res += '.'
            res += i[1]

        result = res
        return result

    def broadcast_decimal(self):
        return to_decimal(self.broadcast_binary())