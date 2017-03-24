from bs4 import BeautifulSoup
import requests
import time

'''
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

titles = soup.select('div.property_title > a[target="_blank"]')
images = soup.select('img[width="160"].photo_image')
cates = soup.select('div > div.element_wrap > div > div.p13n_reasoning_v2 > a:nth-of-type(1)')

print(titles,images,cates,sep='\n==============================\n')

for title,image,cate in zip(titles,images,cates):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'cates':list(cate.stripped_strings)
    }
    print(data)
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'ServerPool=X; TASSK=enc%3AAP%2FPyLtcdIa4dzxk9dIPSztvAm3506XD2vMFHniTBfpVQzdpETRDAfb8LBLImAfUBozSCoUYswSm3cbdNBNpGplN2jtKh%2Bph1FI%2FHYJ5M25Py69BVkl%2Bqh%2Bww3D7Uxy0XA%3D%3D; TAUnique=%1%enc%3AaLlKFhLZQrZ%2BGi%2BPKejEvR5cQjY6%2FTd0wSWUqPxdPz8FzeIXfRYx4g%3D%3D; TART=%1%enc%3AfhovjynoxL2lT85PJ9rvskJOJIZKUMWl%2FmXrd%2BjludPOIQYo4EffNMfJGmT0m8K7vBAVFjqGd%2BM%3D; CommercePopunder=SuppressAll*1490232854973; PAC=AN1y0tbbVMlaa5t5VT3478rc_6ol53wvmjk2ChhnnGia1zdIY9ouXUFYlvrN5Dwj-P-ICmQokSmws8DjvQUWPJcW9mEGQNLtiE-ocECk8N1sq6bWLxLJCdjwJVh1Vvr52Q%3D%3D; PMC=V2*MS.34*MD.20170322*LD.20170323; SecureLogin2=3.4%3AAHzVYm8xf07mkmr%2Bbq%2BUQ3x7hPUgraKkEltchTXPRWFVQPTC9XsPHgu5Q0PkGfoj0vX3Q7nKlpz1E2d2cRKhxaloIhlA24SaLC%2F8I6G9R8Fa6CtN2NIFxRMJy0nXOAeQ16csGVzW9iAnFYhJmLOj3TSWJxugcTHviM3kGzSxtV6C6lAXSKfZIyssXfj1OY4CCdbzuW%2BMXQit%2Fx8izraIYwA%3D; TAAuth3=3%3A07b8abc3bf81b366e3e1fab080fcf5be%3AAHVtmPtJA%2FLKRkuej2bcKL%2F%2BzHna9AbK5gRBWtJ01dOYBIgWH9UsvzQ2ETNTZU7852fabgofpDj3qEJNlek1X4oZ0yYlqMRFFoL3XO%2FIsE%2FooIQaZmMDTDjoY%2Fs4xJ%2FfePpIGUx0PoNrHWP8P7YAUA1GYEyWfzIJCHHHHoR4Yf510dSDA0v43mhkrXTFdj0n1l9bzE2JLUOssCr6ZeHDDhQ%3D; TATravelInfo=V2*AC.RGN*A.2*MG.-1*HP.2*FL.3*RVL.60763_82l105127_82*RS.1; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C4%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1490837632%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7C2016sticksess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!ACgeb1PU27Y2buH9hdm%2BtyvCy7Ltz5Grc6%2BU%2F9HxfDaGWQPTf56%2F0kw%2FrE6m1kdd8NsAQWRJgPNzqpHIQHsI955qWMlYQ%2BIv1oQjMIUV0XchbpR8g9TUoEw%2BCqZjrgzSSA8%2BxwHhZJMG1QwT2%2Fe84TO773Jq4rpiK%2FEA4rO12FZI%2C1; TASession=%1%V2ID.DCFA503C59A73797AD987125D120B1DB*SQ.45*PR.427%7C*LS.MetaPlacementAjax*GR.21*TCPAR.85*TBR.56*EXEX.96*ABTR.89*PHTB.7*FS.82*CPU.48*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.D249AB384490AE5F426281E8B16B9A67*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1490232765571-1*LG-83816400-2.1.F.*LD-83816401-.....; EVT=gac.TopNav*gaa.selectSavedTrips*gal.*gav.0*gani.false*gass.Attraction_Review*gasl.105127*gads.Saves*gadl.*gapu.WNRtGwokMC0AAv5hf9QAAABM*gams.2'
}

url_save = 'https://cn.tripadvisor.com/Saves'
wb_data = requests.get(url_save,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)
titles = soup.select('div > div > div.saves-location-details.ui_media > div.media-content > div > a')
images = soup.select('div > div > div.saves-location-details.ui_media > div.media-left > a')
cates = soup.select('div > div > div.saves-location-details.ui_media > div.media-content > div > div.poi_type_tags > span.ui_icon.attractions')


for title,image,cate in zip(titles,images,cates):
    data={
        'title': title.get_text(),
        'image': image.get('url'),
        'cate': list(cate.stipped_strings)
    }
    print(data)