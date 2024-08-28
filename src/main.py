import sys
import argparse
from services.qr_code import generate_qrcode
from utils.colors import Colors    

def main() -> None:
  parser = argparse.ArgumentParser(description='QRify a QRCode Generator')
  parser.add_argument('--img',action='store_true', help='Flag to generate img')
  parser.add_argument('--url',type=str, required=True, help='URL to generate QRCode')
  parser.add_argument('--p',type=str, help='Path to generate QRCode image')
  args = parser.parse_args()

  if args.img and not args.p:
    print(f"{Colors.FAIL}Erro: O argumento --p é obrigatório quando --img é passado.{Colors.RESET}", file=sys.stderr)
    parser.print_help()
    sys.exit(1)

  generate_qrcode(args.url, args.img, args.p)

if __name__ == '__main__':
  main()

