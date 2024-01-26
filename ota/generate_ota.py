import hashlib

import subprocess

import struct


def execute_tiobj2bin_command(output_file=r"tms320f28335-csd"):
    """
    Executes the TI object to binary conversion command for a specified output file.

    Parameters:
    output_file (str): The base name of the output file, without extension.

    Prints the output and error of the command execution.
    """
    if not output_file:
        print("Error: Output file name is required.")
        return

    command = rf'cmd.exe /c "C:\ti\ccs1240\ccs\utils\tiobj2bin\tiobj2bin {output_file}.out {output_file}.bin C:\ti\ccs1240\ccs\tools\compiler\ti-cgt-c2000_22.6.0.LTS\bin\ofd2000 C:\ti\ccs1240\ccs\tools\compiler\ti-cgt-c2000_22.6.0.LTS\bin\hex2000 C:\ti\ccs1240\ccs\utils\tiobj2bin\mkhex4bin"'

    try:
        result = subprocess.run(
            command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:", result.stdout.decode())
        print("Error:", result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}\nExit Code: {e.returncode}")


def calculate_md5(filename, block_size=4096):
    """ Calculate MD5 checksum of a file """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.digest()


def prepare_ota_file(version, binary_file, ota_file):
    """ Prepare OTA file with version, reserved bytes, MD5 checksum, and binary data """
    reserved_bytes = b'\x00\x00'  # 2 reserved bytes
    # Splitting the 48-bit firmware version into three 16-bit parts
    part1 = (version >> 32) & 0xFFFF  # Upper 16 bits
    part2 = (version >> 16) & 0xFFFF  # Middle 16 bits
    part3 = version & 0xFFFF         # Lower 16 bits
    # Converting each part to bytes in little-endian format
    version_bytes = part1.to_bytes(
        2, 'little') + part2.to_bytes(2, 'little') + part3.to_bytes(2, 'little')
    # version_bytes = version.to_bytes(6, byteorder='big')
    # , byteorder='big'
    with open(binary_file, 'rb') as bin_file:
        binary_data = bin_file.read()
        binary_data_length = len(binary_data)
        # print("Binary Data Length:", len(binary_data), hex(len(binary_data)))
        binary_data_length_bytes = struct.pack(
            '<I', binary_data_length)  # Little-endian
        # print("Binary Data Length (Hex, Little-Endian):",
        #       binary_data_length_bytes.hex())
        binary_data = binary_data_length_bytes+binary_data
    with open(binary_file, 'wb') as bin_file:
        bin_file.write(binary_data)
    md5_checksum = calculate_md5(binary_file)
    print("MD5 Checksum:", md5_checksum.hex())
    with open(ota_file, 'wb') as ota:

        ota.write(version_bytes)
        ota.write(reserved_bytes)
        ota.write(md5_checksum)
        ota.write(binary_data)


def main():
    # output_file = r"tms320f28335-csd_without_power_on_music"
    output_file = r"tms320f28335-csd"
    execute_tiobj2bin_command(output_file)
    # Example usage
    firmware_version = 0x010000010003  # example version number

    prepare_ota_file(firmware_version,
                     rf'{output_file}.bin', rf'{output_file}.ota')


if __name__ == '__main__':
    main()
