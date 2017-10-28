# -*- coding: utf-8 -*-

import TOBY
from TOBY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = TOBY.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
I̴̧̞͔̣͍̾̓͊͛ͭͨ̿̈́͗ͤ͊͗̐́ͣ̏̕ͅN̵̡̡̛̬̖͔̟̹̥̝̘̬̮̮̬̠̪͔̬̄͂ͨ̂̇̒ͬͧ́̐̓̉̔̍͌́ͨO̢̜̞͙͔͎̬̯̮̬̟̊̔ͫ̄͋̔ͫ̍̋ͨͥ͂͊̍ͯ̅̈́͞ͅR̶̙̩̠͉̱̙̟̺̖͔͈͎̲̰̫ͮ͋̆̔̃̌̍͂̈͋̔̀͑̄̒͊̚̚͠I̷̧̋̅̋͑̔͗͑ͯͮ͛ͩͨ̊ͭ̐̆́҉̺͔̯͉̺̲͕ ̷̸̰̬͍̼̲̘͈̳̳̦̖̹̱̻̱̻̀ͯ̾̽ͪ̿͋͢ͅB̴̯̪͇͔͇̤̝̝̰͔̞͐̈̈́̒ͥͤͫ̾͑ͣ̌ͦͨͨ̔̒̚͝Ọ̞̯̖̠̱̣̤̘̫̜ͣͨ̽̓͆̇ͥ̈́̏̽̇ͩͯ͋̀T̵̵̢̼̫̰͚̲͗͂̈́͒ͨ̂̇͌ͣ͂ͣ̈̂ͥͧ̄͢͝ ̡̜̜̬̫͓̝̮̮̮͕͇̱̟͖͎͋̈́ͫ̏͊ͯ͐̾͗͂̉͂͜͝͞C̷̸̢̀ͤ̿̃̎̿͐̉̿͂͑͑̑ͯ́̄͌͠҉̫̝̞̦͉̤̱̫̫̹̰̺Ǫ̴͈̮͔̳͍̦̗͈̉̓̊̎̂̈́͘M͔͈̦͓̱̠̠͓̱̯̭͗̉̽̇̈́̓͒ͤ̔ͨ͒̃̌̏ͩ̀̚̚͜ͅM̸̞̹̭̜̤̤̪̬͚̬̲̟̬͕̊͗̾ͤͦ͐͑ͭ̀͞͞Ȃ̶̵͉͙̪̥͈͍̤̺ͬ͆͊ͦ̾ͩN̡͙̭̘̹͙͈̮̹̙̬͈̲̝̖̮̤̬͛͂͊́͂̈́̈ͤ̑̇ͫ͠D̛̟͕̯̩͇̪̝̽ͨͥ̓͊̽ͥ̆ͬ̀ͅ

🍃 CommandMember 🍃

🍀 Creator 
🍀 Inori  say 
🍀 GCreator 

🌳 Command Creator 🌳

🌴 Admin add @ 
🌴 Admin remove @ 
🌴 Adminlist
🌴 InviteMeTo: 

☔ Command Admin ☔

🌂 Id 
🌂 Mid 
🌂 Mid @ 
🌂 Me 
🌂 Urloff 
🌂 Urlon 
🌂 Ginfo 
🌂 Cancel 
🌂 Gn 
🌂 Cname 
🌂 Cstatus 
🌂 Gcreator:inv 
🌂 Out 
🌂 Invite 
🌂 Cn 
🌂 Gift 
🌂 Respon 
🌂 Tagall 
🌂 Glist 
🌂 Spam: 
🌂 Check > Absen 
🌂 Steal + Mid 
🌂 Steal @ 

🌷 Command Mimic  🌷

🌹 Mimic @ (By Tag)
🌹 Mimic:add: @ (By Tag)
🌹 Mimic:del: @ (By Tag)
🌹 ListTarget 

🌺 CommandPenting 🌺

🌸 Guest On/Off 
🌸 Mad On/Off 
🌸 Qr On/Off 
🌸 Ban @ (By Tag)
🌸 Unban @ (By Tag)
🌸 Kill Ban 
🌸 Kill @ (By Tag)
🌸 Nk 
🌸 Vk 
🌸 Hancur 
 
BOT : PANCY
SUPPORT BY : L̵̛̦̝̟̼͙̬̦̝̯͒͒̊͠I̶̎̎͋̑͂̽ͥ̚҉̼̮͍͇̣̦̪͎͓Ņ̴̠̖̹͙̗͕́̏̉̔̾͋ͧ̑Ḙ̛̦̭̰̘̳̼̪̒͛̃͊̒ͮ̋́̚͡ͅ ̶̣̙͈̳͍͂̀̽̾̇̓̐ͅD͈͎͇̠̪͍͇͉̀̈͌E̵͊̀҉͔͖̭͉̘͇V͈̖̪͈̓̓ͦ̂̓̍͒̐ͅͅE̝̲͋ͨL̛̯͎̝̈̌̃́Ŏ̵͌̔ͤ͊͏̙͙ͅP̴͎͙͔̠̖̫ͬ͑͑̅̆̉̕E̸̴̠͛͂ͨR͈̫͎͒ͮ͒ͯ̀ ̶̢̯̝͕̫̮̺͊̉̿̿̽̈̅͐ͅB̙͉͉̼̫̗̟̯̽̍ͪ̋͆͂͂͘͡Ö̸̧͍̬̟͙́̅͆̎̃̕T̶̯͔̦̟̠̊̀̄̐̇́̄͂ͭ͜S̵̡͈̝̭͈̪ͮ̈̓̍̀
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["uddb6b470ab4b54c5fbc69d7600cc3bc8"]
creator=["uddb6b470ab4b54c5fbc69d7600cc3bc8"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~babydino20",
    "lang":"JP",
    "comment":"Owner : line://ti/p/~babydino20",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImage2(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self._client.sendMessage(M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                cl.updateGroup(X)
                Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
            if op.param3 in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí¤êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí¤êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí¤êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               cl.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL0‰96¥9¡¯\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "Cv1 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "Cv3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "Cv1 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "Cv2 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "Cv3 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["Cv2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Cv1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Cv2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Cv3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"No one is inviting")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 curl","Cv2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 curl","Cv3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Cv1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Cv2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "Cv3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â„1¤7¦Ë„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","K on","Contact on","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â„1¤7¦Ë„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","K off","Contact off","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥Ââ„1¤7šÃ¥Å„1¤7 :Ã£â€šÂªÃ£Æ’Â„1¤7","Join on","Auto join:on","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥ÂÆ’Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥Ââ„1¤7šÃ¥Å„1¤7 :Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Join off","Auto join:off","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥ÂÆ’Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ„1¤7 Ã©â„1¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â„1¤7™Ã§Â»ÂÃ£â‚¬â€šÃ¨Â¦ÂÃ¦â„1¤7”Â¶Ã¥Â¼â‚¬Ã¨Â¯Â·Ã¦Å’â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â„1¤7¢Â°Ã¥Ââ„1¤7˜Ã©â‚¬Â")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â„1¤7žÃ¥Â°ÂÃ§Â»â„1¤7žÃ§â„1¤7Â¨Ã¨â„1¤7¡ÂªÃ¥Å Â¨Ã©â„1¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â„1¤7™Ã§Â»Â„1¤7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡Â„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡ÂºÃ¯Â¼Å¡Ã©â„1¤7“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡Â„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡ÂºÃ¯Â¼Å¡Ã©â„1¤7”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â„1¤7„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â„1¤7„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â„1¤7¦Â³Ã¦â„1¤7“Â­Ã£â‚¬â€„1¤7")
            elif msg.text in ["Set"]:
				if msg.from_ in admin:
					md = ""
					if wait["contact"] == True: md+=" Contact : on\n"
					else: md+=" Contact : off\n"
					if wait["autoJoin"] == True: md+=" Auto join : on\n"
					else: md +=" Auto join : off\n"
					if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " Group cancel : off\n"
					if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
					else: md+=" Auto leave : off\n"
					if wait["timeline"] == True: md+=" Share : on\n"
					else:md+=" Share : off\n"
					if wait["autoAdd"] == True: md+=" Auto add : on\n"
					else:md+=" Auto add : off\n"
					if wait["commentOn"] == True: md+=" Comment : on\n"
					else:md+=" Comment : off\n"
					cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â„1¤7 Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€„1¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å„1¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â„1¤7 Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€„1¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å„1¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë† Ã©â„¢Â¤Ã¤Âºâ„1¤7 Ã¤Âºâ„1¤7¹Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å’Ã£â‚¬â€„1¤7")
            elif msg.text in ["Group id","Ã§Â¾Â¤Ã§Âµâ€žÃ¥â„1¤7¦Â¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"Ã¦â€¹â„1¤7™Ã§Â»ÂÃ¤Âºâ„1¤7 Ã¥â„1¤7¦Â¨Ã©Æ’Â¨Ã§Å¡â„1¤7žÃ©â„1¤7šâ‚¬Ã¨Â¯Â·Ã£â‚¬â„1¤7„1¤7")
            elif "album removeÃ¢â€ â„1¤7„1¤7" in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album removeÃ¢â€ â„1¤7„1¤7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë† Ã©â„¢Â¤Ã¤Âºâ„1¤7 Ã¤Âºâ„1¤7¹Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å’Ã£â‚¬â€„1¤7")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¨Â¿Â½Ã¥Å„1¤7 :Ã£â€šÂªÃ£Æ’Â„1¤7","Add on","Auto add:on","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¨Â¿Â½Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¨Â¿Â½Ã¥Å„1¤7 :Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Add off","Auto add:off","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¨Â¿Â½Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â„1¤7¦Â³Ã¦â„1¤7“Â­Ã£â‚¬â€„1¤7")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneÃ£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Message","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¨Â¿Â½Ã¥Å„1¤7 Ã¥â€¢ÂÃ¥â‚¬â„¢Ã¨ÂªÅ¾Ã§Â¢ÂºÃ¨ÂªÂ„1¤7"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â„1¤7š\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Ã£â€šÂ³Ã£Æ’Â¡Ã£Æ’Â³Ã£Æ’Ë„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","Comment on","Comment:on","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©Â¦â„1¤7“Ã„1¤7 ÂÃ§â€¢â„¢Ã¨Â¨â‚¬Ã¯Â¼Å¡Ã©â„1¤7“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã£â€šÂ³Ã£Æ’Â¡Ã£Æ’Â³Ã£Æ’Ë„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Comment on","Comment off","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©Â¦â„1¤7“Ã„1¤7 ÂÃ§â€¢â„¢Ã¨Â¨â‚¬Ã¯Â¼Å¡Ã©â„1¤7”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â„1¤7¦Â³Ã¦â„1¤7“Â­Ã£â‚¬â€„1¤7")
            elif msg.text in ["Comment","Ã§â€¢â„¢Ã¨Â¨â‚¬Ã§Â¢ÂºÃ¨ÂªÂ„1¤7"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")


            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Absen":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal 7¬8\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n¡¸set¡¹you can send 7¬8 read point will be created 7¬8")
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------

            elif msg.text in ["Masuk","Jarvis"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)

            elif msg.text in ["Cv1 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ti)
					G = kk.getGroup(msg.to)
					G.preventJoinByTicket = True
					ki.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Cv2 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kk.acceptGroupInvitationByTicket(msg.to,Ti)
					G = ki.getGroup(msg.to)
					G.preventJoinByTicket = True
					kk.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Out","out"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv1 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Cv2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv3 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Hancur" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Hancur","")
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						ki.sendText(msg.to,"saya di perintahkan untuk membersikan grub ini´")
						kk.sendText(msg.to,"Group DiBersihkan.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Not found.")
							kk.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[ki,kk,kc]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									ki.sendText(msg.to,"Group cleanse")
									kk.sendText(msg.to,"Group cleanse")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes Cv")
										kk.sendText(msg.to,"Fuck You"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Cv")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak DiTemukan")
							kk.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Berhasil")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif msg.text in ["Test"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Hadir Boss!!")
#-----------------------------------------------
            elif "Inori say " in msg.text:
					bctxt = msg.text.replace("Inori disini ","")
					ki.sendText(msg.to,(bctxt))
#-----------------------------------------------
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "uddb6b470ab4b54c5fbc69d7600cc3bc8"}
					cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif "Admin add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                     else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Steal " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#-----------------------------------------------
            elif "Steal @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
#-----------------------------------------------
            elif msg.text in ["hmm"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Batuk Kong??")
            elif msg.text in ["wkwkwk"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"malik mana ya , gw jadi kangen naena sama dia")
            elif msg.text in ["Cv say chomel pekok"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
					kk.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
					kc.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
            elif msg.text in ["#welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
					kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping","Samlekom","samlekom"]:
				ki.sendText(msg.to,"Mamanx ô€œô€…”Har Harô¿¿")
				kk.sendText(msg.to,"Ngentod ô€œô€…”Har Harô¿¿")
				kc.sendText(msg.to,"Yuuk ô€œô€…”Har Harô¿¿")
#-----------------------------------------------
            elif msg.text in ["Responsename","responsename"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Tob”9±2")
#-----------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "Testing...")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â„1¤7„1¤7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecÃ¢â€ â„1¤7„1¤7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by @Pancy_Bot")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by line.me/ti/p/~babydino20")
						print "DiLike"
					except:
							pass
				else:
						print "Sudah DiLike"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
