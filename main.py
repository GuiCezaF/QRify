import argparse
from services.qr_code import generate_qrcode

def main() -> None:
  parser = argparse.ArgumentParser(description='QRCode Generator')
  parser.add_argument('--img',action='store_true', help='Flag to generate img')
  parser.add_argument('--url',type=str, required=True, help='URL to generate QRCode')
  args = parser.parse_args()

  generate_qrcode(args.url, args.img)

if __name__ == '__main__':
  main()

