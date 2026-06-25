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
nav.pagination, .social-links, .share-buttons {
    display: none !important;
}
main, .container-lg, .row { display: block !important; }
.col.mb-5, .main-content {
    max-width: 100% !important;
    flex: 0 0 100% !important;
    width: 100% !important;
    padding-left: 0 !important;
}

/* Titulos menores e mais proporcionais no PDF */
.main-content h1 { font-size: 20px !important; line-height: 1.3 !important; margin-bottom: 0.4em !important; font-weight: 700 !important; }
.main-content h2 { font-size: 16px !important; font-weight: 700 !important; }
.main-content h3 { font-size: 13.5px !important; font-weight: 700 !important; }
.main-content h4 { font-size: 12.5px !important; font-weight: 700 !important; }

/* Quebras de pagina mais limpas */
.main-content h1, .main-content h2, .main-content h3, .main-content h4 {
    page-break-after: avoid;
    break-after: avoid;
}
.main-content blockquote { page-break-inside: avoid; break-inside: avoid; }
.main-content table { page-break-inside: auto; }
.main-content thead { display: table-header-group; }
.main-content tr, .main-content td { page-break-inside: avoid; break-inside: avoid; }
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

    # Percorre o menu na ordem visual (ordem do documento), preservando a
    # sequencia do menu lateral: itens de topo e pastas intercalados, comecando
    # por Apresentacao.
    for child in menu_nav.find_all(recursive=False):
        classes = child.get('class') or []
        if child.name == 'a' and 'menu-item' in classes:
            add(child.get('href'))
        elif child.name == 'div' and 'menu-folder' in classes:
            for a in child.select('ul li a.menu-item'):
                add(a.get('href'))
    return urls


def download_as_pdf(page, url, output_path):
    try:
        page.goto(url, wait_until='load', timeout=60000)
        page.wait_for_timeout(800)
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

        # Bloqueia recursos externos (fontes Google/rawline, FontAwesome, VLibras):
        # o layout vem do CSS do proprio site (mesma origem), entao recursos de
        # outros dominios apenas atrasam e causam timeouts intermitentes no CI.
        base_host = urlparse(base_site).netloc

        def _route(route):
            req_host = urlparse(route.request.url).netloc
            if req_host == "" or req_host == base_host:
                route.continue_()
            else:
                route.abort()

        page.route("**/*", _route)

        for i, url in enumerate(urls):
            print(f"Processing {i+1}/{len(urls)}: {url}")
            output_pdf = os.path.join(temp_dir, f"page_{i}.pdf")
            if download_as_pdf(page, url, output_pdf):
                pdf_files.append(output_pdf)
        browser.close()

    if pdf_files and len(pdf_files) == len(urls):
        output_file = os.path.join(temp_dir, "merged_site.pdf")
        print(f"Merging {len(pdf_files)} PDFs into {output_file}")
        merge_pdfs(pdf_files, output_file)
        print(f"Successfully created {output_file}")
    else:
        print(f"ERRO: apenas {len(pdf_files)} de {len(urls)} paginas foram convertidas. "
              "Abortando para nao publicar um PDF incompleto.")
        raise SystemExit(1)
