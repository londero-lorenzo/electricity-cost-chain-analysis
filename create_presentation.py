from start_venv import open_venv_shell
import os

JUPYTER_TARGET = "notebooks/04_presentation.ipynb"

OUTPUT_FOLDER = "docs"
OUTPUT_NAME = "index"



NBCONVERT_OUTPUT_SUFFIX = "slides.html"

  
if __name__ == "__main__":
    open_venv_shell(f"jupyter nbconvert {JUPYTER_TARGET} --to slides --SlidesExporter.reveal_number='c/t' --SlidesExporter.reveal_scroll=True --output-dir {OUTPUT_FOLDER} --output {OUTPUT_NAME} & exit")
    
    original_output_path = os.path.join(OUTPUT_FOLDER, f"{OUTPUT_NAME}.{NBCONVERT_OUTPUT_SUFFIX}")
    
    output_extension = OUTPUT_NAME[OUTPUT_NAME.rfind('.'):]
    output_extension = None if len(output_extension) == 1 else output_extension
    new_output_path = os.path.join(OUTPUT_FOLDER, (OUTPUT_NAME + ".html") if not output_extension else OUTPUT_NAME)
    if os.path.exists(new_output_path):
        os.remove(new_output_path)
        
    os.rename(original_output_path, new_output_path)