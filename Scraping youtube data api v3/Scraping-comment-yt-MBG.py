import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Fungsi untuk mendapatkan semua data komentar dari video YouTube
def get_all_comments(video_id, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        comments = []
        next_page_token = None
        
        print("Mulai mengambil komentar...")
        while True:
            """
            Mengirim permintaan API untuk mendapatkan komentar video per halaman
            Catatan: 
            maxResults dibatasi maksimal 100 oleh YouTube API.  
            Tapi kita tetap bisa mengambil semua komentar karena menggunakan perulangan pageToken. 

            """
            
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            ).execute()

            # Mendapatkan semua komentar dari respons API halaman ini
            for item in response['items']:
                comment_id = item['id']
                comment_snippet = item['snippet']['topLevelComment']['snippet']
                
                author_name = comment_snippet.get('authorDisplayName', '')
                author_id = comment_snippet.get('authorChannelId', {}).get('value', '')
                comment_text = comment_snippet.get('textDisplay', '')
                like_count = comment_snippet.get('likeCount', 0)
                comment_link = f"https://www.youtube.com/watch?v={video_id}&lc={comment_id}"

                comments.append({
                    'Comment ID': comment_id,
                    'Comment Link': comment_link,
                    'Commenter Name': author_name,
                    'Commenter ID': author_id,
                    'Comment': comment_text,
                    'Likes': like_count
                })
            
            print(f"Berhasil mengambil {len(comments)} komentar...")

            # Periksa apakah ada halaman berikutnya
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        return comments

    except HttpError as e:
        print(f'Error: {e}')
        return None

# Setel video ID dan kunci API Anda
video_id = 'SVI8xheP-j4'
api_key = 'API Key' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan semua data komentar
comment_data = get_all_comments(video_id, api_key)

if comment_data:
    # Menyimpan data komentar ke dalam file CSV dengan kolom lengkap
    filename = 'comment_data.csv'
    fieldnames = ['Comment ID', 'Comment Link', 'Commenter Name', 'Commenter ID', 'Comment', 'Likes']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for comment in comment_data:
            writer.writerow(comment)

    print(f"Data komentar telah disimpan ke dalam file '{filename}'.")
else:
    print("Gagal mengambil data komentar.")
