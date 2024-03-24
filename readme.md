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
# 正在开发的功能
- 将歌词内嵌至 flac 文件中
- 自动下载封面
- 自动下载歌词
- 嵌入结果可视化
- 支持更多格式
- 补全歌曲信息参数