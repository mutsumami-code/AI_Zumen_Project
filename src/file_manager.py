from pathlib import Path
import config
import fitz
import cv2
import numpy as np


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
    日本語ファイル名対応
    """

    image = cv2.imdecode(
        np.fromfile(image_path, dtype=np.uint8),
        cv2.IMREAD_COLOR
    )

    height, width = image.shape[:2]

    return width, height




def open_image(image_path):
    """
    PNG画像をOpenCVで読み込む
    日本語ファイル名対応
    """

    image = cv2.imdecode(
        np.fromfile(image_path, dtype=np.uint8),
        cv2.IMREAD_COLOR
    )

    return image