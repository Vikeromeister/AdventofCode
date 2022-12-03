input = """E20D41802B2984BD00540010F82D09E35880350D61A41D3004E5611E585F40159ED7AD7C90CF6BD6BE49C802DEB00525272CC1927752698693DA7C70029C0081002140096028C5400F6023C9C00D601ED88070070030005C2201448400E400F40400C400A50801E20004C1000809D14700B67676EE661137ADC64FF2BBAD745B3F2D69026335E92A0053533D78932A9DFE23AC7858C028920A973785338832CFA200F47C81D2BBBC7F9A9E1802FE00ACBA44F4D1E775DDC19C8054D93B7E72DBE7006AA200C41A8510980010D8731720CB80132918319804738AB3A8D3E773C4A4015A498E680292B1852E753E2B29D97F0DE6008CB3D4D031802D2853400D24DEAE0137AB8210051D24EB600844B95C56781B3004F002B99D8F635379EDE273AF26972D4A5610BA51004C12D1E25D802F32313239377B37100105343327E8031802B801AA00021D07231C2F10076184668693AC6600BCD83E8025231D752E5ADE311008A4EA092754596C6789727F069F99A4645008247D2579388DCF53558AE4B76B257200AAB80107947E94789FE76E36402868803F0D62743F00043A1646288800084C3F8971308032996A2BD8023292DF8BE467BB3790047F2572EF004A699E6164C013A007C62848DE91CC6DB459B6B40087E530AB31EE633BD23180393CBF36333038E011CBCE73C6FB098F4956112C98864EA1C2801D2D0F319802D60088002190620E479100622E4358952D84510074C0188CF0923410021F1CE1146E3006E3FC578EE600A4B6C4B002449C97E92449C97E92459796EB4FF874400A9A16100A26CEA6D0E5E5EC8841C9B8FE37109C99818023A00A4FD8BA531586BB8B1DC9AE080293B6972B7FA444285CC00AE492BC910C1697B5BDD8425409700562F471201186C0120004322B42489A200D4138A71AA796D00374978FE07B2314E99BFB6E909678A0
"""


# input = "38006F45291200"
# input = "EE00D40C823060"
# input = "A0016C880162017C3686B18A3D4780"


class Packet:
    def __init__(self, startindex, ID, father=-1):
        self.ID = ID
        self.start = startindex
        self.end = -1
        self.elapsed = 0
        # self.active = True
        self.typeID = -1
        self.version = -1
        self.literal = ""
        self.value = -1
        self.lenID = -1
        self.length = -1
        self.fatherID = father
        self.subpackets = []

    def operate(self):
        if self.typeID == 0:
            self.value = 0
            for id in self.subpackets:
                self.value += packets[id].value
        elif self.typeID == 1:
            self.value = 1
            for id in self.subpackets:
                self.value = self.value * packets[id].value
        elif self.typeID == 2:
            self.value = 999999999999999999999999
            for id in self.subpackets:
                self.value = min(self.value, packets[id].value)
        elif self.typeID == 3:
            self.value = 0
            for id in self.subpackets:
                self.value = max(self.value, packets[id].value)
        elif self.typeID == 5:
            if packets[self.subpackets[0]].value > packets[self.subpackets[1]].value:
                self.value = 1
            else:
                self.value = 0
        elif self.typeID == 6:
            if packets[self.subpackets[0]].value < packets[self.subpackets[1]].value:
                self.value = 1
            else:
                self.value = 0
        elif self.typeID == 7:
            if packets[self.subpackets[0]].value == packets[self.subpackets[1]].value:
                self.value = 1
            else:
                self.value = 0


# print(len(input))
code = bin(int(input, 16))[2:].zfill((len(input) - 1) * 4)
print(code)

totalversion = 0
version_counter = 0
typeID_counter = 0
literal_counter = 0
length_counter = 0
newpacket_flag = True
version_flag = False
typeID_flag = False
literal_flag = False
newliteral_flag = False
lastliteral_flag = False
operator_flag = False
length_flag = False
activePacket = 0
version = ""
typeID = ""
literal = ""
length = ""
packets = []
fatherID = -1
activeStack = []
elapsed = 0
for [i, num] in enumerate(code):
    if newpacket_flag:
        print("")
        packets.append(Packet(i, len(packets), fatherID))
        try:
            activeStack[-1].subpackets.append(len(packets)-1)
        except:
            pass
        newpacket_flag = False
        version_flag = True
        version_counter = 2
        version = num
        activePacket = packets[-1]
    elif version_flag:
        version += num
        version_counter -= 1
        if version_counter == 0:
            activePacket.version = int(version, 2)
            # print("version", int(version, 2))
            totalversion += int(version, 2)
            version = ""
            version_flag = False
            typeID_flag = True
            typeID_counter = 3
    elif typeID_flag:
        typeID += num
        typeID_counter -= 1
        if typeID_counter == 0:
            activePacket.typeID = int(typeID, 2)
            # print("typeID", int(typeID, 2))
            typeID_flag = False
            if int(typeID, 2) == 4:
                newliteral_flag = True
            else:
                operator_flag = True
            typeID = ""
    elif newliteral_flag:
        if num == "0":
            lastliteral_flag = True
        newliteral_flag = False
        literal_flag = True
        literal_counter = 4
    elif literal_flag:
        literal += num
        literal_counter -= 1
        if literal_counter == 0:
            activePacket.literal += literal
            literal = ""
            if lastliteral_flag:
                activePacket.value = int(activePacket.literal, 2)
                print("literal", activePacket.literal)
                literal_flag = False
                lastliteral_flag = False
                # activePacket.active = False
                try:
                    while (activeStack[-1].lenID == 0 and activeStack[-1].end <= i) or \
                            (activeStack[-1].lenID == 1 and len(activeStack[-1].subpackets) >= activeStack[-1].length):
                        # if activeStack[-1].lenID == 1 and len(activeStack[-1].subpackets) > activeStack[-1].length:
                            # print(activeStack[-1].length, "subpackets expected", len(activeStack[-1].subpackets), "found")
                        activeStack.pop(-1)
                except IndexError:
                    pass
                    # if activeStack[-1].lenID == 0 and activeStack[-1].end < i:
                    #     print(activeStack[-1].end, "expected", i, "found")


                # activePacket = packets[activePacket.fatherID]
                # fatherID = activePacket.ID
                newpacket_flag = True
                print(len(activeStack))
            else:
                newliteral_flag = True
                literal_flag = False
    elif operator_flag:
        activeStack.append(activePacket)
        activePacket.lenID = int(num)
        operator_flag = False
        length_flag = True
        if num == "1":
            length_counter = 11
        elif num == "0":
            length_counter = 15
        else:
            print("WTF")
    elif length_flag:
        length += num
        length_counter -= 1
        if length_counter == 0:
            length_flag = False
            activePacket.length = int(length, 2)
            if activePacket.lenID == 1:
                print("length", int(length, 2), "packets")
            else:
                print("length", int(length, 2), "bits")
                activePacket.end = activePacket.start + activePacket.length + 7 + 15 - 1
            print(len(activeStack))
            # packets.append(Packet(i, activePacket.ID))
            # activePacket.subpackets.append(len(packets))
            fatherID = activePacket.ID
            newpacket_flag = True
            # version_flag = True
            # version_counter = 3
            length = ""

print(len(packets[0].subpackets))
print(totalversion)

for depth in range(200):
    for packet in packets:
        packet.operate()

print(packets[0].value)