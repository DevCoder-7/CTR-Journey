#!/usr/bin/env python3

import subprocess
import sys
import os

def run_tshark_command(command, description):
    print(f"[+] {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def extract_amazing_and_previous_packets(pcap_file):
    """Ekstrak packet AMAZING dan packet sebelumnya dari file pcap"""
    
    print("=========================================")
    print("    EXTRACTING AMAZING & PREVIOUS PACKETS")
    print("=========================================")
    
    # 1. Ekstrak semua packet AMAZING dengan frame number
    amazing_packets = run_tshark_command(
        f"tshark -r {pcap_file} -Y 'udp.payload == 41:4d:41:5a:49:4e:47' -T fields -e frame.number -e udp.payload",
        "Extracting AMAZING packets..."
    )
    
    # 2. Ekstrak semua packet UDP dengan frame number dan payload
    all_udp_packets = run_tshark_command(
        f"tshark -r {pcap_file} -Y 'udp' -T fields -e frame.number -e udp.payload",
        "Extracting all UDP packets..."
    )
    
    # 3. Proses untuk mendapatkan packet sebelum AMAZING
    print("[3] Processing packets before AMAZING...")
    
    # Parse packet AMAZING
    amazing_frames = []
    for line in amazing_packets:
        if '\t' in line:
            frame_num, payload = line.split('\t', 1)
            amazing_frames.append(int(frame_num))
    
    # Parse semua packet UDP
    udp_packets = {}
    for line in all_udp_packets:
        if '\t' in line:
            frame_num, payload = line.split('\t', 1)
            udp_packets[int(frame_num)] = payload
    
    print(f"Found {len(amazing_frames)} AMAZING packets")
    print(f"Total UDP packets: {len(udp_packets)}")
    
    # Untuk setiap AMAZING, ambil packet sebelumnya
    result_chars = []
    print("\n=== EXTRACTION DETAILS ===")
    for amazing_frame in sorted(amazing_frames):
        prev_frame = amazing_frame - 1
        if prev_frame in udp_packets:
            prev_payload = udp_packets[prev_frame]
            # Ambil byte terakhir dari payload (2 karakter hex terakhir)
            if len(prev_payload) >= 2:
                last_byte_hex = prev_payload[-2:]
                try:
                    char = chr(int(last_byte_hex, 16))
                    result_chars.append(char)
                    print(f"Frame {prev_frame} -> {last_byte_hex} = '{char}' -> AMAZING at frame {amazing_frame}")
                except ValueError:
                    # Skip jika bukan hex yang valid
                    pass
    
    # Gabungkan semua karakter
    result = ''.join(result_chars)
    print(f"\n=== FINAL RESULT ===")
    print(result)
    
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_amazing.py <pcap_file>")
        print("Example: python3 extract_amazing.py chall.pcap")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    
    if not os.path.exists(pcap_file):
        print(f"Error: File {pcap_file} not found!")
        sys.exit(1)
    
    extract_amazing_and_previous_packets(pcap_file)

if __name__ == "__main__":
    main()
