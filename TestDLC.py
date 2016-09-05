
from computedlc import DLC;


dlcstr = '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';
dlc = DLC()
print "result: ", dlc.decrypt(dlcstr)




""""
        #get response for dlc
        try:
            data = "destType=jdtc5&b=" + self.b + "&p=" + self.p + "&srcType=dlc&data=" + dlc[-88:] + "&v=" + self.v
            header = {'User-agent' : self.user_agent, 'rev': self.v}
            req = urllib2.Request(self.api, data, header)
            h = urllib2.urlopen(req)
            print 'h is:', h
        except:
            return "404"
"""


#jdkey
#?nP:Cn?E?=F?0w