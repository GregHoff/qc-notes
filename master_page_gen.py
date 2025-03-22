import os
import nbformat
import re
from pathlib import Path
import urllib.parse

def find_notebooks(root_dir):
    """Find all notebooks matching nanomod*.ipynb pattern recursively"""
    notebooks = []
    for path in Path(root_dir).glob('**/*nanomod*.ipynb'):
        # Skip checkpoint files
        if 'checkpoint' not in str(path):
            notebooks.append(str(path))
    return notebooks

def extract_info(notebook_path):
    """Extract title and description from notebook"""
    nb = nbformat.read(notebook_path, as_version=4)
    
    title = ""
    description = ""
    
    # Find first markdown cell
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            # Extract title from heading
            heading_match = re.search(r'#\s+(.*)', cell.source)
            if heading_match:
                title = heading_match.group(1).strip()
            
            # Find description
            lines = cell.source.split('\n')
            non_heading_lines = [l for l in lines if 'student will' in l.lower()]
            if non_heading_lines:
                description = non_heading_lines[0].strip()
            
            # We found and processed first markdown cell, so break
            break
    
    return {
        'path': notebook_path,
        'title': title,
        'description': description,
        'unit': get_unit_from_path(notebook_path)
    }

def get_unit_from_path(path):
    """Extract unit from path"""
    parts = Path(path).parts
    for part in parts:
        if part.startswith("Unit "):
            return part
    return "Other"

def group_by_unit(notebooks_info):
    """Group notebooks by unit"""
    unit_groups = {}
    for info in notebooks_info:
        unit = info['unit']
        if unit not in unit_groups:
            unit_groups[unit] = []
        unit_groups[unit].append(info)
    
    # Sort each unit's notebooks
    for unit in unit_groups:
        unit_groups[unit].sort(key=lambda x: x['path'])
    
    # Sort units
    sorted_units = sorted(unit_groups.keys())
    return {unit: unit_groups[unit] for unit in sorted_units}

def create_toc_notebook(notebooks_by_unit, output_path):
    """Create a table of contents notebook"""
    nb = nbformat.v4.new_notebook()
    
    # Title cell
    title_cell = nbformat.v4.new_markdown_cell("# Quantum Cryptography Notes - Table of Contents")
    nb.cells.append(title_cell)
    
    # Introduction cell
    intro_cell = nbformat.v4.new_markdown_cell(
        "This notebook contains links to all modules and lessons in the Quantum Cryptography course."
    )
    nb.cells.append(intro_cell)
    
    # Create a section for each unit
    for unit, notebooks in notebooks_by_unit.items():
        # Unit header
        unit_header = nbformat.v4.new_markdown_cell(f"## {unit}")
        nb.cells.append(unit_header)
        
        # Table header
        table_content = "| Module | Link |\n| ------ | ---- |\n"
        
        # Table rows
        for info in notebooks:
            title = info['title'] if info['title'] else os.path.basename(info['path']).replace('.ipynb', '')
            description = info['description'] if info['description'] else "No description available"
            
            rel_path = os.path.relpath(info['path'], os.path.dirname(output_path))
            rel_path = urllib.parse.quote(rel_path)
            
            link = f"[Open Notebook]({rel_path})"
            table_content += f"| {title} | {link} |\n"
        
        # Add table for this unit
        table_cell = nbformat.v4.new_markdown_cell(table_content)
        nb.cells.append(table_cell)
    
    # Write the notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

def main():
    root_dir = "./Quantum_Cryptography_Notes"
    output_path = root_dir + "/master.ipynb"
    
    print("Finding notebooks...")
    notebooks = find_notebooks(root_dir)
    print(f"Found {len(notebooks)} notebooks")
    
    print("Extracting information...")
    notebooks_info = [extract_info(nb) for nb in notebooks]
    
    print("Grouping by unit...")
    notebooks_by_unit = group_by_unit(notebooks_info)
    
    print("Creating table of contents...")
    create_toc_notebook(notebooks_by_unit, output_path)
    print(f"Table of contents created at {output_path}")

if __name__ == "__main__":
    main()