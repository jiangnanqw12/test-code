import hashlib


def calculate_md5(file_path):
    """计算文件的MD5校验和"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.digest()


def create_header(version_info, reserved_bytes, md5_checksum):
    """创建文件头部信息"""
    return version_info + reserved_bytes + md5_checksum


def add_header_to_bin(header, bin_file_path, output_file_path):
    """将头部信息添加到bin文件并保存"""
    with open(bin_file_path, "rb") as bin_file:
        bin_content = bin_file.read()

    with open(output_file_path, "wb") as output_file:
        output_file.write(header)
        output_file.write(bin_content)


# 示例数据
version_info = b'\x00\x00\x00\x00\x00\x00'  # 6字节版本信息
reserved_bytes = b'\x00\x00'               # 2字节预留

# 计算bin文件的MD5
bin_file_path = "tms320f28335-csd_without_power_on_music.bin"
md5_checksum = calculate_md5(bin_file_path)

# 创建头部
header = create_header(version_info, reserved_bytes, md5_checksum)

# 添加头部到bin文件并保存
output_file_path = "tms320f28335-csd_without_power_on_music.ota"
add_header_to_bin(header, bin_file_path, output_file_path)
