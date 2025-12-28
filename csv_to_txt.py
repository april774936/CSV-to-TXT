import pandas as pd
import re

def clean_and_convert():
    csv_file = "RedditNews.csv"
    output_file = "Historical_News_Archive.txt"
    
    print(f"🔄 '{csv_file}' 변환 시작...")
    try:
        df = pd.read_csv(csv_file)
        with open(output_file, "w", encoding="utf-8") as f:
            for _, row in df.iterrows():
                date = str(row['Date'])
                news = str(row['News'])
                # 지저분한 b' 접두사 제거 로직
                clean_news = re.sub(r"^b['\"]", "", news)
                clean_news = re.sub(r"['\"]$", "", clean_news)
                f.write(f"[{date}] {clean_news}\n")
        print(f"✅ 변환 완료: {output_file}")
    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    clean_and_convert()
