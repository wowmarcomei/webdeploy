from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Cookie':'Cookie:TASSK=enc%3AAP%2FPyLtcdIa4dzxk9dIPSztvAm3506XD2vMFHniTBfpVQzdpETRDAfb8LBLImAfUBozSCoUYswSm3cbdNBNpGplN2jtKh%2Bph1FI%2FHYJ5M25Py69BVkl%2Bqh%2Bww3D7Uxy0XA%3D%3D; TAUnique=%1%enc%3AaLlKFhLZQrZ%2BGi%2BPKejEvR5cQjY6%2FTd0wSWUqPxdPz8FzeIXfRYx4g%3D%3D; TAAuth3=3%3A07b8abc3bf81b366e3e1fab080fcf5be%3AAHVtmPtJA%2FLKRkuej2bcKL%2F%2BzHna9AbK5gRBWtJ01dOYBIgWH9UsvzQ2ETNTZU7852fabgofpDj3qEJNlek1X4oZ0yYlqMRFFoL3XO%2FIsE%2FooIQaZmMDTDjoY%2Fs4xJ%2FfePpIGUx0PoNrHWP8P7YAUA1GYEyWfzIJCHHHHoR4Yf510dSDA0v43mhkrXTFdj0n1l9bzE2JLUOssCr6ZeHDDhQ%3D; ServerPool=T; PAC=ALx0SM8boIS9IfoTuoRcvKhnG9H-sl7kQZjM7EfoAuzIexO1IgU99ksKZLtUvp8uhIB2rQj9dy-_MFx5qq9G5VGRN8p5Va1g1cF2pzk0Ec3MbmNlfrR8y2WoymJW4dOBdQ%3D%3D; PMC=V2*MS.34*MD.20170322*LD.20170329; CommercePopunder=SuppressAll*1490832766416; TART=%1%enc%3AfhovjynoxL2lT85PJ9rvskJOJIZKUMWl%2FmXrd%2BjludPOIQYo4EffNMfJGmT0m8K7vBAVFjqGd%2BM%3D; TATravelInfo=V2*AC.RGN*A.2*MG.-1*HP.2*FL.3*RVL.105127_82l60763_88*RS.1; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1490837632%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7C2016sticksess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!AFA0dIpPln9AzHjaDPdH1H91d3bZLwBBOLXhpx9jQPZS%2FnbpPn2c8ouimACGFHsv1bVxuWOjHilKdF9%2B4aDPEmGmsL0%2FCxYBL%2BRRGitK7p9zmwt%2F%2FUYKFtNxXhP19kD8EvXEeFOdQo7jvw40NAlOhydTOwWfXI9WpSZEfKuas3eC%2C1; TASession=V2ID.ECEAD2ED7D56F5E6D42577603B8C0C9C*SQ.13*LS.PageMoniker*GR.7*TCPAR.12*TBR.21*EXEX.69*ABTR.65*PHTB.80*FS.15*CPU.77*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.D249AB384490AE5F426281E8B16B9A67*FA.1*DF.0*FBH.2*FLO.60763*TRA.true*LD.60763; TAUD=LA-1490832747045-1*LG-168258-2.1.F.*LD-168259-.....'
}

urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html'.format(str(i)) for i in range(0,1050,30)]

def get_tripadvisor(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(4)

    titles = soup.select('div.container.containerLLR > div.title.titleLLR > div')
    images = soup.select('img[width="54"]')
    cates = soup.select('div.container.containerLLR > div.attraction_types > span.moreText')

    for title,image,cate in zip(titles,images,cates):
        data = {
            'title':title.get_text(),
            'image':image.get('src'),
            'cates':cate.get_text()
        }
        print(data)

for singleurl in urls:
    get_tripadvisor(singleurl)