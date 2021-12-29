################# 流程 ###################
# -------------------------------------- #
# 1. 指定資料夾位置
# 2. 指定要讀取的檔名 (使用 RE 規則)
# 3. 指定要查找的字串 (使用 RE 規則)
# 4. 遞迴列出指定資料夾位置下的所有目標檔案
# 5. 解壓縮 (.zip), 存在記憶體
# 6. 一次解壓縮一個檔案
# 7. 查找指定字串
# 8. 將結果寫入 result
# 9. 檢查是否還有檔案要查找 (回到 5.)
# -------------------------------------- #
##########################################

from datetime import datetime

import json
import os
import logging
import re
import zipfile

logging.basicConfig(filename='logs/logfile.log', encoding='utf-8', level=logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

def main():
    config = {}
    results = []
    try:
        with open("conf/config.json", "r", encoding="utf-8") as json_file:
            config = json.load(json_file)
    except Exception as e:
        logger.exception(e)   
        return

    for root, dirnames, zip_filenames in os.walk(config["target_folder"]):
        for zip_filename in zip_filenames:
            target_zippath = os.path.join(root, zip_filename)
            lines = {}
            for pattern in config["target_filenames"]:
                if re.search(pattern, target_zippath):
                    logger.debug(f"search {target_zippath} ... ") 
                    lines = search_targets(target_zippath, config["target_strings"])
                    results.extend(lines)
    
    now = datetime.now()
    result_filename = f"result/{now.strftime('%Y-%m-%d_%H-%M-%S')}.log"
    with open(result_filename, 'w', encoding="utf-8") as result_file:
        result_file.writelines(results)
    logger.info(f"result at: {result_filename}")
        

def search_targets(target_zipfile, target_strings):
    result = []
    target_zip = zipfile.ZipFile(target_zipfile)
    for filename in target_zip.namelist():
        content = target_zip.read(filename).decode("utf-8")
        for target in target_strings:
            # logger.debug(f"target: {target}")
            lines = re.findall(rf"{target}", content)
            for line in lines:
                logger.debug("Found!")
                result.append(f"{target_zipfile}\\{filename}: {line}")
    return result

if __name__ == '__main__':
    main()