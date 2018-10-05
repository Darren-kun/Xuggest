

import random

class MatchingHeaders():

    def __init__(self):

        # self.USA_cookie = 'x-wl-uid=18OFwwOgo1yq08sFZJRIeWYisOH8morTTb+XylBVl+C4n9C5FLAGN4d2sbjzQj1+KrWq1Q6TxZy8=; session-token=owbniuTqY8cRHUN93X8yK6GsKrrMuwigRGro7lN5aBkX5IADGZFrBSIJsy6+Rd8aO1CDzLv9l5bcrowEiC0Xs2FL60UFvuU7u0RVuFSdCMV+mgrrat5J6hvnw3htaSNVFMVlxviTqMiLpMxIwqgVCVyFX5khTQTEqPyv4OEwP2O388zACB0KVS6Hz5OPMfJY; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714; csm-hit=tb:H2H5S3GV40FN9RKEY15K+b-9FQC9XX9BPZNNW31WXSR|1536033272985&adb:adblk_no'
        self.USA_cookie = 'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; s_vn=1567824131517%26vn%3D6; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; session-token=xRRGCBw33Akur0tJF0r8++qJqF6m8bxQXyFr/q4yDswcTdvQr2z/a7hGhXWX272+FsHfCuLNnzL6Nge94L2RCryUjKvgsw7rgnYUNY/8FwUknUSFweoq7jsOIxmvyrLkqvKpcA57rSz51LBYu+Spgcb997ogjIcvMXXCRRunMQ4YHXwB0sDKPUy7u6uxekw7Fh2J5KieZe2IQ9l0HLJbCYWfQm+7AwefYRVf6jHSw/SGTi0nwb2lBzedXBADeuDCo7kep59F3amZOvVfRX4Ulg==; csm-hit=tb:RFS8ADR7Z22MV5CSTAFC+s-RFS8ADR7Z22MV5CSTAFC|1537837609176&adb:adblk_no; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714'

        self.UK_cookie = '''at-acbuk=Atza|IwEBILB65q8rA2KSv-Y8WFXWgH0UgGbtkWh138wiqt30gBmlJoFVqHF-RB_cziU8xf97HVVgoc7PHRJVcHvnz200wg5jUAdPozEskgo7DdZTgPMKSK-grfbbN3EZIGfcWEuok2g-diK2jy8OggRAt8k5ej_ZwR4MS6w1NDI0N25OaqU9gOq7WRak4khdNV1z7cSlOVR5vRDbIN4EoBlCzn3TfLROmwUYMOwp1OAWCxZniWqU3_UEjJgBLu-BF5awXhVmjWrh2VFm2Oeg87c40AZxIppx0T6hMB-Ap8OScBubGE0BtdG44RLbUZX7PMj-MiTd1i9qhqvybdatVFrGQaAM2BZMOpfYDntKyI2-otvFkqln7_Q1yqNsJ4zozlXL4oMTgMVpDybUm8TrHiiPdTrlZETX; sess-at-acbuk="Nuv2g/dTPhm4YjP6mh6hUAAm6VgZP3p/hJdAnRcadr0="; sst-acbuk=Sst1|PQGsOeWO2qEow4NwlQj1gOY5Cxj5QlTHhg-L3rcs9PAvIYbb710RcSF_p551DagxfFp0LHldbQQ0mJ04YTg8pEG_KurLjd05IWRE6LD1k2-2QfmsRPwWbhtfq7DLc-IZxVWSL2TE9a47-owVudIUUbUd3YQddFNoGkM1x4MDEOe3uOP06flbRZ-f416a7nh2WBb477ll2Otiy5wlU0nGTRktmiRh9WHfx5j_9T7XXTgKbARSiPFNniIWitk5dGNiDPz44McutLcLni1rgO-olN4krQoNsm_7rchji9lTG3AIJv9A_LRLQCbRadwgmbUj3_hJHepFXc-OP9NLnmYhCA1Kzw; x-wl-uid=1muHCEEwwEyWq0VHosiHEIhK+KteZZdxwOkO8RB4DzUorsFMkQxLiwMDY4bOkZPTcwezTMn0zV15TFgEPZEOkCg==; lc-acbuk=en_GB; session-token="wwMRrbXenCcqMsbuKQNkL8BXTVc2I48Uj1PptQmMhaBtsizquVR13Jnz3cyzj5pv9C0q1KfnEEzTn/YKiBpF2/SE0PEFAAI3KImvZcPxSXDAi8JShqzqKnZbGNqPRGfIvBFK1jK++P6XIDtgY9ipArGBZIo1S0c9DuLkBPGPTdNu/O2GDaeatqrpaCDCvUVbHsYvmK82+Lx0WL8/ut/cD9z3siIwgRL7D0fghtZtAvnuEGLC4cMlHrXsTi/JtqZlfcGbEhtXrG2TtT1SBkAluA=="; x-acbuk="74P@bJpcWxl2tNk6mUvBXgxPaT8YlslXrwRwXIG5y3woZtzlLTWe1d33@w46RcCL"; ubid-acbuk=259-2948611-7840936; session-id-time=2082758401l; session-id=259-1136416-4224409; csm-hit=tb:0NR6843RBJBQ97858B5K+s-CFD45CQH10NX7FR7KD2Y|1537430364810&adb:adblk_no&t:1537430364810'''

        self.user_agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36']


    def matching_Header(self,Country,url):

        cookic = eval('self.{}_cookie'.format(Country))
        user_agent = random.choice(self.user_agent)
        headers = {
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'accept-encoding': 'gzip, deflate, br',
             'accept-language': 'zh-CN,zh;q=0.9',
             'cache-control': 'max-age=0',
             'cookie': cookic,
             'referer': url,
             'upgrade-insecure-requests': '1',
             'user-agent': user_agent
        }

        return headers

matching_headers_obj = MatchingHeaders()

