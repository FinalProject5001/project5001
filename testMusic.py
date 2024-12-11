from spotify_app.features.music_recognition import identify_and_search

def test_music_recognition():
    # 替换为实际音频文件路径
    audio_file_path =  "./testSong.mp3"   # 指向准备好的音频文件
   # 指向准备好的音频文件

    # 调用音乐识别功能
    result = identify_and_search(audio_file_path)

    # 打印结果
    print("Music Recognition Result:")
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Audd.io Result:")
        print(result["audd_result"])
        print("\nSpotify Details:")
        print(result["spotify_details"])

if __name__ == "__main__":
    test_music_recognition()