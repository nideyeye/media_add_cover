# 使用说明
1. 安装依赖包
```bash
pip install -r requirements.txt 
```
2. 将需要添加封面的歌曲文件移动至 musics 文件夹下
3. 将需要添加的封面文件重命名为对应的音乐文件名称,如音乐名称为 music.flac,则封面文件名为 music.jpg
4. 运行main.py
```bash
python main.py 
```
5. 添加完成的音乐文件将会出现在dist目录下
# 已实现功能
- 将封面内嵌至 flac 文件中
- 增加音频格式转换功能
- 支持命令行调用实现音频格式转化, 默认输出位置为项目的`output`目录下，需自行安装 `ffmpeg`，具体安装参考[ffmpeg官网](https://ffmpeg.org/download.html)
```bash
usage: convert_music_format.py [-h] [-p PATH] [-a {wav,mp3,flac,ogg,aac,m4a}] [-o OUTPUT_DIR] [-b {64k,128k,192k,256k,320k}] [-f] [-v]

音频格式转换工具 - 支持多种音频格式互转

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  输入音频文件路径 (default: None)
  -a {wav,mp3,flac,ogg,aac,m4a}, --aim-format {wav,mp3,flac,ogg,aac,m4a}
                        目标格式 (区分大小写) (default: None)
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        自定义输出目录 (默认: ./output) (default: None)
  -b {64k,128k,192k,256k,320k}, --bitrate {64k,128k,192k,256k,320k}
                        输出文件比特率 (default: 128k)
  -f, --force           强制覆盖已存在文件 (default: False)
  -v, --verbose         显示详细处理信息 (default: False)
```
# 正在开发的功能
- 将歌词内嵌至 flac 文件中
- 自动下载封面
- 自动下载歌词
- 嵌入结果可视化
- 支持更多格式
- 补全歌曲信息参数