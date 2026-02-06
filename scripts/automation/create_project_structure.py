import pathlib
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
def create_project_structure(project_name):
    # Initialize the path object for the new directory
    base_dir = pathlib.Path(project_name)
    
    try:
        # 1. Create the directory
        # exist_ok=True prevents an error if the folder already exists
        base_dir.mkdir(exist_ok=True)
        print(f"Directory created: {base_dir}")
        
        # 2. Define the markdown file path inside that directory
        # This joins the folder name with 'README.md'
        md_file = base_dir / f"{project_name}.md"
        
        # 3. Create the markdown file and add a header
        md_file.write_text(f"# Project: {project_name}\n\n# Today's Agenda")
        print(f"Markdown file created: {md_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # name = input("Enter the name for your folder and file: ").strip()
    args = parser.parse_args()
    if args.name:
        create_project_structure(args.name)
    else:
        print("Please provide a valid name.")
