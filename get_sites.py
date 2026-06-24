import os
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger
from playwright.sync_api import sync_playwright

# CSS injetado em cada pagina antes de imprimir: oculta a "moldura" do site
# (cabecalho, menu lateral, rodape, atalhos, widget VLibras, paginacao e botoes
# de compartilhar) e expande a coluna de conteudo para ocupar a largura total.
HIDE_CSS = """
header.br-header, .br-skiplink, footer, #footer,
#menuref, .site-menu, .br-menu,
[vw], .vw-plugin-wrapper, .enabled[vw],
nav.pagination, .share-buttons {
    display: none !important;
}
main, .container-lg, .row { display: block !important; }
.col.mb-5, .main-content {
    max-width: 100% !important;
    flex: 0 0 100% !important;
    width: 100% !important;
    padding-left: 0 !important;
}
"""


def get_urls_from_navbar(base_site):
    response = requests.get(base_site)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    menu_nav = soup.find('nav', class_='menu-body')
    if not menu_nav:
        menu_nav = soup.find('nav', id='main-navigation')
    if not menu_nav:
        raise Exception('Could not find navbar/menu in the HTML')

    base_host = urlparse(base_site).netloc
    urls = []
    seen = set()

    def add(href):
        if not href or href.startswith('javascript'):
            return
        full = urljoin(base_site, href)
        if urlparse(full).netloc != base_host:
            return
        if full not in seen:
            seen.add(full)
            urls.append(full)

    for a in menu_nav.find_all('a', class_='menu-item divider', href=True):
        add(a['href'])
    for folder in menu_nav.find_all('div', class_='menu-folder'):
        ul = folder.find('ul')
        if ul:
            for li in ul.find_all('li'):
                a = li.find('a', class_='menu-item', href=True)
                if a:
                    add(a['href'])
    return urls


def download_as_pdf(page, url, output_path):
    try:
        page.goto(url, wait_until='networkidle', timeout=60000)
        page.add_style_tag(content=HIDE_CSS)
        page.emulate_media(media='screen')
        page.pdf(
            path=output_path,
            format='A4',
            print_background=True,
            margin={'top': '1.2cm', 'bottom': '1.2cm', 'left': '1.2cm', 'right': '1.2cm'},
        )
        return True
    except Exception as e:
        print(f"Error converting {url} to PDF: {e}")
        return False


def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        if os.path.exists(pdf):
            merger.append(pdf)
    merger.write(output_path)
    merger.close()


if __name__ == "__main__":
    base_site = os.environ.get(
        "SITE_BASE_URL",
        "https://alesmelo74.github.io/guiaobservatorio/",
    )
    if not base_site.endswith('/'):
        base_site += '/'

    urls = get_urls_from_navbar(base_site)

    temp_dir = "temp_pdfs"
    os.makedirs(temp_dir, exist_ok=True)

    print(f"Base site: {base_site}")
    print(f"Found {len(urls)} URLs to process (from navbar order)")

    pdf_files = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for i, url in enumerate(urls):
            print(f"Processing {i+1}/{len(urls)}: {url}")
            output_pdf = os.path.join(temp_dir, f"page_{i}.pdf")
            if download_as_pdf(page, url, output_pdf):
                pdf_files.append(output_pdf)
        browser.close()

    if pdf_files:
        output_file = os.path.join(temp_dir, "merged_site.pdf")
        print(f"Merging {len(pdf_files)} PDFs into {output_file}")
        merge_pdfs(pdf_files, output_file)
        print(f"Successfully created {output_file}")
    else:
        print("No PDFs were created.")
        raise SystemExit(1)
