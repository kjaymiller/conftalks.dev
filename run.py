import config
import shutil
from pathlib import Path
from pages import (
        Page,
        Collection
        )
from pages.generators import gen_static 
from pages.writer import write_page, writer


pages = Collection(name='pages', content_type=Page, content_path='pages')
shutil.rmtree(Path(config.OUTPUT_PATH))

# build static pages
gen_static()
 
pages.output_path.mkdir(parents=True, exist_ok=True)
for page in pages.pages:
    write_page(f'{pages.output_path}/{page.id}.html', page.html)

@writer(route='index.html')
def index():
    return Page(template='index.html').html


@writer(route='user.html')
def user():
    return Page(template='developer_page.html').html

index()
user()
