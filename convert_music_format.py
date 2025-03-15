import os
import argparse
from pydub import AudioSegment
from typing import Optional


def convert_audio_format(
        input_path: str,
        output_format: str,
        output_dir: Optional[str] = None,
        bitrate: str = "128k",
        overwrite: bool = False
) -> str:
    """音频格式转换核心函数

    Args:
        input_path: 输入文件路径
        output_format: 目标格式 (wav/mp3/flac等)
        output_dir: 输出目录 (默认为当前目录下的output文件夹)
        bitrate: 比特率 (默认128k)
        overwrite: 是否覆盖已存在文件

    Returns:
        转换后的文件完整路径

    Raises:
        FileNotFoundError: 输入文件不存在
        ValueError: 不支持的格式
        RuntimeError: 转换失败
    """
    # 输入文件验证
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    if not os.path.isfile(input_path):
        raise ValueError("输入路径必须是文件")

    # 准备输出路径
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = output_dir or os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{base_name}.{output_format.lower()}")

    # 避免重复转换
    if os.path.exists(output_path) and not overwrite:
        print(f"文件已存在, 跳过转换: {output_path}")
        return output_path

    # 执行格式转换
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(
            output_path,
            format=output_format,
            bitrate=bitrate
        )
    except Exception as e:
        raise RuntimeError(f"格式转换失败: {str(e)}") from e

    return output_path


def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="音频格式转换工具 - 支持多种音频格式互转",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-p", "--path",
        type=str,
        help="输入音频文件路径"
    )

    parser.add_argument(
        "-a", "--aim-format",
        type=str.lower,
        choices=["wav", "mp3", "flac", "ogg", "aac", "m4a"],
        help="目标格式 (区分大小写)"
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default=None,
        help="自定义输出目录 (默认: ./output)"
    )

    parser.add_argument(
        "-b", "--bitrate",
        type=str,
        default="128k",
        choices=["64k", "128k", "192k", "256k", "320k"],
        help="输出文件比特率"
    )

    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="强制覆盖已存在文件"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="显示详细处理信息"
    )

    args = parser.parse_args()

    # 执行转换
    try:
        print(f"⌛ 开始转换: {os.path.basename(args.path)}")
        output_path = convert_audio_format(
            input_path=args.path,
            output_format=args.aim_format,
            output_dir=args.output_dir,
            bitrate=args.bitrate,
            overwrite=args.force
        )

        if args.verbose:
            input_size = os.path.getsize(args.path) / 1024 / 1024
            output_size = os.path.getsize(output_path) / 1024 / 1024
            print(f"✅ 转换成功\n"
                  f"📥 输入文件: {args.path} ({input_size:.2f}MB)\n"
                  f"📤 输出文件: {output_path} ({output_size:.2f}MB)\n"
                  f"🎚️ 比特率: {args.bitrate}")
        else:
            print(f"✅ 转换完成: {output_path}")

    except Exception as e:
        print(f"❌ 转换失败: {str(e)}")
        exit(1)


if __name__ == "__main__":
    convert_audio_format("F:\BaiduNetdiskDownload\Call recording 猪猪号_241225_143812.m4a", "wav")
    main()
