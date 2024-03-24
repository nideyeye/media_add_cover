def split_name(file_name:str)->str:
    """
    切分文件名后缀,返回正式文件名
    :param file_name: "music_file.mp3"
    :return: "music_file"
    """
    return file_name.split(".")[0]