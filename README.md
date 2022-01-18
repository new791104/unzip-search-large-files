# unzip-search-large-files

根據特定字串查找指定目錄下的檔案內容

## 注意事項
* 請確保記憶體空間足夠容納解壓縮後的 zip 檔案

## 使用方法
* 設定 `config.json`
    ```json
    // conf/config.json 
    {
        // 資料夾路徑
        "target_folder": "",
        // 要搜尋的檔案名稱, 使用 RE 規則
        "target_filenames": ["test.zip"],
        // 要搜尋的字串, 使用 RE 規則
        "target_strings": ["charlie"]
    }
    ```
* 執行
    ```sh
    unzip-search-large-files$> python main.py
    ```
* 搜尋結果
    ```json
    // result/yyyy-mm-dd_hh-mm-ss.log
    .\test.zip\test.txt: charlie
    ```

---
author:
  - Charlie Chen, new791104@gmail.com
---