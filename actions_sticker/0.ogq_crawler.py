import re
import time
import requests

page_index = 0
page_size = 30

while True:
    page_url = f"https://api.ogqmarket.naver.com/da/digital-assets/search/stickers?ordering=RECENT&page={page_index}&pageSize={page_size}"
    page = requests.get(page_url)

    if page.ok:
        page_list = page.json()
        artwork_list = page_list["data"]
        total_count = page_list["totalCount"]
        hasNext = page_list["hasNext"]
        
        # pdb.set_trace()
        for i, artwork in enumerate(artwork_list):
            artwork["artworkId"]            # 5f4bd5ffa5efd
            artwork["defaultName"]          # '오늘도 출근! 아기 고양이 쫀떡의 직장 생활'
            artwork["defaultDescription"]   # '퇴사를 꿈꾸지만.. 오늘도 출근합니다!'
            artwork["tags"]                 # ['고양이', '쫀떡', '회사', '귀여운', '직장']
            artwork["mainImageUrl"]         # https://storep-phinf.pstatic.net/ogq-5f56c4f796a63/stk/plabcaoh.png?type=m240_240
            artwork["creator"]["userId"]    # '5f48f62eea469'
            artwork["creator"]["nickname"]  # '체예'
            
            # # read stickers
            # artwork_url = f"https://ogqmarket.naver.com/artworks/sticker/detail?artworkId={artwork['artworkId']}"
            # artwork_html = requests.get(artwork_url)
            
            # matches = re.findall(r"stickerImages:\s*\[(.*?)\]", artwork_html.text)
            # matches = re.findall(r"imageLoc:\s*\"(.*?)\"", matches[0])
            
            # for sticker_raw_url in matches:
            #     sticker_url = bytes(sticker_raw_url, "utf-8").decode("unicode_escape")
            #     time.sleep(0.1)
            #     print(f"crawling: {sticker_url} [{page_index*page_size+i}/{total_count}]")
        
        if hasNext: page_index += 1
        else: break
print("crawling finished!!!")
