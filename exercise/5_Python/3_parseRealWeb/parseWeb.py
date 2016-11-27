from bs4 import BeautifulSoup
import requests
import time


url = 'https://cn.tripadvisor.com/Tourism-g298184-Tokyo_Tokyo_Prefecture_Kanto-Vacations.html'
url_saves = 'https://cn.tripadvisor.com/Saves/all'
urls = ['https://cn.tripadvisor.com/Tourism-g{}-Tokyo_Tokyo_Prefecture_Kanto-Vacations.html'.format(str(i)) for i in range(30,930,30)]

headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Cookies':'VRMCID=%1%V1*id.10568*llp.%2F; ServerPool=B; TASSK=enc%3AALkJ40e4MgAO%2Bxj%2FfRVcvZVVhaMHwFdlYKtPdWQ3g%2FVAX8Dzgtn7CKFaHkqJiA%2BR5xFcUcyh425Ix52fKYvHTLmG43WTO9LTsnKwXmBzZzTR2tjyH1ivODwCyRB0%2BIZVrw%3D%3D; TAUnique=%1%enc%3Agr3ekGijTca40EVZwz9g%2BpvYUnWTGIgzKJ0O%2B1z0JI82jHwltRJPGQ%3D%3D; TART=%1%enc%3AuNBFWcM%2FYPrJmseNGPii3z2MUnpfKGJH6GR%2BmlppsOk9h2xemaIdTPYkpK5f%2Fv7nJ7r1iEgl44g%3D; __gads=ID=d0e9b5654ba6f730:T=1480132924:S=ALNI_MZz7kiNab8cjrgaClUnJ5AJkzULww; CommercePopunder=SuppressAll*1480133104291; SecureLogin2=3.4%3AAM%2FmZtPsiNgHqmAmcwF2QuuUCEq33PHy4Ldvdwrw7F2Pe2Qz1iAiEsYqOBF7tBXAh5SNffCNcGbh6FZyUL%2B5fhNhqUUpPEeNp8dWzDSqeFYYXOyxv4h%2FlCxL0lhkc1%2FThzHAVqER861G82eBgxvpxxUfwiOJyw4PE5kHTuz%2FKSdbftiaz5ehMoT8LK%2B7Vuppu1j%2FWKFtXe3Ul2TSDJBxJ6Q%3D; TAAuth3=3%3Abe5337493eb849ea885373017231db2f%3AAE86bF0hQyYSyO1lbKghsVthtgXMTCiOkThVlkVa17Az75Z0GpmULdNttRqIqXjQDJujyGV1mOp%2BQSDlD2xn%2B7%2F7DDy5jfXOdarYT6J224eCso5ZMFfnlf5tgXYnJ2TgBWvbNlwnN3vlxG0W5%2Ba9NTJrmUJy5BsfYe%2FsWaGWDP9WP3ZxW8hHN9Vmi3UbJMRZMD%2BSBEisuxIy0dzqICzCwSE%3D; PAC=AHUOtVJXU0QUyae9BBn7Tk6Km5WwY4MVFJkhbgyq99KmcBq9_peKxLi4YTfzSTnwGqOQY442rBNyVrvrk6Xpk_d_JOTkNUAkDAp5T0BCNqqJamm5FAA08pO9RYUTv1GrHQ%3D%3D; TATravelInfo=V2*AC.RGN*A.2*MG.-1*HP.2*FL.3*RVL.28953_330l298184_330l310298_330l60763_330l105125_331l105127_331l60827_331l102741_331l103887_331*RS.1; TAReturnTo=%1%%2FAttraction_Review-g60763-d103887-Reviews-Statue_of_Liberty-New_York_City_New_York.html; NPID=; TASession=%1%V2ID.C75173E243503D44E1175C004806BFE5*SQ.176*PR.427%7C*LS.Saves*GR.11*TCPAR.72*TBR.68*EXEX.60*ABTR.87*PPRP.98*PHTB.3*FS.2*CPU.18*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.D249AB384490AE5F426281E8B16B9A67*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.103887; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C9%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C7%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C5%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1480737725%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Cpssamex%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAUD=LA-1480132908475-1*LG-82655304-2.1.F.*LD-82655305-.....; roybatty=TNI1625!AN5Q1Se81Qw%2FBF%2F3vMBeGBZA98ZjRT2%2B85DJZHCdiHc%2BwY44RFqNX2tWNDNM6XfxaDy1G%2FSRfNSwC%2BiLPaCteobS3xecRdo6xD49pzv0IZPS06R3l5UKAfIJrqsqWYaCnjAfbE4bwGRugloSlrPA7tQlpNmrxy8xq12nLS22eOxd%2C1',
}

headers_mobile = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Cookies':'VRMCID=%1%V1*id.10568*llp.%2F; ServerPool=B; TASSK=enc%3AALkJ40e4MgAO%2Bxj%2FfRVcvZVVhaMHwFdlYKtPdWQ3g%2FVAX8Dzgtn7CKFaHkqJiA%2BR5xFcUcyh425Ix52fKYvHTLmG43WTO9LTsnKwXmBzZzTR2tjyH1ivODwCyRB0%2BIZVrw%3D%3D; TAUnique=%1%enc%3Agr3ekGijTca40EVZwz9g%2BpvYUnWTGIgzKJ0O%2B1z0JI82jHwltRJPGQ%3D%3D; TART=%1%enc%3AuNBFWcM%2FYPrJmseNGPii3z2MUnpfKGJH6GR%2BmlppsOk9h2xemaIdTPYkpK5f%2Fv7nJ7r1iEgl44g%3D; __gads=ID=d0e9b5654ba6f730:T=1480132924:S=ALNI_MZz7kiNab8cjrgaClUnJ5AJkzULww; CommercePopunder=SuppressAll*1480133104291; SecureLogin2=3.4%3AAM%2FmZtPsiNgHqmAmcwF2QuuUCEq33PHy4Ldvdwrw7F2Pe2Qz1iAiEsYqOBF7tBXAh5SNffCNcGbh6FZyUL%2B5fhNhqUUpPEeNp8dWzDSqeFYYXOyxv4h%2FlCxL0lhkc1%2FThzHAVqER861G82eBgxvpxxUfwiOJyw4PE5kHTuz%2FKSdbftiaz5ehMoT8LK%2B7Vuppu1j%2FWKFtXe3Ul2TSDJBxJ6Q%3D; TAAuth3=3%3Abe5337493eb849ea885373017231db2f%3AAE86bF0hQyYSyO1lbKghsVthtgXMTCiOkThVlkVa17Az75Z0GpmULdNttRqIqXjQDJujyGV1mOp%2BQSDlD2xn%2B7%2F7DDy5jfXOdarYT6J224eCso5ZMFfnlf5tgXYnJ2TgBWvbNlwnN3vlxG0W5%2Ba9NTJrmUJy5BsfYe%2FsWaGWDP9WP3ZxW8hHN9Vmi3UbJMRZMD%2BSBEisuxIy0dzqICzCwSE%3D; PAC=AHUOtVJXU0QUyae9BBn7Tk6Km5WwY4MVFJkhbgyq99KmcBq9_peKxLi4YTfzSTnwGqOQY442rBNyVrvrk6Xpk_d_JOTkNUAkDAp5T0BCNqqJamm5FAA08pO9RYUTv1GrHQ%3D%3D; TATravelInfo=V2*AC.RGN*A.2*MG.-1*HP.2*FL.3*RVL.28953_330l298184_330l310298_330l60763_330l105125_331l105127_331l60827_331l102741_331l103887_331*RS.1; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C9%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C7%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C5%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1480737725%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Cpssamex%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d103887-Reviews-Statue_of_Liberty-New_York_City_New_York.html; roybatty=TNI1625!ALdSIdWiQUTX8B6AjfjRJMRF%2Brzclg2Mof0%2FFB875fVELTkG5KXnMeL4f%2Fmurk%2Bb2j3cF6p%2BvvFCJOrRUZXvrM29TL%2F1b499puSCmkzCUzvPgFXVeJ8LhEPzFW7kVWTjOLKo4BMYd9Mm%2FozmzJfLTwWR3uDX2Jt8IKCf8KzMjVEF%2C1; TASession=%1%V2ID.C75173E243503D44E1175C004806BFE5*SQ.187*PR.427%7C*LS.MetaPlacementAjax*GR.11*TCPAR.72*TBR.68*EXEX.60*ABTR.87*PPRP.98*PHTB.3*FS.2*CPU.18*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.D249AB384490AE5F426281E8B16B9A67*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.103887; TAUD=LA-1480132908475-1*LG-83416954-2.1.F.*LD-83416955-.....; NPID=',
}

'''
使用函数get_attractions直接抓取网页
'''
def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(4) #中断4s
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div div > a.hotel.name')
    images = soup.select('img[width="400"]')
    cates = soup.select('div.p13n_reasoning_v2')
    print(titles,images,cates,sep='\n***********\n')
    for title,image in zip(titles,images):
        data = {
            'title': title.get_text(),
            'img': image.get('src'),
            # 'cate': list(cate.stripped_strings)
        }
        print(data)

'''
使用函数get_favs传入header参数进行解析
'''
def get_favs(url,data):
    wb_data = requests.get(url,headers=data)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.location_summary a.title')
    images = soup.select('a.thumbnail')
    telephones = soup.select('span.text')

    for title, image, telephone in zip(titles,images,telephones):
        data={
            'title':title.get_text(),
            'image':image.get('style'),
            'telephone':telephone.get_text(),
        }
        print(data)

get_favs(url_saves,headers_mobile)
