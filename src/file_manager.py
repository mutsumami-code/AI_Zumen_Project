from pathlib import Path
import config
import fitz
import cv2


def get_pdf_files():
    """
    pdfフォルダ内のPDFファイル一覧を取得する
    """

    pdf_path = Path(config.PDF_FOLDER)
    pdf_files = sorted(pdf_path.glob("*.pdf"))

    return pdf_files
 

def open_pdf(pdf_path):
    """
    PDFを開く
    """

    document = fitz.open(pdf_path)

    return document


def pdf_to_image(document, output_path):
    """
    PDFの1ページ目をPNG画像として保存する
    """

    page = document.load_page(0)

    pix = page.get_pixmap(dpi=300)

    pix.save(output_path)


def get_page_size(document):
    """
    PDF1ページ目のサイズを取得する
    """

    page = document.load_page(0)

    rect = page.rect

    return rect.width, rect.height


def get_image_size(image_path):
    """
    PNG画像のサイズを取得する
    """

    image = cv2.imread(str(image_path))

    height, width = image.shape[:2]

    return width, height