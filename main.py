import importlib
import os
import shutil
import mutagen
from mutagen import FileType, id3

from config import MUSICS_PATH, COVERS_PATH, LYRICS_PATH, OUTPUT_PATH
from utils import split_name
from PIL import Image

def query_file_type(file_path: str):
    """判断文件格式"""
    return mutagen.File(file_path, easy=True)


def add_cover2file(file_instance: FileType, cover_path: str):
    """
    添加封面图片到文件中
    :param file_instance: 文件实例
    :param cover_path: 封面图片路径
    :return:
    """
    # 获取当前文件的模块路径
    module = file_instance.__module__
    module_inst = importlib.import_module(module)
    pic_cls = getattr(module_inst, "Picture")
    if pic_cls is None:
        raise Exception("导入图片类失败")
    pic = pic_cls()
    img = Image.open(cover_path)
    width = img.width  # 图片的宽
    height = img.height  # 图片的高
    _format = img.format  # 图像格式
    with open(cover_path, "rb") as f:
        pic.data = f.read()
    # 设置图片格式
    pic.type = id3.PictureType.COVER_FRONT  # noqa
    mime = f"image/{_format}"
    pic.mime = u"%s" % mime
    pic.width = width
    pic.height = height
    pic.depth = 16
    # 添加对应的图片
    file_instance.add_picture(pic)
    file_instance.save()


def add_lyric2file(file_type_instance, lyric_path: str):
    """
    添加歌词到文件中
    :param file_type_instance: 文件实例
    :param lyric_path: 歌词路径
    :return:
    """
    pass


def main():
    """主程序入口"""
    fail_list = list()
    success_list = list()
    # 遍历指定文件路径下的所有文件
    for file_name in os.listdir(MUSICS_PATH):
        cover_message = ""
        lyric_message = ""
        # 获取音乐文件类型
        file_type_instance = query_file_type(os.path.join(MUSICS_PATH, file_name))
        # 判断是否识别出该文件
        if file_type_instance is None:
            fail_list.append({"name": file_name, "reason": "未识别出文件格式"})
        # 查询封面图片
        cover_file_list = os.listdir(COVERS_PATH)
        # 判断是否有对应的封面图片
        cover_name = [cover_name for cover_name in cover_file_list if cover_name.startswith(split_name(file_name))]
        if cover_name:
            try:
                add_cover2file(file_type_instance, os.path.join(COVERS_PATH, cover_name[0]))
            except Exception as e:
                cover_message = str(e)
        # 判断是否有对应的歌词
        lyric_file_list = os.listdir(LYRICS_PATH)
        lyric_name = [lyric_name for lyric_name in lyric_file_list if lyric_name.startswith(split_name(file_name))]
        if lyric_name:
            try:
                add_lyric2file(file_type_instance, os.path.join(LYRICS_PATH, lyric_name[0]))
            except Exception as e:
                lyric_message = str(e)
        if any([cover_message, lyric_message]):
            fail_list.append({"name": file_name, "reason": cover_message or lyric_message})
            continue
        success_list.append({"name": file_name, "reason": "success"})
        # 移动成功的文件到输出目录
        shutil.move(os.path.join(MUSICS_PATH, file_name), os.path.join(OUTPUT_PATH, file_name))

if __name__ == "__main__":
    main()
