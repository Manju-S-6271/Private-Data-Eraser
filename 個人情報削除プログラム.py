import csv
import sys
import time

def timesender(status, service):
    return f"[" + time.strftime("%a %H:%M:%S", time.localtime()) + " " + status + " " + service + "] "

def extract_data(output_file):
    current_line = 0
    # ユーザーがファイルをドラッグ＆ドロップした場合、ファイルパスはsys.argvに格納される
    if len(sys.argv) > 0:
        input_filename = sys.argv[1]
        print(timesender("INFO", "LOADER") + f"ファイル読込中 (0/2)")
    else:
        # ユーザーにファイルをドラッグ＆ドロップするように促す
        print(timesender("ERROR", "INPUT CHECKER") + f"入力値チェックエラー")
        print(timesender("INFO", "INPUT CHECKER") + f"ファイルをドラッグ＆ドロップしてください。")
        time.sleep(5)
        sys.exit()

    # CSVファイルを開く
    with open(input_filename, 'r') as csv_file:
        # CSVリーダーを作成
        csv_reader = csv.reader(csv_file)
        print(timesender("INFO", "LOADER") + f"ファイル読込中 (1/2)")
        
        # 新しいファイルに書き込むためのCSVライターを作成
        with open(output_file, 'w', newline='') as new_csv_file:
            print(timesender("INFO", "LOADER") + f"ファイル読込中 (2/2)")
            csv_writer = csv.writer(new_csv_file)
            indices_to_extract = [0, 1, 3, 8, 9, 12, 26, 34, 35, 49, 50]
            
            # ヘッダー行を抜き出して新しいファイルに書き込む
            header_row = next(csv_reader)  # 最初の行をヘッダーとして取得
            header_row = [header_row[i] for i in indices_to_extract]
            csv_writer.writerow(header_row)
            current_line = 0

            # データ行を抜き出して新しいファイルに書き込む
            for row in csv_reader:
                current_line += 1
                print(timesender("INFO", "WRITER") + f"データ呼出中 ({current_line}番目・{row[0]})")

                data_row = [row[i] for i in indices_to_extract]
                csv_writer.writerow(data_row)

    print(timesender("INFO", "System") + f"全{current_line}オーダーのデータは、 {output_file} として保存されました。")
    print(timesender("INFO", "System") + f"このプロンプトは5秒後に消えます。")
    time.sleep(5)
        

# ユーザーに入力ファイルと出力ファイルを指定させる
extract_data("output.csv")
